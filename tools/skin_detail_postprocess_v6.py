"""KWU detailed-skin pass for the anatomical MakeHuman mannequins.

The upstream human base mesh remains unchanged anatomically; it is a CC0
artist mesh, not an actual scan. This pass adds soft skin color micro-variation
and near-neutral physically based roughness to the body geometry in GLB files.
It deliberately adds NO body hair, which is a requirement for KWU jewelry.

Run *after* tools/build_anatomical_cc0.py:
    python tools/skin_detail_postprocess_v6.py

This script can run standalone against any existing v5/v6 GLB collection.
"""
from __future__ import annotations
from pathlib import Path
from PIL import Image
import numpy as np
import trimesh
from scipy.ndimage import gaussian_filter
from trimesh.visual.material import PBRMaterial
from trimesh.visual.texture import TextureVisuals

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'site/models'


def make_skin_map(face:bool, pixels:int=2048)->Image.Image:
    """Tile-safe mostly diffuse albedo, subtle enough to look like skin rather than painted dots."""
    seed=101 if face else 67
    rng=np.random.default_rng(seed)
    # Four frequency bands; suppress harsh artifacts at product-card sizes.
    low=rng.standard_normal((100,100)).astype('float32')
    low=gaussian_filter(low,5.2,mode='wrap')
    low/=max(.0001,float(low.std()))
    low=np.asarray(Image.fromarray(np.uint8(np.clip(127+low*21,0,255)),'L').resize((pixels,pixels),Image.Resampling.BICUBIC),dtype='float32')
    low=(low-127)/21
    medium=rng.standard_normal((pixels,pixels)).astype('float32')
    medium=gaussian_filter(medium,5.1,mode='wrap')
    medium/=max(.0001,float(medium.std()))
    fine=rng.standard_normal((pixels,pixels)).astype('float32')
    fine=gaussian_filter(fine,.8,mode='wrap')
    fine/=max(.0001,float(fine.std()))
    YY,XX=np.ogrid[:pixels,:pixels]
    u=XX/(pixels-1);v=YY/(pixels-1)
    blush=np.broadcast_to(2.1*np.exp(-((v-.53)/.22)**2),(pixels,pixels)).copy()
    if face:
        blush+=3.9*np.exp(-((u-.39)/.1)**2-((v-.60)/.11)**2)
        blush+=3.9*np.exp(-((u-.61)/.1)**2-((v-.60)/.11)**2)
    else:
        blush+=1.3*np.exp(-((v-.69)/.22)**2)
    variation=low*2.2+medium*1.55+fine*.85
    rgb=np.empty((pixels,pixels,3),dtype=np.uint8)
    rgb[:,:,0]=np.clip(220+variation+blush,0,255).astype(np.uint8)
    rgb[:,:,1]=np.clip(179+variation*.55+blush*.22,0,255).astype(np.uint8)
    rgb[:,:,2]=np.clip(157+variation*.38+blush*.13,0,255).astype(np.uint8)
    return Image.fromarray(rgb,'RGB')


def improve_body_mesh(mesh:trimesh.Trimesh,face:bool):
    # Subdivide rather than replacing MakeHuman contours with ellipsoids.
    if len(mesh.faces)<180000:
        v,f=trimesh.remesh.subdivide(mesh.vertices,mesh.faces)
        refined=trimesh.Trimesh(vertices=v,faces=f,process=False)
        trimesh.repair.fix_normals(refined)
    else:
        refined=mesh.copy()
    v=refined.vertices
    low=v.min(axis=0);high=v.max(axis=0)
    extent=np.maximum(high-low,0.0001)
    # Planar anatomical UVs are sufficient for restrained non-directional skin
    # grain; avoids altering the original shape or finger/neck pose.
    uv=np.column_stack(((v[:,0]-low[0])/extent[0], 1-(v[:,1]-low[1])/extent[1]))
    mat=PBRMaterial(
        name='KWU_ANATOMICAL_SKIN_CC0_TEXTURE_V6',
        baseColorTexture=make_skin_map(face),
        baseColorFactor=[255,255,255,255],
        metallicFactor=0.0,
        roughnessFactor=.86,
        doubleSided=True)
    refined.visual=TextureVisuals(uv=uv,material=mat)
    return refined


def update_kind(kind):
    path=OUT/f'{kind}.glb'
    old=trimesh.load(path,force='scene')
    ordered=list(old.geometry.items())
    if len(ordered)<2:raise ValueError(f'{kind} must contain anatomical mesh + jewelry')
    body_i=max(range(len(ordered)),key=lambda j:len(ordered[j][1].faces))
    if body_i!=0:
        # Existing renderer treats geometry 0 as the mannequin, so keep it first.
        ordered.insert(0,ordered.pop(body_i))
    scene=trimesh.Scene()
    for j,(_,m) in enumerate(ordered):
        mm=improve_body_mesh(m,kind=='necklace') if j==0 else m.copy()
        scene.add_geometry(mm,geom_name=f'kwu_{kind}_v6_{j:02d}')
    data=scene.export(file_type='glb')
    dest=path.with_name(path.stem+'.v6.glb');dest.write_bytes(data)
    verify=trimesh.load(dest,force='scene')
    if len(verify.geometry)!=len(ordered):raise ValueError(f'{kind} geometry count lost')
    skin=next(iter(verify.geometry.values()))
    if not isinstance(skin.visual,TextureVisuals):raise ValueError('skin texture not embedded')
    dest.replace(path)
    print(f'{kind}: {sum(len(g.faces) for g in verify.geometry.values()):,} triangles, {len(data):,} bytes, {len(verify.geometry)} meshes')


if __name__=='__main__':
    for kind in ('bracelet','ring','necklace'):update_kind(kind)
