"""Integrity and catalog consistency audit of all mobile-friendly GLB files."""
from pathlib import Path
import json,struct,hashlib,sys
root=Path(__file__).resolve().parent.parent
catalog=json.loads((root/'site/models/model-catalog.json').read_text())
models=root/'site/models';previews=root/'site/assets/previews'
errors=[];items=[]
expected={*('bracelet','ring','necklace','bag-charm','bottle','phone','tablet','macbook')}
for kind,variants in catalog['groups'].items():
 expected.update(variants.keys())
for name in sorted(expected):
 f=models/(name+'.glb');poster=previews/(name+'.webp')
 if not f.exists():errors.append(name+': missing GLB');continue
 data=f.read_bytes()
 try:
  header=struct.unpack_from('<III',data,0)
  assert header==(0x46546C67,2,len(data))
  jsize,jtype=struct.unpack_from('<II',data,12)
  assert jtype==0x4e4f534a
  obj=json.loads(data[20:20+jsize]);assert len(obj['meshes'])>0
  faces=sum(obj['accessors'][pr['indices']]['count']//3 for mesh in obj['meshes'] for pr in mesh['primitives'])
  assert faces>0
  if len(data)>3.5*1024*1024:errors.append(f'{name}: model exceeds mobile per-scene budget (3.5 MB)')
  if len(obj['meshes'])>150:errors.append(f'{name}: too many separate meshes')
  if not poster.exists() or poster.stat().st_size<1500:errors.append(f'{name}: missing/empty WebP')
  items.append({'asset':name,'bytes':len(data),'triangles':faces,'mesh_count':len(obj['meshes']),'sha256':hashlib.sha256(data).hexdigest()[:16]})
 except Exception as e:errors.append(f'{name}: {e}')
for category,variants in catalog['groups'].items():
 for vid,v in variants.items():
  if len(v['dims_mm'])!=3 or not all(isinstance(x,(int,float)) and x>0 for x in v['dims_mm']):errors.append(f'{vid}: invalid dimension')
  if not v.get('colors') or not str(v.get('source','')).startswith('https://'):errors.append(f'{vid}: missing color/source')
output={'passed':not errors,'files':len(items),'expected':len(expected),'assets':items,'errors':errors,'renderer_real_gpu_tested':False,'accuracy_photogrammetric':False}
(root/'qa-model-audit.json').write_text(json.dumps(output,indent=2,ensure_ascii=False))
print(json.dumps({'passed':output['passed'],'glb':len(items),'expected':len(expected),'errors':errors},indent=2))
if errors:sys.exit(1)
