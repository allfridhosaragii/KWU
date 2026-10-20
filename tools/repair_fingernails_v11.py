"""Replace incomplete open nail rims with natural solid nail plates.

The MakeHuman hand GLB builder produces five thin open nail meshes. In the
studio offline renderer these can appear as white holes against the background.
This postprocess keeps the anatomical skin and jewelry untouched, and swaps
only the five specific nail meshes for curved opaque nail plates.
"""
from __future__ import annotations
from pathlib import Path
import numpy as np
import trimesh

ROOT=Path(__file__).resolve().parent.parent
MODELS=ROOT/'site/models'

# Anatomical positions from the CC0 MakeHuman reference after KWU alignment.
NAIL_ANCHORS=[(-.55,1.29),(-.15,1.60),(.18,1.69),(.51,1.43),(-.99,.16)]

def nail_plate(cx:float,cy:float,front_z:float,width:float=.100,length:float=.165):
    solid=trimesh.creation.icosphere(subdivisions=3,radius=1)
    solid.apply_scale([width*.48,length*.47,.012])
    solid.apply_translation([cx,cy,front_z+.015])
    solid.visual.vertex_colors=np.tile(np.array([183,144,129,255],dtype=np.uint8),(len(solid.vertices),1))
    return solid

def repair(name:str):
    file=MODELS/f'{name}.glb'
    scene=trimesh.load(file,force='scene',process=False)
    ordered=list(scene.geometry.items())
    if len(ordered)<3:raise RuntimeError(f'{name}: expected skin + jewelry scene')
    body=ordered[0][1]
    nails=[]
    for i,(key,mesh) in enumerate(ordered[1:],start=1):
        span=np.ptp(mesh.vertices,axis=0)
        center=mesh.bounds.mean(axis=0)
        if (center[1] > .03 and span[0] < .23 and span[1] < .23
            and span[2] < .08 and 250<=len(mesh.faces)<=800):
            nails.append((i,key,mesh))
    if len(nails) not in (0,5):
        raise RuntimeError(f'{name}: ambiguous nail geometry: {len(nails)}; abort to protect jewelry')
    ordered_nails=[]
    if nails:
        for i,key,mesh in nails:
            extent=np.ptp(mesh.vertices,axis=0)
            center=mesh.bounds.mean(axis=0)
            plate=nail_plate(center[0],center[1],mesh.bounds[1,2],extent[0],extent[1])
            ordered[i]=(key,plate)
    else:
        # Anatomical builder without nail submeshes: insert them BEFORE ring and
        # charm so the existing viewer's last-two-objects jewelry rule survives.
        skin_points=np.asarray(body.vertices)
        for i,(cx,cy) in enumerate(NAIL_ANCHORS):
            nearby=skin_points[np.linalg.norm(skin_points[:,:2]-np.array([cx,cy]),axis=1)<.040]
            if len(nearby)<3:
                print(f'{name}: nail anchor mismatch at {i}; preserving original mesh for safety',flush=True)
                return
            z=float(np.quantile(nearby[:,2],.94))
            ordered_nails.append((f'kwu_{name}_nail_v11_{i:02d}',nail_plate(cx,cy,z)))
        ordered=ordered[:1]+ordered_nails+ordered[1:]
    output=trimesh.Scene()
    for key,mesh in ordered:output.add_geometry(mesh,geom_name=key)
    payload=output.export(file_type='glb')
    import io
    check=trimesh.load(file_obj=io.BytesIO(payload),file_type='glb',force='scene')
    assert len(check.geometry)==len(ordered)
    assert len(check.geometry)>=8
    file.write_bytes(payload)
    print(name,': 5 fully capped natural fingernails,',len(payload),'bytes')

if __name__=='__main__':
    for name in ['bracelet','ring']:repair(name)
