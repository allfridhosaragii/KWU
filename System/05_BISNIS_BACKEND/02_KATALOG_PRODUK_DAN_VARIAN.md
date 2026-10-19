# Katalog, Variasi SKU, Komponen, dan Aturan Produksi

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Pemisahan entitas
- `Category`: bracelet/ring/necklace/bag-charm/sticker; `studioType` bisa kategori preview phone/tablet/macbook/bottle.
- `Product`: barang dagang dengan SKU/base price (aksesori atau stiker), status active/draft/archive.
- `Variant`: ukuran/warna/bahan/casing bila casing memang SKU; `Component`: charm, pendant, chain, sticker art.
- `ModelAsset`: asset viewer yang dapat dipakai beberapa products.
- `ProductComponent`: daftar kompatibilitas, max quantity, required size/material, price delta.
- `AttachmentPoint/PrintableSurface`: constraints berversi milik preview/produk.

## Produk stiker yang sering tertukar
SKU `STICKER-STAR-3CM` adalah stiker, sedangkan HP dan botol bisa saja **hanya media preview**. Harga tidak menambah HP/MacBook. Jika botol nyata akan dijual, buat SKU terpisah atau bundle eksplisit; jangan memanfaatkan field preview untuk menyimpulkan stok botol.

## Owner CRUD
- Create draft, atur SKU, deskripsi, media foto, price, variant, component compatibility, preset/model asset.
- Preview dan validasi semua kombinasi yang bisa dibeli.
- Publish hanya jika punya media utama, harga valid, stock policy, 3D manifest+rules untuk custom products.
- Archive bukan hard delete ketika sudah pernah masuk order; semua item order menyimpan snapshot.

## Ketersediaan
Product availability ditentukan status, varian, komponen/material aktual dan aturan produksi. Jangan izinkan add-to-cart atas component habis tanpa peringatan; tergantung bisnis boleh backorder jika owner menyalakan kebijakan eksplisit.

## Search/filter
Filter category/status/color/material/price dan sort; query `shop` via URL, pagination cursor/offset yang stabil, index DB. Optimalkan gambar kartu dan SEO metadata, tidak load GLB sebagai product list.
