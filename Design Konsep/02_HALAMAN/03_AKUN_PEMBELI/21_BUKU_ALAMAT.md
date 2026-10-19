# 21. Buku Alamat

**Route:** `/account/addresses`  
**Kelompok:** Akun Pembeli  
**Pola visual:** Address Utility  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Membantu pembeli mengelola alamat pengiriman yang valid.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul “Alamat Pengiriman”, daftar kartu alamat, tombol Tambah Alamat yang jelas.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Alamat utama | Kartu teratas dengan label “Utama”. |
| 2 | Alamat lain | Nama penerima, telepon parsial bila perlu, jalan/kota/kode pos. |
| 3 | Tambah/edit | Form alamat pada sheet/page fokus; label di atas field. |
| 4 | Pilih utama | Set alamat default tanpa menghapus yang lama. |
| 5 | Hapus | Konfirmasi sebelum penghapusan jika dipakai pesanan aktif. |

## 4. Arah visual spesifik

Card putih dengan divider; fokus keterbacaan alamat multi-line.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Tambah/edit membuka form lengkap.
2. Ubah utama menunjukkan penanda.
3. Hapus meminta konfirmasi.
4. Back dari checkout kembali ke pilihan alamat.

## 6. Loading, empty, error, dan edge cases

- Kosong: CTA Tambah Alamat.
- Alamat tidak valid: error per field.
- Gagal save: isi form dipertahankan.

## 7. Copy contoh

CTA: “Tambah Alamat”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop list dan panel form dua kolom jika nyaman.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan membuat peta interaktif sebagai syarat wajib.

## 9. Kriteria penerimaan UI/UX

- [ ] Alamat default mudah dikenali.
- [ ] Tidak ada pemotongan alamat yang menyembunyikan detail penting.
- [ ] Keyboard numerik untuk kode pos/telepon bila relevan.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
