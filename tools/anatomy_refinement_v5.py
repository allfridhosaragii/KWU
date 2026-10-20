"""High-detail *procedural* mannequin geometry for KWU jewelry.
Not a substitute for actual photogrammetry/skin scans. Derived from the
continuous anatomy base and refined via higher tessellation and nail plates.
"""
from pathlib import Path
import sys, math, json
import numpy as np
import trimesh
from scipy.ndimage import gaussian_filter
from skimage.measure import marching_cubes
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals
sys.path.insert(0,str(Path(__file__).resolve().parent))
from anatomical_hand import hand_surface
from make_models_v2 import torus,sphere,tube
BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'site/models'


def skin_colors(p):
 x,y,z=p[:,0],p[:,1],p[:,2]
 blush=np.exp(-((y-.65)/.35)**2)*6.5
 knuckle=np.exp(-((y-1.06)/.14)**2)*3.
 veins=np.sin(y*2.1+x*1.2)*1.5
 freckles=(np.sin(x*73.7+y*89.1+z*13.7)+np.sin(x*121.1-y*56.1+z*33.2))*.65
 r=211+blush+knuckle+veins+freckles
 g=165-blush*.18+freckles*.75
 b=144-blush*.23+freckles*.5
 return np.column_stack([np.clip(r,0,255),np.clip(g,0,255),np.clip(b,0,255),np.full(len(p),255)]).astype(np.uint8)


def nail(cx,cy,cz,angle=0,width=.104,length=.172):
 # Curved oval nail surface sitting on the dorsal side of finger tips.
 nx=14;ny=19;v=[];f=[];colors=[]
 c=math.cos(angle);s=math.sin(angle)
 for j in range(ny+1):
  t=j/ny
  yy=(t-.5)*length
  half=width*.5*math.sqrt(max(.0001,1-(2*t-1)**4))
  for i in range(nx+1):
   u=(i/nx*2-1)
   xx=u*half
   xp=c*xx-s*yy+cx;yp=s*xx+c*yy+cy
   zp=cz+.012*(1-u*u)+.006*math.sin(math.pi*t)
   v.append((xp,yp,zp))
   tone= np.array([235,194,176],float)
   # translucent-ish free edge with clean cuticle, non-white manicure.
   tone= tone+(12 if t>.78 else (3 if t>.32 else -3))
   colors.append([*np.clip(tone,0,255).astype(np.uint8),255])
 for j in range(ny):
  for i in range(nx):
   a=j*(nx+1)+i;b=a+1;c=(j+1)*(nx+1)+i+1;d=c-1
   f.extend([(a,b,c),(a,c,d)])
 m=trimesh.Trimesh(vertices=v,faces=f,process=False)
 trimesh.repair.fix_normals(m)
 m.visual.vertex_colors=np.array(colors,dtype=np.uint8)
 return m


def highres_hand():
 m=hand_surface(res=.018)
 m.visual.vertex_colors=skin_colors(np.asarray(m.vertices))
 nails=[(-.55,1.29,.075,.04),(-.15,1.60,.078,-.01),(.18,1.69,.078,.015),(.51,1.43,.077,.05),(-.99,.16,.082,.68)]
 out=[m]
 from scipy.spatial import cKDTree
 tree=cKDTree(np.asarray(m.vertices)[:,:2]);skin_pts=np.asarray(m.vertices)
 for x,y,z,angle in nails:
  plate=nail(x,y,z,angle)
  p=np.array(plate.vertices);_,inds=tree.query(p[:,:2],k=36)
  top=np.max(skin_pts[inds,2],axis=1)
  p[:,2]=top+.004
  plate.vertices=p
  out.append(plate)
 return out


def neck_surface(res=.018):
 xx=np.arange(-1.61,1.61,res);yy=np.arange(-1.29,1.08,res);zz=np.arange(-.72,.73,res)
 X,Y,Z=np.meshgrid(xx,yy,zz,indexing='ij')
 # Human-like bust: broad torso with an upper shoulder slope, not a single ellipsoid.
 shoulder_y=-.29-.47*np.power(np.minimum(np.abs(X)/1.52,1.4),1.5)
 torso_section=np.sqrt((X/1.45)**4+((Z+.13)/.47)**2)-1.
 torso_sdf=np.maximum(torso_section*.43,(Y-shoulder_y)*.9)
 torso_sdf=np.maximum(torso_sdf,(-1.19-Y)*.85)
 # Neck with nearly uniform anatomical width and a deliberately flat jaw cut.
 neck_sdf=np.sqrt((X/.38)**2+((Z+.09)/.335)**2)-1.
 neck_sdf=np.maximum(neck_sdf*.31,(-.63-Y)*.75)
 neck_sdf=np.maximum(neck_sdf,(Y-1.01)*.92)
 k=.17;h=np.maximum(k-np.abs(torso_sdf-neck_sdf),0)/k
 field=np.minimum(torso_sdf,neck_sdf)-h*h*k*.25
 # Soft clavicle relief over upper chest, subtle on the anterior surface.
 collar=.011*np.exp(-((Y+.54)/.115)**2)*np.exp(-((np.abs(X)-.61)/.38)**2)
 field+=collar*np.maximum(Z+.4,0)
 field=gaussian_filter(field,.48)
 v,f,_,_=marching_cubes(field,level=0,spacing=(res,res,res))
 v+=np.array([xx[0],yy[0],zz[0]])
 m=trimesh.Trimesh(vertices=v,faces=f,process=False);trimesh.repair.fix_normals(m)
 m.visual.vertex_colors=skin_colors(m.vertices)
 return m

def export(name,meshes):
 scene=trimesh.Scene()
 for i,m in enumerate(meshes):scene.add_geometry(m,geom_name=f'{name}__mesh{i:03d}')
 b=scene.export(file_type='glb');(OUT/f'{name}.glb').write_bytes(b)
 print(name,'verts',sum(len(x.vertices) for x in meshes),'triangles',sum(len(x.faces) for x in meshes),'bytes',len(b))

if __name__=='__main__':
 for name in ('bracelet','ring'):
  meshes=highres_hand()
  if name=='bracelet':
   meshes.append(torus(.30,.039,(0,-1.10,0),(188,193,200),axis='y',sections=96,tube_segments=20))
   meshes.append(sphere((.080,.090,.049),(-.17,-1.10,.28),(218,178,139),3))
  else:
   meshes.append(torus(.133,.025,(-.19,1.10,.03),(209,173,116),axis='y',sections=80,tube_segments=18))
   meshes.append(sphere((.102,.045,.058),(-.19,1.18,.16),(233,229,218),3))
  export(name,meshes)
 mesh=neck_surface()
 chain=tube([(-.36,.23,.27),(-.42,-.10,.32),(-.33,-.45,.45),(0,-.78,.51),(.33,-.45,.45),(.42,-.10,.32),(.36,.23,.27)],.018,(209,173,116),18)
 pearl=sphere((.13,.17,.05),(0,-.84,.55),(244,225,209),3)
 export('necklace',[mesh,chain,pearl])
