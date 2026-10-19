# Fallback 2D, WebGL Context Loss, dan Asset Cache

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Progressive enhancement
Saat membuka studio, poster dari komposisi default tampil instan. Canvas dimuat setelah capability check. Jika WebGL unsupported, GPU memory exhausted, asset decoder gagal, atau pengguna memilih Hemat Data, tampilkan poster 2D dan pesan jujur; interaksi 3D tidak boleh pura-pura berfungsi.

## Error categories
- Network/timeout CDN → retry dengan exponential backoff terbatas, pertahankan state.
- Format tidak didukung → catat assetId/version, fallback quality alternate jika tersedia.
- WebGL context lost → pause render, cleanup handlers, wait `webglcontextrestored`, restore dari serialized design, tampilkan error bila gagal.
- Low memory → turunkan DPR/quality, unload inactive models, batasi jumlah texture simultaneous.

## Caching
- URL model immutable dengan content hash dan `Cache-Control: public, max-age=31536000, immutable` hanya bila benar-benar hashed.
- Manifest version dapat berumur pendek dan direvalidasi saat rilis; pastikan CDN invalidation.
- Texture/model reuse dihitung reference count; jangan dispose shared GPU resource yang masih dipakai.
- Prioritaskan satu model utama, quality low sebagai tahap awal; high bisa dimuat saat idle/jaringan bagus.

## Transparansi UI
Fallback harus mengatakan mode preview tidak aktif, menyediakan ulangi dan lihat foto. Checkout hanya boleh menerima konfigurasi yang divalidasi, bukan model visual yang gagal di-render tanpa konfirmasi.

## Sumber
https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices
