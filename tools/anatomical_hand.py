"""Experimental continuous hand surface for the jewelry prototype.
Not a human scan; anatomy is approximate.  Voxels and smooth union avoid visible
seams between fingers, thumb and palm.  Web GLB remains small.
"""
from __future__ import annotations
import numpy as np
import trimesh
from skimage.measure import marching_cubes
from scipy.ndimage import gaussian_filter


def hand_surface(res:float=.032)->trimesh.Trimesh:
 X,Y,Z=np.meshgrid(np.arange(-1.47,1.10,res),np.arange(-1.46,1.96,res),np.arange(-.45,.50,res),indexing='ij')
 # smoothly varying palm elliptical cross-section
 yc=np.array([-1.35,-1.2,-.95,-.75,-.42,-.1,.20,.45,.67])
 ws=np.array([.265,.31,.37,.44,.55,.63,.64,.59,.50])
 ds=np.array([.19,.235,.248,.251,.247,.244,.222,.195,.14])
 w=np.interp(Y,yc,ws);d=np.interp(Y,yc,ds)
 # superellipse falloff builds more credible dorsum silhouette
 sd=(np.power((X-.012)/w,2)+np.power((Z+.017)/d,2))**.5-1
 sd=sd*np.minimum(w,d)
 # taper caps vertically
 sd=np.maximum(sd,np.maximum(-1.34-Y,Y-.72)*.9)
 
 def smooth_union(a,b,k=.07):
  h=np.maximum(k-np.abs(a-b),0)/k
  return np.minimum(a,b)-h*h*k*.25

 def tapered_segment(a,b,r0,r1,depth=.82):
  a=np.array(a);b=np.array(b);v=b-a;vec2=(v*v).sum()
  t=np.clip(((X-a[0])*v[0]+(Y-a[1])*v[1]+(Z-a[2])*v[2])/vec2,0,1)
  px=a[0]+t*v[0];py=a[1]+t*v[1];pz=a[2]+t*v[2]
  radius=(r0*(1-t)+r1*t)*(1+.07*np.exp(-((t-.43)/.14)**2))
  # tapered cross-section
  dx=(X-px);dy=Y-py;dz=(Z-pz)/depth
  return np.sqrt(dx*dx+dy*dy+dz*dz)-radius

 fingers=[
  ((-.47,.52,.015),(-.52,1.25,.01),(-.55,1.38,-.003),.126),
  ((-.18,.61,.02),(-.17,1.49,.00),(-.15,1.70,-.015),.136),
  ((.14,.62,.02),(.15,1.64,-.04),(.18,1.80,-.028),.135),
  ((.43,.54,.02),(.47,1.33,-.012),(.51,1.53,-.025),.121),
 ]
 for p0,p1,p2,r in fingers:
  sdf=smooth_union(tapered_segment(p0,p1,r,r*.82),tapered_segment(p1,p2,r*.83,r*.69),.06)
  sd=smooth_union(sd,sdf,.11)
 # thumb has a carefully curved shape emerging from left side of palm
 thumb0=(-.53,-.45,.075);thumb1=(-.79,-.18,.085);thumb2=(-1.06,.20,.06)
 td=smooth_union(tapered_segment(thumb0,thumb1,.215,.175),tapered_segment(thumb1,thumb2,.17,.11),.12)
 sd=smooth_union(sd,td,.16)
 # moderate smoothing for voxel edges
 sdf=gaussian_filter(sd,sigma=.55)
 verts,faces,normals,values=marching_cubes(sdf,level=0,spacing=(res,res,res))
 verts+=np.array([-1.47,-1.46,-.45])
 mesh=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
 trimesh.repair.fix_normals(mesh)
 # subtle regional skin shading with very low-amplitude variation
 p=np.asarray(mesh.vertices)
 grain=2*np.sin(p[:,0]*41)*np.sin(p[:,1]*33)+2*np.sin(p[:,2]*49)
 skin=np.column_stack([np.clip(211+grain,0,255),np.clip(170+grain,0,255),np.clip(149+grain,0,255),np.full(len(p),255)]).astype(np.uint8)
 mesh.visual.vertex_colors=skin
 return mesh

if __name__=='__main__':
 mesh=hand_surface()
 print('hand triangles',len(mesh.faces),'vertices',len(mesh.vertices),'watertight',mesh.is_watertight)
 mesh.export('/mnt/data/KWU-working/hand-smooth-test.glb')
