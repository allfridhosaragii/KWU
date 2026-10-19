# 05. Customizer 3D

**Route:** `/studio/[type]/[productId]`  
**Kelompok:** Toko & Publik  
**Pola visual:** Immersive Product Studio  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memberikan kendali 3D yang nyaman pada HP, memungkinkan preset dan custom bebas, dan menghubungkan hasil ke pembelian.

## 2. Komposisi 1 layar pertama (_above the fold_)

Header ringkas Back, judul produk, Undo/Save. Canvas mendominasi ruang yang tersisa; bottom sheet collapsed untuk pilihan. Total harga dan CTA tetap ditemukan tanpa menutup objek.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | 3D scene | Model/manekin, kamera, rotasi, zoom, hotspot/anchor, material terkalibrasi. |
| 2 | Mode dan preset | Toggle Preset/Custom; preset menyiapkan susunan valid, custom memperbolehkan modifikasi dalam aturan produk. |
| 3 | Library komponen | Charm, warna, bahan, ukuran, desain stiker sesuai kategori yang aktif. |
| 4 | Manipulasi objek | Pilih objek → tampil transform controls → geser/rotasi/scale; disable orbit saat drag objek. |
| 5 | Ringkasan desain | Komponen terpilih, harga dasar, biaya tambahan, total, status tersimpan. |
| 6 | Action bar | Simpan desain, reset view, undo/redo, tambahkan ke keranjang. |
| 7 | Fallback mobile | Jika WebGL gagal, tampil foto/fallback dan penjelasan fungsi yang tidak tersedia. |

## 4. Arah visual spesifik

Studio scene berwarna netral hangat. Kontrol UI terracotta seperlunya; menghindari highlight neon. Perubahan kualitas scene tidak boleh mengubah susunan ornamen.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Satu jari pada area kosong = orbit; satu jari pada objek terpilih = drag objek; dua jari = zoom.
2. Alternatif tombol untuk perpindahan/rotasi/skala harus tersedia.
3. Save menyimpan data desain dan menghasilkan thumbnail; drawer dapat diperbesar/diperkecil.
4. Keluar dengan perubahan belum tersimpan memunculkan dialog pilihan simpan/buang/batal.
5. Zoom/reset kamera tidak mengubah desain produk.

## 6. Loading, empty, error, dan edge cases

- Model loading: thumbnail + progress + cancel/retry.
- WebGL error: preview 2D + instruksi mencoba lagi.
- Perubahan invalid: jelaskan area valid, tetap bisa undo.
- Simpan gagal: desain tetap lokal selama sesi, tampil retry tanpa sukses palsu.

## 7. Copy contoh

Prompt singkat: “Putar untuk melihat detail.” “Ketuk ornamen untuk mengatur posisi.” CTA: “Tambah ke Keranjang”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop canvas kiri sekitar 65%, panel permanen kanan; keyboard shortcuts bisa ditambahkan hanya jika didokumentasikan.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menyelesaikan custom hanya sebagai screenshot; simpan struktur desain. Jangan paksa mode High di perangkat lemah.

## 9. Kriteria penerimaan UI/UX

- [ ] 3D berfungsi pada HP target tanpa jank parah.
- [ ] Touch gesture tidak memutar kamera ketika ornamen di-drag.
- [ ] Harga dan thumbnail konsisten setelah save/cart.
- [ ] Akses alternatif tanpa drag tersedia.
- [ ] 8 varian sesuai dokumen 03_STUDIO_3D.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
