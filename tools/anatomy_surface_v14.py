"""KWU V14 anatomical surface quality improvement.

Keeps the CC0 MakeHuman body and PBR texture UVs intact, relaxes only the
anatomical body surface, leaves rings/chains/nails untouched.
This does not constitute a human scan or a claim of photorealistic 1:1 anatomy.
"""
from __future__ import annotations
from pathlib import Path
import io
import numpy as np
import trimesh

ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'site/models'

def refine(name:str):
    path=OUT/f'{name}.glb'
    scene=trimesh.load(path,force='scene',process=False)
    original=list(scene.geometry.items())
    if not original or len(original[0][1].faces)<10000:
        raise RuntimeError(f'{name}: missing anatomical base')
    first,body=original[0]
    if body.visual.kind!='texture':
        raise RuntimeError(f'{name}: anatomical material lost')
    improved=body.copy()
    before=np.array(improved.vertices,copy=True)
    iterations=7 if name!='necklace' else 4
    trimesh.smoothing.filter_humphrey(improved,alpha=.10,beta=.45,iterations=iterations)
    displacement=np.linalg.norm(improved.vertices-before,axis=1)
    extent=np.ptp(before,axis=0)
    maximum=float(displacement.max())
    if not np.isfinite(improved.vertices).all():
        raise RuntimeError(f'{name}: nonfinite geometry')
    # The current MakeHuman hand has sharper boundary vertices than the V7
    # local reference. Cap displacement rather than aborting or distorting nails.
    limit=float(max(extent))*.008
    if maximum>limit:
        ratio=limit/maximum
        improved.vertices=before+(improved.vertices-before)*ratio
        displacement=np.linalg.norm(improved.vertices-before,axis=1)
        maximum=float(displacement.max())
    if maximum>limit*1.0001:
        raise RuntimeError(f'{name}: smoothing cap violated {maximum:.5f}>{limit:.5f}')
    if improved.faces.shape!=body.faces.shape or improved.visual.kind!='texture':
        raise RuntimeError(f'{name}: topology or UV material changed')
    output=trimesh.Scene()
    for i,(key,mesh) in enumerate(original):
        output.add_geometry(improved if i==0 else mesh.copy(),
                            geom_name=f'{key}_surface_v14' if i==0 else key)
    blob=output.export(file_type='glb')
    verify=trimesh.load(file_obj=io.BytesIO(blob),file_type='glb',force='scene')
    if len(verify.geometry)!=len(original) or next(iter(verify.geometry.values())).visual.kind!='texture':
        raise RuntimeError(f'{name}: corrupted result')
    path.write_bytes(blob)
    print(f'{name}: smoothed {len(improved.faces):,} faces; mean={displacement.mean():.5f} max={maximum:.5f}',flush=True)

if __name__=='__main__':
    for kind in ('bracelet','ring','necklace'):refine(kind)
