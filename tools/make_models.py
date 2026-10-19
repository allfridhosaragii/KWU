from pathlib import Path
import numpy as np, trimesh, math, json
OUT=Path(__file__).parent.parent/'site'/'models';OUT.mkdir(exist_ok=True,parents=True)
M={
 'skin': [223,184,156,255], 'nail':[248,222,207,255], 'silver':[202,199,193,255], 'silverlight':[224,222,217,255],
 'gold':[195,149,85,255], 'bronze':[156,93,64,255], 'black':[48,46,45,255], 'white':[238,234,228,255],
 'sage':[110,127,104,255], 'graphite':[99,102,103,255], 'glass':[208,218,215,190], 'pearl':[242,226,211,255]
}

def trans_obj(m,at=(0,0,0),rot=None):
 if rot is not None:
  ang,axis=rot; m.apply_transform(trimesh.transformations.rotation_matrix(ang,axis))
 m.apply_translation(at);return m

def mesh_sphere(size,at,c,sub=2):
 m=trimesh.creation.icosphere(subdivisions=sub,radius=1);m.apply_scale(size);m.apply_translation(at);m.visual.vertex_colors=M[c];return m

def cyl(radius,height,at,c,rot=None,sections=20):
 m=trimesh.creation.cylinder(radius=radius,height=height,sections=sections);m.visual.vertex_colors=M[c];return trans_obj(m,at,rot)

def box(size,at,c):
 m=trimesh.creation.box(extents=size);m.visual.vertex_colors=M[c];m.apply_translation(at);return m

def tube(points,r,c,seg=10):
 pts=np.array(points,dtype=float); meshes=[]
 for a,b in zip(pts[:-1],pts[1:]):
  v=b-a; length=np.linalg.norm(v)
  if length<1e-6:continue
  m=trimesh.creation.cylinder(radius=r,height=length,sections=seg)
  z=np.array([0.,0.,1.]);v/=length
  t=trimesh.geometry.align_vectors(z,v);m.apply_transform(t);m.apply_translation((a+b)/2)
  m.visual.vertex_colors=M[c];meshes.append(m)
 for p in pts[1:-1]:meshes.append(mesh_sphere((r,r,r),p,c,1))
 return trimesh.util.concatenate(meshes)

def ring(radius,r,c,at=(0,0,0),axis='z'):
 pts=[]
 for i in range(57):
  t=i/56*math.tau
  if axis=='x':pts.append([0,radius*math.cos(t),radius*math.sin(t)])
  elif axis=='y':pts.append([radius*math.cos(t),0,radius*math.sin(t)])
  else:pts.append([radius*math.cos(t),radius*math.sin(t),0])
 m=tube(pts,r,c,8);m.apply_translation(at);return m

def base_hand():
 out=[]
 # hand upright palm at center and individual fingers in upper half, z forward toward camera
 out.append(mesh_sphere((0.69,0.83,0.22),(0,-0.05,0),'skin',3))
 out.append(mesh_sphere((0.34,0.56,0.27),(0,-1.02,-0.01),'skin',3))
 for x,fy,length,width in [(-.49,.57,.74,.132),(-.18,.66,1.00,.14),(.14,.7,1.09,.14),(.45,.54,.81,.132)]:
  p0=np.array([x,fy-.2,0]);p1=np.array([x*.95,fy+length-.15,-.03]);out.append(tube([p0,p1],width,'skin',14));out.append(mesh_sphere((width,width,width),p1,'skin',2))
  out.append(mesh_sphere((width*.8,.06,.015),[p1[0],p1[1]-.1,width*.95],'nail',1))
 out.append(tube([[-.48,-.34,0],[-.82,-.05,.05],[-1.08,.30,.12]],.15,'skin',16))
 out.append(mesh_sphere((.15,.15,.15),(-1.08,.30,.12),'skin',2))
 return out

def save(name,meshes):
 sc=trimesh.Scene();
 for i,m in enumerate(meshes):sc.add_geometry(m,node_name=f'{name}-{i}',geom_name=f'{name}-{i}')
 blob=sc.export(file_type='glb');(OUT/f'{name}.glb').write_bytes(blob)
 return {'name':name,'bytes':len(blob),'parts':len(meshes),'triangles':sum(len(m.faces) for m in meshes)}

manifest=[]
# single-category models, each GLB stays under 1 MB most of the time
bracelet=base_hand()+[ring(.39,.044,'silver',at=(0,-1.03,0),axis='y')]
for j,x in enumerate([-.34,.0,.34]):bracelet.append(mesh_sphere((.09,.105,.045),(x,-1.03,.32),'gold' if j!=1 else 'pearl',2))
manifest.append(save('bracelet',bracelet))
hand=base_hand();hand.append(ring(.16,.031,'gold',at=(-.18,1.01,0),axis='y'));hand.append(mesh_sphere((.1,.05,.06),(-.18,1.08,.16),'pearl'))
manifest.append(save('ring',hand))
neck=[mesh_sphere((.72,1.25,.46),(0,.25,-.17),'skin',3),mesh_sphere((1.6,.43,.69),(0,-1.1,-.19),'skin',3)]
neck+=[ring(.68,.031,'gold',(0,.27,.12),'z'),tube([[-.60,.1,.12],[-.33,-.48,.4],[0,-.83,.57],[.33,-.48,.4],[.60,.1,.12]],.025,'gold',12),mesh_sphere((.15,.18,.05),(0,-.9,.64),'pearl',2)]
manifest.append(save('necklace',neck))
bag=[mesh_sphere((1.14,.78,.31),(0,-.34,0),'pearl',3),box((2.28,.06,.60),(0,.35,0),'bronze')]
bag.extend([tube([[-.68,.32,0],[-.62,.86,0],[0,1.19,0],[.62,.86,0],[.68,.32,0]],.095,'bronze',14),tube([[.76,.30,.26],[.93,-.13,.30],[1.04,-.54,.33]],.032,'gold'),mesh_sphere((.18,.19,.07),(1.05,-.68,.36),'gold')])
manifest.append(save('bag-charm',bag))
phone=[box((1.45,2.48,.13),(0,0,0),'graphite'),box((1.50,2.53,.05),(0,0,.09),'silverlight')]
for a,b in [(-.47,.91),(-.47,.53),(-.13,.91)]:phone.extend([cyl(.12,.055,(a,b,.16),'black'),cyl(.078,.058,(a,b,.198),'silver')])
manifest.append(save('phone',phone))
tablet=[box((2.35,1.72,.10),(0,0,0),'silver'),box((2.22,1.6,.02),(0,0,-.058),'graphite'),cyl(.10,.05,(-1.02,.66,.08),'black')]
manifest.append(save('tablet',tablet))
macbook=[box((2.60,.12,1.72),(0,-.88,0),'silver'),box((2.58,1.70,.09),(0,.08,.38),'silver'),box((2.45,1.55,.012),(0,.11,.44),'silverlight')]
manifest.append(save('macbook',macbook))
bottle=[cyl(.53,2.55,(0,-.1,0),'graphite'),mesh_sphere((.53,.14,.53),(0,1.14,0),'graphite',2),cyl(.40,.28,(0,1.42,0),'black'),cyl(.51,.08,(0,-1.39,0),'black')]
manifest.append(save('bottle',bottle))
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf8')
print(json.dumps(manifest,indent=2))
