# 32. Pelanggan Owner

**Route:** `/owner/customers`  
**Kelompok:** Owner  
**Pola visual:** Customer Directory  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Membantu owner mencari pelanggan dan melihat riwayat pembelian seperlunya.

## 2. Komposisi 1 layar pertama (_above the fold_)

Search nama/email terkontrol, daftar pelanggan dengan inisial, jumlah transaksi, tanggal terakhir.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Search | Nama/email/nomor yang diizinkan; privacy-aware. |
| 2 | Customer list | Nama, kontak seperlunya, jumlah order, update terakhir. |
| 3 | Detail ringkas | Riwayat order terkait dan status utama tanpa data pribadi berlebih. |
| 4 | Filter | Aktif/transaksi terakhir bila relevan. |
| 5 | Tindakan | Buka pesanan, bantuan pelanggan; ekspor hanya dengan kebijakan keamanan. |

## 4. Arah visual spesifik

Daftar minimal, avatar inisial, divider, warna netral.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Search dengan debounce.
2. Tap membuka detail yang diizinkan.
3. Tidak ada penghapusan data tanpa mekanisme yang terdefinisi.

## 6. Loading, empty, error, dan edge cases

- Data kosong: empty info.
- Lookup error: retry.
- Akses tidak diizinkan: tampilan aman.

## 7. Copy contoh

“Temukan pelanggan dan pesanan.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop tabel kompak dengan kolom minimal.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan memperlakukan data pelanggan sebagai dekorasi dashboard.

## 9. Kriteria penerimaan UI/UX

- [ ] Hanya data relevan terlihat.
- [ ] Teks tidak mengungkap informasi pelanggan yang tidak dibutuhkan.
- [ ] List terbaca 320 px.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
