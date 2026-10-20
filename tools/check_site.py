"""Offline static export audit: no external deps, intended for CI."""
import json,struct,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
required=[ROOT/'site/index.html',ROOT/'site/404.html',ROOT/'site/assets/app.js',ROOT/'site/assets/viewer.js',ROOT/'site/assets/style.css',ROOT/'src/app.ts',ROOT/'src/viewer.ts',ROOT/'package.json',ROOT/'tsconfig.json']
kinds=['bracelet','ring','necklace','bag-charm','phone','tablet','macbook','bottle']
errors=[];info=[]
for p in required:
 if not p.is_file() or p.stat().st_size<20:errors.append(f'Missing/empty required file: {p.relative_to(ROOT)}')
for kind in kinds:
 p=ROOT/'site/models'/f'{kind}.glb';q=ROOT/'site/assets/previews'/f'{kind}.webp'
 if not p.is_file():errors.append(f'Missing {kind} GLB');continue
 try:
  b=p.read_bytes();magic,version,size=struct.unpack_from('<III',b)
  assert magic==0x46546c67 and version==2 and size==len(b)
  jsize,jtype=struct.unpack_from('<II',b,12)
  assert jtype==0x4e4f534a
  gltf=json.loads(b[20:20+jsize]);assert gltf.get('meshes') and gltf.get('accessors')
  tris=0
  for mesh in gltf['meshes']:
   for prim in mesh['primitives']:
    tris+=gltf['accessors'][prim['indices']]['count']//3
  assert tris>0
  info.append(f'{kind}: {tris} triangles, {len(b)//1024} KiB')
 except Exception as e:errors.append(f'Invalid GLB {kind}: {e}')
 if not q.exists() or q.stat().st_size<1000:errors.append(f'Missing {kind} preview')
 # Higher fidelity for anatomy is intentional. These GLBs load only when
 # their Studio category is opened; catalog cards use lightweight posters.
 budget_mb=16 if kind in {'bracelet','ring','necklace'} else 3
 if p.stat().st_size>budget_mb*1024*1024:
  errors.append(f'{kind} exceeds {budget_mb} MB per-model transfer budget')
# Every selectable Apple variant must have its own GLB and poster.
try:
 catalog=json.loads((ROOT/'site/models/model-catalog.json').read_text(encoding='utf8'))
 for family,variants in catalog['groups'].items():
  for vid in variants:
   if not (ROOT/'site/models'/f'{vid}.glb').is_file():errors.append(f'Missing variant GLB: {vid}')
   if not (ROOT/'site/assets/previews'/f'{vid}.webp').is_file():errors.append(f'Missing variant preview: {vid}')
except Exception as e: errors.append(f'Invalid model catalog: {e}')
src=(ROOT/'src/app.ts').read_text(encoding='utf8')
for path in ['/shop','/studio','/cart','/checkout','/help','/about','/login','/register','/account','/owner']:
 if path not in src:errors.append(f'Route absent from source: {path}')
if 'DEMO INTERAKTIF KWU' in src:errors.append('Global demo banner must remain removed')
if 'Mode demonstrasi: tombol di bawah hanya membuat pesanan lokal' not in src:errors.append('Checkout must disclose simulated payments')
if 'Ini bukan autentikasi sungguhan' not in src:errors.append('Login must disclose local-only authentication')
if 'DOMPurify' in src:pass
site_size=sum(p.stat().st_size for p in (ROOT/'site').rglob('*') if p.is_file())
# Entire site size is not initial-page transfer size; 3D assets load lazily.
if site_size>70*1024*1024:errors.append('Static site exceeds 70 MB total asset archive budget')
report={'passed':not errors,'models':info,'static_site_bytes':site_size,'issues':errors}
(ROOT/'qa-static-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))
sys.exit(1 if errors else 0)
