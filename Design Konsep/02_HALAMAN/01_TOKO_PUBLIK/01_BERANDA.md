# 01. Beranda

**Route:** `/`  
**Kelompok:** Toko & Publik  
**Pola visual:** Editorial Luxury  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menjelaskan proposisi personalisasi 3D dan mengarahkan pengunjung ke produk atau Studio dalam beberapa detik.

## 2. Komposisi 1 layar pertama (_above the fold_)

Header ringkas di atas hero fotografi warm ivory. Headline serif “Hal kecil, terasa lebih personal.” Dua tindakan jelas: Jelajahi Koleksi dan Mulai Custom; produk tetap menjadi pusat perhatian.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Hero dan CTA | Satu visual kampanye dengan produk nyata; headline 2–3 baris; CTA utama ke /studio dan alternatif ke /shop. |
| 2 | Dua kategori inti | Dua kartu besar Accessories dan Stickers dengan foto berbeda, deskripsi pendek, dan jumlah pilihan jika valid. |
| 3 | Koleksi pilihan | Carousel manual maksimal beberapa item, bukan autoplay. Harga dan nama selalu terlihat. |
| 4 | Cara kerja tiga tahap | Pilih produk → atur 3D → simpan/pesan. Pakai tiga ilustrasi ringan/thumbnail, tidak menjalankan canvas. |
| 5 | Cerita brand & kepercayaan | Tunjukkan bahan, proses personalisasi, transparansi preview versus barang asli, dan tautan kebijakan. |
| 6 | Footer | Navigasi toko, bantuan, kontak, kebijakan, identitas brand tanpa promo mengganggu. |

## 4. Arah visual spesifik

Sebagian besar background ivory; hero boleh edge-to-edge; heading Cormorant, semua navigasi Manrope. Jangan membuat foto hero membelakangi CTA.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Ketuk kategori membuka katalog terfilter; Back mempertahankan scroll.
2. CTA Mulai Custom membuka /studio; tidak memuat renderer 3D di beranda.
3. Thumbnail produk membuka detail; gambar punya loading terukur.
4. Header search membawa pengguna ke /shop dengan fokus input.

## 6. Loading, empty, error, dan edge cases

- Loading: placeholder hero ukuran tetap.
- Tanpa produk unggulan: tampil dua kategori dan CTA studio, jangan ruang kosong.
- Gambar gagal: fallback foto produk atau warna surface dengan alt.

## 7. Copy contoh

Heading: “Hal kecil, terasa lebih personal.” CTA: “Mulai Custom”. Subcopy: “Lihat desainmu dari setiap sisi sebelum memesan.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop menggunakan hero asimetris 55/45 dengan foto dominan; nav horizontal tipis; grid koleksi 3–4 kolom.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Hindari video autoplay berat, animasi masuk panjang, dan CTA yang hilang di bawah foto.

## 9. Kriteria penerimaan UI/UX

- [ ] Hero dan satu CTA terbaca di 390×844 tanpa scroll horizontal.
- [ ] Kategori accessories dan sticker ditemukan dalam satu alur scroll.
- [ ] LCP diuji dengan foto hero yang dioptimasi.
- [ ] Tidak ada autoplay yang sulit dihentikan.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
