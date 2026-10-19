# 03. Detail Produk

**Route:** `/products/[slug]`  
**Kelompok:** Toko & Publik  
**Pola visual:** Product Showcase  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Membantu pembeli mengevaluasi bahan, varian, ukuran, stok, harga, dan keputusan membuka Studio 3D.

## 2. Komposisi 1 layar pertama (_above the fold_)

Gallery visual besar di atas, indikator gambar, lalu judul produk, harga, varian utama dan satu CTA “Custom di 3D”.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Galeri produk | Urutan foto utama, samping, detail, penggunaan, referensi hasil custom; pinch zoom untuk gambar jika tersedia. |
| 2 | Informasi pilihan | Judul, kode singkat, harga awal/rentang, bahan, warna, ukuran, ketersediaan. |
| 3 | Aksi pembelian | CTA Custom di 3D utama; alternatif Tambah ke Keranjang untuk produk noncustom yang diizinkan. |
| 4 | Penjelasan produk fisik | Tuliskan jelas apakah yang dibeli stiker/casing/produk aksesori; media HP/tablet/MacBook tidak otomatis termasuk. |
| 5 | Detail lanjutan | Accordion bahan, perawatan, estimasi produksi/pengiriman jika sudah valid, kebijakan dan bantuan. |
| 6 | Rekomendasi terkait | 3–6 produk yang sejenis, tanpa memecah fokus pembelian. |

## 4. Arah visual spesifik

Foto produk tajam berlatar ivory; teks harga Manrope; hero nama editorial kecil bila cocok. Sticky CTA tidak menutup variannya.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Klik varian memperbarui harga dan foto bila relevan.
2. Tombol Studio mengirim productId/variant yang kompatibel.
3. Wishlist membutuhkan state login/guest yang jelas.
4. Zoom gallery tidak bentrok dengan scroll halaman.

## 6. Loading, empty, error, dan edge cases

- Varian tidak tersedia: tombol nonaktif dengan alasan.
- Gallery belum dimuat: image fallback pada rasio tetap.
- Produk tak ditemukan: not-found friendly ke katalog.

## 7. Copy contoh

CTA: “Custom di 3D”. Hint: “Preview membantu melihat hasil desain; warna fisik dapat dipengaruhi layar.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop galeri kiri ~60%, panel beli sticky kanan; accordion di panel kanan.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menyembunyikan ongkos atau informasi penting di footer; jangan menampilkan benda preview seolah barang dijual.

## 9. Kriteria penerimaan UI/UX

- [ ] Harga, varian, CTA terlihat sebelum konten editorial panjang.
- [ ] Informasi apa yang dibeli bisa ditemukan cepat.
- [ ] CTA tetap bisa diakses dengan satu tangan.
- [ ] Switch varian tidak melompatkan layout.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
