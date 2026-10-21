"""Verify final anatomical models no longer contain old sawtooth base."""
from pathlib import Path
import trimesh
import numpy as np

ROOT=Path(__file__).resolve().parent.parent
for name in ('bracelet','ring'):
    scene=trimesh.load(ROOT/'site/models'/f'{name}.glb',force='scene',process=False)
    body=next(iter(scene.geometry.values()))
    p=np.asarray(body.vertices)
    assert body.visual.kind=='texture' and len(scene.geometry)>=3
    assert -1.231<p[:,1].min()<-1.229,(name,'ragged old cut',p[:,1].min())
    assert (np.abs(p[:,1]+1.23)<1e-4).sum()>25,(name,'missing cap')
    assert np.isfinite(p).all()
    print(f'{name}: wrist plane clean, PBR and jewelry preserved')
