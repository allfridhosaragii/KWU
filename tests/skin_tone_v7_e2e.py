"""V7 regression for swatches, selection, saved design and owner navigation.
Browser WebGL may fall back to 2D when software GPU is unavailable.
"""
from __future__ import annotations
from pathlib import Path
import base64,json
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent.parent
css=(R/'site/assets/style.css').read_text().split('\n',1)[1]
viewer=(R/'site/assets/viewer.js').read_text().replace('export class Viewer3D','class Viewer3D')
app=(R/'site/assets/app.js').read_text().replace("import { Viewer3D } from './viewer.js';",'')
assets={kind:base64.b64encode((R/'site/models'/f'{kind}.glb').read_bytes()).decode() for kind in ('bracelet','ring','necklace')}
checks=[]
def check(label,ok):
 checks.append((label,bool(ok)))
 if not ok: print('FAILED',label)
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--enable-unsafe-swiftshader','--enable-webgl'])
 for width in (320,390,768,1440):
  ctx=browser.new_context(viewport={'width':width,'height':844});page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content('<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+css+'</style></head><body><div id="app"></div></body></html>')
  page.evaluate('''()=>{const store={};Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>store[k]||null,setItem:(k,v)=>store[k]=String(v),removeItem:k=>delete store[k]}})}''')
  page.evaluate('''(models)=>{window.KWU_BASE='/';window.__KWU_TEST_MODE=true;window.__KWU_TEST_PATH='/';window.__GLOBS=models;window.fetch=async function(url){let id=String(url).split('/').pop().replace('.glb','');if(models[id]){let b=atob(models[id]),a=new Uint8Array(b.length);for(let i=0;i<b.length;i++)a[i]=b.charCodeAt(i);return new Response(a,{status:200})}return new Response('',{status:404})}}''',assets)
  page.add_script_tag(content=viewer+'\n'+app)
  page.wait_for_timeout(350)
  for kind,product in [('bracelet','charm-bracelet'),('ring','daily-ring'),('necklace','petite-necklace')]:
   page.evaluate('''(r)=>{window.__KWU_TEST_PATH=r;window.__KWU_TEST_RENDER()}''',f'/studio/{kind}/{product}')
   page.wait_for_selector('[data-action="set-skin-tone:sawo-matang"]',timeout=5000)
   check(f'{width}/{kind}/five tones',page.locator('[data-action^="set-skin-tone:"]').count()==5)
   check(f'{width}/{kind}/default sawo',page.locator('[data-action="set-skin-tone:sawo-matang"]').get_attribute('aria-pressed')=='true')
   page.locator('[data-action="set-skin-tone:deep-brown"]').click()
   check(f'{width}/{kind}/select deep',page.locator('[data-action="set-skin-tone:deep-brown"]').get_attribute('aria-pressed')=='true')
   check(f'{width}/{kind}/label updated',page.locator('#skin-tone-name').inner_text()=='Deep Brown')
   page.locator('[data-action="save-design"]').first.click()
   saved=page.evaluate("()=>JSON.parse(localStorage.getItem('kwu-atelier-demo-v1')||'{}').designs||[]")
   check(f'{width}/{kind}/persist tone',bool(saved and saved[0].get('skinTone')=='deep-brown'))
   page.wait_for_timeout(100)
  check(f'{width}/no JS errors',not errors)
  ctx.close()
 browser.close()
report={'passed':all(ok for _,ok in checks),'checks':len(checks),'failures':[name for name,ok in checks if not ok]}
(R/'qa-skin-tone-v7.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
if report['failures']:raise SystemExit(1)
