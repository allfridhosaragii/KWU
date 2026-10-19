# DESIGN KONSEP — KWU Digital Atelier

**Versi:** 1.0 · **Tanggal baseline:** 20 Oktober 2026 · **Status:** blueprint UI/UX, belum menjadi implementasi dan belum diuji pada pengguna.

Folder ini adalah _single source of truth_ rancangan visual dan pengalaman pengguna website KWU. Semua dokumen di dalamnya adalah Markdown dan dapat dibaca langsung di GitHub, VS Code, Obsidian, atau diimpor sebagai referensi ke Figma.

## Tujuan proyek

Website e-commerce **mobile-first** untuk personalisasi produk dengan preview **3D interaktif**. Dua role: **Pembeli** dan **Owner**. Delapan pengalaman customizer:

1. Gelang pada manekin tangan.
2. Cincin yang dapat berpindah ke lima jari.
3. Kalung pada manekin leher.
4. Gantungan tas pada model tas.
5. Stiker untuk HP dengan casing polos atau transparan.
6. Stiker untuk tablet Apple.
7. Stiker untuk MacBook.
8. Stiker untuk botol stainless hitam atau abu-abu.

**Model bisnis yang dipakai dalam UI:** perangkat HP/tablet/MacBook dan botol berperan sebagai media pratinjau stiker, bukan otomatis sebagai barang dagangan. Harga checkout harus mengacu pada barang yang memang dijual. Owner dapat menjual casing atau botol sebagai SKU tersendiri hanya jika katalog dan stok mendukungnya.

## Keputusan final

- **Konsep visual:** Warm Modern Atelier / Quiet Luxury, hangat dan editorial, bukan dashboard SaaS generik.
- **Tema utama:** Warm Light, dengan detail token di [`01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md`](01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md).
- **Font:** Cormorant Garamond untuk display editorial, Manrope untuk antarmuka.
- **Mobile baseline:** frame Figma 390 × 844 CSS px, kemudian pengujian 320, 360, 375, 390, 430, 768, 1024, 1440.
- **Navigasi pembeli:** Beranda, Belanja, Studio, Keranjang, Akun.
- **Navigasi owner:** Ringkasan, Pesanan, Produk, Lainnya.
- **34 template halaman:** 11 toko/publik, 4 autentikasi, 7 akun pembeli, 12 owner.
- **8 kategori customizer:** memakai satu template layout, setiap kategori memiliki visual dan kontrol khusus.
- **Alur custom:** preset + penempatan bebas yang dibatasi kondisi produksi nyata.

## Peta dokumen

| Direktori | Isi | Mulai dari |
|---|---|---|
| `00_FONDASI/` | tujuan, brand, mood, referensi, aturan copy | `01_VISI_DAN_PRINSIP.md` |
| `01_DESIGN_SYSTEM/` | warna, font, grid, icon, komponen, motion, aksesibilitas, status, responsif | `01_WARNA_DAN_TOKEN.md` |
| `02_HALAMAN/` | spesifikasi **34 template** satu file per halaman | `00_INDEKS_34_HALAMAN.md` |
| `03_STUDIO_3D/` | aturan universal dan **8 kategori 3D**, gesture, fallback, save | `00_PRINSIP_STUDIO.md` |
| `04_ALUR_PENGGUNA/` | journeys, flow pembeli, owner, IA/route | `01_USER_JOURNEYS.md` |
| `05_VALIDASI_DAN_HANDOFF/` | QA, komponen Figma, urutan implementasi, keputusan | `01_CHECKLIST_QA_UI_UX.md` |

## Cara memakai paket

1. Baca fondasi brand, lalu token warna dan tipografi.
2. Buat Figma Variables dan komponen dari bagian design system.
3. Desain lima alur kritis dulu: Beranda → Katalog → Detail → Studio → Keranjang → Checkout; login; detail pesanan; owner pesanan.
4. Pakai spesifikasi per halaman sebagai checklist layer, teks, states, dan interaksi.
5. Gunakan dokumen 3D sebelum membuat prototipe gesture, agar kontrol tidak saling bertabrakan.
6. Validasi dengan checklist UI/UX; jangan menyebutnya selesai sebelum pengujian nyata.

## Prinsip konsistensi

- Jangan menambah route utama tanpa memperbarui `02_HALAMAN/00_INDEKS_34_HALAMAN.md` dan sitemap.
- Jangan menggunakan warna literal sembarangan; rujuk token semantik.
- Jangan menjadikan model 3D aktif sebagai thumbnail setiap kartu katalog.
- Jangan menyembunyikan total harga, biaya pengiriman, atau status pembayaran.
- Jangan memaksa pengguna drag untuk fungsi penting tanpa alternatif ketuk/tombol.
- Konsep _quiet luxury_ berasal dari ketepatan tipografi, fotografi, material, dan ruang kosong, **bukan** efek dekoratif berat.

## Batas dokumen

Paket ini adalah rancangan **UI/UX**, bukan PRD backend, skema database, model Blender, atau proyek Figma jadi. Spesifikasi teknis disebut hanya sepanjang memengaruhi pengalaman pengguna dan handoff developer. Contoh nama, gambar, harga, metrik, dan copy bersifat ilustratif sampai brand, SKU, dan aturan bisnis disetujui.
