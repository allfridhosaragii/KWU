"""KWU procedurally authored *prototype* product assets.

Inputs: official Apple exterior dimensions (mm) and user-provided front references.
Outputs: browser-compatible vertex-colored GLB; mm dimensions recorded separately.
No claim of exact photogrammetric or authorized manufacturer CAD similarity.
All assets are original generated geometry, suitable for further Blender refinement.
"""
from __future__ import annotations
from pathlib import Path
import math, json
import numpy as np
import trimesh
from PIL import Image, ImageDraw

BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'site'/'models';OUT.mkdir(parents=True,exist_ok=True)
ASSET_DATA=BASE/'assets'/'metadata';ASSET_DATA.mkdir(parents=True,exist_ok=True)
COL={
'fabric':[23,24,25], 'fabriclight':[31,32,34], 'fabricshadow':[18,18,20],
'zipper':[42,43,44], 'metal':[191,194,197], 'highlight':[232,235,234],
'white':[243,239,233], 'black':[24,27,29], 'lens':[17,26,36],
'skin':[208,164,140], 'skin2':[218,176,152], 'nail':[238,202,188],
'steel':[183,187,190], 'pearl':[241,224,209], 'rose':[198,125,124],
'gold':[201,162,106], 'wine':[127,76,63], 'sage':[118,140,122]
}

def rgba(color, alpha=255):
 if isinstance(color,str):c=COL.get(color, [118,118,118]);return list(c)+[alpha]
 if isinstance(color,tuple):return list(color)+[alpha]
 return list(color[:3])+[alpha]

def paint(m,color,alpha=255,variation=0,seed=1):
 c=np.tile(np.array(rgba(color,alpha),dtype=np.uint8),(len(m.vertices),1))
 if variation:
  rng=np.random.default_rng(seed)
  v=rng.normal(0,variation,size=(len(m.vertices),1));c[:,:3]=np.clip(c[:,:3].astype(float)+v,0,255).astype('uint8')
 m.visual.vertex_colors=c
 return m

def sphere(ext,at,color,sub=2,variation=0,seed=1):
 m=trimesh.creation.icosphere(subdivisions=sub)
 m.apply_scale(ext);m.apply_translation(at);return paint(m,color,variation=variation,seed=seed)

def cylinder(radius,height,at,color,sections=32,axis='z'):
 m=trimesh.creation.cylinder(radius=radius,height=height,sections=sections)
 if axis=='y':m.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[1,0,0]))
 if axis=='x':m.apply_transform(trimesh.transformations.rotation_matrix(math.pi/2,[0,1,0]))
 m.apply_translation(at);return paint(m,color)

def box(ext,at,color):
 m=trimesh.creation.box(extents=ext);m.apply_translation(at);return paint(m,color)

def rounded_rect_outline(w,h,r,segments=9):
 r=max(0.001,min(r,w/2-.0001,h/2-.0001))
 pts=[]
 for cx,cy,base in [(w/2-r,h/2-r,0),(-w/2+r,h/2-r,90),(-w/2+r,-h/2+r,180),(w/2-r,-h/2+r,270)]:
  for j in range(segments+1):
   a=math.radians(base + j*90/segments)
   # top-right from right->top, top-left top->left etc counterclockwise
   pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
 return np.asarray(pts,dtype=float)

def rounded_box(w,h,d,r,color,z=0,bevel=.018,seg=10):
 """Rounded industrial solid with split cap vertices.
 This removes the cross-shaped / pyramidal shading artifact seen on flat
 Apple and backpack panels when the cap and bezel shared vertex normals.
 The cap remains planar, while rounded walls use smooth contiguous rings.
 """
 inset=max(.003,min(bevel,w/15,h/15,d/4))
 side_sections=[(z-d/2,1-inset/min(w,h)),(z-d/2+inset,1),
                (z+d/2-inset,1),(z+d/2,1-inset/min(w,h))]
 vertices=[];faces=[];n=None
 for zz,shrink in side_sections:
  pts=rounded_rect_outline(w*shrink,h*shrink,r*shrink,seg)
  if n is None:n=len(pts)
  vertices.extend([(x,y,zz) for x,y in pts])
 for k in range(len(side_sections)-1):
  for j in range(n):
   a=k*n+j;b=k*n+(j+1)%n;c=(k+1)*n+(j+1)%n;dd=(k+1)*n+j
   faces.extend([(a,b,c),(a,c,dd)])
 # Duplicate rim for planar end faces. No vertex normal sharing with bevel.
 for k in (0,len(side_sections)-1):
  zz,shrink=side_sections[k]
  base=len(vertices)
  pts=rounded_rect_outline(w*shrink,h*shrink,r*shrink,seg)
  vertices.extend([(x,y,zz) for x,y in pts]);center=len(vertices);vertices.append((0,0,zz))
  for j in range(n):
   a=base+j;b=base+(j+1)%n
   faces.append((center,b,a) if k==0 else (center,a,b))
 m=trimesh.Trimesh(vertices=np.asarray(vertices,dtype=float),faces=faces,process=False)
 trimesh.repair.fix_normals(m)
 return paint(m,color)

