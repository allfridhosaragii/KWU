# 04. Pilih Studio 3D

**Route:** `/studio`  
**Kelompok:** Toko & Publik  
**Pola visual:** Experience Gateway  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memperlihatkan delapan pengalaman custom dengan jelas tanpa membebani HP dengan delapan renderer aktif.

## 2. Komposisi 1 layar pertama (_above the fold_)

Heading editorial “Buat jadi milikmu.” Dua kategori besar Aksesoris dan Stiker, kemudian grid delapan kartu preview statis.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Intro studio | Satu paragraf pendek cara kerja preset + custom bebas. |
| 2 | Pintu masuk unggulan | Gelang dan stiker HP dibuat lebih besar sebagai contoh dua jenis custom berbeda. |
| 3 | Empat aksesoris | Gelang, Cincin, Kalung, Gantungan Tas dengan gambar dan satu kalimat interaksi. |
| 4 | Empat media stiker | HP, Tablet Apple, MacBook, Botol Stainless dengan gambar dan satu kalimat tentang permukaan. |
| 5 | Informasi penggunaan | 3 langkah: pilih produk, atur, simpan atau beli; link bantuan. |
| 6 | Kinerja & fallback | Kartu memakai screenshot statis, bukan canvas 3D untuk semua kartu. |

## 4. Arah visual spesifik

Gallery hangat dengan kartu foto 4:5 dan heading serif; tiap kategori konsisten framing produk.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Ketuk kartu membuka pemilih produk/route customizer sesuai kategori.
2. Kategori dapat ditelusuri dengan scroll biasa.
3. Kartu mengindikasikan apabila 3D belum tersedia.
4. Pilihan produk bisa dibuka tanpa login; login dibutuhkan saat menyimpan ke akun jika kebijakan demikian.

## 6. Loading, empty, error, dan edge cases

- Kategori tanpa model: tampil “Belum tersedia” dan tautan katalog.
- Foto gagal: fallback thumbnail produk.
- Daftar kosong: CTA Jelajahi Koleksi.

## 7. Copy contoh

Subcopy: “Pilih media atau aksesori. Putar, coba variasi, dan atur detailnya.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop memakai dua section grid 4 kolom dan ruang editorial lebih luas.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menggabungkan “stiker HP” dengan penjualan HP tanpa keterangan.

## 9. Kriteria penerimaan UI/UX

- [ ] 8 kategori ditemukan tanpa kebingungan istilah.
- [ ] Tidak lebih dari satu canvas aktif, idealnya nol di halaman ini.
- [ ] Kartu menampilkan apa yang bisa dikustom.
- [ ] Alur kategori → produk → Studio dapat diikuti.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
