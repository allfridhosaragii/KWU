# 28. Library Komponen

**Route:** `/owner/components`  
**Kelompok:** Owner  
**Pola visual:** Asset Gallery  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Mengelola charm, liontin, elemen gantungan, dan artwork stiker agar dapat dipilih customer.

## 2. Komposisi 1 layar pertama (_above the fold_)

Header Library Komponen, segment Charm/Ornamen/Stiker, search dan CTA Tambah Komponen.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Grid library | Thumbnail, nama, jenis, harga tambahan, status aktif, stok bila fisik. |
| 2 | Upload/edit | Artwork gambar/stiker, GLB charm, metadata ukuran dan kompatibilitas. |
| 3 | Kompatibilitas | Produk mana yang boleh menggunakan komponen. |
| 4 | Pratinjau | Thumbnail dengan background yang benar, untuk stiker ada area transparansi yang ditandai. |
| 5 | Validasi kualitas | Tunjukkan file terlalu besar, resolusi tidak cukup untuk cetak, atau model tidak valid. |

## 4. Arah visual spesifik

Grid pada mobile dua kolom jika label terbaca; detail item di sheet atau halaman editor reuse.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Filter jenis, status dan penggunaan.
2. Upload dengan progress nyata.
3. Edit harga menandai efek untuk pesanan baru saja.

## 6. Loading, empty, error, dan edge cases

- Belum ada komponen: CTA Tambah.
- Upload gagal: retry.
- Aset bermasalah: warning spesifik.

## 7. Copy contoh

“Setiap detail punya tempatnya.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop grid besar + panel detail.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mengunggah file stiker resolusi cetak rendah tanpa peringatan.

## 9. Kriteria penerimaan UI/UX

- [ ] Artwork transparan mudah dibedakan dari latar.
- [ ] Harga komponen terlihat.
- [ ] Kompatibilitas jelas.
- [ ] Aset tidak bisa dihapus diam-diam jika digunakan pesanan.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