def tube(points,r,color,sections=12):
 points=np.asarray(points,float)
 out=[]
 for i,(a,b) in enumerate(zip(points[:-1],points[1:])):
  d=b-a;L=np.linalg.norm(d)
  if L<1e-5:continue
  m=trimesh.creation.cylinder(radius=r,height=L,sections=sections)
  m.apply_transform(trimesh.geometry.align_vectors([0,0,1],d/L));m.apply_translation((a+b)/2);paint(m,color);out.append(m)
 for p in points[1:-1]:out.append(sphere((r,r,r),p,color,1))
 return trimesh.util.concatenate(out) if out else sphere((.001,)*3,points[0],color,1)

def torus(R,r,at,color,axis='z',sections=56,tube_segments=12):
 V=[];F=[]
 for j in range(sections):
  a=j/sections*math.tau
  for k in range(tube_segments):
   b=k/tube_segments*math.tau
   x=(R+r*math.cos(b))*math.cos(a);y=(R+r*math.cos(b))*math.sin(a);z=r*math.sin(b)
   if axis=='y': x,y,z=x,z,y
   if axis=='x': x,y,z=z,y,x
   V.append((x+at[0],y+at[1],z+at[2]))
 for j in range(sections):
  for k in range(tube_segments):
   a=j*tube_segments+k;b=((j+1)%sections)*tube_segments+k
   c=((j+1)%sections)*tube_segments+(k+1)%tube_segments;d=j*tube_segments+(k+1)%tube_segments
   F.extend([(a,b,c),(a,c,d)])
 m=trimesh.Trimesh(vertices=V,faces=F,process=False);trimesh.repair.fix_normals(m);return paint(m,color)

def lathe(profile, color,segments=72, variations=0, seed=3):
 """profile as [(height_y, radius)] for bottle/shoulder/body."""
 V=[];F=[]
 rng=np.random.default_rng(seed)
 for yi,(y,r) in enumerate(profile):
  for j in range(segments):
   a=j/segments*math.tau
   rough=(1 + .0012*math.sin(a*17+yi*.22)) if variations else 1
   V.append((math.cos(a)*r*rough,y,math.sin(a)*r*rough))
 for i in range(len(profile)-1):
  for j in range(segments):
   a=i*segments+j;b=i*segments+(j+1)%segments;c=(i+1)*segments+(j+1)%segments;d=(i+1)*segments+j
   F.extend([(a,b,c),(a,c,d)])
 for idx in (0,len(profile)-1):
  p=len(V);V.append((0,profile[idx][0],0));k=idx*segments
  for j in range(segments):
   a=k+j;b=k+(j+1)%segments
   F.append((p,a,b) if idx==0 else (p,b,a))
 m=trimesh.Trimesh(vertices=V,faces=F,process=False);trimesh.repair.fix_normals(m)
 return paint(m,color,variation=variations,seed=seed)

