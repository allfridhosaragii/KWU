# 07. Checkout

**Route:** `/checkout`  
**Kelompok:** Toko & Publik  
**Pola visual:** Focused Transaction  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menyelesaikan pembelian dengan minimum gangguan, memberi rasa aman dan transparansi pembayaran.

## 2. Komposisi 1 layar pertama (_above the fold_)

Header kecil Checkout, step indicator ringan bila lebih dari satu langkah, ringkasan item dapat dilihat; alamat dan pembayaran tidak tersembunyi.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Ringkasan pesanan | Gambar item, nama, varian, qty, tombol expand untuk rincian custom. |
| 2 | Alamat | Pilih/tambah alamat, input dengan label dan validasi jelas. |
| 3 | Pengiriman | Metode, biaya, estimasi bila tersedia dari data layanan yang valid. |
| 4 | Metode pembayaran | Pilihan gateway dan penjelasan proses konfirmasi. |
| 5 | Breakdown biaya | Subtotal + ongkir + diskon + biaya lain yang benar-benar dikenakan. |
| 6 | Action area | Tombol Bayar Sekarang dengan nominal final dan loading state. |

## 4. Arah visual spesifik

Satu kolom warm ivory, form putih berborder; tidak memakai promo hero. Elemen utama membentuk ritme yang mudah dipindai.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Alamat valid memengaruhi opsi ongkir; total dikalkulasi ulang dengan penjelasan.
2. Tombol Bayar mengunci submit ganda dan menunjukkan proses.
3. Jika login diwajibkan, arahkan kembali ke checkout setelah login.
4. Pembayaran eksternal kembali ke route hasil dengan status yang divalidasi server.

## 6. Loading, empty, error, dan edge cases

- Field salah: error inline dan fokus ke field pertama.
- Pembayaran pending: tampilan status pending, bukan sukses.
- Gateway gagal: jangan menghapus checkout; retry aman.

## 7. Copy contoh

CTA: “Bayar Sekarang · RpXX.XXX”. Status: “Memproses pembayaran…”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop dua kolom: form kiri, ringkasan sticky kanan, tanpa sidebar toko.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menampilkan centang sukses dari return URL saja; periksa status server.

## 9. Kriteria penerimaan UI/UX

- [ ] Total final terlihat sebelum transaksi.
- [ ] Form dapat diselesaikan pada 320 px tanpa horizontal scroll.
- [ ] Submit ganda dicegah.
- [ ] Skrip visual dekoratif tidak mengganggu payment.
- [ ] Keyboard mobile tidak menutup field/tombol.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
