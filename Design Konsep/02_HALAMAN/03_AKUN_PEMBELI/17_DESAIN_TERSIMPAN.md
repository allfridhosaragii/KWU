# 17. Desain Tersimpan

**Route:** `/account/designs`  
**Kelompok:** Akun Pembeli  
**Pola visual:** Product Library  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memudahkan pembeli membuka, mengubah, menggandakan, dan menghapus desain custom.

## 2. Komposisi 1 layar pertama (_above the fold_)

Heading “Desain Tersimpan”, jumlah desain, lalu grid thumbnail dua kolom.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Filter kecil | Filter kategori, urut terbaru, pencarian nama desain bila diperlukan. |
| 2 | Design card | Thumbnail final, nama desain, tipe, tanggal revisi, state draft/selesai. |
| 3 | Aksi card | Lanjutkan, Duplikat, Ganti Nama, Hapus dalam menu overflow. |
| 4 | Sinkronisasi | Status menyimpan saat desain baru/belum tersinkron. |
| 5 | Empty state | Ilustrasi sederhana dan CTA Mulai Custom. |

## 4. Arah visual spesifik

Thumbnail gaya galeri produk, background ivory; nama desain penting, metadata ringkas.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Lanjutkan mengembalikan model dan elemen pada versi asset yang kompatibel.
2. Duplikat membuat salinan baru bukan menimpa original.
3. Hapus meminta konfirmasi dan menyediakan undo bila dapat.

## 6. Loading, empty, error, dan edge cases

- Belum ada desain: CTA Studio.
- Thumbnail belum jadi: placeholder dengan label.
- Versi model tidak kompatibel: pesan dan opsi lihat gambar/konversi bila ada.

## 7. Copy contoh

Empty: “Belum ada desain yang disimpan.” CTA: “Buat Desain”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop grid 3–4 kolom.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mengedit metadata tanpa memperbarui preview.

## 9. Kriteria penerimaan UI/UX

- [ ] Thumbnail sejalan dengan konfigurasi tersimpan.
- [ ] Aksi destruktif tidak dilakukan satu ketuk tanpa feedback.
- [ ] Kartu dua kolom terbaca pada 360 px.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