def finger(start,control,end,r0,r1,skin='skin',seg=18,step=22):
 """Tapered elliptical finger swept along smooth Bezier, mild knuckles."""
 a=np.array(start,float);b=np.array(control,float);c=np.array(end,float)
 vv=[];ff=[]
 for i in range(step+1):
  t=i/step;pos=(1-t)**2*a+2*(1-t)*t*b+t*t*c
  tan=2*(1-t)*(b-a)+2*t*(c-b);tan=tan/(np.linalg.norm(tan)+1e-8)
  xaxis=np.cross(tan,[0,0,1]);xaxis=xaxis/(np.linalg.norm(xaxis)+1e-8)
  zaxis=np.cross(xaxis,tan);zaxis=zaxis/(np.linalg.norm(zaxis)+1e-8)
  taper=(1-t)*r0+t*r1;knuckle=1+.085*math.exp(-((t-.40)/.11)**2)+.046*math.exp(-((t-.71)/.09)**2)
  r=taper*knuckle*(.72+.28*min(1,t*15,(1-t)*15))
  for j in range(seg):
   ang=math.tau*j/seg
   v=pos+xaxis*r*math.cos(ang)+zaxis*r*.82*math.sin(ang)
   vv.append(v)
 for i in range(step):
  for j in range(seg):
   t0=i*seg+j;t1=i*seg+(j+1)%seg;t2=(i+1)*seg+(j+1)%seg;t3=(i+1)*seg+j
   ff.extend([(t0,t1,t2),(t0,t2,t3)])
 for ring_id in [0,step]:
  cen=len(vv);vv.append(a if ring_id==0 else c)
  off=ring_id*seg
  for j in range(seg):ff.append((cen,off+(j+1)%seg,off+j) if ring_id==0 else (cen,off+j,off+(j+1)%seg))
 m=trimesh.Trimesh(vertices=vv,faces=ff,process=False);trimesh.repair.fix_normals(m)
 return paint(m,skin,variation=1.1,seed=12)

def palm():
 # hand torso loft; wider at knuckles, slimmer at wrist
 profiles=[(-1.27,.29,.28),(-1.05,.35,.27),(-.82,.44,.26),(-.53,.58,.235),(-.22,.65,.23),(.12,.66,.22),(.38,.61,.20),(.58,.58,.18),(.70,.48,.16)]
 V=[];F=[];seg=48
 for y,w,d in profiles:
  for j in range(seg):
   a=j/seg*math.tau
   x=w*math.cos(a)*(1-.10*(math.sin(a)**2));z=d*math.sin(a)+(0.04 if math.sin(a)>0 else -.02)
   # slight uneven back skin, knuckle ridge
   V.append((x+.035*math.sin((y+1.3)*1.8),y,z))
 for i in range(len(profiles)-1):
  for j in range(seg):
   a=i*seg+j;b=i*seg+(j+1)%seg;c=(i+1)*seg+(j+1)%seg;d=(i+1)*seg+j
   F.extend([(a,b,c),(a,c,d)])
 for i in [0,len(profiles)-1]:
  V.append((0,profiles[i][0],0));base=i*seg;ctr=len(V)-1
  for j in range(seg): F.append((ctr,base+(j+1)%seg,base+j) if i==0 else (ctr,base+j,base+(j+1)%seg))
 m=trimesh.Trimesh(vertices=V,faces=F,process=False);trimesh.repair.fix_normals(m)
 return paint(m,'skin',variation=2.2)

def human_hand(standalone=False):
 from anatomical_hand import hand_surface
 out=[hand_surface()]
 # Flat natural nail plates on tips, close to the skin rather than spherical bumps.
 for x,y in [(-.55,1.34),(-.15,1.64),(.18,1.75),(.51,1.47),(-1.05,.17)]:
  n=sphere((.066,.082,.011),(x,y,.098 if x>-.95 else .14),'nail',2)
  out.append(n)
 return out

