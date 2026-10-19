# Prioritas Tahapan Desain dan Kriteria Kelulusan

## Prinsip sequencing

Jangan merancang 34 halaman dengan detail sama sejak hari pertama. Fokuskan alur yang membuktikan value proposition KWU, kemudian turunkan pattern ke layar lain. Semua 34 tetap punya blueprint di paket ini.

## Fase 0 — Fondasi

- Kunci desain token dan keputusan font.
- Buat komponen button, input, card, navigation, sheet, status, error.
- Uji kontras serta ukuran 320/390 px.
- Deliverable: Figma foundation + komponen dasar.

## Fase 1 — Alur pelanggan utama

Halaman prioritas: **01 Beranda, 02 Katalog, 03 Detail, 04 Pilih Studio, 05 Customizer, 06 Keranjang, 07 Checkout, 08 Hasil Pembayaran, 12 Login, 13 Register**.

- Buat High Fidelity mobile untuk 10 template tersebut.
- Validasi alur stiker HP dan gelang lebih dulu.
- QA aksi, harga, fallback, dan kesadaran apa yang sebenarnya dibeli.

## Fase 2 — Operasional owner

Halaman prioritas: **23 Dashboard, 24 Daftar Pesanan, 25 Detail Pesanan, 26 Manajemen Produk, 27 Editor Produk, 31 Pembayaran**.

- Uji bahwa owner dapat memahami order custom dari layar HP.
- Simpan preview final dan production sheet.
- Desain mode belum bayar dan pembayarannya pending.

## Fase 3 — Delapan Studio lengkap

- Ring, Necklace, Bag Charm, Tablet, MacBook, Bottle.
- Perluas pattern layer/gesture berdasarkan category-specific constraints.
- Uji rotasi, anchor, UV, seam, pose, dan fallback.

## Fase 4 — Halaman pendukung

Lengkapi 09–11, 14–22, 28–30, 32–34. Pertahankan komponen design system agar UI tidak terfragmentasi.

## Fase 5 — Handoff & QA

- Uji Figma prototype pada HP.
- Implementasikan token dan UI components.
- Jalankan QA aksesibilitas, pembayaran sandbox, rendering, dan flow role.
- Revisi berdasarkan masalah pengguna nyata, bukan semata selera visual.

## DoD desain per halaman

- Tujuan pengguna eksplisit.
- Frame default dan state penting tersedia.
- Interaksi tombol/gesture terdefinisi.
- Semua informasi pembelian/owner yang kritis tidak tersembunyi.
- Responsif minimal 320, 390, 768 dan desktop.
- Kontras dan target sentuh diverifikasi.
- Tidak membutuhkan klaim data/aset yang belum ada.
