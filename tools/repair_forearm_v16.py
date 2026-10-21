"""Remove the jagged MakeHuman forearm cut, preserving skin PBR and jewelry."""
from pathlib import Path
import io
import numpy as np
import trimesh
from scipy.spatial import ConvexHull
from trimesh.visual.texture import TextureVisuals

ROOT=Path(__file__).resolve().parent.parent
CUTOFF_Y=-1.230

def repair(path:Path,cutoff_y:float=CUTOFF_Y):
    original=list(trimesh.load(path,force='scene',process=False).geometry.items())
    body=original[0][1]
    if body.visual.kind!='texture' or len(body.faces)<10000:
        raise ValueError(f'{path}: anatomical PBR body missing')
    y=body.vertices[:,1]
    if y.min()>=cutoff_y-.07 or y.max()<.8:
        raise ValueError(f'{path}: unexpected bounds {y.min()}..{y.max()}')
    clipped=trimesh.intersections.slice_mesh_plane(
        body,plane_normal=(0,1,0),plane_origin=(0,cutoff_y,0),cap=False)
    v=np.asarray(clipped.vertices)
    rim_idx=np.flatnonzero(np.abs(v[:,1]-cutoff_y)<1e-5)
    if len(rim_idx)<8:raise ValueError(f'Invalid wrist perimeter: {len(rim_idx)}')
    hull=ConvexHull(v[rim_idx][:,[0,2]])
    edge=rim_idx[hull.vertices]
    center=v[edge].mean(axis=0);center[1]=cutoff_y
    verts=np.vstack([v,center])
    center_i=len(v)
    faces=np.vstack([clipped.faces,np.asarray([
        [center_i,int(edge[(i+1)%len(edge)]),int(edge[i])]
        for i in range(len(edge))],dtype=np.int64)])
    old_uv=np.asarray(clipped.visual.uv)
    uv=np.vstack([old_uv,old_uv[edge].mean(axis=0)])
    fixed=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
    fixed.visual=TextureVisuals(uv=uv,material=clipped.visual.material)
    if not np.isfinite(verts).all() or len(fixed.faces)<len(body.faces)*.5:
        raise ValueError('Invalid rebuilt forearm')
    assert np.min(fixed.vertices[:,1])>=cutoff_y-1e-5
    scene=trimesh.Scene()
    for i,(name,mesh) in enumerate(original):
        scene.add_geometry(fixed if i==0 else mesh.copy(),geom_name=name)
    blob=scene.export(file_type='glb')
    check=trimesh.load(io.BytesIO(blob),file_type='glb',force='scene',process=False)
    assert len(check.geometry)==len(original)
    assert next(iter(check.geometry.values())).visual.kind=='texture'
    assert min(next(iter(check.geometry.values())).vertices[:,1])>=cutoff_y-1e-4
    path.write_bytes(blob)
    print(f'{path.name}: repaired {np.count_nonzero(y<cutoff_y)} damaged vertices; {len(edge)} cap triangles')

if __name__=='__main__':
    for kind in ('bracelet','ring'):repair(ROOT/'site/models'/f'{kind}.glb')