def bag_mesh():
 out=[]
 # black backpack matching user photo: tall rounded rectangular shell, round shoulder crown, boxy lower area
 body=rounded_box(2.25,2.95,.67,.42,'fabric',z=-.09,bevel=.07)
 # rounded top silhouette: adjust y>0.55 x profile to make taller curved shoulder
 verts=np.asarray(body.vertices)
 for i,(x,y,z) in enumerate(verts):
  if y>.42:
   t=min(1,(y-.42)/1.10);verts[i,0]=x*(1-.11*t-.08*t*t)
   verts[i,1]+= .025*math.cos(x*3.3)*t
 body.vertices=verts
 paint(body,'fabric',variation=2.0,seed=20);out.append(body)
 # top seam around arch and front pocket flap
 out.append(tube([(-.88,.84,.27),(-.82,1.13,.28),(-.50,1.34,.30),(0,1.44,.31),(.50,1.34,.30),(.82,1.13,.28),(.88,.84,.27)],.014,'fabriclight',10))
 # front large pocket lower, rounded-rect pill
 pocket=rounded_box(1.96,1.34,.20,.13,'fabriclight',z=.35,bevel=.045);pocket.apply_translation([0,-.72,0]);out.append(pocket)
 # pocket upper horizontal separation/zipper at y -.20
 out.append(box((1.89,.032,.02),(0,-.23,.475),'zipper'))
 out.append(tube([(-.90,-.26,.49),(-.35,-.26,.50),(.30,-.26,.50),(.85,-.26,.49)],.009,'metal',8))
 # secondary front upper pocket shallow flap
 flap=rounded_box(2.12,.37,.065,.08,'fabric',z=.39);flap.apply_translation([0,-.16,0]);out.append(flap)
 # vertical main seams on both sides
 for xx in (-.93,.93):out.append(tube([(xx,-1.30,.38),(xx,-.45,.40),(xx,.38,.37)],.009,'fabricshadow',8))
 # side pockets
 for side in (-1,1):
  px=side*1.14
  pocket_side=rounded_box(.28,.88,.36,.095,'fabriclight',z=.02);pocket_side.apply_translation([px,-.79,0]);out.append(pocket_side)
  out.append(tube([(px-side*.16,-.44,.21),(px,-.42,.23),(px+side*.12,-.44,.20)],.018,'fabricshadow',8))
 # top carry handle black U loop, stitching highlight slight
 out.append(tube([(-.42,1.38,-.06),(-.34,1.69,-.05),(-.18,1.78,-.05),(.18,1.78,-.05),(.34,1.69,-.05),(.42,1.38,-.06)],.080,'fabricshadow',20))
 # shoulder straps glimpse behind backpack
 for xx in (-.63,.63):out.append(tube([(xx,1.16,-.46),(xx*1.12,.45,-.51),(xx*.95,-.63,-.50)],.105,'fabricshadow',16))
 # label patch bottom right - generic no brand claim
 out.append(rounded_box(.32,.17,.018,.014,(132,132,130),z=.49,bevel=.004))
 out[-1].apply_translation((.61,-1.02,0))
 # tiny material stitch dotted line on label
 for k in range(7):out.append(sphere((.009,.006,.005),(.48+k*.042,-1.10,.504),'metal',1))
 # Front pocket edge stitches and zip pull; small details batched into few meshes.
 stitch=[]
 for yy in (-1.33,-.32):
  for xx in np.linspace(-.82,.82,29):
   stitch.append(box((.022,.006,.006),(float(xx),yy,.477 if yy==-.32 else .465),'fabricshadow'))
 if stitch:out.append(trimesh.util.concatenate(stitch))
 for xx in (-.89,.89):
  out.append(tube([(xx,-1.24,.473),(xx,-.41,.474)],.008,'fabricshadow',8))
 # Zipper pull hardware under the pocket lip, visible from a front 3/4 view.
 out.append(rounded_box(.095,.145,.021,.025,'metal',z=.507,bevel=.005))
 out[-1].apply_translation((.70,-.295,0))
 out.append(torus(.045,.011,(.70,-.39,.52),'metal',axis='z',sections=20,tube_segments=8))
 # charm clips two anchors on zipper tips to enable bag-charm
 for xx in (-.79,.78):
  out.append(torus(.060,.015,(xx,-.27,.52),'metal',axis='y',sections=28))
 # default decorative metal chain and charm
 out.append(tube([(.78,-.29,.56),(.87,-.43,.60),(.86,-.62,.63)],.021,'metal',10))
 out.append(sphere((.17,.18,.045),(.86,-.74,.67),'gold',2))
 return out

