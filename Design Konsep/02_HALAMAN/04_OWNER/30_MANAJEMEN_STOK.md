# 30. Manajemen Stok

**Route:** `/owner/inventory`  
**Kelompok:** Owner  
**Pola visual:** Operational Utility  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Mengetahui ketersediaan komponen dan produk agar pesanan yang diterima dapat diproduksi.

## 2. Komposisi 1 layar pertama (_above the fold_)

Kartu Stok Menipis/Stok Habis, search item, daftar material dengan angka kuantitas besar.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Overview | Jumlah item kritis, stok habis, item normal. |
| 2 | Daftar stok | Nama/SKU komponen, unit, angka tersedia, batas minimum. |
| 3 | Perubahan stok | Tambah, koreksi, alasan, dan catatan. |
| 4 | Riwayat perubahan | Audit waktu, nominal, jenis perubahan. |
| 5 | Filter | Kategori/level stok. |

## 4. Arah visual spesifik

Satu kolom dengan angka legible dan warna hanya untuk status kritis.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Tambah stok memvalidasi angka positif.
2. Koreksi stok memerlukan alasan.
3. Klik item membuka detail riwayat.

## 6. Loading, empty, error, dan edge cases

- Tidak ada stok: onboarding import/manual.
- Stok minus: peringatan dan blok transaksi yang relevan.
- Koreksi gagal: tampil state lama.

## 7. Copy contoh

“3 komponen perlu restock.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop tabel sort berdasarkan sisa stok.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan membiarkan koreksi stok tanpa riwayat.

## 9. Kriteria penerimaan UI/UX

- [ ] Unit ukuran jelas (pcs/meter/set).
- [ ] Status kritis tidak hanya warna.
- [ ] Setiap perubahan dapat ditelusuri.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
