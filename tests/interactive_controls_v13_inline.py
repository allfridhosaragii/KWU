"""V13: visual state must change when editing a 360-degree product.

The offline renderer is frame-based, so we check the explicitly labelled
ornament overlay, quality and pose response without pretending it is WebGL.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'site/assets/turntable.js').read_text(encoding='utf-8')
source=source.replace('export class Turntable360','class Turntable360')
with sync_playwright() as p:
    browser=p.chromium.launch(headless=True)
    page=browser.new_page(viewport={'width':390,'height':844})
    page.set_content('<html><body><div id="viewer" style="width:390px;height:420px;position:relative"></div></body></html>')
    page.add_script_tag(content=source+'''
       window.__turntable=new Turntable360(document.getElementById('viewer'),'/',()=>{});
       window.__edit=(v)=>window.__turntable.setCustomization(v);
    ''')
    original={'kind':'bracelet','ornament':'heart','color':'#C8B5A0','placement':50,'rotation':0,'scale':1,'finger':2,'caseType':'plain','pose':50,'quality':'auto'}
    page.evaluate('(v)=>window.__edit(v)',original)
    x=page.locator('.kwu-decoration-preview')
    badge=page.locator('.kwu-design-readout')
    assert x.inner_text()=='♥'
    assert 'Hati' in badge.inner_text()
    updated=dict(original,ornament='star',color='#8F503C',placement=80,scale=1.4,rotation=45,pose=90,quality='high')
    page.evaluate('(v)=>window.__edit(v)',updated)
    assert x.inner_text()=='★'
    assert 'Bintang' in badge.inner_text()
    assert '80%' in badge.inner_text()
    assert '1.40×' in badge.inner_text()
    assert x.evaluate('(el)=>el.style.color')=='rgb(143, 80, 60)'
    assert '45deg' in x.get_attribute('style')
    assert x.evaluate('(el)=>el.style.left')=='57%'
    assert page.evaluate('window.__turntable.requestedQuality')=='high'
    # Finger selection must visibly move a ring preview.
    ring=dict(original,kind='ring',finger=0)
    page.evaluate('(v)=>window.__edit(v)',ring)
    t0=x.evaluate('(el)=>el.style.top')
    ring['finger']=2
    page.evaluate('(v)=>window.__edit(v)',ring)
    assert x.evaluate('(el)=>el.style.top')!=t0
    browser.close()
print('PASS V13 360 customizer interaction controls')
