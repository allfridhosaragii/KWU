"""Build source-photo-referenced 3D relief surfaces and material-backed GLB assets.

The front texture is from photographs furnished by the product owner.
The original material geometry is maintained for side and back views; only front
photograph is matched. A single view cannot establish literal 1:1 back shape.
All 3D mesh data and texture maps are saved in standalone GLB files.
"""
from __future__ import annotations
import json, math, sys
from pathlib import Path
import numpy as np
import cv2
import trimesh
from PIL import Image, ImageFilter
from trimesh.visual.texture import TextureVisuals
from trimesh.visual.material import PBRMaterial

BASE=Path(__file__).resolve().parent.parent
SOURCE=BASE/'site/assets/references'
MODEL=BASE/'site/models'; MODEL.mkdir(parents=True,exist_ok=True)
TEXTURES=BASE/'assets/materials'; TEXTURES.mkdir(parents=True,exist_ok=True)


def matte_rgba(src:Path, kind:str, out:Path):
    rgb=np.asarray(Image.open(src).convert('RGB'))
    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    if kind in ('bag','bag-charm'):
        # The near-black fabric is strongly separated from white photo backdrop.
        mask=np.where(gray<235,255,0).astype(np.uint8)
        n, lab, stats, centers=cv2.connectedComponentsWithStats(mask)
        big=np.zeros_like(mask)
        for i in range(1,n):
            if stats[i,cv2.CC_STAT_AREA]>420: big[lab==i]=255
        mask=cv2.morphologyEx(big,cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
        mask[950:,:]=0
        box=(187,39,838,930)
    else:
        # Stainless shoulder profile recovered from provided frontal photograph.
        # Exclude the black cap and carabiner, which have real 3D geometry.
        mask=np.zeros_like(gray)
        control=[(149,446,578),(170,450,586),(190,451,599),(210,435,615),
                 (230,408,630),(245,393,642),(260,386,642),
                 (900,386,642),(956,394,638)]
        cy=np.array([q[0] for q in control],float)
        lx=np.array([q[1] for q in control],float)
        rx=np.array([q[2] for q in control],float)
        for y in range(149,957):
            xmin=int(np.interp(y,cy,lx));xmax=int(np.interp(y,cy,rx))
            mask[y,xmin:xmax+1]=255
        box=(372,145,665,966)
    mask=cv2.GaussianBlur(mask,(3,3),0.7)
    im=np.dstack([rgb,mask])
    rgba=Image.fromarray(im,'RGBA').crop(box)
    rgba.save(out,optimize=True)
    return rgba,box


def projected_grid(kind:str, im:Image.Image, bounds, divisions=(42,70)):
    """UV texture applied to displaced front mesh. Normal geometry behind stays 3D."""
    l,t,r,b=bounds
    nu,nv=divisions
    verts=[];uv=[];faces=[]
    for j in range(nv+1):
        v=j/nv
        py=t+(b-t)*v
        for i in range(nu+1):
            u=i/nu
            px=l+(r-l)*u
            if kind=='bag':
                x=(px-513.0)*.00406
                y=(488.0-py)*.00395
                # Draped fabric bulge follows front pockets. Sides recede.
                front=.50
                lower=1/(1+math.exp(np.clip((py-625)/19.,-50,50)))
                # Actual front pocket lies below image row 625.
                front+=.09*(1-lower)
                front+=.014*math.cos(x*2.8)*math.cos(y*1.8)
                z=front+.03
            else:
                x=(px-512.5)*(.90/256.)
                y=(535.0-py)*(.00342)
                if py<154: radius=.31
                elif py<255: radius=.31+(.445-.31)*(py-154)/101
                else: radius=.447
                # Project onto front half of curved stainless shell.
                z=math.sqrt(max(.0008,radius**2-x**2))+.010
            verts.append((x,y,z))
            uv.append((u,1.0-v))
    for j in range(nv):
        for i in range(nu):
            a=j*(nu+1)+i;bb=a+1;c=a+nu+2;d=a+nu+1
            faces.extend([(a,c,bb),(a,d,c)])
    mesh=trimesh.Trimesh(vertices=np.array(verts),faces=faces,process=False)
    # PBR material: photo is already lit, viewer marks photo_proj for no extra baking.
    material=PBRMaterial(name=f'photo_projected_{kind}_front', baseColorTexture=im,
        baseColorFactor=[255,255,255,255],roughnessFactor=0.98,
        metallicFactor=0.0,alphaMode='BLEND',doubleSided=False)
    mesh.visual=TextureVisuals(uv=np.array(uv,dtype=np.float32),material=material)
    return mesh


def generate(kind, source_file):
    texture_file=TEXTURES/f'{kind}_reference_front_rgba.png'
    im,bounds=matte_rgba(source_file,kind,texture_file)
    scene=trimesh.load(MODEL/f'{kind}.glb',force='scene')
    if kind=='bag-charm':
        # Remove the demonstrator charm; shoppers add their own from customizer.
        scene.delete_geometry('bag-charm__mesh030')
        scene.delete_geometry('bag-charm__mesh031')
    # Keep original geometry, but add photo surface as a named extra mesh.
    photographic=projected_grid('bag' if kind=='bag-charm' else 'bottle',im,bounds,
        divisions=(56,78) if kind=='bag-charm' else (42,96))
    scene.add_geometry(photographic,geom_name=f'photo_projected_{kind}_front',node_name=f'photo_{kind}')
    data=scene.export(file_type='glb')
    target=MODEL/f'{kind}.glb'
    target.write_bytes(data)
    again=trimesh.load(target,force='scene')
    meshes=len(again.geometry);tris=sum(len(x.faces) for x in again.geometry.values())
    result={'model':kind,'size_bytes':len(data),'triangles':tris,'meshes':meshes,
        'reference':str(source_file),'texture_png':str(texture_file),
        'front_projection':'photographic texture onto 3d relief',
        'known_limit':'unobserved side and rear remain inferred, not a 1:1 reconstruction'}
    print(json.dumps(result,ensure_ascii=False))
    return result

if __name__=='__main__':
    results=[generate('bag-charm',SOURCE/'backpack-user.jpeg'),generate('bottle',SOURCE/'bottle-user.jpeg')]
    (BASE/'assets/metadata/PHOTO_PROJECTION_V5.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
