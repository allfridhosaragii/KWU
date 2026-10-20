"""Offline Chromium UI regression suite. Browser admin policy blocks network and WebGL.
Fallback and UI are tested in Chromium; GLB mesh validity tested separately.
Run: python tests/e2e_inline.py
"""
from pathlib import Path
import base64, json, re, time, sys
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).parent.parent
css=(ROOT/'site/assets/style.css').read_text().split('\n',1)[1]
turnfile=ROOT/'site/assets/turntable.js'
turntable=(turnfile.read_text().replace('export class Turntable360','class Turntable360') if turnfile.is_file() else '')
viewer=(ROOT/'site/assets/viewer.js').read_text().replace('export class Viewer3D','class Viewer3D')
viewer=re.sub(r'^import .*?from [\"\']\./turntable\.js[^\"\']*[\"\'];?\s*','',viewer,flags=re.M)
app=(ROOT/'site/assets/app.js').read_text()
app=re.sub(r'^import .*?from [\"\']\./viewer\.js[^\"\']*[\"\'];?\s*','',app,flags=re.M)
models={p.stem:base64.b64encode(p.read_bytes()).decode() for p in (ROOT/'site/models').glob('*.glb')}
previews={p.stem:base64.b64encode(p.read_bytes()).decode() for p in (ROOT/'site/assets/previews').glob('*.webp')}
script=turntable+'\n'+viewer+'\n'+app
PUBLIC=['/','/shop','/products/charm-bracelet','/studio','/studio/bracelet/charm-bracelet','/cart','/checkout','/checkout/result','/help','/about','/legal/privacy']
AUTH=['/login','/register','/forgot-password','/reset-password']
ACCOUNT=['/account','/account/designs','/account/wishlist','/account/orders','/account/orders/DEMO-000','/account/addresses','/account/profile']
OWNER=['/owner','/owner/orders','/owner/orders/DEMO-000','/owner/products','/owner/products/new','/owner/components','/owner/assets','/owner/inventory','/owner/payments','/owner/customers','/owner/reports','/owner/settings']
STUDIOS=[f'/studio/{kind}/{id}' for kind,id in [('bracelet','charm-bracelet'),('ring','daily-ring'),('necklace','petite-necklace'),('bag-charm','bag-story'),('phone','phone-sticker'),('tablet','tablet-sticker'),('macbook','laptop-sticker'),('bottle','bottle-sticker')]]

