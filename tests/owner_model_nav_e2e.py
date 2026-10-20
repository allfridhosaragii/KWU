"""Owner model library regression: 21 navigable GLB assets on phone/tablet/desktop.
Browser engine in this sandbox does not expose WebGL2. Tests exercise real UI,
responsive nav, model metadata, file selection and 2D fallback, not GPU FPS.
"""
from pathlib import Path
import base64,json
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]
css=(R/'site/assets/style.css').read_text().split('\n',1)[1]
viewer=(R/'site/assets/viewer.js').read_text().replace('export class Viewer3D','class Viewer3D')
app=(R/'site/assets/app.js').read_text().replace("import { Viewer3D } from './viewer.js';",'')
models={p.stem:base64.b64encode(p.read_bytes()).decode() for p in (R/'site/models').glob('*.glb')}
photos={p.stem:base64.b64encode(p.read_bytes()).decode() for p in (R/'site/assets/previews').glob('*.webp')}
expected=['bracelet','ring','necklace','bag-charm','phone','tablet','macbook','bottle', 'iphone-17','iphone-air','iphone-17-pro','iphone-17-pro-max','iphone-17e','ipad-pro-11','ipad-pro-13','ipad-air-11','ipad-air-13','macbook-air-13','macbook-air-15','macbook-pro-14','macbook-pro-16']
report={'viewports':[],'failures':[],'gpu_render_tested':False}
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for width,height in [(320,720),(390,844),(768,1024),(1440,900)]:
  ctx=browser.new_context(viewport={'width':width,'height':height},device_scale_factor=1)
  page=ctx.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.set_content('<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>'+css+'</style></head><body><div id="app"></div></body></html>')
  page.evaluate('''(data)=>{window.KWU_BASE='/';window.__KWU_TEST_MODE=true;window.__KWU_TEST_PATH='/';
  window.fetch=async function(url){const id=String(url).split('/').pop().replace('.glb','');const b64=data.models[id];if(!b64)return new Response('',{status:404});const raw=atob(b64),buf=new Uint8Array(raw.length);for(let i=0;i<raw.length;i++)buf[i]=raw.charCodeAt(i);return new Response(buf,{status:200})};
  new MutationObserver(()=>{document.querySelectorAll('img[src$=".webp"]').forEach(el=>{const id=el.getAttribute('src').split('/').pop().replace('.webp','');if(data.photos[id])el.setAttribute('src','data:image/webp;base64,'+data.photos[id])})}).observe(document,{childList:true,subtree:true});
  }''',{'models':models,'photos':photos})
  page.add_script_tag(content=viewer+'\n'+app)
  page.wait_for_function('window.__KWU_TEST_RENDER!==undefined')
  page.evaluate('''()=>{window.__KWU_TEST_PATH='/login';window.__KWU_TEST_RENDER()}''')
  page.locator('#login-email').fill('owner@example.test');page.locator('#login-role').select_option('owner');page.locator('#login-form button[type="submit"]').click()
  page.evaluate('''()=>{window.__KWU_TEST_PATH='/owner/assets';window.__KWU_TEST_RENDER()}''')
  check_count=0
  def check(cond,message):
   global check_count
   check_count+=1
   if not cond: report['failures'].append(f'{width}px: {message}')
  check(page.locator('.owner-model-link').count()==21,'global owner 3D navigation must show 21 models')
  check(page.locator('.owner-model-card').count()==21,'library must show 21 model cards')
  check(page.locator('.owner-featured-preview canvas').count()==1,'preview must provide 3D canvas')
  check(page.locator('.owner-model-download').count()==21,'each model needs downloadable GLB link')
  check(page.locator('.owner-sidebar-models a').count()==21,'desktop sidebar model links retained in DOM')
  check(page.locator('.owner-sidebar').is_visible()==(width>800),'sidebar visibility adapts to viewport')
  if width<=800:
   check(page.locator('.owner-mobile-nav a[data-nav="/owner/assets"]').count()==1,'owner mobile bottom navigation needs Model 3D')
   check(page.locator('.owner-model-scroll').evaluate('(e)=>getComputedStyle(e).overflowX')=='auto','model nav must scroll horizontally')
  for mid in expected:
   page.evaluate('''(id)=>{window.__KWU_TEST_PATH='/owner/assets?model='+id;window.__KWU_TEST_RENDER()}''',mid)
   chosen=page.evaluate('''()=>document.querySelector('.owner-model-link.active')?.getAttribute('data-nav')''')
   check(chosen==f'/owner/assets?model={mid}',f'active model mismatch {mid}')
   check(page.locator(f'a[download="{mid}.glb"]').count()>=2,f'GLB download missing {mid}')
   check(page.locator('.owner-featured-preview canvas').count()==1,f'preview canvas missing {mid}')
  # restore and visually inspect CSS layout for all routes on a narrow device
  page.evaluate("()=>{window.__KWU_TEST_PATH='/owner/assets';window.__KWU_TEST_RENDER()}")
  check(page.evaluate('document.documentElement.scrollWidth <= window.innerWidth + 2'),'horizontal document overflow')
  if width in (390,1440):page.screenshot(path=str(R/f'qa-owner-models-{width}.png'),full_page=True)
  check(not errors,f'JavaScript errors: {errors[:2]}')
  report['viewports'].append({'width':width,'checks':check_count,'gpu_available':page.evaluate("Boolean(document.createElement('canvas').getContext('webgl2'))")})
  ctx.close()
 browser.close()
(R/'qa-owner-models.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({'viewports':report['viewports'],'failures':report['failures'],'checks':sum(x['checks'] for x in report['viewports'])},ensure_ascii=False,indent=2))
if report['failures']:raise SystemExit(1)
