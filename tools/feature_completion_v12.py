"""Idempotent migration for the GitHub Pages KWU demo's owner functionality.

Changes only features that can honestly work offline. Never pretends to process
money, send emails, or create authenticated multi-user server accounts.
"""
from __future__ import annotations
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
FILE=ROOT/'src/app.ts'
s=FILE.read_text(encoding='utf-8')
MARKER='// KWU_FEATURE_COMPLETION_V12'
if MARKER in s:
    print('KWU V12 feature migration already present')
    raise SystemExit(0)

def replace_once(old:str,new:str,label:str):
    global s
    if s.count(old)!=1:
        raise RuntimeError(f'{label}: expected exactly one anchor, found {s.count(old)}')
    s=s.replace(old,new,1)
    print('Applied',label)

def replace_func(start:str,end:str,replacement:str,label:str):
    global s
    a=s.find(start)
    if a<0:raise RuntimeError(f'{label}: function start not found')
    b=s.find(end,a+len(start))
    if b<0:raise RuntimeError(f'{label}: next function not found')
    s=s[:a]+replacement+'\n'+s[b:]
    print('Applied',label)

# Existing SKU catalog is kept at 8 categories; update those SKU values locally.
replace_once('type DB={role:', 'type DB={productEdits:Record<string,{name:string;desc:string;price:number}>;store:{name:string;supportEmail:string};role:', 'DB types')
replace_once("const START:DB={role:'guest'", "const START:DB={productEdits:{},store:{name:'ATELIER',supportEmail:''},role:'guest'", 'state defaults')
replace_once("const persist=()=>{", """// KWU_FEATURE_COMPLETION_V12
if(!db.productEdits||typeof db.productEdits!=='object')db.productEdits={};
if(!db.store||typeof db.store!=='object')db.store={name:'ATELIER',supportEmail:''};
for(const p of PRODUCT_TYPES){
 const edit=db.productEdits[p.id];
 if(!edit)continue;
 if(typeof edit.name==='string'&&edit.name.trim())p.name=edit.name.slice(0,80);
 if(typeof edit.desc==='string'&&edit.desc.trim())p.desc=edit.desc.slice(0,240);
 if(Number.isFinite(edit.price)&&edit.price>=0)p.price=edit.price;
}
const persist=()=>{""", 'load owner product overrides')

replace_once("anchor('/owner/products/new','+ Produk Demo','primary')", "anchor('/owner/products/new','Atur Produk Demo','primary')", 'clarify editor link')
replace_once("${btn(db.productsHidden.includes(p.id)?'Aktifkan':'Arsipkan',`toggle-product:${p.id}`,'secondary')}", "${anchor(`/owner/products/${p.id}`,'Edit','secondary')} ${btn(db.productsHidden.includes(p.id)?'Aktifkan':'Arsipkan',`toggle-product:${p.id}`,'secondary')}", 'edit links')

owner_editor='''function ownerEditor(){
 const id=currentPath.split('/')[3]||PRODUCT_TYPES[0].id;
 const item=PRODUCT_TYPES.find(p=>p.id===id)||PRODUCT_TYPES[0];
 const selector=PRODUCT_TYPES.map(p=>`<option value="${esc(p.id)}" ${p.id===item.id?'selected':''}>${esc(p.name)}</option>`).join('');
 return ownerLayout(`${pageHead('PRODUCT EDITOR','Edit katalog demo.','Perubahan produk dan stok disimpan pada browser ini.')}
 <form id="owner-product-form" class="card max-700 stack">
  <div><label for="owner-product-id" class="field-label">Pilih produk</label><select class="field" id="owner-product-id" name="productId">${selector}</select></div>
  <div><label for="owner-product-name" class="field-label">Nama produk</label><input class="field" id="owner-product-name" name="name" maxlength="80" minlength="2" required value="${esc(item.name)}"></div>
  <div><label for="owner-product-desc" class="field-label">Deskripsi produk</label><textarea class="field" id="owner-product-desc" name="desc" maxlength="240" minlength="5" required rows="3">${esc(item.desc)}</textarea></div>
  <div><label for="owner-product-price" class="field-label">Harga dasar (Rp)</label><input class="field" id="owner-product-price" type="number" name="price" min="0" max="999999999" step="1000" required value="${item.price}"></div>
  <div><label for="owner-product-stock" class="field-label">Stok unit</label><input class="field" id="owner-product-stock" type="number" name="stock" min="0" max="999999" step="1" required value="${db.inventory[item.id]??0}"></div>
  <div class="warning">Editor lokal untuk delapan SKU demo. Menambah SKU/model fisik baru, sinkronisasi multi-pengguna, dan pembayaran sungguhan membutuhkan backend.</div>
  <button class="primary full" type="submit">Simpan Perubahan Produk</button>
  ${anchor('/owner/products','← Kembali ke Katalog','secondary full')}
 </form>`)
}
'''
replace_func('function ownerEditor(){','function ownerComponents(){',owner_editor,'owner product editor implementation')

