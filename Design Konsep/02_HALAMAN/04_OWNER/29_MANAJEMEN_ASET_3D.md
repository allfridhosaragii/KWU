# 29. Manajemen Aset 3D

**Route:** `/owner/assets`  
**Kelompok:** Owner  
**Pola visual:** Technical Asset Library  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memberi owner visibilitas atas model manekin, device, casing, tas, dan botol serta kualitas aset.

## 2. Komposisi 1 layar pertama (_above the fold_)

Daftar aset, status Siap/Perlu Optimasi/Error, ukuran file, thumbnail, filter kategori.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Asset grid | Model, kategori, versi, ukuran file, status validasi. |
| 2 | Asset detail | Preview dan ringkasan dimensi, UV, material, attachment points. |
| 3 | Upload | Input file melalui storage; proses optimasi dengan progress. |
| 4 | Aturan anchor | Lihat titik pemasangan; editor presisi diprioritaskan desktop. |
| 5 | Quality checks | Triangle budget, texture budget, nama anchor, konsistensi glTF/GLB. |
| 6 | Versi aset | Versi aktif dan history kompatibilitas dengan desain yang tersimpan. |

## 4. Arah visual spesifik

Operasional teknis tetapi tetap memakai card hangat; preview aktif hanya satu pada satu waktu.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Ketuk model untuk preview on demand.
2. Filter aset siap/bermasalah.
3. Tindakan publikasikan aset hanya ketika valid.

## 6. Loading, empty, error, dan edge cases

- File gagal dimuat: fallback metadata.
- Model belum siap: status jelas.
- Upload gagal: retry tanpa menggandakan assetId.

## 7. Copy contoh

“Periksa kualitas model sebelum dipakai pembeli.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop menyediakan panel 3D lebih besar dan alat penempatan anchor.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan membuat editor rig kompleks wajib di HP; tugas presisi sebaiknya desktop.

## 9. Kriteria penerimaan UI/UX

- [ ] Model yang error tidak bisa dipilih untuk produk baru.
- [ ] Ukuran file mudah dibaca.
- [ ] Preview tidak memuat semua model sekaligus.
- [ ] Versi tetap dapat ditelusuri.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
