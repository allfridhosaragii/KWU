"""Produce anatomically grounded jewelry bodies from the CC0 MakeHuman base mesh.

The upstream human mesh is artwork, *not* a medical scan. Transformations are
intended for retail preview scenes, not manufacturing/clinical measurement.
Source provenance: makehumancommunity/makehuman, makehuman/data/3dobjs/base.obj
The source declares CC0 explicitly in its own header (September 2020).
"""
from __future__ import annotations
import os
from pathlib import Path
import numpy as np
import trimesh
from scipy.spatial import cKDTree

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / 'assets/upstream/makehuman/base.obj'
OUT = ROOT / 'site/models'


def read_base():
    vertices = []
    faces = []
    for line in SOURCE.open(encoding='utf-8'):
        if line.startswith('v '):
            vertices.append(tuple(float(k) for k in line.split()[1:4]))
        elif line.startswith('f '):
            ix = [int(k.split('/')[0])-1 for k in line.split()[1:]]
            if max(ix) >= 13380 or min(ix) < 0:
                continue  # skip joint cubes / helper mesh geometry
            for j in range(1, len(ix)-1):
                faces.append((ix[0], ix[j], ix[j+1]))
    m = trimesh.Trimesh(vertices=np.asarray(vertices[:13380]),faces=faces,process=False)
    m.remove_unreferenced_vertices()
    assert len(m.faces)>10000, f'Upstream anatomy unexpectedly small: {len(m.faces)}'
    return m


def crop_mesh(mesh, normal, point):
    # Slice through a joint/torso boundary, preserve original complex anatomy.
    result=trimesh.intersections.slice_mesh_plane(mesh,plane_normal=normal,plane_origin=point,cap=False)
    result.remove_unreferenced_vertices()
    assert len(result.faces)>100, 'Anatomical crop unexpectedly empty'
    return result


def human_skin(mesh,head=False):
    p=np.asarray(mesh.vertices)
    x,y,z=p[:,0],p[:,1],p[:,2]
    # Restrained color variation rather than noisy synthetic freckles.
    # Material remains a non-hairy, matte skin suitable for jewelry photography.
    warm = 2.0*np.sin(6.3*x+3.2*y)*np.sin(4.1*z)
    if head:
        cheek = 6*np.exp(-((np.abs(x)-.33)/.31)**2 - ((y-.75)/.34)**2)
        lips = 6*np.exp(-(x/.28)**2 - ((y-.48)/.10)**2)
        warm += cheek + lips
    base=np.column_stack([np.full(len(p),210.0),np.full(len(p),170.0),np.full(len(p),151.0)])
    base[:,0]+=warm
    base[:,1]+=warm*.30
    base[:,2]+=warm*.12
    m=mesh.copy()
    m.visual.vertex_colors=np.column_stack([np.clip(base,0,255).astype(np.uint8),np.full(len(p),255,np.uint8)])
    return m


def align_hand(mesh):
    # Original MakeHuman pose: right arm extended, wrist near (-4.31,2.45,1.75).
    # New axes center the palm vertically; fingertips point toward the top.
    p=np.asarray(mesh.vertices)
    root=np.array([-4.31,2.45,1.74])
    vertical=np.array([.19,-.25,.95]);vertical/=np.linalg.norm(vertical)
    horizontal=np.array([-.97,0.0,.2]);horizontal-=vertical*np.dot(horizontal,vertical);horizontal/=np.linalg.norm(horizontal)
    front=np.cross(horizontal,vertical);front/=np.linalg.norm(front)
    rel=p-root
    coords=np.column_stack((rel@horizontal*1.35,rel@vertical*1.35-.85,rel@front*1.18+.17))
    coords[:,2] -= np.median(coords[:,2])*.45
    m=mesh.copy();m.vertices=coords
    # Source may be flipped by the reorientation; update normals after mapping.
    trimesh.repair.fix_normals(m)
    return human_skin(m)


def align_bust(mesh):
    p=np.asarray(mesh.vertices)
    coords=np.column_stack((p[:,0]*.67,(p[:,1]-6.28)*.79,(p[:,2]-.6)*.73))
    m=mesh.copy();m.vertices=coords
    trimesh.repair.fix_normals(m)
    return human_skin(m,head=True)