def bottle_mesh():
 # stainless vessel from supplied photo: cylinder base, taper shoulder, narrower threaded throat
 profile=[(-1.42,0.0),(-1.42,.365),(-1.39,.427),(-1.34,.438),(-1.08,.444),(-.45,.447),(.30,.448),(.86,.441),(1.02,.410),(1.13,.340),(1.18,.315),(1.31,.314),(1.38,.326)]
 out=[lathe(profile,'steel',96,variations=.5)]
 # thin bottom lip and brushed center bands
 out.append(torus(.424,.012,(0,-1.365,0),'highlight',axis='y',sections=72))
 # bottle cap black with arched loop
 out.append(lathe([(1.30,.305),(1.33,.340),(1.43,.335),(1.55,.32),(1.60,.26),(1.63,.20)],'black',64))
 # loop upright curvilinear in x/y plane, connected cap
 out.append(tube([(-.24,1.57,0),(-.26,1.71,0),(-.20,1.81,0),(0,1.87,0),(.20,1.81,0),(.26,1.71,0),(.24,1.57,0)],.065,'black',16))
 # Cap gasket and brushed metal neck ring, matching reference contrast.
 out.append(torus(.316,.012,(0,1.315,0),'fabricshadow',axis='y',sections=64))
 out.append(torus(.314,.009,(0,1.283,0),'highlight',axis='y',sections=64))
 # metal carabiner clip right like photo, oval U with gate
 loop=[(.28,1.76,.015),(.49,1.87,.015),(.64,1.80,.015),(.82,1.56,.015),(.89,1.35,.015),(.83,1.17,.015),(.65,1.13,.015),(.51,1.20,.015),(.41,1.38,.015)]
 out.append(tube(loop,.034,'metal',18))
 out.append(tube([(.41,1.38,.015),(.65,1.73,.015)],.020,'highlight',12))
 # lid steel hook eye
 out.append(torus(.095,.032,(.28,1.76,.015),'metal',axis='z',sections=32))
 return out

def iphone_body(name,dim,finish,cam='dual'):
 # dimensions in millimeters scaled height around 2.55 units
 W,H,D=dim;fac=2.55/H;w=W*fac;h=2.55;d=D*fac
 frame=finish
 out=[rounded_box(w,h,d,.20,frame,z=0,bevel=.012),
      rounded_box(w*.985,h*.990,.015,.19,frame,z=d/2+.008,bevel=.004),
      rounded_box(w*.94,h*.95,.010,.165,'black',z=-d/2-.008,bevel=.003)]
 # dynamic island in front (on negative z)
 out.append(rounded_box(.27,.070,.012,.032,'black',z=-d/2-.018))
 out[-1].apply_translation([0,h*.420,0])
 # camera layouts: rear on z-positive plane
 if cam=='pro':
  # crossbody aluminum plateau, distinctive iPhone 17 Pro
  panel=rounded_box(w*.945,.56,.105,.105,frame,z=d/2+.06,bevel=.018)
  panel.apply_translation((0,h*.335,0));out.append(panel)
  centers=[(-w*.310,h*.403),(-w*.310,h*.245),(-w*.11,h*.330)]
 elif cam=='air':
  panel=rounded_box(w*.925,.29,.075,.08,frame,z=d/2+.04);panel.apply_translation((0,h*.397,0));out.append(panel)
  centers=[(-w*.34,h*.397)]
 elif cam=='single':
  panel=rounded_box(.37,.39,.060,.085,frame,z=d/2+.037);panel.apply_translation((-w*.275,h*.345,0));out.append(panel)
  centers=[(-w*.275,h*.345)]
 else:
  panel=rounded_box(.40,.56,.055,.085,frame,z=d/2+.03);panel.apply_translation((-w*.290,h*.337,0));out.append(panel)
  centers=[(-w*.290,h*.412),(-w*.290,h*.264)]
 for i,(cx,cy) in enumerate(centers):
  out.append(cylinder(.116,.030,(cx,cy,d/2+.127 if cam=='pro' else d/2+.08),'metal',sections=40))
  out.append(cylinder(.083,.041,(cx,cy,d/2+.147 if cam=='pro' else d/2+.104),'lens',sections=40))
  out.append(sphere((.026,.032,.008),(cx-.018,cy+.023,d/2+.170 if cam=='pro' else d/2+.13),'highlight',1))
 # flash and lidar side positions
 fy=h*.34
 fx=w*.31 if cam=='pro' else -w*.035
 out.append(cylinder(.036,.019,(fx,fy,d/2+.129 if cam=='pro' else d/2+.079),'white',sections=24))
 if cam=='pro':out.append(cylinder(.028,.020,(fx,fy-.16,d/2+.129),'black',sections=24))
 # side buttons: approximate ports visible in 3D; extra details have correct side
 out.append(box((.025,.235,.034),(-w/2-.009,h*.18,0),frame))
 out.append(box((.026,.22,.033),(-w/2-.009,-h*.012,0),frame))
 out.append(box((.025,.26,.033),(w/2+.009,h*.08,0),frame))
 # bottom USB-C port physical impression
 out.append(box((.16,.012,.018),(0,-h/2-.004,0),'black'))
 # Independent casing overlay is always final mesh for WebGL transparency control.
 out.append(rounded_box(w*1.025,h*1.012,.026,.207,frame,z=d/2+.015,bevel=.005))
 return out

