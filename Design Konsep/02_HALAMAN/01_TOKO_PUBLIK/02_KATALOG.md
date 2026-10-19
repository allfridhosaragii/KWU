# 02. Katalog Produk

**Route:** `/shop`  
**Kelompok:** Toko & Publik  
**Pola visual:** Product Gallery  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memungkinkan pengguna menemukan barang dan membandingkan opsi custom dalam waktu singkat.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul “The Collection”, search field mudah disentuh, kategori horizontal dan bar Filter/Urutkan dengan jumlah hasil. Di bawahnya grid dua kolom dengan foto besar.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Search & kategori | Cari gelang/cincin/stiker dengan hasil yang dapat diurutkan; kategori yang aktif tampil jelas. |
| 2 | Filter mobile | Bottom sheet kategori, rentang harga, bahan, warna, kompatibilitas; tombol “Lihat X hasil” melakukan apply. |
| 3 | Grid produk | Foto statis rasio konsisten, nama, harga mulai, varian; pilih kartu membuka /products/[slug]. |
| 4 | Filter aktif | Chip removable yang memperlihatkan semua pilihan; tombol Reset semua. |
| 5 | Rekomendasi saat kosong | Tampilkan alternatif kategori atau hapus filter, bukan banner tidak relevan. |

## 4. Arah visual spesifik

Grid berjarak 12 px; foto polos beige; tanpa highlight multiwarna. Harga Manrope 600 dan metadata sekunder taupe.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Multiple filter jenis yang sama boleh dipilih; UI menampilkan hitung hasil sebelum apply.
2. Kembali dari detail memulihkan filter, sort, dan posisi daftar.
3. Pencarian punya clear button dan label.
4. Swatch preview boleh berubah tanpa otomatis memasukkan ke cart.

## 6. Loading, empty, error, dan edge cases

- Loading: skeleton grid 4 item pertama.
- Zero results: penjelasan filter dan tombol Hapus Filter.
- Error API: tampil retry tanpa menghapus pilihan filter.

## 7. Copy contoh

Empty: “Belum ada produk yang cocok.” CTA: “Hapus filter”. Label kategori: “Semua / Aksesoris / Stiker”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop grid 4 kolom; filter sidebar boleh persist jika tidak mempersempit konten.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menggunakan endless horizontal categories tanpa petunjuk; jangan menjalankan 3D tiap kartu.

## 9. Kriteria penerimaan UI/UX

- [ ] Chip filter aktif terlihat setelah apply.
- [ ] Harga selalu terlihat tanpa hover.
- [ ] Kartu tetap terbaca pada 320/360 px.
- [ ] Pencarian dan filter tidak memuat WebGL.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
