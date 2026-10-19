# 12. Login

**Route:** `/login`  
**Kelompok:** Autentikasi  
**Pola visual:** Focused Form  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Membantu akun pembeli dan owner masuk melalui halaman yang sama tanpa kebingungan.

## 2. Komposisi 1 layar pertama (_above the fold_)

Logotype kecil, heading “Selamat datang kembali”, form email/password satu kolom, CTA Masuk penuh, tautan lupa password dan register.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Identitas halaman | Logo kecil, tombol kembali ke toko dan heading ringkas. |
| 2 | Form login | Email, password dengan show/hide, label selalu terlihat, auto-fill tidak dihalangi. |
| 3 | Aksi utama | Masuk; tombol disable hanya selama submit, loading jelas. |
| 4 | Tautan alternatif | Lupa password dan Buat akun; role owner diarahkan setelah login berdasarkan izin server. |
| 5 | Keamanan & bantuan | Pesan error tidak membuka informasi akun terdaftar/tidak secara berlebihan. |

## 4. Arah visual spesifik

Card putih di atas ivory; heading serif kecil opsional, konten Manrope; tidak ada foto hero yang mendorong form di bawah layar.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Enter/submit menjalankan satu kali login.
2. Show password men-toggle isi dan state aksesibel.
3. Login sukses kembali ke intended page bila valid.
4. Kesalahan form mempertahankan alamat email.

## 6. Loading, empty, error, dan edge cases

- Password salah: pesan netral dan jelas.
- Jaringan gagal: retry.
- Session expired: arahkan login tanpa hilangnya konteks yang aman.

## 7. Copy contoh

Judul: “Selamat datang kembali.” CTA: “Masuk”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop card berlebar sekitar 440 px di tengah dengan ruang kosong editorial.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Tidak membuat login terpisah owner kecuali kebutuhan keamanan resmi berubah.

## 9. Kriteria penerimaan UI/UX

- [ ] Form selesai satu tangan pada 360 px.
- [ ] Owner tidak memilih role dari UI login.
- [ ] Terdapat link register dan reset.
- [ ] Password tidak muncul dalam log UI.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
