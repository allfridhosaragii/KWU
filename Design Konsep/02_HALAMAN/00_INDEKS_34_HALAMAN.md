# Indeks Detail 34 Halaman

**Kontrak jumlah:** 11 Store/Public + 4 Auth + 7 Buyer + 12 Owner = **34 template**. Halaman no. 05 memakai **8 variasi studio**, jadi 8 pengalaman 3D tidak dihitung 8 halaman berbeda.

| No | Template & spesifikasi | Route | Role/Group | Arah visual |
| --- | --- | --- | --- | --- |
| 01 | [Beranda](01_TOKO_PUBLIK/01_BERANDA.md) | `/` | Toko & Publik | Editorial Luxury |
| 02 | [Katalog Produk](01_TOKO_PUBLIK/02_KATALOG.md) | `/shop` | Toko & Publik | Product Gallery |
| 03 | [Detail Produk](01_TOKO_PUBLIK/03_DETAIL_PRODUK.md) | `/products/[slug]` | Toko & Publik | Product Showcase |
| 04 | [Pilih Studio 3D](01_TOKO_PUBLIK/04_PILIH_STUDIO.md) | `/studio` | Toko & Publik | Experience Gateway |
| 05 | [Customizer 3D](01_TOKO_PUBLIK/05_CUSTOMIZER_3D.md) | `/studio/[type]/[productId]` | Toko & Publik | Immersive Product Studio |
| 06 | [Keranjang](01_TOKO_PUBLIK/06_KERANJANG.md) | `/cart` | Toko & Publik | Commerce Utility |
| 07 | [Checkout](01_TOKO_PUBLIK/07_CHECKOUT.md) | `/checkout` | Toko & Publik | Focused Transaction |
| 08 | [Hasil Pembayaran](01_TOKO_PUBLIK/08_HASIL_PEMBAYARAN.md) | `/checkout/result` | Toko & Publik | Transaction Status |
| 09 | [Pusat Bantuan](01_TOKO_PUBLIK/09_PUSAT_BANTUAN.md) | `/help` | Toko & Publik | Calm Support |
| 10 | [Tentang Brand](01_TOKO_PUBLIK/10_TENTANG_BRAND.md) | `/about` | Toko & Publik | Brand Storytelling |
| 11 | [Kebijakan dan Ketentuan](01_TOKO_PUBLIK/11_KEBIJAKAN.md) | `/legal/[slug]` | Toko & Publik | Editorial Document |
| 12 | [Login](02_AUTENTIKASI/12_LOGIN.md) | `/login` | Autentikasi | Focused Form |
| 13 | [Daftar Akun](02_AUTENTIKASI/13_REGISTER.md) | `/register` | Autentikasi | Focused Form |
| 14 | [Lupa Password](02_AUTENTIKASI/14_LUPA_PASSWORD.md) | `/forgot-password` | Autentikasi | Focused Form |
| 15 | [Reset Password](02_AUTENTIKASI/15_RESET_PASSWORD.md) | `/reset-password` | Autentikasi | Focused Form |
| 16 | [Akun Saya](03_AKUN_PEMBELI/16_AKUN_SAYA.md) | `/account` | Akun Pembeli | Personal Utility |
| 17 | [Desain Tersimpan](03_AKUN_PEMBELI/17_DESAIN_TERSIMPAN.md) | `/account/designs` | Akun Pembeli | Product Library |
| 18 | [Wishlist](03_AKUN_PEMBELI/18_WISHLIST.md) | `/account/wishlist` | Akun Pembeli | Product Gallery |
| 19 | [Riwayat Pesanan](03_AKUN_PEMBELI/19_RIWAYAT_PESANAN.md) | `/account/orders` | Akun Pembeli | Order History |
| 20 | [Detail Pesanan Pembeli](03_AKUN_PEMBELI/20_DETAIL_PESANAN.md) | `/account/orders/[id]` | Akun Pembeli | Order Timeline |
| 21 | [Buku Alamat](03_AKUN_PEMBELI/21_BUKU_ALAMAT.md) | `/account/addresses` | Akun Pembeli | Address Utility |
| 22 | [Profil dan Pengaturan](03_AKUN_PEMBELI/22_PROFIL_PENGATURAN.md) | `/account/profile` | Akun Pembeli | Account Settings |
| 23 | [Dashboard Owner](04_OWNER/23_DASHBOARD_OWNER.md) | `/owner` | Owner | Quiet Operations |
| 24 | [Daftar Pesanan Owner](04_OWNER/24_SEMUA_PESANAN_OWNER.md) | `/owner/orders` | Owner | Action Queue |
| 25 | [Detail Pesanan Owner](04_OWNER/25_DETAIL_PESANAN_OWNER.md) | `/owner/orders/[id]` | Owner | Order Operations |
| 26 | [Manajemen Produk](04_OWNER/26_MANAJEMEN_PRODUK.md) | `/owner/products` | Owner | Inventory Catalogue |
| 27 | [Editor Produk](04_OWNER/27_EDITOR_PRODUK.md) | `/owner/products/new dan /owner/products/[id]/edit` | Owner | Guided Editor |
| 28 | [Library Komponen](04_OWNER/28_LIBRARY_KOMPONEN.md) | `/owner/components` | Owner | Asset Gallery |
| 29 | [Manajemen Aset 3D](04_OWNER/29_MANAJEMEN_ASET_3D.md) | `/owner/assets` | Owner | Technical Asset Library |
| 30 | [Manajemen Stok](04_OWNER/30_MANAJEMEN_STOK.md) | `/owner/inventory` | Owner | Operational Utility |
| 31 | [Pembayaran Owner](04_OWNER/31_PEMBAYARAN_OWNER.md) | `/owner/payments` | Owner | Financial Operations |
| 32 | [Pelanggan Owner](04_OWNER/32_PELANGGAN_OWNER.md) | `/owner/customers` | Owner | Customer Directory |
| 33 | [Laporan Penjualan](04_OWNER/33_LAPORAN_OWNER.md) | `/owner/reports` | Owner | Quiet Analytics |
| 34 | [Pengaturan Toko](04_OWNER/34_PENGATURAN_TOKO.md) | `/owner/settings` | Owner | Settings Utility |

## Pengelompokan desain

- **Editorial Luxury:** homepage dan brand story.
- **Product Gallery:** katalog, wishlist, desain tersimpan.
- **Immersive Product Studio:** 3D Studio dengan tab kontekstual.
- **Commerce Utility:** cart, checkout, payment result.
- **Quiet Operations:** owner dashboard, orders, produk, stok, laporan.

## Catatan penghitungan

- `new/edit` editor produk menggunakan satu template.
- `legal/[slug]` satu template untuk beberapa isi kebijakan.
- `studio/[type]/[productId]` satu shell, delapan kombinasi produk/kontrol 3D.
- Filter katalog bukan halaman baru.
- Form input alamat atau pilihan varian tidak wajib membuat route terpisah.

## Rujukan desain

[Palet dan token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) · [Tipografi](../01_DESIGN_SYSTEM/02_TIPOGRAFI.md) · [Responsive](../01_DESIGN_SYSTEM/11_RESPONSIVE_MOBILE_FIRST.md) · [Studio 3D](../03_STUDIO_3D/00_PRINSIP_STUDIO.md) · [Sitemap](../04_ALUR_PENGGUNA/04_SITEMAP_ROUTES_DAN_NAV.md).
