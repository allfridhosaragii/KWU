# 22. Profil dan Pengaturan

**Route:** `/account/profile`  
**Kelompok:** Akun Pembeli  
**Pola visual:** Account Settings  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memberikan kontrol informasi pribadi, keamanan, dan preferensi tampilan.

## 2. Komposisi 1 layar pertama (_above the fold_)

Heading Profil, avatar/inisial, field nama dan informasi kontak, pengaturan sesi, kualitas 3D otomatis.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Identitas | Ubah nama/foto opsional, kontak email dan telepon yang relevan. |
| 2 | Keamanan | Ganti password, status sesi bila tersedia. |
| 3 | Preferensi | Kualitas 3D Auto/Low/Balanced/High; reduced motion mengikuti OS. |
| 4 | Informasi akun | Tautan privasi dan bantuan. |
| 5 | Logout | Tindakan terpisah pada bagian akhir. |

## 4. Arah visual spesifik

Grouped settings satu kolom seperti aplikasi iOS yang bersih; gunakan divider bukan banyak card.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Edit per bagian mempertahankan data di bagian lain.
2. Kualitas 3D berubah setelah konfirmasi/pilihan sadar.
3. Logout jelas dan aman.

## 6. Loading, empty, error, dan edge cases

- Foto gagal upload: fallback inisial.
- Update gagal: nilai lama tetap.
- Perubahan akun sukses: status terlihat.

## 7. Copy contoh

Label: “Kualitas 3D” pilihan default “Otomatis”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop max-width form 720 px.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menawarkan setting kompleks yang belum diimplementasikan.

## 9. Kriteria penerimaan UI/UX

- [ ] Bagian setting mudah dipindai.
- [ ] Kontrol kualitas menjelaskan tradeoff performa.
- [ ] Password tidak ditampilkan secara terbuka.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
