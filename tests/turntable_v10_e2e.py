"""Proof of interactive GPU-free rotation: verify visible frame changes on drag and buttons.
Test environment intentionally has WebGL disabled, so this does not claim a GPU test.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
import json,base64
ROOT=Path(__file__).resolve().parents[1]
CSS=(ROOT/'site/assets/style.css').read_text()
manifest=json.loads((ROOT/'site/assets/turntables/manifest.json').read_text())
frame_data=base64.b64encode((ROOT/'site/assets/turntables/bracelet.webp').read_bytes()).decode()
turntable=(ROOT/'site/assets/turntable.js').read_text().replace('export class Turntable360','class Turntable360')
# In the offline harness use embedded image data to isolate browser interactions from restricted networking.
turntable=turntable.replace('im.src = `${this.base}assets/turntables/${meta.name}${toneSuffix}.webp?v=${manifest.version}`;',f"im.src = 'data:image/webp;base64,{frame_data}';")
viewer=(ROOT/'site/assets/viewer.js').read_text().replace("import { Turntable360 } from './turntable.js';",'').replace('export class Viewer3D','class Viewer3D')
app=(ROOT/'site/assets/app.js').read_text().replace("import { Viewer3D } from './viewer.js';",'')
result=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':390,'height':860})
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 if True:
  page.set_content('<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style>'+CSS+'</style></head><body><div id="app"></div></body></html>')
  page.evaluate('''()=>{const mem={};Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:k=>mem[k]||null,setItem:(k,v)=>mem[k]=String(v),removeItem:k=>delete mem[k]}})}''')
  page.evaluate("""()=>{window.KWU_BASE='/';window.__KWU_TEST_MODE=true;window.__KWU_TEST_PATH='/studio/bracelet/charm-bracelet'}""")
  page.evaluate('(manifest)=>{window.fetch=async()=>({ok:true,json:async()=>manifest});}',manifest)
  page.add_script_tag(content=turntable+'\n'+viewer+'\n'+app)
  page.wait_for_function("document.querySelector('.kwu-turntable[data-frame]') !== null",timeout=10000)
 for width in [320,390,768,1440]:
  page.set_viewport_size({'width':width,'height':860})
  stage=page.locator('.kwu-turntable')
  page.locator('[data-action="reset-camera"]').first.click()
  before=int(stage.get_attribute('data-frame'))
  page.locator('[data-action="rotate-view-right"]').click()
  after=int(stage.get_attribute('data-frame'))
  assert before!=after,(width,before,after);result.append((width,'button',before,after))
  rect=stage.bounding_box();assert rect
  x,y=rect['x']+rect['width']*.5,rect['y']+rect['height']*.5
  page.mouse.move(x,y);page.mouse.down();page.mouse.move(x+100,y+4,steps=8);page.mouse.up()
  dragged=int(stage.get_attribute('data-frame'))
  assert dragged!=after,(width,dragged,after);result.append((width,'drag',after,dragged))
  a=page.locator('.kwu-turntable-sprite').evaluate('(e)=>getComputedStyle(e).transform')
  page.locator('[data-action="zoom-view-in"]').click()
  b=page.locator('.kwu-turntable-sprite').evaluate('(e)=>getComputedStyle(e).transform')
  assert a!=b,(width,a,b);result.append((width,'zoom',a,b))
  assert '360°' in page.locator('.viewer-top .pill').first.inner_text();result.append((width,'status','360°','ok'))
  assert not errors,(width,errors);result.append((width,'js_errors',0,0))
  if width==390:page.screenshot(path='/mnt/data/KWU_v10_browser_390.png',full_page=False)
  print('PASS',width,'rotate',before,after,'drag',dragged,'zoom',b)
 page.close()
 browser.close()
print(f'PASS {len(result)} checks across four viewport sizes')
(ROOT/'qa-turntable-v10.json').write_text(json.dumps({'passed':True,'checks':len(result),'viewports':[320,390,768,1440],'scope':'GPU-free 360-degree drag/zoom, not arbitrary-angle WebGL rendering'},indent=2))