owner_settings='''function ownerSettings(){
 return ownerLayout(`${pageHead('ATELIER SETTINGS','Pengaturan toko.','Identitas toko demonstrasi yang dapat kamu ubah secara lokal.')}
 <form id="owner-settings-form" class="card max-700 stack">
  <div><label class="field-label" for="store-name">Nama toko demo</label><input id="store-name" name="name" class="field" maxlength="70" minlength="2" value="${esc(db.store.name)}" required></div>
  <div><label class="field-label" for="store-email">Email kontak (opsional)</label><input id="store-email" name="supportEmail" type="email" class="field" maxlength="120" value="${esc(db.store.supportEmail)}" placeholder="admin@contoh.com"></div>
  <div class="warning">Perubahan ini tersimpan di browser dan akan terlihat di halaman Bantuan serta ringkasan owner. Pengaturan pembayaran nyata memerlukan server produksi.</div>
  <button class="primary full" type="submit">Simpan Pengaturan Toko</button>
  ${anchor('/owner','← Kembali ke Ringkasan','secondary full')}
 </form>`)
}
'''
replace_func('function ownerSettings(){','function notFound(){',owner_settings,'owner settings editable')

replace_once("function help(){const faqs=", "function help(){const faqs=", 'help anchor no change') if False else None
replace_once('Untuk demo ini, silakan hubungi tim proyek melalui informasi yang diberikan di kelas.',
 "${db.store.supportEmail?`Hubungi ${esc(db.store.name)} melalui <a href=\"mailto:${esc(db.store.supportEmail)}\">${esc(db.store.supportEmail)}</a>.`:'Untuk demo ini, silakan hubungi tim proyek melalui informasi yang diberikan di kelas.'}", 'display saved contact on help')
replace_once("pageHead('OWNER STUDIO','At a glance.','Ringkasan aktivitas toko untuk pengujian alur bisnis.')",
 "pageHead('OWNER STUDIO','At a glance.',`Ringkasan ${esc(db.store.name)} untuk pengujian alur bisnis.`)", 'show store name in owner dashboard')

# Owner role guarding: prevent unintended owner-only changes from ordinary customers.
replace_once("function actionDo(action:string){const [name,arg,arg2]=action.split(':');const p=PRODUCT_TYPES.find(p=>p.id===arg);",
 """function actionDo(action:string){const [name,arg,arg2]=action.split(':');const p=PRODUCT_TYPES.find(p=>p.id===arg);
 if(['toggle-product','stock','save-order-status'].includes(name)&&db.role!=='owner'){notify('Masuk sebagai Owner Demo untuk mengubah data toko');return} """, 'owner action guard')
replace_once("if(name==='delete-address'){db.addresses=db.addresses.filter(x=>x.id!==arg);persist();render();return}",
 "if(name==='delete-address'){if(!confirm('Hapus alamat ini?'))return;db.addresses=db.addresses.filter(x=>x.id!==arg);persist();render();return}", 'confirm address deletion')

anchor="function formSubmit(form:HTMLFormElement){const f=new FormData(form);const id=form.id;"
extra='''function formSubmit(form:HTMLFormElement){const f=new FormData(form);const id=form.id;
 if(id==='owner-product-form'){
  if(db.role!=='owner'){notify('Akses hanya untuk Owner Demo');return}
  const sku=String(f.get('productId')||'');const item=PRODUCT_TYPES.find(p=>p.id===sku);
  const name=String(f.get('name')||'').trim();const desc=String(f.get('desc')||'').trim();
  const price=Number(f.get('price'));const stock=Number(f.get('stock'));
  if(!item||name.length<2||desc.length<5||!Number.isSafeInteger(price)||price<0||price>999999999||!Number.isSafeInteger(stock)||stock<0||stock>999999){notify('Data produk belum valid');return}
  db.productEdits[sku]={name,desc,price};item.name=name;item.desc=desc;item.price=price;db.inventory[sku]=stock;
  persist();nav('/owner/products');notify('Produk dan stok demo berhasil diperbarui');return;
 }
 if(id==='owner-settings-form'){
  if(db.role!=='owner'){notify('Akses hanya untuk Owner Demo');return}
  const name=String(f.get('name')||'').trim();const email=String(f.get('supportEmail')||'').trim();
  if(name.length<2||name.length>70||email.length>120){notify('Periksa nama dan email toko');return}
  db.store={name,supportEmail:email};persist();nav('/owner/settings');notify('Pengaturan toko berhasil disimpan di browser');return;
 }
'''
replace_once(anchor,extra,'owner forms submit handlers')
replace_once("ROOT.addEventListener('change',e=>{const t=e.target as HTMLInputElement;", """ROOT.addEventListener('change',e=>{const t=e.target as HTMLInputElement;
 if(t.id==='owner-product-id'){nav('/owner/products/'+encodeURIComponent(t.value));return;}""",'owner product change route')

FILE.write_text(s,encoding='utf-8')
print('KWU V12 feature migration complete')
