# 19. Riwayat Pesanan

**Route:** `/account/orders`  
**Kelompok:** Akun Pembeli  
**Pola visual:** Order History  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memudahkan pembeli melihat semua pembelian dan membuka status terbaru.

## 2. Komposisi 1 layar pertama (_above the fold_)

Heading “Pesanan”, segmented tabs Semua / Diproses / Dikirim / Selesai, daftar kartu kronologis.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Filter status | Tab dengan jumlah jika tersedia, tetap mempertahankan filter saat kembali. |
| 2 | Order card | Nomor, tanggal, thumbnail, ringkasan item, total, status. |
| 3 | Detail access | Seluruh kartu menuju /account/orders/[id]. |
| 4 | Pencarian | Cari berdasarkan nomor pesanan jika daftar panjang. |
| 5 | Bantuan | Pusat Bantuan bagi pesanan bermasalah. |

## 4. Arah visual spesifik

Kartu netral satu kolom; gunakan status teks dan ikon kecil; warna status seperlunya.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Tab mengganti daftar tanpa kehilangan informasi.
2. Tap kartu buka detail.
3. Swipe tidak menjadi satu-satunya navigasi.

## 6. Loading, empty, error, dan edge cases

- Tidak ada pesanan: CTA Jelajahi Koleksi.
- Tidak ada dalam filter: Reset Filter.
- API error: retry.

## 7. Copy contoh

Empty: “Belum ada pesanan untuk kategori ini.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop tabel sederhana atau list lebar dengan kolom nomor/tanggal/status.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mencampur status pembayaran dan pengiriman menjadi satu status ambigu.

## 9. Kriteria penerimaan UI/UX

- [ ] Status pesanan dapat dipindai cepat.
- [ ] Nomor order disalin/dilihat.
- [ ] Kartu tidak dipenuhi metadata teknis.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
