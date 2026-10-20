"""Synchronize glTF catalog with actual output files after V5 asset generation."""
from pathlib import Path
import json,struct
R=Path(__file__).resolve().parent.parent
M=R/'site/models'
for name in ('manifest.json','model-catalog.json'):
 path=M/name;obj=json.loads(path.read_text(encoding='utf8'))
 items=obj['models'] if isinstance(obj,dict) else obj
 for o in items:
  f=M/o['file']
  if not f.exists():continue
  b=f.read_bytes();ln=struct.unpack_from('<I',b,12)[0];scene=json.loads(b[20:20+ln]);
  faces=sum(scene['accessors'][p['indices']]['count']//3 for mesh in scene['meshes'] for p in mesh['primitives'])
  if 'bytes' in o:o['bytes']=len(b)
  if 'triangles' in o:o['triangles']=faces
  if 'meshes' in o:o['meshes']=len(scene['meshes'])
  if o['id'] in ('bag-charm','bottle'):
   o['status']='user-photo-projected-front-v5';o['fidelity']='one photographed side; side/back inferred'
  elif o['id'] in ('bracelet','ring','necklace'):o['status']='high-density-procedural-v5'
  elif o['id'].startswith(('iphone-','ipad-','macbook-')):o['status']='manufacturer-dimensioned-procedural-v5'
 path.write_text(json.dumps(obj,indent=2,ensure_ascii=False),encoding='utf8')
print('Catalog synchronized')
