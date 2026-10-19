# 20. Detail Pesanan Pembeli

**Route:** `/account/orders/[id]`  
**Kelompok:** Akun Pembeli  
**Pola visual:** Order Timeline  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menjelaskan status pembelian, visual desain final, pembayaran, dan pengiriman.

## 2. Komposisi 1 layar pertama (_above the fold_)

Header nomor order, status terkini, timeline produksi/pengiriman, lalu item dan rincian pembayaran.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Timeline | Dibayar → Diproses → Dikemas → Dikirim → Selesai, dengan tanggal aktual jika diketahui. |
| 2 | Item final | Thumbnail custom, ringkasan ornamen/stiker, ukuran, warna, qty dan harga. |
| 3 | Lihat desain | Buka preview final 3D secara lazy, tidak otomatis di halaman ini. |
| 4 | Payment info | Status uang, nominal, metode, referensi bila valid. |
| 5 | Shipping info | Alamat, kurir, nomor resi jika ada. |
| 6 | Bantuan | Link hubungi toko yang menyertakan nomor order dengan aman. |

## 4. Arah visual spesifik

Timeline tipis, card ringan, heading Manrope; 3D preview tombol sekunder.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Resi dapat disalin.
2. Lihat desain membuka modal/halaman fokus lalu kembali.
3. Bantuan membawa konteks pesanan.

## 6. Loading, empty, error, dan edge cases

- Status belum berubah: jelaskan terakhir diperbarui.
- Preview gagal: thumbnail statis + rincian desain.
- Order tak berizin: tampil akses ditolak, tidak mengungkap data.

## 7. Copy contoh

“Pesanan sedang dibuat.” “Lihat desain final”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop timeline kiri, order summary kanan.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mengubah snapshot order lama ketika produk katalog berubah.

## 9. Kriteria penerimaan UI/UX

- [ ] Pembeli membedakan uang sudah diterima vs barang sedang dibuat.
- [ ] Thumbnail akurat untuk pesanan versi itu.
- [ ] Timeline jelas di mobile.
- [ ] Bukti info pembayaran tidak mengandung rahasia gateway.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
