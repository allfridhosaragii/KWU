# 15. Reset Password

**Route:** `/reset-password`  
**Kelompok:** Autentikasi  
**Pola visual:** Focused Form  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Membuat password baru dengan jelas dan memberi status token yang valid.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul “Buat password baru” dengan input password, konfirmasi, petunjuk syarat, CTA Simpan Password.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Validitas tautan | Jika token kedaluwarsa, tampil instruksi meminta tautan baru. |
| 2 | Form password | Dua field, show/hide, validasi panjang/aturan yang benar. |
| 3 | Simpan | Tombol menyimpan lalu konfirmasi sukses. |
| 4 | Sukses | Link Masuk Kembali. |
| 5 | Keamanan | Hindari menampilkan token mentah di konten UI. |

## 4. Arah visual spesifik

Form kompak hangat, pesan success forest + ikon dan teks.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Mismatch diberi error di field kedua.
2. Simpan sekali per submit.
3. Setelah sukses tombol Login jelas.

## 6. Loading, empty, error, dan edge cases

- Token kedaluwarsa: CTA Minta Tautan Baru.
- Password tidak cocok: inline error.
- Server error: retry aman.

## 7. Copy contoh

CTA: “Simpan Password”. Sukses: “Password berhasil diperbarui.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop max-width 440 px.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan memberi kesan reset berhasil sebelum verifikasi server.

## 9. Kriteria penerimaan UI/UX

- [ ] Field tidak kehilangan isi saat validasi lokal.
- [ ] Sukses hanya setelah respons server valid.
- [ ] Tautan kedaluwarsa punya recovery path.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
