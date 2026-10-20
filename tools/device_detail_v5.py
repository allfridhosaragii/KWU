"""Additional hard-surface detail for Apple-like reference previews.

Meshes are original approximations. Manufacturer dimensions come from the
existing catalog; not official Apple CAD, textures or manufacturer endorsement.
"""
from __future__ import annotations
import sys,json,math
from pathlib import Path
import numpy as np
from PIL import Image,ImageDraw,ImageFilter
import trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals
sys.path.insert(0,str(Path(__file__).resolve().parent))
from make_models_v2 import APPLE_PHONES,APPLE_TABLETS,APPLE_LAPTOPS,torus,cylinder,sphere,paint
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'site/models'


def logo_texture():
 # Brand symbol from Font Awesome Free icons (CC BY 4.0), attributions below.
 import cairosvg,io
 svg=ROOT/'assets/sources/apple-symbol-fontawesome.svg'.read_bytes()
 rendered=cairosvg.svg2png(bytestring=svg,output_width=512,output_height=512)
 icon=Image.open(io.BytesIO(rendered)).convert('RGBA')
 alpha=icon.getchannel('A')
 tinted=Image.new('RGBA',icon.size,(65,67,68,255));tinted.putalpha(alpha)
 return tinted

LOGO=logo_texture()

def logo_plane(w,h,cx,cy,z):
 vs=[(cx-w/2,cy-h/2,z),(cx+w/2,cy-h/2,z),(cx+w/2,cy+h/2,z),(cx-w/2,cy+h/2,z)]
 f=[(0,1,2),(0,2,3)]
 m=trimesh.Trimesh(vertices=vs,faces=f,process=False)
 # Matching the GLB UV axis verified via software GLB importer.
 mat=PBRMaterial(name='photo_projected_device_mark',baseColorTexture=LOGO,
    metallicFactor=0,roughnessFactor=1,alphaMode='BLEND',doubleSided=False)
 m.visual=TextureVisuals(uv=np.array([(0,0),(1,0),(1,1),(0,1)],dtype=np.float32),material=mat)
 return m

def lens_rings(center_z,x,y,r=.116):
 out=[]
 for rr,th,col,dz in [(.125,.010,(174,179,185),-.014),(.107,.009,(27,33,41),.004),(.090,.006,(86,113,137),.014),(.074,.003,(12,19,29),.016)]:
  out.append(torus(rr,th,(x,y,center_z+dz),col,axis='z',sections=64,tube_segments=12))
 # tiny blue reflection polygon on the spherical optical glass
 out.append(sphere((.014,.028,.006),(x-.03,y+.035,center_z+.028),(159,199,219),2))
 return out

def upgrade(name,kind,obj):
 path=OUT/f'{name}.glb';scene=trimesh.load(path,force='scene')
 meshes=[]
 if kind=='phone':
  W,H,D=obj['dims_mm'];fac=2.55/H;w=W*fac;h=2.55;d=D*fac;cam=obj['cam']
  if cam=='pro': centers=[(-w*.310,h*.403),(-w*.310,h*.245),(-w*.11,h*.330)];cz=d/2+.17
  elif cam=='air':centers=[(-w*.34,h*.397)];cz=d/2+.13
  elif cam=='single':centers=[(-w*.275,h*.345)];cz=d/2+.13
  else:centers=[(-w*.29,h*.412),(-w*.29,h*.264)];cz=d/2+.13
  for x,y in centers:meshes.extend(lens_rings(cz,x,y))
  meshes.append(logo_plane(w*.32,w*.32,0,-h*.05,d/2+.043))
 elif kind=='tablet':
  W,H,D=obj['dims_mm'];fac=2.90/max(W,H);w=W*fac;h=H*fac;d=D*fac
  meshes.extend(lens_rings(d/2+.07,-w*.37,h*.38,r=.084))
  meshes.append(logo_plane(w*.24,w*.24,0,0,d/2+.03))
 else:
  # Lid outer cover faces forward (+Z) in the renderer, separate from keyboard.
  meshes.append(logo_plane(.36,.36,0,1.12,.22+.082/2+.007))
 for i,m in enumerate(meshes):scene.add_geometry(m,geom_name=f'{name}__optical_v5_{i:02d}')
 b=scene.export(file_type='glb');path.write_bytes(b)
 return {'asset':name,'bytes':len(b),'meshes':len(scene.geometry),'triangles':sum(len(m.faces) for m in scene.geometry.values())}

if __name__=='__main__':
 result=[]
 for group,kind in [(APPLE_PHONES,'phone'),(APPLE_TABLETS,'tablet'),(APPLE_LAPTOPS,'macbook')]:
  for name,obj in group.items():result.append(upgrade(name,kind,obj))
 for name,origin in [('phone','iphone-17'),('tablet','ipad-pro-11'),('macbook','macbook-air-13')]:
  (OUT/f'{name}.glb').write_bytes((OUT/f'{origin}.glb').read_bytes())
 (ROOT/'assets/metadata/DEVICE_DETAIL_V5.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf8')
 print('Detailed devices',len(result),'total bytes',sum(r['bytes'] for r in result))