def tablet_body(wmm,hmm,dmm,color,camera_kind='pro'):
 fac=2.90/max(wmm,hmm);w=wmm*fac;h=hmm*fac;d=dmm*fac
 out=[rounded_box(w,h,d,.12,color,z=0,bevel=.01),rounded_box(w*.96,h*.96,.012,.12,'black',z=-d/2-.01),
      rounded_box(.25,.24,.036,.053,color,z=d/2+.025)]
 out[-1].apply_translation((-w*.37,h*.38,0))
 out.append(cylinder(.077,.027,(-w*.37,h*.38,d/2+.056),'lens'))
 if camera_kind=='pro':out.append(cylinder(.025,.025,(-w*.275,h*.37,d/2+.04),'black'))
 out.append(box((.20,.015,.022),(0,-h/2,0),'black'))
 for side in (-1,1):out.append(box((.030,.12,.030),(w/2*side,h*.28,0),color))
 return out

def laptop_body(widthmm,depthmm,thicknessmm,color):
 # scale width to 2.85 units, with x left/right and y height desktop screen
 fac=2.85/widthmm;w=2.85;dep=depthmm*fac;th=thicknessmm*fac
 out=[]
 # base appears open with top keyboard at y -.9 and z forward; lower half near bottom of model
 out.append(rounded_box(w,dep,.085,.10,color,z=-.16,bevel=.008))
 # above base visual keyboard rows, touchpad; separate keys as repeated geometry but light
 kb=rounded_box(w*.88,dep*.51,.007,.045,'black',z=-.106,bevel=.002)
 kb.apply_translation([0,-.03,0]);out.append(kb)
 # key rows as abstract minimal but convincing
 for row in range(4):
  for k in range(13):
   xx=-w*.4+k*(w*.8/12); yy=-.21+row*.075
   out.append(rounded_box(.135,.042,.002,.012,(56,58,60),z=-.09,bevel=.001))
   out[-1].apply_translation([xx,yy,0])
 out.append(rounded_box(.64,.31,.004,.028,color,z=-.075))
 out[-1].apply_translation((0,-dep*.28,0))
 # lid seen from back, standing on top of base. For stickers outer lid at positive z
 lid=rounded_box(w,1.75,.082,.095,color,z=.22,bevel=.012)
 lid.apply_translation((0,.86,0));out.append(lid)
 screen=rounded_box(w*.965,1.60,.010,.08,'black',z=.164,bevel=.003);screen.apply_translation((0,.89,0));out.append(screen)
 # hinge line
 out.append(cylinder(.047,w*.85,(0,0,.13),'metal',axis='x',sections=32))
 return out

def necklace_body():
 out=[sphere((.71,.90,.36),(0,.26,-.15),'skin',3),sphere((1.46,.31,.47),(0,-.72,-.15),'skin2',3)]
 # elegantly hanging necklace around neck
 out.append(tube([(-.54,.35,.20),(-.42,-.01,.30),(-.29,-.39,.46),(0,-.71,.51),(.29,-.39,.46),(.42,-.01,.30),(.54,.35,.20)],.025,'gold',12))
 out.append(sphere((.15,.21,.04),(0,-.79,.55),'pearl',2))
 return out

def bracelet_body():
 out=human_hand()
 out.append(torus(.30,.045,(0,-1.10,0),'metal',axis='y',sections=56))
 for j,ang in enumerate([-.50,0,.50]):
  out.append(sphere((.08,.096,.044),(ang,-1.10,.28),'gold' if j!=1 else 'pearl',2))
 return out

