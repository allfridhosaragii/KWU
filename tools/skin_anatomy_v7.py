"""Improve KWU jewelry anatomy skin fidelity with a restrained PBR skin set.

Run after build_anatomical_cc0.py and skin_detail_postprocess_v6.py.
Based on the explicitly CC0 MakeHuman geometry in this repository. This is
procedural artistic skin, not a photogrammetry/medical 1:1 scan. No body hair.

Output: the three GLB body+accessory scenes updated in place. The default
embedded albedo is calibrated around Indonesia's warm sawo-matang tone; the
viewer applies selectable skin tones without recoloring jewelry.
"""
from __future__ import annotations
from pathlib import Path
import io
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import gaussian_filter, sobel
import trimesh
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'site/models'
MATS=ROOT/'assets/materials/anatomy-v7'
MATS.mkdir(parents=True,exist_ok=True)

SKIN_BASE=np.array([184,129,95],dtype=np.float32)  # natural warm sawo-matang studio base


def layered_noise(size:int,seed:int)->tuple[np.ndarray,np.ndarray,np.ndarray]:
    rng=np.random.default_rng(seed)
    def octave(grid:int):
        a=rng.normal(0,1,(grid,grid)).astype(np.float32)
        aa=np.array(Image.fromarray(a,mode='F').resize((size,size),Image.Resampling.BICUBIC),dtype=np.float32)
        aa-=aa.mean(); aa/=max(float(aa.std()),.01)
        return aa
    macro=octave(28)
    meso=octave(145)
    micro=octave(610)
    return macro,meso,micro


def textures(is_face:bool,size:int=768):
    """Albedo + tangent normal + roughness: subtle, no hair, no painted freckles."""
    macro,meso,micro=layered_noise(size,2031 if is_face else 2017)
    Y,X=np.mgrid[:size,:size].astype(np.float32)
    U=X/max(1,size-1);V=Y/max(1,size-1)
    # Broad warm and cool regions, stronger variation around facial cheeks.
    flush=np.exp(-((U-.30)/.13)**2-((V-.56)/.20)**2)+np.exp(-((U-.70)/.13)**2-((V-.56)/.20)**2) if is_face else np.exp(-((V-.72)/.23)**2)*.35
    hue=macro*2.15+meso*.82+micro*.28
    albedo=np.empty((size,size,3),dtype=np.uint8)
    albedo[...,0]=np.clip(SKIN_BASE[0]+hue*1.7+flush*4,0,255)
    albedo[...,1]=np.clip(SKIN_BASE[1]+hue*.95+flush*1.2,0,255)
    albedo[...,2]=np.clip(SKIN_BASE[2]+hue*.72-flush*.8,0,255)
    base=Image.fromarray(albedo,'RGB')
    # Height field for pores at sub-millimetre impression, not large freckles.
    height=(meso*.22+micro*.56+macro*.07).astype(np.float32)
    height=gaussian_filter(height,.48)
    gy,gx=np.gradient(height)
    bump_strength=.085 if is_face else .095
    nx=np.clip(-gx*bump_strength,-.48,.48)
    ny=np.clip(-gy*bump_strength,-.48,.48)
    nz=np.sqrt(np.maximum(.05,1-nx**2-ny**2))
    normal=np.stack(((nx*.5+.5)*255,(ny*.5+.5)*255,(nz*.5+.5)*255),axis=2).astype('uint8')
    norm=Image.fromarray(normal,'RGB')
    # Roughness stored as G channel per glTF metallicRoughnessTexture.
    rough=np.clip(201+meso*4+micro*3+flush*-8,160,235).astype('uint8')
    packed=np.zeros((size,size,3),dtype=np.uint8)
    packed[...,1]=rough
    packed[...,2]=0 # metallic = 0
    mr=Image.fromarray(packed,'RGB')
    return base,norm,mr


def apply(kind:str):
    path=OUT/f'{kind}.glb'
    scene=trimesh.load(path,force='scene',process=False)
    ordered=list(scene.geometry.items())
    if len(ordered)<2:raise RuntimeError(f'{kind}: expected anatomy + jewelry geometry')
    largest=max(range(len(ordered)),key=lambda i:len(ordered[i][1].faces))
    assert largest==0, f'{kind}: body should be mesh 0; got largest at {largest}'
    body=ordered[0][1].copy()
    body_name=ordered[0][0]
    verts=np.asarray(body.vertices)
    n_faces=len(body.faces)
    # Preserve source anatomical silhouette and all jewelry geometry.
    # Only subdivide relatively coarse versions; a much denser mesh is not
    # useful unless derived from a higher-detail measured source.
    if n_faces<25000:
        v,f=trimesh.remesh.subdivide(body.vertices,body.faces)
        body=trimesh.Trimesh(vertices=v,faces=f,process=False)
        trimesh.repair.fix_normals(body)
        verts=np.asarray(body.vertices)
    lo=verts.min(axis=0);hi=verts.max(axis=0);span=np.maximum(hi-lo,.001)
    uv=np.column_stack(((verts[:,0]-lo[0])/span[0],1-(verts[:,1]-lo[1])/span[1]))
    base,normal,rough=textures(kind=='necklace')
    prefix='bust' if kind=='necklace' else 'hand'
    base.save(MATS/f'{prefix}-albedo-sawo-matang.png',compress_level=2)
    normal.save(MATS/f'{prefix}-normal.png',compress_level=2)
    rough.save(MATS/f'{prefix}-roughness.png',compress_level=2)
    material=PBRMaterial(name='KWU_ANATOMICAL_SKIN_V7',baseColorTexture=base,normalTexture=normal,
        metallicRoughnessTexture=rough,baseColorFactor=[255,255,255,255],
        metallicFactor=0.0,roughnessFactor=.83,doubleSided=True)
    body.visual=TextureVisuals(uv=uv,material=material)
    output=trimesh.Scene()
    output.add_geometry(body,geom_name=f'kwu_{kind}_skin_v7')
    for i,(_,mesh) in enumerate(ordered[1:],start=1):
        output.add_geometry(mesh.copy(),geom_name=f'kwu_{kind}_jewelry_{i:02d}')
    data=output.export(file_type='glb')
    test=path.with_suffix('.v7.test.glb');test.write_bytes(data)
    check=trimesh.load(test,force='scene',process=False)
    assert len(check.geometry)==len(ordered), f'{kind}: geometry lost during export'
    skin=next(iter(check.geometry.values()))
    assert isinstance(skin.visual,TextureVisuals)
    assert skin.visual.material.normalTexture is not None, 'Missing skin normal map'
    assert skin.visual.material.metallicRoughnessTexture is not None, 'Missing skin roughness map'
    test.replace(path)
    print(f'{kind}: {sum(len(g.faces) for g in check.geometry.values()):,} triangles, {len(data)/1024/1024:.2f} MiB; {len(ordered)} meshes')


def main():
    for k in ['bracelet','ring','necklace']:apply(k)

if __name__=='__main__':main()
