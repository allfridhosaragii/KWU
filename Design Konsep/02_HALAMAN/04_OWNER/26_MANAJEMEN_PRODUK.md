# 26. Manajemen Produk

**Route:** `/owner/products`  
**Kelompok:** Owner  
**Pola visual:** Inventory Catalogue  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memudahkan owner mencari, membuat, mengedit, mengaktifkan, dan mengarsipkan item dagang.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul Produk, tombol Tambah Produk, filter status/kategori, daftar thumbnail + nama + harga + stok.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Filter | Draft/Aktif/Arsip, aksesoris/stiker, status stok. |
| 2 | Produk list | Foto, nama, SKU ringkas, harga dasar, ketersediaan, status published. |
| 3 | Tindakan item | Edit, Duplikat, Arsip, Detail. |
| 4 | Pembuatan | CTA Tambah Produk menuju editor bertahap. |
| 5 | Info ringkas | Jumlah produk aktif/draft tanpa grafik tak perlu. |

## 4. Arah visual spesifik

Pada mobile kartu daftar satu kolom, bukan tabel 8 kolom.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Tambah menuju editor mode create.
2. Edit membuka SKU sesuai id.
3. Arsip mengonfirmasi dampak katalog sebelum menyimpan.
4. Filter/pencarian dipertahankan ketika kembali.

## 6. Loading, empty, error, dan edge cases

- Belum ada produk: onboarding Tambah Produk.
- Foto hilang: placeholder.
- Stok tidak sinkron: status warning dengan perbaikan.

## 7. Copy contoh

“Kelola koleksi tokomu.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop tabel produk dengan kolom yang dapat diatur.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan langsung delete SKU yang punya order historis; gunakan arsip.

## 9. Kriteria penerimaan UI/UX

- [ ] Status draft/aktif dapat dibedakan.
- [ ] Tindakan mudah dilakukan lewat HP.
- [ ] Produk preview tidak bercampur dengan produk yang dijual tanpa label.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
