# 13. Daftar Akun

**Route:** `/register`  
**Kelompok:** Autentikasi  
**Pola visual:** Focused Form  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Membuat akun pembeli baru dengan formulir minimum.

## 2. Komposisi 1 layar pertama (_above the fold_)

Heading “Mulai personalisasi pertamamu.” Nama, email, password, konfirmasi bila dibutuhkan, persetujuan ketentuan, CTA Daftar.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Pengantar | Satu kalimat manfaat akun: menyimpan desain dan memantau pesanan. |
| 2 | Data minimum | Nama, email, password; data alamat diminta di checkout atau profil. |
| 3 | Validasi | Syarat password yang jelas, error inline dan field hint. |
| 4 | Persetujuan | Tautan syarat dan privasi, checkbox bila dibutuhkan secara hukum/produk. |
| 5 | Arah setelah daftar | Ke akun atau studio sesuai intended destination. |

## 4. Arah visual spesifik

Tanpa kartu promo berlebihan; satu kolom formulir dengan jarak 16–20 px.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Validasi password menampilkan syarat yang belum terpenuhi.
2. Password boleh diperlihatkan sementara.
3. Login link tersedia di bawah.
4. Tidak tersedia pilihan daftar sebagai owner.

## 6. Loading, empty, error, dan edge cases

- Email digunakan: instruksi jelas tanpa data pribadi berlebih.
- Jaringan error: input tetap.
- Verifikasi email bila dipakai: status jelas.

## 7. Copy contoh

CTA: “Buat Akun”. Subcopy: “Simpan desain favoritmu dan lihat status pesanan.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop card terpusat max-width 440 px.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan membuat field tambahan yang tidak dipakai pada proses inti.

## 9. Kriteria penerimaan UI/UX

- [ ] Form mobile tidak meminta alamat terlalu dini.
- [ ] Persetujuan tidak prechecked jika diwajibkan pilihan sadar.
- [ ] Keyboard tidak menutupi submit.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
