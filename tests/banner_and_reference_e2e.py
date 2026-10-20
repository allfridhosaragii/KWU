"""Regression for the removed global banner and optional original-photo comparison.
Requires chromium Playwright. Does not claim real-GPU WebGL testing.
"""
import base64, json
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
css=(ROOT/'site/assets/style.css').read_text(encoding='utf8').split('\n',1)[1]
viewer=(ROOT/'site/assets/viewer.js').read_text(encoding='utf8').replace('export class Viewer3D','class Viewer3D')
app=(ROOT/'site/assets/app.js').read_text(encoding='utf8').replace("import { Viewer3D } from './viewer.js';",'')
errors=[]
report={'viewports':[],'failed':[],'webgl2_tested':False}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    for width,height in [(320,720),(390,844),(768,1024),(1440,900)]:
        page=b.new_page(viewport={'width':width,'height':height})
        page.on('pageerror',lambda err: errors.append(str(err)))
        page.set_content('<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>'+css+'</style></head><body><div id="app"></div></body></html>')
        page.evaluate("()=>{window.KWU_BASE='/';window.__KWU_TEST_MODE=true;window.__KWU_TEST_PATH='/';window.fetch=async()=>new Response('',{status:404})}")
        page.add_script_tag(content=viewer+'\n'+app)
        page.wait_for_function('window.__KWU_TEST_RENDER!==undefined')
        cases=0
        def check(ok,what):
            global cases
            cases+=1
            if not ok: report['failed'].append(f'{width}: {what}')
        for route in ['/','/shop','/studio','/login','/register','/help','/about','/owner','/cart']:
            page.evaluate("(route)=>{window.__KWU_TEST_PATH=route;window.__KWU_TEST_RENDER()}",route)
            check(page.locator('.demo-banner').count()==0, f'Banner appeared at {route}')
            check('DEMO INTERAKTIF KWU' not in page.locator('body').inner_text(), f'Banner copy appeared {route}')
        page.evaluate("()=>{window.__KWU_TEST_PATH='/login';window.__KWU_TEST_RENDER()}")
        check('bukan autentikasi sungguhan' in page.locator('body').inner_text(),'Login disclosure missing')
        page.locator('#login-email').fill('owner@example.test')
        page.locator('#login-role').select_option('owner')
        page.locator('#login-form button[type="submit"]').click()
        for mid,ref in [('bag-charm','backpack-user.jpeg'),('bottle','bottle-user.jpeg'),('iphone-17',None)]:
            page.evaluate("(mid)=>{window.__KWU_TEST_PATH='/owner/assets?model='+mid;window.__KWU_TEST_RENDER()}",mid)
            check(page.locator('.owner-model-link').count()==21,'Owner models nav lost')
            check(page.locator('.owner-reference-compare').count()==(1 if ref else 0),f'Comparison count for {mid}')
            if ref:
                check(ref in page.locator('.owner-reference-compare img').get_attribute('src'), f'Reference photo wrong for {mid}')
                page.locator('.owner-reference-compare summary').click(timeout=1200,force=True)
                check(page.locator('.owner-reference-compare').evaluate('(e)=>e.open'),f'Reference compare did not open for {mid}')
        check(page.evaluate('document.documentElement.scrollWidth <= innerWidth + 2'),'Page overflows viewport')
        report['viewports'].append({'width':width,'checks':cases})
        page.close()
    b.close()
report['javascript_errors']=errors
(ROOT/'qa-banner-reference.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
if report['failed'] or errors:raise SystemExit(1)
