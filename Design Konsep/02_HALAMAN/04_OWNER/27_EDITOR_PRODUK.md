# 27. Editor Produk

**Route:** `/owner/products/new dan /owner/products/[id]/edit`  
**Kelompok:** Owner  
**Pola visual:** Guided Editor  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memungkinkan owner membuat produk custom yang jelas harga, varian, preset, dan batas produksinya.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul Tambah/Edit Produk, stepper 5–6 tahap, indikator tersimpan, CTA Simpan Draft.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Identitas | Nama, deskripsi, foto, kategori, status jual. |
| 2 | Harga dan persediaan | Harga dasar, komponen stok, aturan variasi nominal. |
| 3 | Varian | Bahan, warna, ukuran, kompatibilitas. |
| 4 | Custom rules | Preset default, komponen yang diizinkan, batas jumlah ornamen, titik pemasangan. |
| 5 | Aset preview | Pilih model GLB teroptimasi, posisi thumbnail, quality profile. |
| 6 | Review | Ringkasan sebelum publikasi, cek data wajib. |
| 7 | Publish | Konfirmasi aktif/draft dengan alasan bila gagal. |

## 4. Arah visual spesifik

Form bertahap satu kolom; step label jelas dan sticky save yang tidak menutup keyboard.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Bisa kembali antarstep tanpa kehilangan draft.
2. Aset picker membuka library terfilter.
3. Harga akhir diuji pada konfigurasi demo.
4. Publish mencegah kekosongan field wajib.

## 6. Loading, empty, error, dan edge cases

- Belum ada aset 3D: simpan draft, jangan publish custom yang tidak berfungsi.
- Autosave gagal: tampil indikator lokal.
- Varian invalid: error di step terkait.

## 7. Copy contoh

CTA: “Simpan Draft”, “Pratinjau”, “Publikasikan”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop dua kolom form dan panel preview sticky.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menjadikan model HP/tablet otomatis SKU jika hanya untuk sticker preview.

## 9. Kriteria penerimaan UI/UX

- [ ] Produk tidak bisa dipublikasi tanpa aturan custom wajib.
- [ ] Harga dasar dan tambahan tidak ambigu.
- [ ] Draft dapat dilanjutkan.
- [ ] Preview mencerminkan konfigurasi terbaru.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