def main():
 failures=[];passes=0;errors=[];tested=0;checks=[]
 with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None,headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-unsafe-swiftshader','--disable-webgl','--disable-gpu'])
  size=int(sys.argv[1]) if len(sys.argv)>1 else 390
  width,height={320:(320,720),390:(390,844),768:(768,1024),1440:(1440,900)}[size]
  for width,height in [(width,height)]:
   page=b.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
   page.on('pageerror',lambda e:errors.append(str(e)))
   page.set_content('<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>'+css+'</style></head><body><div id="app"></div></body></html>')
   page.evaluate("""()=>{const memory=new Map(); Object.defineProperty(window,'localStorage',{configurable:true,value:{getItem:(k)=>memory.get(k)??null,setItem:(k,v)=>memory.set(k,String(v)),removeItem:(k)=>memory.delete(k),clear:()=>memory.clear()}})}""")
   page.evaluate('''(payload)=>{window.KWU_BASE='/';window.__KWU_TEST_MODE=true;window.__KWU_TEST_PATH='/';let models=payload.models,photos=payload.photos;window.fetch=async function(url){let key=String(url).split('/').pop().replace('.glb','');if(models[key]){let b=atob(models[key]);let a=new Uint8Array(b.length);for(let i=0;i<b.length;i++)a[i]=b.charCodeAt(i);return new Response(a,{status:200});}return new Response('',{status:404})};function apply(){document.querySelectorAll('img').forEach(img=>{const m=img.getAttribute('src')?.match(/\\/([^\\/]+)\\.webp$/);if(m&&photos[m[1]])img.setAttribute('src','data:image/webp;base64,'+photos[m[1]])})}new MutationObserver(apply).observe(document,{childList:true,subtree:true});}''',{'models':models,'photos':previews})
   page.add_script_tag(type='module',content=script)
   page.wait_for_function('window.__KWU_TEST_RENDER!==undefined',timeout=9000)
   results=page.evaluate('''(routes)=>routes.map(route=>{window.__KWU_TEST_PATH=route;window.__KWU_TEST_RENDER();return {route,body:document.body.innerText.length,width:document.documentElement.scrollWidth,inner:innerWidth,canvas:document.querySelectorAll('canvas').length}})''',PUBLIC+AUTH+ACCOUNT+STUDIOS)
   for res in results:
    route=res['route'];tested+=1
    if res['body']<50:failures.append((width,route,'empty view',res))
    if res['width']>width+2:failures.append((width,route,'horizontal overflow',res))
    if route in STUDIOS and res['canvas']!=1:failures.append((width,route,'missing canvas',res))
   # auth owner before owner test
   page.evaluate("()=>{window.__KWU_TEST_PATH='/login';window.__KWU_TEST_RENDER()}")
   page.locator('#login-email').fill('owner@example.test')
   page.locator('#login-role').select_option('owner')
   page.locator('#login-form button[type="submit"]').click()
   results=page.evaluate('''(routes)=>routes.map(route=>{window.__KWU_TEST_PATH=route;window.__KWU_TEST_RENDER();return {route,body:document.body.innerText.length,width:document.documentElement.scrollWidth,inner:innerWidth}})''',OWNER)
   for res in results:
    route=res['route'];tested+=1
    if res['body']<50:failures.append((width,route,'empty owner',res))
    if res['width']>width+2:failures.append((width,route,'owner horizontal overflow',res))
   if width==390:
    page.evaluate("()=>{window.__KWU_TEST_PATH='/';window.__KWU_TEST_RENDER()}");page.wait_for_timeout(60);page.screenshot(path=str(ROOT/'qa-mobile-home.png'),full_page=True)
    page.evaluate("()=>{window.__KWU_TEST_PATH='/studio/bracelet/charm-bracelet';window.__KWU_TEST_RENDER()}");page.wait_for_timeout(60);page.screenshot(path=str(ROOT/'qa-mobile-studio.png'),full_page=True)
    page.evaluate("()=>{window.__KWU_TEST_PATH='/owner';window.__KWU_TEST_RENDER()}");page.wait_for_timeout(60);page.screenshot(path=str(ROOT/'qa-mobile-owner.png'),full_page=True)
   if width==1440:
    page.evaluate("()=>{window.__KWU_TEST_PATH='/';window.__KWU_TEST_RENDER()}");page.wait_for_timeout(60);page.screenshot(path=str(ROOT/'qa-desktop-home.png'),full_page=True)
    page.evaluate("()=>{window.__KWU_TEST_PATH='/studio/phone/phone-sticker';window.__KWU_TEST_RENDER()}");page.wait_for_timeout(60);page.screenshot(path=str(ROOT/'qa-desktop-studio.png'),full_page=True)
   # workflow on each viewport: bracelet studio -> save -> cart -> checkout -> order -> owner update
   try:
    page.evaluate("()=>{window.__KWU_TEST_PATH='/studio/bracelet/charm-bracelet';window.__KWU_TEST_RENDER()}")
    page.locator('[data-action="ornament:star"]').click()
    page.locator('#place-slider').fill('70')
    page.locator('[data-action="save-design"]').click()
    page.locator('[data-action="add-to-cart"]:visible').first.click()
    assert page.locator('.cart-row').count()>=1
    page.locator('a[data-nav="/checkout"]').last.click()
    page.locator('#customer-name').fill('Pembeli Demo')
    page.locator('#customer-email').fill('demo@example.test')
    page.locator('#shipping-address').fill('Jl. Contoh KWU No 12, Bandung')
    page.locator('#checkout-form button[type="submit"]').click()
    assert 'Pesanan demo tercatat.' in page.locator('body').inner_text()
    page.evaluate("()=>{window.__KWU_TEST_PATH='/owner/orders';window.__KWU_TEST_RENDER()}")
    assert 'KWU-' in page.locator('body').inner_text()
    # V12: owner product form, settings, inventory, address, profile and customer flow.
    page.evaluate("()=>{window.__KWU_TEST_PATH='/owner/products';window.__KWU_TEST_RENDER()}")
    assert page.locator('table tbody tr').count()==8
    page.locator('a[data-nav="/owner/products/charm-bracelet"]').click()
    assert page.locator('#owner-product-form').count()==1
    page.locator('#owner-product-name').fill('Gelang Premium KWU')
    page.locator('#owner-product-desc').fill('Gelang custom untuk uji fitur owner')
    page.locator('#owner-product-price').fill('77000')
    page.locator('#owner-product-stock').fill('18')
    page.locator('#owner-product-form button[type=submit]').click()
    assert 'Gelang Premium KWU' in page.locator('table').inner_text()
    assert page.evaluate("JSON.parse(localStorage.getItem('kwu-atelier-demo-v1')).productEdits['charm-bracelet'].price")==77000
    page.evaluate("()=>{window.__KWU_TEST_PATH='/owner/inventory';window.__KWU_TEST_RENDER()}")
    assert 'Tersedia: 18 unit' in page.locator('body').inner_text()
    page.locator('[data-action="stock:charm-bracelet:1"]').click()
    assert page.evaluate("JSON.parse(localStorage.getItem('kwu-atelier-demo-v1')).inventory['charm-bracelet']")==19
    page.evaluate("()=>{window.__KWU_TEST_PATH='/owner/settings';window.__KWU_TEST_RENDER()}")
    page.locator('#store-name').fill('Atelier Surabaya KWU')
    page.locator('#store-email').fill('kwu@example.id')
    page.locator('#owner-settings-form button[type=submit]').click()
    assert page.evaluate("JSON.parse(localStorage.getItem('kwu-atelier-demo-v1')).store.name")=='Atelier Surabaya KWU'
    page.evaluate("()=>{window.__KWU_TEST_PATH='/help';window.__KWU_TEST_RENDER()}")
    assert 'kwu@example.id' in page.locator('body').inner_text()
    page.evaluate("()=>{window.__KWU_TEST_PATH='/account/addresses';window.__KWU_TEST_RENDER()}")
    page.locator('#address-label').fill('Rumah')
    page.locator('#address-text').fill('Jl. Ketintang Baru Surabaya 12')
    page.locator('#address-form button[type=submit]').click()
    assert page.evaluate("JSON.parse(localStorage.getItem('kwu-atelier-demo-v1')).addresses[0].name")=='Rumah'
    page.on('dialog',lambda d:d.accept())
    page.locator('[data-action^="delete-address:"]').click()
    assert page.evaluate("JSON.parse(localStorage.getItem('kwu-atelier-demo-v1')).addresses.length")==0
    page.evaluate("()=>{window.__KWU_TEST_PATH='/account/profile';window.__KWU_TEST_RENDER()}")
    page.locator('#profile-name').fill('Pengguna KWU')
    page.locator('#profile-email').fill('pengguna@example.id')
    page.locator('#profile-form button[type=submit]').click()
    assert page.evaluate("JSON.parse(localStorage.getItem('kwu-atelier-demo-v1')).profile.name")=='Pengguna KWU'
    page.evaluate("()=>{window.__KWU_TEST_PATH='/shop';window.__KWU_TEST_RENDER()}")
    assert 'Gelang Premium KWU' in page.locator('body').inner_text()
    passes+=1
   except Exception as e:failures.append((width,'workflow',str(e)[:250]))
   page.close()
  b.close()
 print(json.dumps({'route_breakpoint_tests':tested,'workflow_passes':passes,'javascript_errors':errors[:15],'failures':failures[:50],'failure_count':len(failures)},indent=2,ensure_ascii=False))
 (ROOT/'qa-browser-results.json').write_text(json.dumps({'route_breakpoint_tests':tested,'workflow_passes':passes,'javascript_errors':errors,'failures':failures},indent=2,ensure_ascii=False))
 if failures or errors:raise SystemExit(1)
if __name__=='__main__':main()
