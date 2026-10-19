# 31. Pembayaran Owner

**Route:** `/owner/payments`  
**Kelompok:** Owner  
**Pola visual:** Financial Operations  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memantau transaksi dan mengidentifikasi pembayaran yang membutuhkan pemeriksaan.

## 2. Komposisi 1 layar pertama (_above the fold_)

Ringkasan sukses, pending, gagal; filter status dan tanggal; daftar transaksi.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Status summary | Nominal berhasil, pending, gagal dengan rentang periode jelas. |
| 2 | Transaction list | ID, nomor order, waktu, nominal, metode, status terverifikasi. |
| 3 | Detail | Referensi provider, kronologi peristiwa, tautan ke order. |
| 4 | Refund/aksi | Hanya jika alur bisnis dan gateway benar-benar mendukung. |
| 5 | Pengecualian | Transaksi duplikat/kondisi tak biasa ditandai. |

## 4. Arah visual spesifik

Finance UI tenang: angka Manrope tabular, warna status dengan ikon, tanpa dekorasi 3D.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Filter date/status dan copy ID transaksi.
2. Tap transaksi menuju detail/order.
3. Refresh status sesuai otorisasi tanpa memanipulasi hasil.

## 6. Loading, empty, error, dan edge cases

- Gateway tidak respons: state unknown, bukan gagal palsu.
- Tidak ada transaksi: empty.
- Refund tak didukung: tidak tampil tombolnya.

## 7. Copy contoh

“Pembayaran menunggu konfirmasi.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop tabel transaksi dan panel detail.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan membuat tombol “Tandai Berhasil” untuk otomatis payment tanpa kebijakan verifikasi sah.

## 9. Kriteria penerimaan UI/UX

- [ ] Nominal dan status jelas.
- [ ] Pending tidak sama dengan uang diterima.
- [ ] Data sensitif pembayaran tidak diekspos.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
