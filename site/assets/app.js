import { Viewer3D } from './viewer.js?v=v16-1';
const BASE = window.KWU_BASE || '/';
const ROOT = document.getElementById('app');
const makeId = () => globalThis.crypto?.randomUUID?.() || ('demo-' + Date.now().toString(36) + '-' + Math.random().toString(36).slice(2));
const money = (v) => new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', maximumFractionDigits: 0 }).format(v);
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, x => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[x]));
const href = (s) => BASE + (s === '/' ? '' : s.replace(/^\//, ''));
const art = (id) => `${BASE}assets/previews/${id}.webp`;
const PRODUCT_TYPES = [
    { kind: 'bracelet', id: 'charm-bracelet', name: 'Silver Charm Bracelet', label: 'Gelang', price: 55000, desc: 'Gelang personal dengan charm pilihanmu.', tag: 'Best seller', material: 'Stainless steel' },
    { kind: 'ring', id: 'daily-ring', name: 'Everyday Ring', label: 'Cincin', price: 65000, desc: 'Cincin sederhana dengan sentuhan personal.', tag: 'New', material: 'Silver plated' },
    { kind: 'necklace', id: 'petite-necklace', name: 'Petite Pendant', label: 'Kalung', price: 85000, desc: 'Kalung minimalis dengan liontin personal.', tag: 'Curated', material: 'Stainless steel' },
    { kind: 'bag-charm', id: 'bag-story', name: 'Bag Charm Story', label: 'Gantungan Tas', price: 45000, desc: 'Aksen unik untuk tas kesayangan.', tag: 'Favorite', material: 'Alloy & leather' },
    { kind: 'phone', id: 'phone-sticker', name: 'Phone Sticker Set', label: 'Stiker HP', price: 15000, desc: 'Buat casing polos jadi lebih personal.', tag: 'Creative', material: 'Vinyl sticker' },
    { kind: 'tablet', id: 'tablet-sticker', name: 'Tablet Sticker Set', label: 'Stiker Tablet', price: 19000, desc: 'Berikan karakter pada tablet pilihanmu.', tag: 'Creative', material: 'Vinyl sticker' },
    { kind: 'macbook', id: 'laptop-sticker', name: 'MacBook Sticker Set', label: 'Stiker MacBook', price: 24000, desc: 'Susun stiker sesuai mood dan gayamu.', tag: 'Popular', material: 'Vinyl sticker' },
    { kind: 'bottle', id: 'bottle-sticker', name: 'Bottle Sticker Set', label: 'Stiker Botol', price: 15000, desc: 'Dekorasi untuk botol stainless favoritmu.', tag: 'Creative', material: 'Water-resistant vinyl' }
];
const DEVICE_VARIANTS = {
    phone: [
        { id: 'iphone-17', name: 'iPhone 17', colors: ['#262629', '#F5F3EE', '#C5D7E3', '#B4C0AB', '#D7C5E3'] },
        { id: 'iphone-air', name: 'iPhone Air', colors: ['#272729', '#F3F0EB', '#DCCCAF', '#CFDEE9'] },
        { id: 'iphone-17-pro', name: 'iPhone 17 Pro', colors: ['#D6D6D2', '#D9773E', '#37465D'] },
        { id: 'iphone-17-pro-max', name: 'iPhone 17 Pro Max', colors: ['#D6D6D2', '#D9773E', '#37465D'] },
        { id: 'iphone-17e', name: 'iPhone 17e', colors: ['#222326', '#F3F1EA', '#EAD2D7'] }
    ],
    tablet: [
        { id: 'ipad-pro-11', name: 'iPad Pro 11 inci', colors: ['#CED0CE', '#414448'] },
        { id: 'ipad-pro-13', name: 'iPad Pro 13 inci', colors: ['#CED0CE', '#414448'] },
        { id: 'ipad-air-11', name: 'iPad Air 11 inci', colors: ['#B3C8E5', '#C6BBD7', '#DFDACF', '#838588'] },
        { id: 'ipad-air-13', name: 'iPad Air 13 inci', colors: ['#B3C8E5', '#C6BBD7', '#DFDACF', '#838588'] }
    ],
    macbook: [
        { id: 'macbook-air-13', name: 'MacBook Air 13 inci', colors: ['#AEBCC6', '#D1D2D2', '#DCCFBC', '#3B4850'] },
        { id: 'macbook-air-15', name: 'MacBook Air 15 inci', colors: ['#AEBCC6', '#D1D2D2', '#DCCFBC', '#3B4850'] },
        { id: 'macbook-pro-14', name: 'MacBook Pro 14 inci', colors: ['#373839', '#C5C6C6'] },
        { id: 'macbook-pro-16', name: 'MacBook Pro 16 inci', colors: ['#373839', '#C5C6C6'] }
    ]
};
function deviceVariant(kind, id) { return (kind === 'phone' || kind === 'tablet' || kind === 'macbook') ? DEVICE_VARIANTS[kind].find(x => x.id === id) : undefined; }
function deviceList(kind) { return kind === 'phone' || kind === 'tablet' || kind === 'macbook' ? DEVICE_VARIANTS[kind] : []; }
const SKIN_TONES = [
    { id: 'sawo-matang', name: 'Sawo Matang', hex: '#B8825F', note: 'Hangat natural khas Indonesia' },
    { id: 'kuning-langsat', name: 'Kuning Langsat', hex: '#D5A27E', note: 'Cerahan hangat' },
    { id: 'light-beige', name: 'Light Beige', hex: '#E2BC9F', note: 'Terang lembut' },
    { id: 'medium-tan', name: 'Medium Tan', hex: '#9F6D4F', note: 'Tan seimbang' },
    { id: 'deep-brown', name: 'Deep Brown', hex: '#6F4837', note: 'Cokelat gelap kaya' }
];
const START = { productEdits: {}, store: { name: 'ATELIER', supportEmail: '' }, role: 'guest', profile: { name: 'Pengunjung Atelier', email: '' }, wishlist: [], designs: [], cart: [], orders: [], addresses: [], inventory: Object.fromEntries(PRODUCT_TYPES.map(x => [x.id, 24])), productsHidden: [] };
let db;
try {
    const saved = JSON.parse(localStorage.getItem('kwu-atelier-demo-v1') || 'null');
    db = saved ? { ...structuredClone(START), ...saved } : structuredClone(START);
}
catch {
    db = structuredClone(START);
}
// KWU_FEATURE_COMPLETION_V12
if (!db.productEdits || typeof db.productEdits !== 'object')
    db.productEdits = {};
if (!db.store || typeof db.store !== 'object')
    db.store = { name: 'ATELIER', supportEmail: '' };
for (const p of PRODUCT_TYPES) {
    const edit = db.productEdits[p.id];
    if (!edit)
        continue;
    if (typeof edit.name === 'string' && edit.name.trim())
        p.name = edit.name.slice(0, 80);
    if (typeof edit.desc === 'string' && edit.desc.trim())
        p.desc = edit.desc.slice(0, 240);
    if (Number.isFinite(edit.price) && edit.price >= 0)
        p.price = edit.price;
}
const persist = () => { try {
    localStorage.setItem('kwu-atelier-demo-v1', JSON.stringify(db));
}
catch {
    notify('Penyimpanan perangkat penuh. Desain tidak dapat disimpan.');
} };
const getProduct = (kind) => PRODUCT_TYPES.find(p => p.kind === kind || p.id === kind);
const defaultOpts = (kind) => ({ kind, deviceModel: deviceList(kind)[0]?.id || '', color: deviceList(kind)[0]?.colors[0] || (kind === 'bottle' ? '#858988' : kind === 'bag-charm' ? '#222326' : '#C8B5A0'), skinTone: 'sawo-matang', ornament: 'heart', placement: 50, scale: 1, rotation: 0, finger: 2, caseType: 'plain', pose: 50, quality: 'auto' });
function newDesign(kind) { const p = getProduct(kind); return { ...defaultOpts(kind), id: `D-${Date.now()}-${Math.round(Math.random() * 9999)}`, productId: p.id, name: `Desain ${p.label}`, price: p.price, createdAt: new Date().toISOString() }; }
let currentPath = '/';
let viewer = null;
let studioDesign = null;
let toastTimer;
let pendingFocus = null;
function notify(message) { document.querySelector('.toast')?.remove(); const e = document.createElement('div'); e.className = 'toast'; e.setAttribute('role', 'status'); e.textContent = message; document.body.append(e); clearTimeout(toastTimer); toastTimer = setTimeout(() => e.remove(), 3500); }
function routePath() { const p = decodeURI(location.pathname); return p.startsWith(BASE) ? ('/' + p.slice(BASE.length).replace(/^\//, '')) : p; if (false)
    return '/'; }
function parseRoute() { const raw = window.__KWU_TEST_PATH || location.pathname; const p = raw.split('?')[0].split('#')[0]; const path = p.startsWith(BASE) ? '/' + p.slice(BASE.length) : p; return path.length > 1 ? path.replace(/\/$/, '') : '/'; }
function nav(path) { if (window.__KWU_TEST_MODE) {
    window.__KWU_TEST_PATH = path;
}
else {
    history.pushState({}, '', href(path));
} render(); window.scrollTo({ top: 0, behavior: 'instant' }); }
window.addEventListener('popstate', () => render());
const icons = { home: '⌂', shop: '▦', studio: '✧', cart: '♧', account: '♙', orders: '▤', products: '◇', more: '☷', back: '←', next: '↗', heart: '♡', check: '✓', search: '⌕', close: '×', edit: '✎', save: '↓' };
function anchor(path, label, cls = '', other = '') { return `<a href="${esc(href(path))}" data-nav="${esc(path)}" class="${cls}" ${other}>${label}</a>`; }
function btn(label, action, cls = 'secondary', extra = '') { return `<button type="button" class="${cls}" data-action="${esc(action)}" ${extra}>${label}</button>`; }
function bottomNav(owner = false) { const items = owner ? [['/owner', '⌂', 'Ringkasan'], ['/owner/orders', '▤', 'Pesanan'], ['/owner/products', '◇', 'Produk'], ['/owner/assets', '⬡', 'Model 3D'], ['/owner/settings', '☷', 'Lainnya']] : [['/', '⌂', 'Beranda'], ['/shop', '▦', 'Belanja'], ['/studio', '✧', 'Studio'], ['/cart', '♧', 'Keranjang'], ['/account', '♙', 'Akun']]; return `<nav aria-label="Navigasi utama mobile" class="${owner ? 'owner-mobile-nav' : 'bottom-nav'}">${items.map(([path, glyph, label]) => anchor(path, `<span class="glyph" aria-hidden="true">${glyph}</span>${label}`, currentPath === path ? 'active' : '')).join('')}</nav>`; }
function header() { const owner = currentPath.startsWith('/owner'); return `<header class="site-header">${anchor('/', 'ATELIER<span class="dot">.</span>', 'brand')}<nav class="nav-desktop" aria-label="Navigasi utama">${[['/', 'Beranda'], ['/shop', 'Koleksi'], ['/studio', 'Studio 3D'], ['/about', 'Tentang']].map(([p, l]) => anchor(p, l, p === currentPath ? 'current' : '')).join('')}</nav><div class="nav-actions">${anchor('/shop', '⌕', 'icon-btn hide-mobile', 'aria-label="Cari produk"')}${anchor('/account/wishlist', '♡', 'icon-btn hide-mobile', 'aria-label="Wishlist"')}${anchor('/cart', `♧${db.cart.length ? `<sup>${db.cart.reduce((n, x) => n + x.qty, 0)}</sup>` : ''}`, 'icon-btn', 'aria-label="Keranjang"')}${anchor(db.role === 'owner' ? '/owner' : '/account', '♙', 'icon-btn', 'aria-label="Akun"')}</div></header>${owner ? '' : bottomNav(false)}`; }
function footer() { return `<footer class="footer"><div class="footer-inner"><div><div class="footer-brand">ATELIER.</div><p>A little piece of you, made tangible. Studio personalisasi 3D untuk aksesoris dan stiker pilihanmu.</p><p style="margin-top:25px;font-size:.64rem">Proyek akademik KWU · Simulasi e-commerce, bukan toko pembayaran nyata.</p></div><div><h4>Jelajahi</h4>${anchor('/shop', 'Koleksi')}${anchor('/studio', 'Studio 3D')}${anchor('/about', 'Cerita Kami')}</div><div><h4>Bantuan</h4>${anchor('/help', 'Pusat Bantuan')}${anchor('/legal/privacy', 'Privasi')}${anchor('/legal/terms', 'Ketentuan')}</div></div></footer>`; }
function publicLayout(body, withFooter = true) { return header() + `<main id="main">${body}</main>` + (withFooter ? footer() : ''); }
const pageHead = (ey, title, desc = '', extra = '') => `<div class="page-header"><div><p class="eyebrow">${ey}</p><h1>${title}</h1>${desc ? `<p>${desc}</p>` : ''}</div>${extra}</div>`;
function featureStrip() { return `<div class="feature-strip"><div class="feature"><strong>✦ Buat sesuai gayamu</strong><p>Pilih preset lalu sesuaikan setiap detail.</p></div><div class="feature"><strong>◌ Lihat dalam 3D</strong><p>Putar, zoom, dan lihat dari berbagai sisi.</p></div><div class="feature"><strong>♡ Simpan kreasi</strong><p>Desainmu tersimpan untuk dilanjutkan.</p></div></div>`; }
function productCard(p) { return `<article class="product-card">${anchor(`/products/${p.id}`, `<div class="product-image"><span class="tag">${p.tag}</span><img src="${art(p.kind)}" alt="Preview ${esc(p.name)}" loading="lazy"></div>`)}<div class="product-text"><div>${anchor(`/products/${p.id}`, `<div class="product-name">${esc(p.name)}</div>`)}<p class="product-desc">${esc(p.label)}</p></div><div class="product-price">${money(p.price)}</div></div><button class="heart-btn ${db.wishlist.includes(p.id) ? 'liked' : ''}" type="button" data-action="wish:${p.id}" aria-label="${db.wishlist.includes(p.id) ? 'Hapus dari' : 'Tambah ke'} wishlist">${db.wishlist.includes(p.id) ? '♥' : '♡'}</button></article>`; }
function productGrid(ps) { return `<div class="product-grid">${ps.map(productCard).join('')}</div>`; }
function home() { return publicLayout(`<div class="container"><section class="hero"><div class="hero-copy"><span class="eyebrow">THE PERSONAL COLLECTION · 2026</span><h1>Little things.<br>Uniquely yours.</h1><p class="sub">Dari gelang yang penuh cerita sampai stiker untuk benda favoritmu. Buat setiap detail menjadi milikmu.</p><div class="row" style="flex-wrap:wrap">${anchor('/studio', 'Mulai Custom <span aria-hidden="true">↗</span>', 'primary')}${anchor('/shop', 'Lihat Koleksi', 'secondary')}</div></div><div class="hero-art"><img class="hero-object" src="${art('necklace')}" alt="Manekin leher dengan kalung yang dapat dipersonalisasi"><span class="hero-number">01 / MADE PERSONAL</span></div></section>${featureStrip()}<section class="section"><div class="section-title"><div><p class="eyebrow">EXPLORE THE ATELIER</p><h2>Find your canvas.</h2></div>${anchor('/studio', 'Jelajahi Studio ↗', 'ghost')}</div><div class="category-grid">${[getProduct('bracelet'), getProduct('ring'), getProduct('phone'), getProduct('bag-charm')].map(p => anchor(`/studio/${p.kind}/${p.id}`, `<img loading="lazy" src="${art(p.kind)}" alt="${esc(p.label)}"><span class="cat-label">${esc(p.label)} ↗</span>`, 'category-card')).join('')}</div></section><section class="section"><div class="section-title"><div><p class="eyebrow">CURATED FOR YOU</p><h2>Objects to adore.</h2></div>${anchor('/shop', 'Semua Produk ↗', 'ghost')}</div>${productGrid(PRODUCT_TYPES.slice(0, 4))}</section><section class="section"><div class="grid-2" style="align-items:center;gap:35px"><div class="card-soft" style="min-height:350px;display:grid;place-items:center"><img style="max-height:350px" src="${art('phone')}" alt="Preview HP dengan casing untuk stiker" loading="lazy"></div><div class="stack" style="padding:20px"><span class="eyebrow">YOUR NEXT FAVORITE</span><h2>Your style, your surface.</h2><p class="muted">Personalisasi stiker untuk HP, tablet, MacBook, atau botol. Atur warna, bentuk, dan posisi melalui preview 3D interaktif.</p>${anchor('/studio', 'Buka 3D Studio ↗', 'primary')}</div></div></section></div>`); }
function shop() { const u = new URL(location.href), selected = u.searchParams.get('category') || 'all', q = u.searchParams.get('q') || ''; const kinds = [['all', 'Semua Produk'], ...PRODUCT_TYPES.map(p => [p.kind, p.label])]; const ps = PRODUCT_TYPES.filter(p => (selected === 'all' || p.kind === selected) && !db.productsHidden.includes(p.id) && (`${p.name} ${p.label}`).toLowerCase().includes(q.toLowerCase())); return publicLayout(`<div class="content">${pageHead('THE CURATED COLLECTION', 'Explore our pieces.', 'Setiap karya bisa kamu lihat dan sesuaikan dalam studio 3D.')}<div class="shop-layout"><aside class="filter-panel" aria-label="Filter kategori"><h3>Kategori</h3>${kinds.map(([k, l]) => `<button class="filter-link ${selected === k ? 'active' : ''}" data-action="filter:${k}">${esc(l)}</button>`).join('')}</aside><div><div class="shop-top"><input class="search" id="shop-search" type="search" placeholder="Cari gelang, stiker, cincin..." aria-label="Cari produk" value="${esc(q)}"><div class="row">${btn('☷ Filter', 'open-filter', 'secondary shop-filter-trigger')}<span class="muted small">${ps.length} produk</span></div></div><div class="mobile-filter chips" id="mobile-filter" style="margin-bottom:17px">${kinds.map(([k, l]) => `<button class="chip ${selected === k ? 'active' : ''}" data-action="filter:${k}">${esc(l)}</button>`).join('')}</div>${ps.length ? productGrid(ps) : empty('Tidak ada produk cocok', 'Coba kata kunci atau kategori lain.', '/shop', 'Tampilkan semua')}</div></div></div>`); }
function detail(id) { const p = PRODUCT_TYPES.find(x => x.id === id); if (!p)
    return notFound(); return publicLayout(`<div class="content"><div class="detail-layout"><div class="detail-art"><img src="${art(p.kind)}" alt="Model produk ${esc(p.name)}"></div><div class="detail-info"><span class="eyebrow">ATELIER / ${esc(p.label)}</span><h1>${esc(p.name)}</h1><p class="price" style="font-size:1.25rem">Mulai ${money(p.price)}</p><p class="detail-desc">${esc(p.desc)} Lihat produk dari berbagai sisi dan pilih detailnya di studio interaktif.</p><div class="spec"><strong>Material</strong><span>${esc(p.material)}</span></div><div class="spec"><strong>Kategori</strong><span>${esc(p.label)}</span></div><div class="spec"><strong>Customization</strong><span>3D Preset + Bebas</span></div><div class="stack" style="margin-top:30px">${anchor(`/studio/${p.kind}/${p.id}`, '✧ Custom dalam 3D Studio ↗', 'primary full')}${btn('♡ Simpan ke Wishlist', `wish:${p.id}`, 'secondary full')}</div><p class="small muted" style="margin-top:15px">Harga akhir akan menyesuaikan desain. Pembelian dalam versi ini hanyalah simulasi.</p></div></div><section class="section"><div class="section-title"><h2>You might also love.</h2></div>${productGrid(PRODUCT_TYPES.filter(x => x.id !== p.id).slice(0, 4))}</section></div>`); }
function studio() { return publicLayout(`<div class="content">${pageHead('WELCOME TO THE STUDIO', 'Make it yours.', 'Delapan cara untuk merancang produk. Pilih kategori, lalu putar model dan personalisasikan detailnya.')}<div class="studio-grid">${PRODUCT_TYPES.map(p => anchor(`/studio/${p.kind}/${p.id}`, `<img loading="lazy" src="${art(p.kind)}" alt="Model ${esc(p.label)}"><div><strong>${esc(p.label)} ↗</strong><p>${esc(p.desc)}</p></div>`, 'studio-category')).join('')}</div><section class="section"><div class="card-soft"><span class="eyebrow">HOW IT WORKS</span><div class="grid-3" style="margin-top:15px"><div><h3>01. Pilih</h3><p class="small muted">Mulai dari model atau preset.</p></div><div><h3>02. Buat</h3><p class="small muted">Atur warna, ornamen, dan posisinya.</p></div><div><h3>03. Simpan</h3><p class="small muted">Lanjutkan kapan pun atau coba checkout demo.</p></div></div></div></section></div>`); }
function empty(title, sub, path, label) { return `<div class="empty"><div class="empty-icon">✧</div><h3>${title}</h3><p>${sub}</p>${anchor(path, label + ' ↗', 'primary')}</div>`; }
function studioEditor(kind, id) { const p = getProduct(kind); if (!p || p.id !== id)
    return notFound(); const q = new URL(location.href).searchParams.get('design'); const saved = db.designs.find(x => x.id === q); if (!studioDesign || studioDesign.kind !== kind || q && studioDesign.id !== q)
    studioDesign = saved ? structuredClone(saved) : newDesign(kind); const d = studioDesign; if (!d.skinTone)
    d.skinTone = 'sawo-matang'; const currentSkin = SKIN_TONES.find(x => x.id === d.skinTone) || SKIN_TONES[0]; const isSticker = ['phone', 'tablet', 'macbook', 'bottle'].includes(kind); const palette = deviceVariant(kind, d.deviceModel)?.colors || (kind === 'bottle' ? ['#3E4141', '#858988'] : kind === 'bag-charm' ? ['#222326'] : ['#C8B5A0', '#CCAA74', '#A6A7A7', '#8F503C', '#64735B']); const colors = palette.map(v => `<button type="button" class="swatch ${d.color === v ? 'active' : ''}" style="--color:${v}" data-action="set-color:${v}" aria-label="Warna ${v}" aria-pressed="${d.color === v}"></button>`).join(''); const skinSwatches = SKIN_TONES.map(t => `<button type="button" class="swatch ${d.skinTone === t.id ? 'active' : ''}" style="--color:${t.hex}" data-action="set-skin-tone:${t.id}" aria-label="Tone kulit ${t.name}" aria-pressed="${d.skinTone === t.id}" title="${t.name} · ${t.note}"></button>`).join(''); const opts = ['heart', 'star', 'flower', 'pearl'].map(v => `<button class="chip ${d.ornament === v ? 'active' : ''}" data-action="ornament:${v}" aria-pressed="${d.ornament === v}">${{ heart: '♡ Hati', star: '☆ Bintang', flower: '✿ Bunga', pearl: '◉ Pearl' }[v]}</button>`).join(''); const headerHTML = `<header class="studio-head">${anchor('/studio', '← Kembali ke Studio', 'ghost small')}${anchor('/', 'ATELIER.', 'brand')}${btn('↺ Reset', 'reset-camera', 'ghost')}</header>`; return `<div class="studio-page">${headerHTML}<main class="studio-shell"><section class="viewer" id="viewer" aria-label="Area pratinjau 3D"><div class="viewer-top"><span class="pill" style="background:#FFF9F2">● 3D Interaktif</span><span class="pill" style="background:#FFF9F2">360° · Zoom</span></div><p class="viewer-info">Seret untuk memutar · Geser vertikal ubah sudut · Cubit untuk zoom</p><div class="viewer-quality">${btn('↶', 'rotate-view-left', 'secondary small', 'aria-label="Putar model ke kiri 45 derajat"')}${btn('↷', 'rotate-view-right', 'secondary small', 'aria-label="Putar model ke kanan 45 derajat"')}${btn('−', 'zoom-view-out', 'secondary small', 'aria-label="Perkecil model"')}${btn('+', 'zoom-view-in', 'secondary small', 'aria-label="Perbesar model"')}${btn('360°', 'force-360', 'secondary small', 'aria-label="Beralih ke mode putar 360 derajat tanpa GPU"')}${btn('⤢ Reset View', 'reset-camera', 'secondary small')}</div></section><aside class="studio-panel" aria-label="Pengaturan desain"><div class="studio-title"><div><span class="eyebrow">YOUR PERSONAL STUDIO</span><h2>${esc(p.name)}</h2></div></div><p class="small muted">${isSticker ? 'Atur desain stiker pada permukaan produk.' : 'Pilih model, warna, dan detail ornamen yang paling cocok.'}</p><div class="studio-controls">${deviceList(kind).length ? `<div><label class="field-label" for="device-model-select">Model perangkat Apple</label><select class="field" id="device-model-select">${deviceList(kind).map(m => `<option value="${m.id}" ${d.deviceModel === m.id ? 'selected' : ''}>${esc(m.name)}</option>`).join('')}</select><p class="small muted" style="margin-top:6px">Proporsi bodi mengikuti ukuran resmi. Mesh 3D masih prototipe, bukan CAD resmi.</p></div>` : ''}<div><span class="field-label">01 · Pilih Ornamen / Stiker</span><div class="chips">${opts}</div></div><div><span class="field-label">02 · Warna Material</span><div class="swatches">${colors}</div></div>${['bracelet', 'ring', 'necklace'].includes(kind) ? `<div><span class="field-label">03 · Tone Kulit <span class="muted" id="skin-tone-name">${esc(currentSkin.name)}</span></span><div class="swatches">${skinSwatches}</div><p class="small muted" style="margin-top:8px">Default menggunakan tone kulit Indonesia sawo matang, dan bisa diganti kapan saja.</p></div>` : ''}${kind === 'phone' ? `<div><label class="field-label" for="case-select">03 · Jenis Casing</label><select id="case-select" class="field"><option value="plain" ${d.caseType === 'plain' ? 'selected' : ''}>Casing Polos</option><option value="clear" ${d.caseType === 'clear' ? 'selected' : ''}>Casing Transparan</option></select></div>` : ''}${kind === 'ring' ? `<div><label class="field-label" for="finger-select">04 · Jari Cincin</label><select id="finger-select" class="field">${['Ibu Jari', 'Telunjuk', 'Tengah', 'Manis', 'Kelingking'].map((x, i) => `<option value="${i}" ${d.finger === i ? 'selected' : ''}>${x}</option>`).join('')}</select></div>` : ''}<div><label class="field-label" for="place-slider">${isSticker ? 'Posisi Stiker' : 'Posisi Ornamen'} <span id="placement-number" class="muted">${d.placement}%</span></label><input class="range" type="range" min="0" max="100" value="${d.placement}" id="place-slider"></div><div class="grid-2"><div><label class="field-label" for="scale-slider">Ukuran</label><input class="range" type="range" min="0.55" max="1.55" step="0.05" value="${d.scale}" id="scale-slider"></div><div><label class="field-label" for="rotate-slider">Rotasi Stiker/Charm</label><input class="range" type="range" min="0" max="360" step="5" value="${d.rotation}" id="rotate-slider"></div></div>${['ring', 'necklace', 'bracelet', 'macbook'].includes(kind) ? `<div><label class="field-label" for="pose-slider">${kind === 'macbook' ? 'Sudut pandang laptop' : 'Sudut tampilan manekin'}</label><input class="range" type="range" min="0" max="100" value="${d.pose}" id="pose-slider"></div>` : ''}<div class="row" style="flex-wrap:wrap">${btn('← Posisi', 'place:-10', 'secondary')}${btn('Posisi →', 'place:+10', 'secondary')}${btn('↻ Putar 15°', 'rotate-decal', 'secondary')}</div><div><label class="field-label" for="render-quality">Kualitas pratinjau</label><select class="field" id="render-quality"><option value="auto" ${d.quality === 'auto' ? 'selected' : ''}>Otomatis (disarankan)</option><option value="low" ${d.quality === 'low' ? 'selected' : ''}>Hemat baterai</option><option value="high" ${d.quality === 'high' ? 'selected' : ''}>Detail tinggi</option></select></div></div><div class="summary-box"><div class="row between"><span class="small muted">Model dasar</span><span class="small">${money(p.price)}</span></div><div class="row between" style="margin-top:8px"><span class="small muted">Ornamen personal</span><span class="small">${money(isSticker ? 0 : 8000)}</span></div><div class="summary-total"><span>Total desain</span><span id="studio-price">${money(p.price + (isSticker ? 0 : 8000))}</span></div></div><div class="stack">${btn('✧ Simpan Desain', 'save-design', 'secondary full')}${btn('Tambah ke Keranjang ↗', 'add-to-cart', 'primary full')}</div></aside></main><div class="sticky-action"><div><div class="tiny muted">Total desain</div><strong class="price" id="sticky-price">${money(p.price + (isSticker ? 0 : 8000))}</strong></div>${btn('Keranjang ↗', 'add-to-cart', 'primary')}</div></div>`; }
function calcDesign(d) { const p = getProduct(d.kind); return p.price + (['phone', 'tablet', 'macbook', 'bottle'].includes(d.kind) ? 0 : 8000); }
function cart() { const rows = db.cart.map((e, i) => `<div class="cart-row"><img src="${art(e.design.kind)}" alt="${esc(e.design.name)}"><div><h3>${esc(e.design.name)}</h3><p class="small muted">${esc(e.design.ornament)} · ${esc(e.design.color)} · ${e.qty} item</p><div class="row" style="margin-top:8px">${btn('−', `qty:${i}:-1`, 'secondary')}${btn('+', `qty:${i}:1`, 'secondary')}${btn('Hapus', `remove-cart:${i}`, 'ghost')}</div></div><strong class="price">${money(e.design.price * e.qty)}</strong></div>`).join(''); const total = db.cart.reduce((a, x) => a + x.design.price * x.qty, 0); return publicLayout(`<div class="content">${pageHead('YOUR SELECTION', 'Your little treasures.', 'Periksa kembali hasil custom sebelum melanjutkan.')}${db.cart.length ? `${rows}<div class="cart-total"><div class="summary-line"><span>Subtotal</span><strong>${money(total)}</strong></div><div class="summary-line"><span>Pengiriman</span><span>Ditentukan saat checkout</span></div><div class="line"></div><div class="summary-line"><strong>Total sementara</strong><strong>${money(total)}</strong></div>${anchor('/checkout', 'Lanjut Checkout ↗', 'primary full')}<p class="tiny muted" style="margin-top:15px">Ini simulasi. Tidak ada pembayaran sungguhan.</p></div>` : empty('Keranjangmu masih kosong', 'Saatnya menemukan sesuatu yang bisa kamu buat sendiri.', '/shop', 'Jelajahi Koleksi')}</div>`); }
function checkout() { if (!db.cart.length)
    return cart(); const sub = db.cart.reduce((a, x) => a + x.design.price * x.qty, 0); return publicLayout(`<div class="content">${pageHead('FINAL TOUCH', 'Almost yours.', 'Lengkapi detail berikut untuk membuat pesanan demo.')}<div class="checkout-layout"><form id="checkout-form" class="stack"><div class="checkout-section"><h3>01. Informasi Penerima</h3><div class="stack"><div><label class="field-label" for="customer-name">Nama lengkap</label><input class="field" id="customer-name" name="customer" value="${esc(db.profile.name === 'Pengunjung Atelier' ? '' : db.profile.name)}" required minlength="2" autocomplete="name"></div><div><label class="field-label" for="customer-email">Alamat email</label><input class="field" id="customer-email" type="email" name="email" value="${esc(db.profile.email)}" required autocomplete="email"></div><div><label class="field-label" for="shipping-address">Alamat pengiriman</label><textarea class="field" rows="3" id="shipping-address" name="address" minlength="10" required>${esc(db.addresses[0]?.address || '')}</textarea></div></div></div><div class="checkout-section"><h3>02. Pilihan Pengiriman</h3><label class="row small"><input type="radio" name="ship" value="Reguler Demo" checked> Pengiriman Reguler · Rp0 (simulasi)</label></div><div class="checkout-section"><h3>03. Pembayaran</h3><div class="warning">Mode demonstrasi: tombol di bawah hanya membuat pesanan lokal. Tidak mengirim dana atau memanggil Midtrans.</div><div class="row small" style="margin-top:12px"><input type="radio" checked disabled> Pembayaran Simulasi</div></div><button class="primary full" type="submit">Buat Pesanan Demo ↗</button></form><aside><div class="checkout-section"><h3>Ringkasan pesanan</h3>${db.cart.map(e => `<div class="summary-line"><span>${esc(e.design.name)} × ${e.qty}</span><strong>${money(e.design.price * e.qty)}</strong></div>`).join('')}<div class="line"></div><div class="summary-line"><strong>Total</strong><strong>${money(sub)}</strong></div></div></aside></div></div>`, false); }
function result() { const o = db.orders[0]; return publicLayout(`<div class="content max-700"><div class="empty" style="margin-top:40px"><div class="empty-icon">✓</div><h2>Pesanan demo tercatat.</h2><p>Terima kasih sudah mencoba Atelier. Ini hanya simulasi dan tidak ada pembayaran nyata.</p>${o ? `<div class="card-soft" style="margin:20px 0"><div class="small">Nomor pesanan: <strong>${esc(o.id)}</strong></div><div class="price">${money(o.total)}</div></div>` : ''}${anchor('/account/orders', 'Lihat Riwayat Pesanan ↗', 'primary')}</div></div>`); }
function help() { const faqs = [['Bagaimana cara membuat desain 3D?', 'Buka Studio, pilih kategori, lalu gunakan panel preset, warna, ornamen, posisi, dan rotasi. Seret model untuk memutar dan cubit untuk zoom.'], ['Apakah uang akan terpotong saat checkout?', 'Tidak. Website ini adalah demo untuk tugas KWU. Tidak ada payment gateway produksi atau transaksi uang asli.'], ['Apakah desain bisa disimpan?', 'Bisa. Pada versi ini desain disimpan di penyimpanan browser perangkat yang sama. Jika data browser dihapus, desain dapat hilang.'], ['Apakah casing dan botol juga dijual?', 'Pada prototipe ini HP, tablet, MacBook, dan botol adalah media pratinjau. Produk yang dihitung adalah stiker, kecuali katalog menyediakan produk fisik terpisah.'], ['Kenapa 3D tampak berbeda dari foto asli?', 'Model 3D saat ini merupakan prototipe prosedural untuk demonstrasi interaksi. Akurasi material dan bentuk akan disempurnakan melalui produksi aset Blender.'], ['Apakah dapat dipakai di HP?', 'Ya, layout mobile-first dan renderer WebGL 2 dibuat responsif. Pada perangkat tanpa WebGL 2, area akan menampilkan pemberitahuan.']]; return publicLayout(`<div class="content max-700">${pageHead('HERE TO HELP', 'How can we help?', 'Jawaban atas pertanyaan yang paling sering muncul.')}<div class="help-list">${faqs.map(([a, b]) => `<details><summary>${a}</summary><p>${b}</p></details>`).join('')}</div><div class="card-soft" style="margin-top:36px"><h3>Masih ada pertanyaan?</h3><p class="small muted">${db.store.supportEmail ? `Hubungi ${esc(db.store.name)} melalui <a href="mailto:${esc(db.store.supportEmail)}">${esc(db.store.supportEmail)}</a>.` : 'Untuk demo ini, silakan hubungi tim proyek melalui informasi yang diberikan di kelas.'}</p></div></div>`); }
function about() { return publicLayout(`<div class="container"><section class="hero" style="margin-top:15px"><div class="hero-copy"><p class="eyebrow">OUR STORY</p><h1>Made to feel like you.</h1><p class="sub">Kami percaya benda kecil punya cerita. Atelier memberikan ruang untuk memilih detail dan melihat hasilnya sebelum memutuskan.</p>${anchor('/studio', 'Ciptakan Sesuatu ↗', 'primary')}</div><div class="hero-art"><img class="hero-object" src="${art('bracelet')}" alt="Gelang custom pada manekin tangan"></div></section><section class="section max-700" style="margin:80px auto"><p class="eyebrow">WHY ATELIER?</p><h2>Your imagination, made visible.</h2><p class="muted" style="margin-top:20px">Proyek kewirausahaan ini mengeksplorasi pengalaman personalisasi aksesori dan stiker dengan visualisasi 3D yang dapat diputar. Kami merancang antarmuka yang tenang, hangat, dan mudah dipakai di perangkat mobile.</p></section></div>`); }
function legal(slug) { const privacy = slug === 'privacy'; return publicLayout(`<div class="content legal">${pageHead('THE DETAILS', privacy ? 'Privasi & Data.' : 'Syarat & Ketentuan.')}<article><h3>${privacy ? 'Penyimpanan lokal' : 'Status demonstrasi'}</h3><p>${privacy ? 'Aplikasi demo menggunakan localStorage untuk menyimpan desain, daftar favorit, keranjang, dan pesanan pada perangkatmu. Tidak ada server akun atau basis data eksternal pada versi GitHub Pages ini.' : 'Atelier yang berjalan di GitHub Pages merupakan prototipe akademik. Produk dan harga adalah data contoh, dan tombol checkout tidak memproses pembayaran asli.'}</p><h3>${privacy ? 'Tidak ada pembayaran nyata' : 'Aset produk'}</h3><p>${privacy ? 'Tidak ada metode pembayaran aktif dan data kartu tidak diminta. Jangan gunakan informasi pribadi sensitif saat mencoba formulir demo.' : 'Model 3D merupakan prototipe prosedural. Visual tidak boleh dianggap menjamin ukuran atau material barang fisik sampai diverifikasi oleh owner.'}</p><h3>Perubahan layanan</h3><p>Fitur dapat berubah selama pengembangan tugas KWU. Perubahan produksi akan memerlukan kebijakan bisnis, autentikasi server, dan pembayaran terverifikasi yang terpisah.</p></article></div>`); }
function login() { return publicLayout(`<div class="content"><div class="form-layout"><span class="eyebrow">WELCOME BACK</span><h1>Welcome to Atelier.</h1><p>Pilih mode pengguna untuk mencoba alur pembeli atau pengelolaan owner. Ini bukan autentikasi sungguhan.</p><form id="login-form"><div><label class="field-label" for="login-email">Email demo</label><input id="login-email" class="field" type="email" name="email" value="${esc(db.profile.email)}" placeholder="kamu@contoh.com" autocomplete="email" required></div><div><label class="field-label" for="login-role">Masuk sebagai</label><select id="login-role" class="field" name="role"><option value="buyer">Pembeli Demo</option><option value="owner">Owner Demo</option></select></div><div class="form-note">Tidak memerlukan password dan tidak membuat sesi aman. Mode owner hanya untuk pengujian tampilan.</div><button class="primary full" type="submit">Masuk Mode Demo ↗</button><div class="row between">${anchor('/register', 'Buat Profil Demo', 'ghost small')}${anchor('/forgot-password', 'Lupa Password?', 'ghost small')}</div></form></div></div>`, false); }
function register() { return publicLayout(`<div class="content"><div class="form-layout"><p class="eyebrow">PERSONALIZE YOUR SPACE</p><h1>Make it yours.</h1><p>Buat profil demo yang tersimpan hanya di browser ini.</p><form id="register-form"><div><label for="register-name" class="field-label">Nama</label><input class="field" name="name" id="register-name" required minlength="2" autocomplete="name"></div><div><label for="register-email" class="field-label">Email</label><input class="field" name="email" type="email" id="register-email" required autocomplete="email"></div><div class="form-note">Mode demo tidak menyimpan password. Untuk akun nyata dibutuhkan sistem autentikasi server.</div><button type="submit" class="primary full">Buat Profil Demo</button>${anchor('/login', 'Sudah punya profil? Masuk', 'ghost small')}</form></div></div>`, false); }
function recovery(reset = false) { return publicLayout(`<div class="content"><div class="form-layout"><span class="eyebrow">ACCOUNT HELP</span><h1>${reset ? 'Set a new password.' : 'Reset your access.'}</h1><p>Versi demo belum mempunyai server email, jadi proses reset password nyata belum tersedia.</p><div class="form-note" style="margin:25px 0">Silakan masuk melalui Mode Demo tanpa password untuk mencoba seluruh alur aplikasi.</div>${anchor('/login', 'Kembali ke Login ↗', 'primary')}</div></div>`, false); }
function accessCard(path, symbol, title, desc) { return anchor(path, `<span style="font-size:1.35rem;color:var(--primary)">${symbol}</span><br>${title}<small>${desc}</small>`); }
function account() { return publicLayout(`<div class="content max-700">${pageHead('YOUR PERSONAL SPACE', 'Your atelier.', 'Satu tempat untuk desain, koleksi, dan riwayatmu.')}<div class="account-head"><div><span class="eyebrow">HELLO THERE</span><h3>${esc(db.profile.name)}</h3><p class="small muted">${db.role === 'guest' ? 'Mode tamu' : db.role === 'owner' ? 'Owner Demo' : 'Pembeli Demo'}</p></div>${anchor('/login', 'Ganti Mode', 'secondary')}</div><div class="account-menu">${accessCard('/account/designs', '✧', 'Desain Tersimpan', `${db.designs.length} kreasi personal`)}${accessCard('/account/wishlist', '♡', 'Wishlist', `${db.wishlist.length} produk favorit`)}${accessCard('/account/orders', '▤', 'Riwayat Pesanan', `${db.orders.length} pesanan demo`)}${accessCard('/account/addresses', '⌂', 'Buku Alamat', 'Alamat pengiriman')}${accessCard('/account/profile', '♙', 'Profil & Pengaturan', 'Informasi profil dan preferensi')}${accessCard('/help', '?', 'Pusat Bantuan', 'Cara custom dan transaksi')}</div>${db.role === 'owner' ? `<div style="margin-top:20px">${anchor('/owner', 'Masuk Dashboard Owner ↗', 'primary')}</div>` : ''}</div>`); }
function designs() { return publicLayout(`<div class="content">${pageHead('YOUR COLLECTION', 'Saved creations.', 'Lanjutkan desain yang sudah kamu buat.')}${db.designs.length ? `<div class="product-grid">${db.designs.map(d => `<article class="product-card"><div class="product-image"><img src="${art(d.kind)}" alt="${esc(d.name)}"></div><strong class="product-name">${esc(d.name)}</strong><span class="small muted">${esc(d.ornament)} · ${money(d.price)}</span><div class="row">${anchor(`/studio/${d.kind}/${d.productId}?design=${encodeURIComponent(d.id)}`, 'Edit', 'secondary')}${btn('Hapus', `delete-design:${d.id}`, 'ghost')}</div></article>`).join('')}</div>` : empty('Belum ada desain tersimpan', 'Buka studio dan buat kreasi pertama kamu.', '/studio', 'Mulai Mendesain')}</div>`); }
function wishlist() { const ps = PRODUCT_TYPES.filter(p => db.wishlist.includes(p.id)); return publicLayout(`<div class="content">${pageHead('HANDPICKED', 'Your favorites.', 'Produk yang ingin kamu simpan untuk nanti.')}${ps.length ? productGrid(ps) : empty('Belum ada favorit', 'Tap ikon hati pada produk yang kamu suka.', '/shop', 'Cari Produk')}</div>`); }
function orders() { return publicLayout(`<div class="content max-700">${pageHead('YOUR PURCHASES', 'Order history.', 'Seluruh pesanan yang kamu buat pada mode demo.')}${db.orders.length ? db.orders.map(o => `<div class="order-item"><div><p class="small muted">${esc(o.id)} · ${new Date(o.createdAt).toLocaleDateString('id-ID')}</p><strong>${esc(o.items[0]?.design.name || 'Pesanan')}</strong><p class="price">${money(o.total)}</p></div><div class="stack"><span class="status ${o.status === 'Selesai' ? 'done' : 'pending'}">${esc(o.status)}</span>${anchor(`/account/orders/${o.id}`, 'Detail ↗', 'ghost small')}</div></div>`).join('') : empty('Belum ada pesanan', 'Kamu bisa mencoba alur checkout tanpa membayar uang sungguhan.', '/shop', 'Mulai Belanja')}</div>`); }
function orderDetail(id, owner = false) { const o = db.orders.find(x => x.id === id); if (!o)
    return notFound(); const info = `<div class="stack max-700"><div class="card"><div class="row between"><strong>Pesanan ${esc(o.id)}</strong><span class="status pending">${esc(o.status)}</span></div><p class="muted small">${new Date(o.createdAt).toLocaleString('id-ID')}</p><div class="line"></div>${o.items.map(e => `<div class="cart-row"><img src="${art(e.design.kind)}" alt="${esc(e.design.name)}"><div><strong>${esc(e.design.name)}</strong><p class="small muted">Charm: ${esc(e.design.ornament)} · ${esc(e.design.color)}</p><p class="small muted">Posisi: ${e.design.placement}% · Ukuran: ${e.design.scale}×</p></div><strong>${money(e.design.price * e.qty)}</strong></div>`).join('')}<div class="summary-line"><strong>Total</strong><strong>${money(o.total)}</strong></div></div><div class="card"><h3 style="font-family:Manrope,sans-serif;font-size:1rem">Pengiriman</h3><p class="small muted" style="margin-top:10px">${esc(o.customer)} · ${esc(o.address)}</p><p class="small muted">${esc(o.shipping)}</p></div><div class="card"><h3 style="font-family:Manrope,sans-serif;font-size:1rem">Status pembayaran</h3><p class="small muted">SIMULASI. Tidak ada transaksi uang asli.</p></div>${owner ? `<div class="card"><label class="field-label" for="owner-status">Ubah status pesanan</label><select class="field" id="owner-status">${['Menunggu Proses', 'Diproduksi', 'Dikemas', 'Dikirim', 'Selesai', 'Dibatalkan'].map(x => `<option value="${x}" ${o.status === x ? 'selected' : ''}>${x}</option>`).join('')}</select>${btn('Simpan Status', `save-order-status:${o.id}`, 'primary full', 'style="margin-top:12px"')}</div>` : ''}</div>`; return owner ? ownerLayout(pageHead('ORDER MANAGEMENT', 'Detail Pesanan') + info) : publicLayout(`<div class="content">${pageHead('ORDER DETAIL', 'Your order.')}${info}</div>`); }
function addresses() { return publicLayout(`<div class="content max-700">${pageHead('DELIVERY DETAILS', 'Address book.')}<div class="stack">${db.addresses.map(a => `<div class="order-item"><div><strong>${esc(a.name)}</strong><p class="small muted">${esc(a.address)}</p></div>${btn('Hapus', `delete-address:${a.id}`, 'ghost')}</div>`).join('')}<form id="address-form" class="card stack"><h3 style="font-family:Manrope,sans-serif;font-size:.9rem">Alamat baru</h3><div><label class="field-label" for="address-label">Nama Alamat</label><input class="field" id="address-label" name="name" placeholder="Rumah" required></div><div><label class="field-label" for="address-text">Alamat lengkap</label><textarea class="field" rows="3" id="address-text" name="address" required minlength="10"></textarea></div><button class="primary" type="submit">Tambah Alamat</button></form></div></div>`); }
function profile() { return publicLayout(`<div class="content max-700">${pageHead('ACCOUNT SETTINGS', 'Your profile.')}<form class="card stack" id="profile-form"><div><label class="field-label" for="profile-name">Nama</label><input class="field" name="name" id="profile-name" value="${esc(db.profile.name)}" required minlength="2"></div><div><label class="field-label" for="profile-email">Email</label><input class="field" name="email" id="profile-email" type="email" value="${esc(db.profile.email)}" required></div><button class="primary" type="submit">Simpan Profil</button></form><div class="card" style="margin-top:15px"><h3 style="font-family:Manrope;font-size:.9rem">Mode Demonstrasi</h3><p class="muted small" style="margin:10px 0">Keluar hanya mengubah mode lokal. Data demo tetap tersimpan di perangkat ini.</p>${btn('Keluar dari Mode', 'logout', 'secondary')}${btn('Hapus Semua Data Demo', 'reset-data', 'danger-btn', 'style="margin-left:8px"')}</div></div>`); }
const OWNER_MENU = [['/owner', '⌂', 'Ringkasan'], ['/owner/orders', '▤', 'Pesanan'], ['/owner/products', '◇', 'Produk'], ['/owner/components', '✧', 'Komponen'], ['/owner/assets', '⬡', 'Aset 3D'], ['/owner/inventory', '▥', 'Stok'], ['/owner/payments', '◈', 'Pembayaran'], ['/owner/customers', '♙', 'Pelanggan'], ['/owner/reports', '▤', 'Laporan'], ['/owner/settings', '☷', 'Pengaturan']];
// Inventory for both owner navigation and asset library. Category and Apple variants use the same model IDs as Studio.
const OWNER_3D_MODELS = [
    ...PRODUCT_TYPES.map(p => ({ id: p.kind, name: p.label, kind: p.kind, group: '8 Model Utama' })),
    ...['phone', 'tablet', 'macbook'].flatMap(kind => DEVICE_VARIANTS[kind].map(v => ({ id: v.id, name: v.name, kind, group: kind === 'phone' ? 'iPhone' : kind === 'tablet' ? 'iPad' : 'MacBook' })))
];
function ownerModelPath(id) { return `/owner/assets?model=${encodeURIComponent(id)}`; }
function currentOwnerModel() { const query = window.__KWU_TEST_MODE ? String(window.__KWU_TEST_PATH || '').split('?')[1] || '' : location.search; const id = new URLSearchParams(query).get('model'); return OWNER_3D_MODELS.find(m => m.id === id) || OWNER_3D_MODELS[0]; }
function ownerModelNav() { const model = currentOwnerModel(); return `<nav class="owner-model-nav" aria-label="Daftar seluruh model 3D owner"><div class="owner-model-nav-title"><span>KOLEKSI 3D · ${OWNER_3D_MODELS.length} MODEL</span>${anchor('/owner/assets', 'Lihat Semua ↗', 'owner-model-all')}</div><div class="owner-model-scroll">${OWNER_3D_MODELS.map(m => anchor(ownerModelPath(m.id), `<img src="${art(m.id)}" alt="" loading="lazy"><span>${esc(m.name)}</span>`, `owner-model-link ${currentPath === '/owner/assets' && model.id === m.id ? 'active' : ''}`)).join('')}</div></nav>`; }
function ownerLayout(body) { if (db.role !== 'owner')
    return publicLayout(`<div class="content max-700">${empty('Akses Owner Demo', 'Untuk melihat dashboard, masuk ke Mode Owner melalui halaman login demo.', '/login', 'Pilih Mode Demo')}</div>`); return `<div class="demo-banner"><strong>DASHBOARD OWNER DEMO</strong> · Data lokal, bukan data pembeli nyata.</div><header class="site-header">${anchor('/', 'ATELIER<span class="dot">.</span>', 'brand')}<div class="row"><span class="small muted">Owner Workspace</span>${anchor('/', 'Buka Toko ↗', 'secondary small')}</div></header><div class="owner-shell"><aside class="owner-sidebar"><h3>Management</h3>${OWNER_MENU.map(([p, i, l]) => anchor(p, `<span aria-hidden="true">${i}</span>${l}`, currentPath === p ? 'active' : '')).join('')}<div class="owner-sidebar-models"><h3>Semua Model 3D</h3>${OWNER_3D_MODELS.map(m => anchor(ownerModelPath(m.id), `<span class="owner-model-index">▧</span>${esc(m.name)}`, currentPath === '/owner/assets' && currentOwnerModel().id === m.id ? 'active' : '')).join('')}</div></aside><main class="owner-main" id="main">${ownerModelNav()}${body}</main></div>${bottomNav(true)}`; }
function ownerHome() { const rev = db.orders.filter(o => o.status !== 'Dibatalkan').reduce((sum, o) => sum + o.total, 0), ongoing = db.orders.filter(o => !['Selesai', 'Dibatalkan'].includes(o.status)).length; return ownerLayout(`${pageHead('OWNER STUDIO', 'At a glance.', `Ringkasan ${esc(db.store.name)} untuk pengujian alur bisnis.`)}<div class="stat-grid"><div class="stat-card"><div class="stat-label">Omzet Demo</div><div class="stat-number">${money(rev)}</div></div><div class="stat-card"><div class="stat-label">Total Pesanan</div><div class="stat-number">${db.orders.length}</div></div><div class="stat-card"><div class="stat-label">Perlu Diproses</div><div class="stat-number">${ongoing}</div></div><div class="stat-card"><div class="stat-label">Produk Aktif</div><div class="stat-number">${PRODUCT_TYPES.length - db.productsHidden.length}</div></div></div><section class="section"><div class="section-title"><h2>Latest orders.</h2>${anchor('/owner/orders', 'Lihat semua ↗', 'ghost')}</div>${db.orders.length ? db.orders.slice(0, 5).map(o => `<div class="order-item"><div><strong>${esc(o.customer)}</strong><p class="small muted">${esc(o.id)} · ${money(o.total)}</p></div>${anchor(`/owner/orders/${o.id}`, `<span class="status pending">${esc(o.status)}</span> →`, 'ghost')}</div>`).join('') : empty('Belum ada pesanan', 'Coba tambahkan produk ke keranjang lalu buat pesanan demo dari sisi pembeli.', '/shop', 'Coba Belanja')}</section><section class="section"><div class="card-soft"><h3>Creative commerce.</h3><p class="small muted" style="margin:12px 0">Kelola katalog, komponennya, dan model GLB yang dipakai pada delapan scene 3D.</p>${anchor('/owner/assets', 'Lihat Library 3D ↗', 'primary')}</div></section>`); }
function ownerOrders() { return ownerLayout(`${pageHead('ORDER MANAGEMENT', 'Incoming orders.', 'Lihat dan ubah status pesanan simulasi.')}${db.orders.length ? `<div class="stack">${db.orders.map(o => `<div class="order-item"><div><strong>${esc(o.id)}</strong><p class="small muted">${esc(o.customer)} · ${new Date(o.createdAt).toLocaleDateString('id-ID')}</p><p class="price">${money(o.total)}</p></div><div class="stack"><span class="status pending">${esc(o.status)}</span>${anchor(`/owner/orders/${o.id}`, 'Buka ↗', 'secondary')}</div></div>`).join('')}</div>` : empty('No orders yet', 'Coba membuat satu pesanan dari checkout mode demo.', '/shop', 'Belanja Demo')}`); }
function ownerProducts() { return ownerLayout(`${pageHead('PRODUCT MANAGEMENT', 'The collection.', 'Edit status produk, stok, atau lihat detail produknya.', anchor('/owner/products/new', 'Atur Produk Demo', 'primary'))}<div class="table-wrap"><table><thead><tr><th>Produk</th><th>Harga</th><th>Stok</th><th>Status</th><th>Aksi</th></tr></thead><tbody>${PRODUCT_TYPES.map(p => `<tr><td><div class="row"><img src="${art(p.kind)}" style="width:49px;height:52px;object-fit:contain;border-radius:8px;background:var(--soft)" alt=""><strong>${esc(p.name)}</strong></div></td><td>${money(p.price)}</td><td>${db.inventory[p.id] ?? 0}</td><td><span class="status ${db.productsHidden.includes(p.id) ? 'cancelled' : 'paid'}">${db.productsHidden.includes(p.id) ? 'Draft' : 'Aktif'}</span></td><td>${anchor(`/owner/products/${p.id}`, 'Edit', 'secondary')} ${btn(db.productsHidden.includes(p.id) ? 'Aktifkan' : 'Arsipkan', `toggle-product:${p.id}`, 'secondary')}</td></tr>`).join('')}</tbody></table></div>`); }
function ownerEditor() {
    const id = currentPath.split('/')[3] || PRODUCT_TYPES[0].id;
    const item = PRODUCT_TYPES.find(p => p.id === id) || PRODUCT_TYPES[0];
    const selector = PRODUCT_TYPES.map(p => `<option value="${esc(p.id)}" ${p.id === item.id ? 'selected' : ''}>${esc(p.name)}</option>`).join('');
    return ownerLayout(`${pageHead('PRODUCT EDITOR', 'Edit katalog demo.', 'Perubahan produk dan stok disimpan pada browser ini.')}
 <form id="owner-product-form" class="card max-700 stack">
  <div><label for="owner-product-id" class="field-label">Pilih produk</label><select class="field" id="owner-product-id" name="productId">${selector}</select></div>
  <div><label for="owner-product-name" class="field-label">Nama produk</label><input class="field" id="owner-product-name" name="name" maxlength="80" minlength="2" required value="${esc(item.name)}"></div>
  <div><label for="owner-product-desc" class="field-label">Deskripsi produk</label><textarea class="field" id="owner-product-desc" name="desc" maxlength="240" minlength="5" required rows="3">${esc(item.desc)}</textarea></div>
  <div><label for="owner-product-price" class="field-label">Harga dasar (Rp)</label><input class="field" id="owner-product-price" type="number" name="price" min="0" max="999999999" step="1000" required value="${item.price}"></div>
  <div><label for="owner-product-stock" class="field-label">Stok unit</label><input class="field" id="owner-product-stock" type="number" name="stock" min="0" max="999999" step="1" required value="${db.inventory[item.id] ?? 0}"></div>
  <div class="warning">Editor lokal untuk delapan SKU demo. Menambah SKU/model fisik baru, sinkronisasi multi-pengguna, dan pembayaran sungguhan membutuhkan backend.</div>
  <button class="primary full" type="submit">Simpan Perubahan Produk</button>
  ${anchor('/owner/products', '← Kembali ke Katalog', 'secondary full')}
 </form>`);
}
function ownerComponents() { const charms = [['heart', '♡', 'Hati'], ['star', '☆', 'Bintang'], ['flower', '✿', 'Bunga'], ['pearl', '◉', 'Pearl']]; return ownerLayout(`${pageHead('COMPONENT LIBRARY', 'Small details.', 'Pilihan stiker dan ornamen yang tersedia pada seluruh studio.')}<div class="grid-4">${charms.map(([id, ic, name]) => `<div class="card" style="text-align:center"><div style="font-size:3.7rem;color:var(--primary)">${ic}</div><strong>${name}</strong><p class="small muted">Komponen Demo</p></div>`).join('')}</div><div class="card-soft" style="margin-top:24px"><h3>Placement rules</h3><p class="small muted" style="margin-top:12px">Charm mengikuti jalur pemasangan, cincin mengikuti jari yang dipilih, dan stiker dibatasi pada permukaan valid model. Pengaturan komponen baru akan membutuhkan backend dan pipeline aset.</p></div>`); }
function ownerAssets() {
    const selected = currentOwnerModel();
    const groups = [...new Set(OWNER_3D_MODELS.map(m => m.group))];
    const userReference = selected.id === 'bag-charm' ? 'backpack-user.jpeg' : selected.id === 'bottle' ? 'bottle-user.jpeg' : null;
    const comparison = userReference ? `<details class="owner-reference-compare"><summary>Lihat foto referensi produk asli</summary><img loading="lazy" src="${BASE}assets/references/${userReference}" alt="Foto referensi asli untuk membandingkan kemiripan model ${esc(selected.name)}"><p class="small muted">Foto dari referensi pengguna. Bentuk 3D saat ini masih interpretasi, bukan hasil pemindaian produk.</p></details>` : '';
    return ownerLayout(`${pageHead('3D MODEL LIBRARY', 'Every model, in one place.', 'Akses langsung seluruh 8 kategori dan 13 perangkat Apple. Putar model 3D, periksa preview, dan unduh GLB prototipe.')}<section class="owner-featured-model"><div class="owner-featured-preview" id="owner-model-viewer" role="region" aria-label="Preview model ${esc(selected.name)}"><div class="viewer-top"><span class="pill">${esc(selected.group)}</span><span class="pill">Putar · Zoom · GLB</span></div></div><div class="owner-featured-meta"><span class="eyebrow">MODEL TERPILIH</span><h2>${esc(selected.name)}</h2><p class="muted small">Model prosedural untuk demo KWU, belum hasil scan atau replika fotorealistis 1:1. Model hanya dimuat saat halaman ini dibuka.</p><div class="row" style="flex-wrap:wrap"><a class="primary" download="${esc(selected.id)}.glb" href="${BASE}models/${selected.id}.glb">↓ Download GLB</a>${anchor(`/studio/${selected.kind}/${getProduct(selected.kind).id}`, 'Buka Studio ↗', 'secondary')}</div><p class="small muted">File: ${esc(selected.id)}.glb</p>${comparison}</div></section>${groups.map(g => `<section class="owner-model-group" aria-label="Grup ${esc(g)}"><div class="section-title"><h2>${esc(g)}</h2><span class="muted small">${OWNER_3D_MODELS.filter(m => m.group === g).length} model</span></div><div class="owner-model-grid">${OWNER_3D_MODELS.filter(m => m.group === g).map(m => `<article class="owner-model-card ${selected.id === m.id ? 'active' : ''}">${anchor(ownerModelPath(m.id), `<img src="${art(m.id)}" alt="Pratinjau ${esc(m.name)}" loading="lazy"><strong>${esc(m.name)}</strong>`, 'owner-model-card-link')}<a class="owner-model-download" download="${esc(m.id)}.glb" href="${BASE}models/${m.id}.glb">Unduh GLB ↓</a></article>`).join('')}</div></section>`).join('')}<div class="warning" style="margin-top:24px">Aset web saat ini adalah prototipe. Akurasi terhadap barang fisik, rigging anatomis, dan kualitas material premium masih membutuhkan referensi terukur dan pengujian perangkat nyata.</div>`);
}
function ownerInventory() { return ownerLayout(`${pageHead('INVENTORY', 'Stock overview.', 'Ubah stok simulasi untuk delapan SKU.')}<div class="stack max-700">${PRODUCT_TYPES.map(p => `<div class="order-item"><div><strong>${esc(p.name)}</strong><p class="small muted">Tersedia: ${db.inventory[p.id] ?? 0} unit</p></div><div class="row">${btn('−', `stock:${p.id}:-1`, 'secondary')}${btn('+', `stock:${p.id}:1`, 'secondary')}</div></div>`).join('')}</div>`); }
function ownerPayments() { return ownerLayout(`${pageHead('TRANSACTIONS', 'Payment log.', 'Seluruh transaksi adalah simulasi tanpa pemrosesan dana.')}<div class="warning">Midtrans tidak terhubung pada GitHub Pages. Status berikut hanya merepresentasikan alur demonstrasi.</div><div class="table-wrap" style="margin-top:20px"><table><thead><tr><th>No. Pesanan</th><th>Pelanggan</th><th>Nominal</th><th>Metode</th></tr></thead><tbody>${db.orders.map(o => `<tr><td>${esc(o.id)}</td><td>${esc(o.customer)}</td><td>${money(o.total)}</td><td>Simulasi</td></tr>`).join('') || '<tr><td colspan="4">Belum ada transaksi.</td></tr>'}</tbody></table></div>`); }
function ownerCustomers() { const names = [...new Map(db.orders.map(o => [o.customer, o])).values()]; return ownerLayout(`${pageHead('CUSTOMERS', 'People of Atelier.', 'Ringkasan pelanggan dari pesanan simulasi pada browser ini.')}${names.length ? names.map(o => `<div class="order-item"><div><strong>${esc(o.customer)}</strong><p class="small muted">Pelanggan demo</p></div><span class="status">${money(db.orders.filter(x => x.customer === o.customer).reduce((sum, x) => sum + x.total, 0))}</span></div>`).join('') : empty('Belum ada pelanggan demo', 'Coba alur checkout untuk membuat pelanggan lokal.', '/shop', 'Belanja Demo')}`); }
function ownerReports() { const total = db.orders.reduce((s, o) => s + o.total, 0); return ownerLayout(`${pageHead('ANALYTICS', 'Quiet numbers.', 'Ringkasan penjualan berdasarkan data demo lokal.')}<div class="stat-grid"><div class="stat-card"><div class="stat-label">Nilai Pesanan</div><div class="stat-number">${money(total)}</div></div><div class="stat-card"><div class="stat-label">Pesanan</div><div class="stat-number">${db.orders.length}</div></div><div class="stat-card"><div class="stat-label">Rata-rata Pesanan</div><div class="stat-number">${money(db.orders.length ? total / db.orders.length : 0)}</div></div><div class="stat-card"><div class="stat-label">SKU</div><div class="stat-number">${PRODUCT_TYPES.length}</div></div></div><div class="card" style="margin-top:24px"><h3>Produk paling diminati</h3>${PRODUCT_TYPES.map(p => { const n = db.orders.flatMap(o => o.items).filter(e => e.design.productId === p.id).reduce((a, e) => a + e.qty, 0); return `<div class="summary-line"><span>${p.name}</span><strong>${n} terjual (demo)</strong></div>`; }).join('')}</div>`); }
function ownerSettings() {
    return ownerLayout(`${pageHead('ATELIER SETTINGS', 'Pengaturan toko.', 'Identitas toko demonstrasi yang dapat kamu ubah secara lokal.')}
 <form id="owner-settings-form" class="card max-700 stack">
  <div><label class="field-label" for="store-name">Nama toko demo</label><input id="store-name" name="name" class="field" maxlength="70" minlength="2" value="${esc(db.store.name)}" required></div>
  <div><label class="field-label" for="store-email">Email kontak (opsional)</label><input id="store-email" name="supportEmail" type="email" class="field" maxlength="120" value="${esc(db.store.supportEmail)}" placeholder="admin@contoh.com"></div>
  <div class="warning">Perubahan ini tersimpan di browser dan akan terlihat di halaman Bantuan serta ringkasan owner. Pengaturan pembayaran nyata memerlukan server produksi.</div>
  <button class="primary full" type="submit">Simpan Pengaturan Toko</button>
  ${anchor('/owner', '← Kembali ke Ringkasan', 'secondary full')}
 </form>`);
}
function notFound() { return publicLayout(`<div class="not-found"><p class="eyebrow">PAGE NOT FOUND</p><h1>404</h1><p class="muted">Halaman yang kamu cari tidak tersedia.</p><div style="margin-top:28px">${anchor('/', 'Kembali ke Beranda ↗', 'primary')}</div></div>`); }
function render() {
    viewer?.dispose();
    viewer = null;
    currentPath = parseRoute();
    document.title = (currentPath.startsWith('/studio/') ? 'Studio 3D' : currentPath.startsWith('/owner') ? 'Owner Dashboard' : 'ATELIER') + ' · KWU Digital Atelier';
    let html;
    const parts = currentPath.split('/').filter(Boolean);
    if (currentPath === '/')
        html = home();
    else if (currentPath === '/shop')
        html = shop();
    else if (parts[0] === 'products' && parts[1])
        html = detail(parts[1]);
    else if (currentPath === '/studio')
        html = studio();
    else if (parts[0] === 'studio' && parts.length >= 3 && PRODUCT_TYPES.some(x => x.kind === parts[1]))
        html = studioEditor(parts[1], parts[2]);
    else if (currentPath === '/cart')
        html = cart();
    else if (currentPath === '/checkout')
        html = checkout();
    else if (currentPath === '/checkout/result')
        html = result();
    else if (currentPath === '/help')
        html = help();
    else if (currentPath === '/about')
        html = about();
    else if (parts[0] === 'legal')
        html = legal(parts[1] || 'terms');
    else if (currentPath === '/login')
        html = login();
    else if (currentPath === '/register')
        html = register();
    else if (currentPath === '/forgot-password')
        html = recovery();
    else if (currentPath === '/reset-password')
        html = recovery(true);
    else if (currentPath === '/account')
        html = account();
    else if (currentPath === '/account/designs')
        html = designs();
    else if (currentPath === '/account/wishlist')
        html = wishlist();
    else if (currentPath === '/account/orders')
        html = orders();
    else if (parts[0] === 'account' && parts[1] === 'orders' && parts[2])
        html = orderDetail(parts[2]);
    else if (currentPath === '/account/addresses')
        html = addresses();
    else if (currentPath === '/account/profile')
        html = profile();
    else if (currentPath === '/owner')
        html = ownerHome();
    else if (currentPath === '/owner/orders')
        html = ownerOrders();
    else if (parts[0] === 'owner' && parts[1] === 'orders' && parts[2])
        html = orderDetail(parts[2], true);
    else if (currentPath === '/owner/products')
        html = ownerProducts();
    else if (parts[0] === 'owner' && parts[1] === 'products' && parts[2])
        html = ownerEditor();
    else if (currentPath === '/owner/components')
        html = ownerComponents();
    else if (currentPath === '/owner/assets')
        html = ownerAssets();
    else if (currentPath === '/owner/inventory')
        html = ownerInventory();
    else if (currentPath === '/owner/payments')
        html = ownerPayments();
    else if (currentPath === '/owner/customers')
        html = ownerCustomers();
    else if (currentPath === '/owner/reports')
        html = ownerReports();
    else if (currentPath === '/owner/settings')
        html = ownerSettings();
    else
        html = notFound();
    ROOT.innerHTML = html;
    if (currentPath === '/owner/assets' && db.role === 'owner') {
        const preview = document.getElementById('owner-model-viewer');
        if (preview) {
            const m = currentOwnerModel();
            viewer = new Viewer3D(preview, { ...defaultOpts(m.kind), deviceModel: m.id !== m.kind ? m.id : '' }, BASE, () => { });
        }
    }
    if (parts[0] === 'studio' && parts.length >= 3 && studioDesign) {
        const el = document.getElementById('viewer');
        if (el)
            viewer = new Viewer3D(el, studioDesign, BASE, n => { if (studioDesign) {
                studioDesign.placement = Math.round(n);
                const r = document.getElementById('place-slider');
                if (r)
                    r.value = String(studioDesign.placement);
                document.getElementById('placement-number').textContent = studioDesign.placement + '%';
                viewer?.update(studioDesign);
            } });
    }
    if (pendingFocus) {
        const f = document.getElementById(pendingFocus);
        f?.focus();
        pendingFocus = null;
    }
}
function modifyStudio(key, value) { if (!studioDesign)
    return; studioDesign[key] = value; studioDesign.price = calcDesign(studioDesign); viewer?.update(studioDesign); const n = document.getElementById('studio-price'); if (n)
    n.textContent = money(studioDesign.price); const sticky = document.getElementById('sticky-price'); if (sticky)
    sticky.textContent = money(studioDesign.price); }
function actionDo(action) {
    const [name, arg, arg2] = action.split(':');
    const p = PRODUCT_TYPES.find(p => p.id === arg);
    if (['toggle-product', 'stock', 'save-order-status'].includes(name) && db.role !== 'owner') {
        notify('Masuk sebagai Owner Demo untuk mengubah data toko');
        return;
    }
    if (name === 'wish' && p) {
        db.wishlist = db.wishlist.includes(p.id) ? db.wishlist.filter(x => x !== p.id) : [...db.wishlist, p.id];
        persist();
        notify(db.wishlist.includes(p.id) ? 'Ditambahkan ke wishlist' : 'Dihapus dari wishlist');
        render();
        return;
    }
    if (name === 'filter') {
        nav(`/shop${arg === 'all' ? '' : `?category=${encodeURIComponent(arg)}`}`);
        return;
    }
    if (name === 'open-filter') {
        const box = document.getElementById('mobile-filter');
        if (box)
            box.style.display = box.style.display === 'flex' ? 'none' : 'flex';
        return;
    }
    if (name === 'set-color') {
        modifyStudio('color', arg);
        refreshStudioChips();
        return;
    }
    if (name === 'set-skin-tone') {
        modifyStudio('skinTone', arg);
        refreshStudioChips();
        return;
    }
    if (name === 'ornament') {
        modifyStudio('ornament', arg);
        refreshStudioChips();
        return;
    }
    if (name === 'place' && studioDesign) {
        const n = Math.max(0, Math.min(100, studioDesign.placement + (arg === '+10' ? 10 : -10)));
        modifyStudio('placement', n);
        const e = document.getElementById('place-slider');
        if (e)
            e.value = String(n);
        document.getElementById('placement-number').textContent = n + '%';
        return;
    }
    if (name === 'rotate-decal' && studioDesign) {
        const n = (studioDesign.rotation + 15) % 360;
        modifyStudio('rotation', n);
        document.getElementById('rotate-slider').value = String(n);
        return;
    }
    if (name === 'force-360') {
        viewer?.useTurntable();
        return;
    }
    if (name === 'rotate-view-left') {
        viewer?.rotate(-45);
        return;
    }
    if (name === 'rotate-view-right') {
        viewer?.rotate(45);
        return;
    }
    if (name === 'zoom-view-in') {
        viewer?.zoom(-.65);
        return;
    }
    if (name === 'zoom-view-out') {
        viewer?.zoom(.65);
        return;
    }
    if (name === 'reset-camera') {
        viewer?.reset();
        notify('Tampilan model direset');
        return;
    }
    if (name === 'save-design' && studioDesign) {
        const old = db.designs.findIndex(x => x.id === studioDesign.id);
        if (old >= 0)
            db.designs[old] = structuredClone(studioDesign);
        else
            db.designs.unshift(structuredClone(studioDesign));
        persist();
        notify('Desain berhasil disimpan di perangkat ini');
        return;
    }
    if (name === 'add-to-cart' && studioDesign) {
        const entry = { id: makeId(), design: structuredClone(studioDesign), qty: 1 };
        db.cart.push(entry);
        persist();
        notify('Desain ditambahkan ke keranjang');
        nav('/cart');
        return;
    }
    if (name === 'qty') {
        const i = Number(arg), step = Number(arg2);
        if (db.cart[i]) {
            db.cart[i].qty += step;
            if (db.cart[i].qty < 1)
                db.cart.splice(i, 1);
            persist();
            render();
        }
        return;
    }
    if (name === 'remove-cart') {
        db.cart.splice(Number(arg), 1);
        persist();
        render();
        return;
    }
    if (name === 'delete-design') {
        if (!confirm('Hapus desain tersimpan ini?'))
            return;
        db.designs = db.designs.filter(x => x.id !== arg);
        persist();
        render();
        return;
    }
    if (name === 'delete-address') {
        if (!confirm('Hapus alamat ini?'))
            return;
        db.addresses = db.addresses.filter(x => x.id !== arg);
        persist();
        render();
        return;
    }
    if (name === 'logout') {
        db.role = 'guest';
        persist();
        nav('/');
        notify('Keluar dari mode demo');
        return;
    }
    if (name === 'reset-data') {
        if (!confirm('Hapus seluruh data demo di browser ini?'))
            return;
        db = structuredClone(START);
        persist();
        nav('/');
        return;
    }
    if (name === 'toggle-product') {
        db.productsHidden = db.productsHidden.includes(arg) ? db.productsHidden.filter(x => x !== arg) : [...db.productsHidden, arg];
        persist();
        render();
        return;
    }
    if (name === 'stock') {
        db.inventory[arg] = Math.max(0, (db.inventory[arg] || 0) + Number(arg2));
        persist();
        render();
        return;
    }
    if (name === 'save-order-status') {
        const o = db.orders.find(o => o.id === arg);
        const s = document.getElementById('owner-status')?.value;
        if (o && s) {
            o.status = s;
            persist();
            notify('Status pesanan demo diperbarui');
            render();
        }
        return;
    }
}
function refreshStudioChips() { if (!studioDesign)
    return; document.querySelectorAll('[data-action^="ornament:"]').forEach(x => { const active = x.getAttribute('data-action') === `ornament:${studioDesign.ornament}`; x.classList.toggle('active', active); x.setAttribute('aria-pressed', String(active)); }); document.querySelectorAll('[data-action^="set-color:"]').forEach(x => { const active = x.getAttribute('data-action') === `set-color:${studioDesign.color}`; x.classList.toggle('active', active); x.setAttribute('aria-pressed', String(active)); }); document.querySelectorAll('[data-action^="set-skin-tone:"]').forEach(x => { const active = x.getAttribute('data-action') === `set-skin-tone:${studioDesign.skinTone}`; x.classList.toggle('active', active); x.setAttribute('aria-pressed', String(active)); }); const label = document.getElementById('skin-tone-name'); if (label)
    label.textContent = SKIN_TONES.find(t => t.id === studioDesign.skinTone)?.name || SKIN_TONES[0].name; }
function formSubmit(form) {
    const f = new FormData(form);
    const id = form.id;
    if (id === 'owner-product-form') {
        if (db.role !== 'owner') {
            notify('Akses hanya untuk Owner Demo');
            return;
        }
        const sku = String(f.get('productId') || '');
        const item = PRODUCT_TYPES.find(p => p.id === sku);
        const name = String(f.get('name') || '').trim();
        const desc = String(f.get('desc') || '').trim();
        const price = Number(f.get('price'));
        const stock = Number(f.get('stock'));
        if (!item || name.length < 2 || desc.length < 5 || !Number.isSafeInteger(price) || price < 0 || price > 999999999 || !Number.isSafeInteger(stock) || stock < 0 || stock > 999999) {
            notify('Data produk belum valid');
            return;
        }
        db.productEdits[sku] = { name, desc, price };
        item.name = name;
        item.desc = desc;
        item.price = price;
        db.inventory[sku] = stock;
        persist();
        nav('/owner/products');
        notify('Produk dan stok demo berhasil diperbarui');
        return;
    }
    if (id === 'owner-settings-form') {
        if (db.role !== 'owner') {
            notify('Akses hanya untuk Owner Demo');
            return;
        }
        const name = String(f.get('name') || '').trim();
        const email = String(f.get('supportEmail') || '').trim();
        if (name.length < 2 || name.length > 70 || email.length > 120) {
            notify('Periksa nama dan email toko');
            return;
        }
        db.store = { name, supportEmail: email };
        persist();
        nav('/owner/settings');
        notify('Pengaturan toko berhasil disimpan di browser');
        return;
    }
    if (id === 'login-form') {
        db.role = f.get('role') === 'owner' ? 'owner' : 'buyer';
        db.profile.email = String(f.get('email') || '');
        if (db.profile.name === 'Pengunjung Atelier')
            db.profile.name = db.role === 'owner' ? 'Owner Demo' : 'Pembeli Demo';
        persist();
        nav(db.role === 'owner' ? '/owner' : '/account');
        notify('Mode demo berhasil diaktifkan');
        return;
    }
    if (id === 'register-form') {
        db.profile = { name: String(f.get('name') || 'Pengunjung'), email: String(f.get('email') || '') };
        db.role = 'buyer';
        persist();
        nav('/account');
        notify('Profil demo dibuat');
        return;
    }
    if (id === 'profile-form') {
        db.profile = { name: String(f.get('name')), email: String(f.get('email')) };
        persist();
        notify('Profil lokal berhasil disimpan');
        render();
        return;
    }
    if (id === 'address-form') {
        db.addresses.unshift({ id: makeId(), name: String(f.get('name')), address: String(f.get('address')) });
        persist();
        notify('Alamat demo berhasil disimpan');
        render();
        return;
    }
    if (id === 'checkout-form') {
        if (!db.cart.length) {
            nav('/cart');
            return;
        }
        const total = db.cart.reduce((s, x) => s + x.design.price * x.qty, 0);
        const customer = String(f.get('customer')), address = String(f.get('address'));
        if (!customer.trim() || address.trim().length < 10) {
            notify('Lengkapi data penerima dan alamat');
            return;
        }
        db.profile = { name: customer, email: String(f.get('email')) };
        db.orders.unshift({ id: 'KWU-' + Date.now().toString().slice(-9), items: structuredClone(db.cart), total, customer, address, status: 'Menunggu Proses', createdAt: new Date().toISOString(), payment: 'DEMO', shipping: 'Reguler Demo' });
        db.cart = [];
        persist();
        nav('/checkout/result');
        return;
    }
}
ROOT.addEventListener('click', (e) => { const el = e.target.closest('[data-nav],[data-action]'); if (!el)
    return; const path = el.dataset.nav, action = el.dataset.action; if (path) {
    e.preventDefault();
    nav(path);
}
else if (action) {
    e.preventDefault();
    actionDo(action);
} });
ROOT.addEventListener('submit', e => { if (e.target instanceof HTMLFormElement) {
    e.preventDefault();
    if (e.target.reportValidity())
        formSubmit(e.target);
} });
ROOT.addEventListener('change', e => {
    const t = e.target;
    if (t.id === 'owner-product-id') {
        nav('/owner/products/' + encodeURIComponent(t.value));
        return;
    }
    if (t.id === 'device-model-select' && studioDesign) {
        const v = deviceVariant(studioDesign.kind, t.value);
        if (v) {
            studioDesign.deviceModel = v.id;
            studioDesign.color = v.colors[0];
            render();
            notify('Model ' + v.name + ' siap');
        }
    }
    if (t.id === 'case-select')
        modifyStudio('caseType', t.value);
    if (t.id === 'finger-select')
        modifyStudio('finger', Number(t.value));
    if (t.id === 'render-quality')
        modifyStudio('quality', t.value);
});
ROOT.addEventListener('input', e => {
    const t = e.target;
    if (t.id === 'shop-search') {
        const val = t.value;
        const url = new URL(location.href);
        if (val)
            url.searchParams.set('q', val);
        else
            url.searchParams.delete('q');
        history.replaceState({}, '', url);
        pendingFocus = 'shop-search';
        const sel = t.selectionStart;
        render();
        const fresh = document.getElementById('shop-search');
        if (fresh && sel !== null)
            fresh.setSelectionRange(sel, sel);
        return;
    }
    if (t.id === 'place-slider') {
        modifyStudio('placement', Number(t.value));
        const n = document.getElementById('placement-number');
        if (n)
            n.textContent = t.value + '%';
    }
    if (t.id === 'scale-slider')
        modifyStudio('scale', Number(t.value));
    if (t.id === 'rotate-slider')
        modifyStudio('rotation', Number(t.value));
    if (t.id === 'pose-slider')
        modifyStudio('pose', Number(t.value));
});
if (window.__KWU_TEST_MODE)
    window.__KWU_TEST_RENDER = render;
render();
