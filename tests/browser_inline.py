from pathlib import Path
import base64,re,json
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).parent.parent
css=(ROOT/'site/assets/style.css').read_text().split('\n',1)[1]
viewer=(ROOT/'site/assets/viewer.js').read_text().replace('export class Viewer3D','class Viewer3D')
app=(ROOT/'site/assets/app.js').read_text().replace("import { Viewer3D } from './viewer.js';",'')
script=viewer+'\n'+app
models={p.stem:base64.b64encode(p.read_bytes()).decode() for p in (ROOT/'site/models').glob('*.glb')}
previews={p.stem:base64.b64encode(p.read_bytes()).decode() for p in (ROOT/'site/assets/previews').glob('*.png')}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--enable-unsafe-swiftshader','--enable-webgl','--disable-web-security','--disable-gpu-sandbox'])
 page=browser.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
 errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
 page.set_content('<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>'+css+'</style></head><body><div id="app"></div></body></html>')
 page.evaluate('''(models)=>{window.KWU_BASE='/';window.__KWU_TEST_MODE=true;window.__KWU_TEST_PATH='/';window.__GLB_MODELS=models;window.fetch=async function(url){let key=String(url).split('/').pop().replace('.glb','');if(models[key]){let b=atob(models[key]);let a=new Uint8Array(b.length);for(let i=0;i<b.length;i++)a[i]=b.charCodeAt(i);return new Response(a,{status:200});}return new Response('',{status:404})};}''',models)
 try:
  page.evaluate('''(photos)=>{window.__PHOTOS=photos;function apply(){document.querySelectorAll('img').forEach(img=>{const m=img.getAttribute('src')?.match(/\/([^\/]+)\.png$/);if(m&&photos[m[1]])img.setAttribute('src','data:image/png;base64,'+photos[m[1]])})}new MutationObserver(apply).observe(document,{childList:true,subtree:true});}''',previews)
  page.add_script_tag(type='module',content=script)
  page.wait_for_timeout(1500)
  print('home:',page.locator('body').inner_text()[:250]);print('errors:',errors[:10]);page.screenshot(path=str(ROOT/'test-home.png'),full_page=True)
  page.evaluate('window.__KWU_TEST_PATH="/studio/bracelet/charm-bracelet"')
  # trigger SPA nav through clickable studio link instead
  page.locator('.bottom-nav a[data-nav="/studio"]').click()
  page.locator('a[data-nav="/studio/bracelet/charm-bracelet"]').first.click()
  page.wait_for_timeout(1600)
  print('studio:',page.locator('body').inner_text()[:340]);print('canvas:',page.locator('canvas').count());print('errors:',errors[:10]);page.screenshot(path=str(ROOT/'test-studio.png'),full_page=True)
 except Exception as e:
  print('TEST_ERROR:',str(e)[:1200]);print('errors:',errors)
 finally:browser.close()
