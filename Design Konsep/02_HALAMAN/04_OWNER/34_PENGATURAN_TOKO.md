# 34. Pengaturan Toko

**Route:** `/owner/settings`  
**Kelompok:** Owner  
**Pola visual:** Settings Utility  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Mengatur identitas, informasi kontak, kebijakan, pembayaran, dan pengiriman yang memengaruhi pengalaman pembeli.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul Pengaturan Toko dan grup menu Brand, Kontak, Pembayaran, Pengiriman, Kebijakan, Preferensi.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Brand identity | Nama toko, logo, deskripsi singkat, social links. |
| 2 | Kontak | Email/WhatsApp/operating hours bila valid. |
| 3 | Pengiriman | Metode/biaya dan kebijakan yang sedang aktif. |
| 4 | Pembayaran | Informasi integrasi secara aman; tidak tampilkan API secret pada UI. |
| 5 | Kebijakan | Tautan edit kebijakan sesuai kontrol akses. |
| 6 | Review dan save | Perubahan penting membutuhkan konfirmasi dan penanda perubahan tersimpan. |

## 4. Arah visual spesifik

Grouped form satu kolom, accordion/group label; tidak menjadi halaman panjang tanpa navigasi.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Setiap grup bisa disimpan independen bila didukung.
2. Upload logo memiliki preview dan batas ukuran.
3. Perubahan berdampak besar menampilkan konfirmasi.

## 6. Loading, empty, error, dan edge cases

- Save gagal: perubahan pengguna tidak lenyap.
- Logo gagal: placeholder brand.
- Pengaturan belum lengkap: tampil checklist onboarding.

## 7. Copy contoh

“Kelola informasi yang dilihat pelanggan.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop sidebar subsetting dan form kanan.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mengaktifkan metode pembayaran hanya dari toggle UI tanpa konfigurasi backend sah.

## 9. Kriteria penerimaan UI/UX

- [ ] Tidak menampilkan kunci API.
- [ ] Ada ringkasan perubahan berhasil.
- [ ] Setiap field punya helper text bila berisiko.
- [ ] Role check server.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
