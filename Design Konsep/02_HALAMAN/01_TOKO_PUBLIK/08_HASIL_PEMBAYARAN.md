# 08. Hasil Pembayaran

**Route:** `/checkout/result`  
**Kelompok:** Toko & Publik  
**Pola visual:** Transaction Status  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memberi kepastian status transaksi dan mengarahkan pembeli ke pesanan.

## 2. Komposisi 1 layar pertama (_above the fold_)

Satu ikon status besar, heading faktual, deskripsi pendek, nomor pesanan dan total. CTA Lihat Pesanan paling jelas.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Identitas status | Berhasil / Menunggu / Gagal menggunakan ikon, teks, dan warna pendukung. |
| 2 | Ringkasan | Nomor pesanan, nominal, metode pembayaran, waktu terkini yang valid. |
| 3 | Langkah berikutnya | Jika pending tampil instruksi penyelesaian; jika gagal beri retry sesuai aturan. |
| 4 | Akses bantuan | Link bantuan ketika status tidak berubah sesuai harapan. |

## 4. Arah visual spesifik

Komposisi terpusat, ikon minimal, sukses menggunakan forest. Tidak ada confetti besar.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Refresh tidak menghasilkan transaksi baru.
2. Lihat Pesanan mengarah ke detail terkait.
3. Saat status pending, ada cara cek ulang yang tidak spam.

## 6. Loading, empty, error, dan edge cases

- Pending: “Menunggu konfirmasi pembayaran”.
- Gagal: “Pembayaran belum berhasil”.
- Berhasil: “Pembayaran diterima”.

## 7. Copy contoh

Berhasil: “Pembayaran diterima. Pesananmu siap diproses.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop card terpusat dengan max width 480–560 px.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mengatakan sukses hanya dari animasi gateway.

## 9. Kriteria penerimaan UI/UX

- [ ] Status berasal dari server yang diverifikasi.
- [ ] Label bukan hanya warna.
- [ ] Nomor pesanan dapat disalin.
- [ ] CTA berikutnya jelas.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
