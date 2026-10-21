"""Browser regression: HD 1536 and atlas 768 must paint onto one canvas.

Test intentionally uses Chromium without WebGL to exercise the same fallback
mode where the user saw detached fingertips. It verifies real pixel updates.
"""
from pathlib import Path
from urllib.parse import urlparse, unquote
from playwright.sync_api import sync_playwright
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
compiled=(ROOT/'site/assets/turntable.js').read_text(encoding='utf-8')
source=compiled.replace('export class Turntable360','class Turntable360')
assert 'class RetinaStill' in source
assert "host.append(image)" not in source, "An HD image is still overlaying the frame canvas"
checks=[]
with sync_playwright() as pw:
  browser=pw.chromium.launch(headless=True,args=['--no-sandbox','--disable-webgl','--disable-gpu'])
  page=browser.new_page(viewport={'width':390,'height':800},device_scale_factor=2)
  exceptions=[]
  page.on('pageerror',lambda exc:exceptions.append(str(exc)))
  def serve(route):
    url=urlparse(route.request.url)
    target=ROOT/'site'/unquote(url.path).lstrip('/')
    if not target.is_file() or target.stat().st_size>12000000:
      route.fulfill(status=404,body='Asset not found')
      return
    mime=('image/png' if target.suffix=='.png' else 'image/webp' if target.suffix=='.webp' else 'application/json')
    route.fulfill(status=200,content_type=mime,body=target.read_bytes())
  page.route('https://kwu.test/**',serve)
  page.set_content("""
  <!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"/>
  <style>html,body{margin:0;background:#FAF8F4}.stage{height:72vh;width:100vw;position:relative;overflow:hidden}
  .kwu-turntable{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden;touch-action:none}
  .kwu-turntable-sprite{width:100%;height:auto;aspect-ratio:1;max-height:100%;flex-shrink:1;pointer-events:none;transform-origin:center center}
  @media(min-aspect-ratio:1/1){.kwu-turntable-sprite{width:auto;height:100%;max-width:100%}}
  </style></head><body><div class="stage"></div><p id="status"></p></body></html>""")
  page.add_script_tag(content=source)
  page.evaluate("""async ()=>{
    window.tt=new Turntable360(document.querySelector('.stage'),'https://kwu.test/',text=>document.querySelector('#status').textContent=text);
    await window.tt.load('bracelet');
  }""")
  page.wait_for_function("window.tt?.retina?.activeFrame()?.naturalWidth===1536 && document.querySelector('.kwu-turntable-sprite canvas').width===1536",timeout=30000)
  assert page.locator('.kwu-turntable img').count()==0,'Second visible HD image returned'
  assert page.locator('.kwu-turntable canvas').count()==1,'More than one canvas in product view'
  checks.append('Only one canvas, no overlaid image, full 1536p frame')
  # Screenshot comparison works even in a cross-origin test fixture where toDataURL is blocked.
  before=page.locator('.kwu-turntable canvas').screenshot()
  page.evaluate('()=>window.tt.rotate(30)')
  page.wait_for_function("window.tt?.retina?.activeFrame()?.naturalWidth===1536 && document.querySelector('.kwu-turntable canvas').width===1536 && Number(window.tt.element.dataset.frame)===2",timeout=30000)
  after=page.locator('.kwu-turntable canvas').screenshot()
  assert hashlib.sha256(before).digest()!=hashlib.sha256(after).digest(),'Canvas image did not change after rotation'
  checks.append('Rotation updates visible HD pixels, not only a frame counter')
  for width in [320,390,768,1440]:
    page.set_viewport_size({'width':width,'height':800})
    page.evaluate('()=>window.tt.zoom(-.25)')
    count=page.locator('.kwu-turntable canvas').count()
    assert count==1 and page.locator('.kwu-turntable img').count()==0,(width,count)
    checks.append(f'Single zoomed product surface at {width}px')
  page.evaluate('()=>window.tt.setSkinTone("deep-brown")')
  page.wait_for_function("window.tt.renderedAtlas.includes('bracelet--deep-brown--e0.png') && window.tt.retina.activeFrame()?.naturalWidth===1536",timeout=30000)
  checks.append('Skin-tone change keeps HD canvas active')
  page.locator('.kwu-turntable').dblclick()
  assert abs(page.evaluate('()=>window.tt.magnification')-1.0)<0.0001,'Double click did not reset zoom'
  checks.append('Double-click resets zoom')
  assert not exceptions,exceptions
  checks.append('No browser JavaScript exceptions')
  browser.close()
print('PASS',len(checks),'checks',checks)