def ring_body():
 out=human_hand()
 # approx finger at index=middle x -.20 near y 1.1
 out.append(torus(.133,.026,(-.19,1.10,.03),'gold',axis='y'))
 out.append(sphere((.105,.045,.060),(-.19,1.18,.16),'pearl',2))
 return out

def save(name, meshes, metadata=None):
 scene=trimesh.Scene()
 tris=0
 for i,m in enumerate(meshes):
  scene.add_geometry(m,geom_name=f'{name}__mesh{i:03d}',node_name=f'{name}__n{i:03d}')
  tris+=len(m.faces)
 data=scene.export(file_type='glb');(OUT/f'{name}.glb').write_bytes(data)
 return {'id':name,'file':f'{name}.glb','bytes':len(data),'triangles':tris,'meshes':len(meshes),**(metadata or {})}

APPLE_PHONES={
 'iphone-17':{'name':'iPhone 17','dims_mm':[71.5,149.6,7.95],'cam':'dual','colors':{'Black':'#262629','White':'#F5F3EE','Mist Blue':'#C5D7E3','Sage':'#B4C0AB','Lavender':'#D7C5E3'},'source':'https://www.apple.com/id/iphone-17/specs/'},
 'iphone-air':{'name':'iPhone Air','dims_mm':[74.7,156.2,5.64],'cam':'air','colors':{'Space Black':'#272729','Cloud White':'#F3F0EB','Light Gold':'#DCCCAF','Sky Blue':'#CFDEE9'},'source':'https://www.apple.com/id/iphone-air/specs/'},
 'iphone-17-pro':{'name':'iPhone 17 Pro','dims_mm':[71.9,150.0,8.75],'cam':'pro','colors':{'Silver':'#D6D6D2','Cosmic Orange':'#D9773E','Deep Blue':'#37465D'},'source':'https://support.apple.com/en-gu/125090'},
 'iphone-17-pro-max':{'name':'iPhone 17 Pro Max','dims_mm':[78.0,163.4,8.75],'cam':'pro','colors':{'Silver':'#D6D6D2','Cosmic Orange':'#D9773E','Deep Blue':'#37465D'},'source':'https://support.apple.com/en-us/108044'},
 'iphone-17e':{'name':'iPhone 17e','dims_mm':[71.5,146.7,7.8],'cam':'single','colors':{'Black':'#222326','White':'#F3F1EA','Soft Pink':'#EAD2D7'},'source':'https://www.apple.com/id/iphone-17e/specs/'},
}
APPLE_TABLETS={
 'ipad-pro-11':{'name':'iPad Pro 11-inch','dims_mm':[177.5,249.7,5.3],'colors':{'Silver':'#CED0CE','Space Black':'#414448'},'source':'https://www.apple.com/id/ipad-pro/specs/','cam':'pro'},
 'ipad-pro-13':{'name':'iPad Pro 13-inch','dims_mm':[215.5,281.6,5.1],'colors':{'Silver':'#CED0CE','Space Black':'#414448'},'source':'https://www.apple.com/id/ipad-pro/specs/','cam':'pro'},
 'ipad-air-11':{'name':'iPad Air 11-inch (M4)','dims_mm':[178.5,247.6,6.1],'colors':{'Blue':'#B3C8E5','Purple':'#C6BBD7','Starlight':'#DFDACF','Space Gray':'#838588'},'source':'https://www.apple.com/id/ipad-air/specs/','cam':'air'},
 'ipad-air-13':{'name':'iPad Air 13-inch (M4)','dims_mm':[214.9,280.6,6.1],'colors':{'Blue':'#B3C8E5','Purple':'#C6BBD7','Starlight':'#DFDACF','Space Gray':'#838588'},'source':'https://www.apple.com/id/ipad-air/specs/','cam':'air'},
}
APPLE_LAPTOPS={
 'macbook-air-13':{'name':'MacBook Air 13-inch M5','dims_mm':[304.1,215.0,11.3],'colors':{'Sky Blue':'#AEBCC6','Silver':'#D1D2D2','Starlight':'#DCCFBC','Midnight':'#3B4850'},'source':'https://www.apple.com/id/macbook-air/specs/'},
 'macbook-air-15':{'name':'MacBook Air 15-inch M5','dims_mm':[340.4,237.6,11.5],'colors':{'Sky Blue':'#AEBCC6','Silver':'#D1D2D2','Starlight':'#DCCFBC','Midnight':'#3B4850'},'source':'https://www.apple.com/id/macbook-air/specs/'},
 'macbook-pro-14':{'name':'MacBook Pro 14-inch M5','dims_mm':[312.6,221.2,15.5],'colors':{'Space Black':'#373839','Silver':'#C5C6C6'},'source':'https://www.apple.com/id/macbook-pro/specs/'},
 'macbook-pro-16':{'name':'MacBook Pro 16-inch M5','dims_mm':[355.7,248.1,16.8],'colors':{'Space Black':'#373839','Silver':'#C5C6C6'},'source':'https://www.apple.com/id/macbook-pro/specs/'},
}

