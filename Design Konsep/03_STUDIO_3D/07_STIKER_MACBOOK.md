# Studio 07. Stiker MacBook | Laptop Canvas

**Kategori:** `macbook-sticker`  
**Template halaman:** `/studio/[type]/[productId]`  
**Perangkat utama:** mobile, tap dan multi-touch.

## 1. Model, framing, dan scene default

Model MacBook dengan engsel animatif, area utama cover luar laptop.

**Framing pertama:** Awal laptop tertutup atau lid view, cover menghadap pengguna. Tombol Buka menampilkan animasi engsel terukur lalu dapat ditutup untuk editing.

**Pencahayaan dan material:** Aluminium lid PBR halus; sisa detail keyboard cukup sederhana karena bukan tempat menempel stiker. Pencahayaan netral agar warna stiker benar.

## 2. Kamera dan pose yang tersedia

Preset Lid Flat, 3/4 Closed, Side, Open Preview. Kamera fokus punggung lid saat editor aktif.

Kamera harus punya tombol **Reset View**, kontrol zoom dengan batas aman, dan petunjuk gesture singkat di awal. Posisi kamera tidak diperlakukan sebagai perubahan barang fisik.

## 3. Variabel produk yang boleh dipilih

- Pilihan model/ukuran MacBook jika tersedia.
- Warna body sesuai model, hanya preview.
- Set stiker preset atau satu-satu.
- Posisi UV pada penutup luar.
- Ukuran fisik stiker dan rotasi.

## 4. Struktur tab Bottom Sheet

| Urutan | Panel |
| --- | --- |
| 1 | Model MacBook |
| 2 | Preset |
| 3 | Tambah Stiker |
| 4 | Layer |
| 5 | Posisi |
| 6 | Lihat Sudut |

Di atas panel selalu ada nama produk dan state editing. Ketika panel collapsed, pengguna melihat lebih banyak model; ketika expanded, scene masih bisa ditemukan dan kembali diperkecil.

## 5. Cara kerja Preset

Preset layout menyebar stiker pada cover luar tanpa menabrak tepi/elemen lain. Pilihan open pose tidak menyimpan posisi baru stiker.

Preset harus diidentifikasi dengan nama yang mudah dikenali dan thumbnail statis. Perubahan preset tidak boleh menghapus custom tanpa konfirmasi jika pengguna sudah memodifikasinya.

## 6. Custom bebas dan kontrol sentuh

Tap stiker pada lid → seleksi; editor membuka view datar; stiker bisa digeser/rotasi/scale. Tombol Buka Laptop hanya mengubah pose model untuk preview.

- Interaksi langsung: tap untuk memilih, drag sesuai mode, gesture dua jari untuk zoom.
- Alternatif aksesibel: tombol step kiri/kanan/atas/bawah, rotasi ±, skala ±, dan pilihan anchor jika relevan.
- Panel kontrol hanya muncul saat objek atau pengaturan terkait aktif; hindari semua slider tampil sekaligus.

## 7. Anchor/surface dan aturan produksi

**Posisi dan koordinat:** UV atlas cover-luar khusus; arah rotasi stiker harus mengikuti orientasi tutup (yang terbalik terhadap pengguna ketika lid dibuka) secara benar.

**Batas valid:** Tidak melampaui seam/hinge, tepi body atau area larangan yang disetujui; jangan menembus material lid saat pose berubah.

Jika pengguna melewati batas, sistem menunjukkan alasan singkat, tidak memindahkan objek ke lokasi acak, dan memungkinkan Undo.

## 8. Anggaran mobile dan fallback

Animasi buka-tutup sederhana rig engsel, tidak ada physics. UV sticker digambar pada surface lid saja; cache geometri.

Target FPS dan ukuran GLB harus ditentukan dari benchmark asset nyata; fallback gambar tetap tersedia. Jangan menggunakan render aktif di semua thumbnail sekaligus.

## 9. Kasus sulit dan state error

- Pose terbuka membuat sticker seolah terbalik: periksa transform lokal lid.
- MacBook belum didukung: pilih model alternatif, jangan memberi janji fit tepat.
- Shader sticker gagal: tampil posisi 2D & preview gambar.

## 10. Copy petunjuk

“Rancang cover MacBook sesuai gayamu.”

## 11. Handoff owner / produksi

Owner menerima versi model MacBook sebagai referensi, artwork, UV/local transform pada lid, ukuran cetak, dan thumbnail. MacBook bukan item yang dijual kecuali SKU terpisah.

## 12. Acceptance test kategori

- [ ] Sticker melekat pada tutup saat buka/tutup.
- [ ] Editing fokus lid menampilkan permukaan tepat.
- [ ] Ukuran sticker sesuai template cetak.
- [ ] Tetap ringan pada mobile setelah toggle pose berulang.

## Referensi silang

- [Prinsip Studio bersama](00_PRINSIP_STUDIO.md)
- [Gesture dan alternatif tanpa drag](09_GESTURE_DAN_KONTROL.md)
- [Penyimpanan desain](10_DESAIN_SIMPAN_PREVIEW.md)
- [Kontras & token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md)
