# 33. Laporan Penjualan

**Route:** `/owner/reports`  
**Kelompok:** Owner  
**Pola visual:** Quiet Analytics  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menunjukkan performa penjualan yang dapat ditindaklanjuti tanpa memadatkan grafik.

## 2. Komposisi 1 layar pertama (_above the fold_)

Date range picker, satu total omzet besar, jumlah pesanan, rata-rata order, lalu chart tren yang dapat dibaca.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Filter periode | 7 hari/30 hari/rentang tanggal, label data jelas. |
| 2 | KPI | Omzet, pesanan dibayar, rata-rata nilai pesanan; definisi terlihat. |
| 3 | Tren | Line chart satu seri utama dan tooltip yang bisa diakses. |
| 4 | Komposisi produk | Bar chart kategori terjual; aksesoris/stiker. |
| 5 | Rincian | Daftar transaksi yang berkaitan dan opsi ekspor jika tersedia. |
| 6 | Info data | Terakhir diperbarui dan apakah refund/pending termasuk. |

## 4. Arah visual spesifik

Line terracotta di atas background ivory, gridline sangat tipis; tidak menggunakan 8 warna acak.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Date change memperbarui KPI dan chart konsisten.
2. Tooltip chart punya alternatif tabel.
3. Ekspor menunjukkan status proses.

## 6. Loading, empty, error, dan edge cases

- Tidak ada data: tampil nol dan penjelasan periode yang benar.
- Partial data: warning yang terlihat.
- Query gagal: retry.

## 7. Copy contoh

“Penjualan dalam 30 hari terakhir.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop chart lebar dengan KPI sejajar, tabel di bawah.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mencampur transaksi pending dan omzet sukses dalam angka sama tanpa label.

## 9. Kriteria penerimaan UI/UX

- [ ] Definisi omzet tidak ambigu.
- [ ] Grafik bisa dipahami tanpa warna saja.
- [ ] Tabel tersedia untuk angka rinci.
- [ ] Mobile tidak memaksa chart selebar 1440 px.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