def make_chain(mesh):
    """Follow anterior bust surface rather than float inside the model."""
    from trimesh.creation import cylinder
    p=np.asarray(mesh.vertices)
    tree=cKDTree(p[:,:2]);out=[]
    # A fine cable necklace draped as a continuous U shape.
    control=np.array([[-.29,-.12],[-.32,-.28],[-.30,-.47],[-.19,-.65],[0,-.79],[.19,-.65],[.30,-.47],[.32,-.28],[.29,-.12]])
    pts=[]
    for i in range(len(control)-1):
        for t in np.linspace(0,1,18,endpoint=False):
            xy=control[i]*(1-t)+control[i+1]*t
            _,idx=tree.query(xy,k=60)
            # Use highest/frontmost z among near-surface vertices, not average
            near=p[np.atleast_1d(idx)]
            d=np.linalg.norm(near[:,:2]-xy,axis=1)
            local=near[d<.17]
            if len(local)==0:local=near[:12]
            z=float(np.percentile(local[:,2],85))+.052
            pts.append([xy[0],xy[1],z])
    pts.append([control[-1,0],control[-1,1],pts[-1][2]])
    for a,b in zip(pts[:-1],pts[1:]):
        a,b=np.array(a),np.array(b);d=b-a
        if np.linalg.norm(d)<1e-4:continue
        tube=trimesh.creation.cylinder(radius=.0105,segment=[a,b],sections=9)
        tube.visual.vertex_colors=[199,167,104,255]
        out.append(tube)
    # Pearl pendant at the actual bottom of the chain; delicately colored.
    pendant=trimesh.creation.icosphere(subdivisions=2,radius=.108)
    pendant.apply_scale([.67,1.22,.48]);pendant.apply_translation(pts[len(pts)//2]+np.array([0,-.09,.045]))
    pendant.visual.vertex_colors=[238,226,207,255]
    chain = trimesh.util.concatenate(out)
    chain.visual.vertex_colors = [199,167,104,255]
    return [chain, pendant]


def jewelry_for_hand(name, hand):
    from make_models_v2 import torus,sphere
    if name=='bracelet':
        # Approximate bracelet around the anatomical wrist section.
        # Fit the bracelet to the actual mesh circumference at wrist height.
        hv=np.asarray(hand.vertices);by=-.89
        section=hv[np.abs(hv[:,1]-by)<.13]
        if len(section)>24:
            cx,cz=np.median(section[:,0]),np.median(section[:,2])
            rx=max(.18,np.ptp(np.quantile(section[:,0],[.05,.95]))*.5+.07)
            rz=max(.16,np.ptp(np.quantile(section[:,2],[.05,.95]))*.5+.07)
        else: cx,cz,rx,rz=0,.17,.30,.24
        ring=torus(1.,.10,(0,0,0),(200,190,177),axis='y',sections=96,tube_segments=18)
        ring.apply_scale([rx,.34,rz]);ring.apply_translation([cx,by,cz])
        charm=sphere((.07,.08,.045),(cx-.12,by-.035,cz+rz+.03),(219,185,134),3)
    else:
        ring=torus(.145,.021,(.82,.60,-.52),(205,167,103),axis='y',sections=70,tube_segments=14)
        charm=sphere((.064,.038,.050),(.82,.62,-.275),(232,222,204),3)
    return [ring,charm]


def face_eyes():
    # Use face bone anchors from MakeHuman default rig; these subtle eye surfaces
    # occupy anatomical sockets rather than the original unfilled eye helper voids.
    from make_models_v2 import sphere
    out=[]
    for x in (-.206,.206):
        out.append(sphere((.087,.047,.026),(x,.793,.51),(233,227,219),3))
        out.append(sphere((.032,.032,.011),(x,.793,.54),(78,66,58),3))
        out.append(sphere((.014,.014,.007),(x,.793,.553),(30,26,25),2))
    return out


def save(name, meshes):
    scene=trimesh.Scene()
    for i,m in enumerate(meshes):
        scene.add_geometry(m,geom_name=f'kwu_{name}_{i:02d}')
    path=OUT/f'{name}.glb'
    path.write_bytes(scene.export(file_type='glb'))
    assert path.stat().st_size>10000
    print(f'{name}: {sum(len(m.faces) for m in meshes):,} triangles / {path.stat().st_size:,} bytes')


def build():
    assert SOURCE.exists(), f'Missing MakeHuman CC0 source: {SOURCE}'
    base=read_base()
    # Negative X is the character's right hand. Crop before elbows to focus jewelry.
    # Crop normal to the anatomical wrist-to-finger axis, not across the forearm.
    # A second lateral crop excludes unrelated body geometry.
    wrist=np.array([-4.31,2.45,1.74]);direction=np.array([.19,-.25,.95]);direction/=np.linalg.norm(direction)
    hand_raw=crop_mesh(base,normal=[-1,0,0],point=[-3.45,0,0])
    hand_raw=crop_mesh(hand_raw,normal=direction,point=wrist-.38*direction)
    hv,hf=trimesh.remesh.subdivide(hand_raw.vertices,hand_raw.faces)
    hand=align_hand(trimesh.Trimesh(vertices=hv,faces=hf,process=False))
    # Shoulder, collarbone, neck, chin, lips, nose, eyes and skull share source topology.
    bust_raw=crop_mesh(base,normal=[0,1,0],point=[0,4.86,0])
    bv,bf=trimesh.remesh.subdivide(bust_raw.vertices,bust_raw.faces)
    bust=align_bust(trimesh.Trimesh(vertices=bv,faces=bf,process=False))
    assert len(hand.faces)>900 and len(bust.faces)>1400
    for n in ('bracelet','ring'):save(n,[hand,*jewelry_for_hand(n,hand)])
    save('necklace',[bust,*make_chain(bust),*face_eyes()])

if __name__=='__main__':
    build()
