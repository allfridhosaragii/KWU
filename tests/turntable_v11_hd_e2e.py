"""Browser E2E for V11 HD atlases; does not rely on WebGL or external network."""
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright
import json

ROOT=Path(__file__).resolve().parents[1]
ATLAS=ROOT/'site/assets/turntables'
MANIFEST=json.loads((ATLAS/'manifest.json').read_text())
SOURCE=(ROOT/'site/assets/turntable.js').read_text().replace('export class Turntable360','class Turntable360')
assert MANIFEST['version']==11
meta=MANIFEST['models']['bracelet']
assert meta['tileSize']==768 and meta['splitElevations'] and meta['atlasFormat']=='png'
checks=[]
with sync_playwright() as playwright:
    browser=playwright.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-webgl','--disable-gpu'])
    page=browser.new_page(viewport={'width':390,'height':850},device_scale_factor=2)
    errors=[]
    page.on('pageerror',lambda error:errors.append(str(error)))
    def route_request(route):
        name=Path(urlparse(route.request.url).path).name
        if name=='manifest.json':
            route.fulfill(status=200,content_type='application/json',body=json.dumps(MANIFEST))
        elif name.endswith('.png'):
            path=ATLAS/name
            if path.is_file():route.fulfill(status=200,content_type='image/png',body=path.read_bytes())
            else:route.fulfill(status=404,body='Missing fixture PNG')
        else:
            route.fulfill(status=404,body='Missing fixture')
    page.route('https://kwu.test/**',route_request)
    page.set_content('<!doctype html><html lang="id"><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>html,body{margin:0;background:#FAF8F4}.stage{width:100vw;height:75vh;position:relative;overflow:hidden}.kwu-turntable{position:absolute;inset:0;display:flex;justify-content:center;align-items:center;touch-action:none;overflow:hidden}.kwu-turntable-sprite{width:100%;height:auto;max-height:100%;aspect-ratio:1;flex-shrink:1;background-repeat:no-repeat;transform-origin:center center;pointer-events:none}@media(min-aspect-ratio:1/1){.kwu-turntable-sprite{width:auto;height:100%;max-width:100%}}</style></head><body><div class="stage"></div><p id="mode"></p></body></html>')
    page.add_script_tag(content=SOURCE)
    page.evaluate('''async ()=>{window.tt = new Turntable360(document.querySelector('.stage'),'https://kwu.test/',s=>document.querySelector('#mode').textContent=s);await window.tt.load('bracelet')}''')
    page.wait_for_function("document.querySelector('.kwu-turntable-sprite').style.backgroundImage.includes('bracelet--sawo-matang--e0.png')",timeout=15000)
    checks.append('Default sawo matang loads 768px e0 PNG')
    assert '360° HD' in page.locator('#mode').inner_text()
    checks.append('HD status shows true source resolution')
    for width in [320,390,768,1440]:
        page.set_viewport_size({'width':width,'height':850})
        stage=page.locator('.kwu-turntable')
        before=int(stage.get_attribute('data-frame'))
        page.evaluate('()=>window.tt.rotate(30)')
        after=int(stage.get_attribute('data-frame'))
        assert before!=after,(width,before,after)
        checks.append(f'rotate via button at {width}px')
        bounds=stage.bounding_box()
        assert bounds
        x=bounds['x']+bounds['width']*.6;y=bounds['y']+bounds['height']*.45
        page.mouse.move(x,y);page.mouse.down();page.mouse.move(x+94,y+3,steps=7);page.mouse.up()
        changed=int(stage.get_attribute('data-frame'))
        assert changed!=after,(width,changed,after)
        checks.append(f'pointer-drag rotation at {width}px')
        before_zoom=page.locator('.kwu-turntable-sprite').evaluate('el=>el.style.transform')
        page.evaluate('()=>window.tt.zoom(-.4)')
        after_zoom=page.locator('.kwu-turntable-sprite').evaluate('el=>el.style.transform')
        assert before_zoom!=after_zoom
        checks.append(f'zoom at {width}px')
    page.set_viewport_size({'width':390,'height':850})
    page.evaluate('()=>window.tt.reset()')
    page.evaluate('()=>window.tt.setSkinTone("deep-brown")')
    page.wait_for_function("document.querySelector('.kwu-turntable-sprite').style.backgroundImage.includes('bracelet--deep-brown--e0.png')",timeout=15000)
    checks.append('Skin tone switches to HD PNG, no low-res fallback')
    stage=page.locator('.kwu-turntable');bounds=stage.bounding_box();x=bounds['x']+bounds['width']*.5;y=bounds['y']+bounds['height']*.55
    page.mouse.move(x,y);page.mouse.down();page.mouse.move(x,y-170,steps=8);page.mouse.up()
    page.wait_for_function("document.querySelector('.kwu-turntable-sprite').style.backgroundImage.includes('bracelet--deep-brown--e1.png')",timeout=15000)
    checks.append('Vertical drag lazy loads independent HD e1 PNG')
    dims=page.evaluate('''()=>({frame:window.tt.element.dataset.frame,mode:document.querySelector('#mode').textContent,background:document.querySelector('.kwu-turntable-sprite').style.backgroundImage})''')
    assert not errors,errors
    checks.append('No JavaScript errors')
    page.screenshot(path=str(ROOT/'qa-v11-hd-mobile.png'),full_page=False)
    browser.close()
print('PASSED',len(checks),'checks',dims)
(ROOT/'qa-turntable-v11.json').write_text(json.dumps({'passed':True,'checks':checks,'note':'GPU-free HD camera-rotation fallback; not real GPU WebGL nor photoreal anatomical verification'},indent=2))