def hexrgb(h):return tuple(int(h[i:i+2],16) for i in (1,3,5))

def main():
 output=[]
 output.append(save('bracelet',bracelet_body(),{'kind':'bracelet','status':'procedural-v2'}))
 output.append(save('ring',ring_body(),{'kind':'ring','status':'procedural-v2'}))
 output.append(save('necklace',necklace_body(),{'kind':'necklace','status':'procedural-v2'}))
 output.append(save('bag-charm',bag_mesh(),{'kind':'bag-charm','status':'reference-inspired-front-only'}))
 output.append(save('bottle',bottle_mesh(),{'kind':'bottle','status':'reference-inspired-front-only'}))
 for uid,o in APPLE_PHONES.items():
  default=hexrgb(list(o['colors'].values())[0]);output.append(save(uid,iphone_body(uid,o['dims_mm'],default,o['cam']),{'kind':'phone','dims_mm':o['dims_mm'],'status':'manufacturer-dimensioned-procedural'}))
 for uid,o in APPLE_TABLETS.items():
  default=hexrgb(list(o['colors'].values())[0]);output.append(save(uid,tablet_body(*o['dims_mm'],default,o['cam']),{'kind':'tablet','dims_mm':o['dims_mm'],'status':'manufacturer-dimensioned-procedural'}))
 for uid,o in APPLE_LAPTOPS.items():
  default=hexrgb(list(o['colors'].values())[0]);output.append(save(uid,laptop_body(*o['dims_mm'],default),{'kind':'macbook','dims_mm':o['dims_mm'],'status':'manufacturer-dimensioned-procedural'}))
 # Defaults preserve existing route compatibility
 for cat,src in [('phone','iphone-17'),('tablet','ipad-pro-11'),('macbook','macbook-air-13')]:
  (OUT/f'{cat}.glb').write_bytes((OUT/f'{src}.glb').read_bytes())
 output.append({'id':'phone','file':'phone.glb','alias':'iphone-17'})
 output.append({'id':'tablet','file':'tablet.glb','alias':'ipad-pro-11'})
 output.append({'id':'macbook','file':'macbook.glb','alias':'macbook-air-13'})
 data={'schemaVersion':2,'notice':'Procedural approximations, not 1:1 scans or manufacturer CAD. Official product dimensions drive base body proportions; finishes are display approximations.','groups':{'phone':APPLE_PHONES,'tablet':APPLE_TABLETS,'macbook':APPLE_LAPTOPS},'models':output}
 (OUT/'model-catalog.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
 (OUT/'manifest.json').write_text(json.dumps(output,ensure_ascii=False,indent=2),encoding='utf8')
 (ASSET_DATA/'SOURCE_ATTRIBUTION.md').write_text('# Model Source & Fidelity\n\nAll meshes in this package are original procedural geometry authored for the KWU prototype. Not official Apple CAD or 3D scans. Device body scale is proportional to Apple published measurements. Backpack and bottle silhouettes are front-reference interpretations of user-supplied images. Hand is an anatomical study and does not pass a 1:1 human scan accuracy test.\n',encoding='utf8')
 print(json.dumps({'n':len(output),'bytes_total':sum(x.get('bytes',0) for x in output),'largest':sorted([(x.get('id'),x.get('bytes',0)) for x in output],key=lambda t:t[1],reverse=True)[:5]},indent=2))

if __name__=='__main__':main()
