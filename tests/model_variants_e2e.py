"""Offline browser E2E for 13 Apple device variants, no local HTTP server needed.
Chrome software WebGL verifies actual GLB load, UI model change, saved config.
"""
from __future__ import annotations
import json,base64
from pathlib import Path
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent.parent
CATEGORIES={
'phone':('phone-sticker',['iphone-17','iphone-air','iphone-17-pro','iphone-17-pro-max','iphone-17e']),
'tablet':('tablet-sticker',['ipad-pro-11','ipad-pro-13','ipad-air-11','ipad-air-13']),
'macbook':('laptop-sticker',['macbook-air-13','macbook-air-15','macbook-pro-14','macbook-pro-16'])
}
css=(R/'site/assets/style.css').read_text().split('\n',1)[1]
viewer=(R/'site/assets/viewer.js').read_text().replace('export class Viewer3D','class Viewer3D')
app=(R/'site/assets/app.js').read_text().replace("import { Viewer3D } from './viewer.js';",'')
script=viewer+'\n'+app
models={p.stem:base64.b64encode(p.read_bytes()).decode() for p in (R/'site/models').glob('*.glb')}
photos={p.stem:base64.b64encode(p.read_bytes()).decode() for p in (R/'site/assets/previews').glob('*.webp')}
report={'checks':[],'failures':[]}
def add(name,ok,extra=None):
 report['checks'].append({'name':name,'pass':bool(ok),'extra':extra})
 if not ok:report['failures'].append(name)

with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--enable-unsafe-swiftshader','--enable-webgl','--disable-gpu-sandbox'])
 for width in [390,768,1440]:
  ctx=browser.new_context(viewport={'width':width,'height':844},device_scale_factor=1)
  page=ctx.new_page();errors=[];requested=[];page.on('pageerror',lambda e: errors.append(str(e)))
  page.set_content('<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+css+'</style></head><body><div id="app"></div></body></html>')
  page.evaluate('''()=>{const store={};Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>store[k]||null,setItem:(k,v)=>store[k]=String(v),removeItem:k=>delete store[k]}})}''')
  page.evaluate('''(models)=>{window.KWU_BASE='/';window.__KWU_TEST_MODE=true;window.__KWU_TEST_PATH='/';window.__LOADS=[];window.fetch=async function(url){let key=String(url).split('/').pop().replace('.glb','');window.__LOADS.push(key);if(models[key]){let b=atob(models[key]);let a=new Uint8Array(b.length);for(let i=0;i<b.length;i++)a[i]=b.charCodeAt(i);return new Response(a,{status:200});}return new Response('',{status:404})};}''',models)
  page.evaluate(r'''(photos)=>{const orig=Element.prototype.setAttribute;window.__PHOTOS=photos;new MutationObserver(()=>{document.querySelectorAll('img[src$=".webp"]').forEach(img=>{const m=img.getAttribute('src')?.match(/\/([^\/]+)\.webp$/);if(m&&photos[m[1]])orig.call(img,'src','data:image/webp;base64,'+photos[m[1]])})}).observe(document,{childList:true,subtree:true});}''',photos)
  page.add_script_tag(content=script)
  page.wait_for_timeout(750)
  for kind,(prod,variants) in CATEGORIES.items():
   page.evaluate('''(route)=>{window.__KWU_TEST_PATH=route;window.__KWU_TEST_RENDER()}''',f'/studio/{kind}/{prod}')
   page.wait_for_selector('#device-model-select',timeout=6000)
   for model in variants:
    page.locator('#device-model-select').select_option(model)
    page.wait_for_timeout(250)
    add(f'{width}px/{kind}/{model} selector',page.locator('#device-model-select').input_value()==model)
    webgl=page.evaluate("Boolean(document.createElement('canvas').getContext('webgl2'))")
    good=page.evaluate('model=>window.__LOADS.includes(model)',model) if webgl else page.evaluate('model=>{const img=document.querySelector("#viewer img");return !!img&&img.getAttribute("src")=="data:image/webp;base64,"+window.__PHOTOS[model]}',model)

    add(f'{width}px/{kind}/{model} '+('GLB fetched' if webgl else '2D fallback selected'),good)
   add(f'{width}px/{kind} has WebGL canvas',page.locator('canvas').count()>0)
   add(f'{width}px/{kind} no JS error',not errors,errors[-2:] if errors else None)
  page.evaluate('''()=>{window.__KWU_TEST_PATH='/studio/phone/phone-sticker';window.__KWU_TEST_RENDER()}''')
  page.locator('#device-model-select').select_option('iphone-17-pro')
  page.locator('#case-select').select_option('clear')
  if width==390:page.locator('#viewer').screenshot(path=str(R/'qa-phone-17pro-model-preview.png'))
  page.locator('[data-action="save-design"]').first.click()
  d=page.evaluate("() => JSON.parse(localStorage.getItem('kwu-atelier-demo-v1')||'{}').designs||[]")
  add(f'{width}px saved iPhone choice',bool(d and d[0].get('deviceModel')=='iphone-17-pro'))
  add(f'{width}px saved clear case',bool(d and d[0].get('caseType')=='clear'))
  if width==390: page.screenshot(path=str(R/'qa-phone-17pro-mobile.png'))
  page.evaluate('''()=>{window.__KWU_TEST_PATH='/';window.__KWU_TEST_RENDER()}''')
  add(f'{width}px home after studio',page.locator('.hero').count()==1)
  ctx.close()
 browser.close()
(R/'qa-model-variants.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps({'checks':len(report['checks']),'failures':report['failures']},indent=2))
if report['failures']:raise SystemExit(1)
