# 14. Lupa Password

**Route:** `/forgot-password`  
**Kelompok:** Autentikasi  
**Pola visual:** Focused Form  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memungkinkan pengguna meminta langkah pemulihan dengan aman.

## 2. Komposisi 1 layar pertama (_above the fold_)

Icon amplop outline, heading “Atur ulang password”, satu input email dan CTA Kirim Tautan.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Petunjuk singkat | Masukkan email akun; jelaskan alur pengiriman dan langkah berikut. |
| 2 | Email form | Input berlabel dengan auto-complete email. |
| 3 | Submission feedback | Halaman/komponen konfirmasi permintaan yang tidak membocorkan eksistensi akun. |
| 4 | Bantuan | Tautan kembali Login dan Pusat Bantuan. |

## 4. Arah visual spesifik

Minimal, tanpa foto, ikon satu warna dengan banyak whitespace.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Submit menampilkan state proses dan konfirmasi.
2. Kembali ke Login tersedia.
3. Resend dibatasi dengan countdown bila backend mendukung.

## 6. Loading, empty, error, dan edge cases

- Email invalid: error inline.
- Request selesai: pesan netral.
- Error jaringan: retry tanpa kosongkan email.

## 7. Copy contoh

“Jika email terdaftar, kami akan mengirim petunjuk pemulihan.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop menggunakan card tunggal max-width 440 px.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan memunculkan pesan “Email tidak terdaftar” bila kebijakan keamanan menghindarinya.

## 9. Kriteria penerimaan UI/UX

- [ ] Tautan login selalu ditemukan.
- [ ] Pesan tetap aman terhadap email tidak dikenal.
- [ ] Tidak meminta password lama.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
