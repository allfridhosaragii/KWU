# Studio 06. Stiker Tablet Apple | Tablet Canvas

**Kategori:** `tablet-sticker`  
**Template halaman:** `/studio/[type]/[productId]`  
**Perangkat utama:** mobile, tap dan multi-touch.

## 1. Model, framing, dan scene default

Model tablet Apple 3D sebagai media preview stiker, fokus pada area punggung.

**Framing pertama:** Tablet landscape di punggung dengan perspektif tiga-perempat, lalu berpindah ke tampilan tegak lurus untuk editing. Mendukung opsi portrait untuk pemeriksaan komposisi.

**Pencahayaan dan material:** Permukaan aluminium brushed dengan refleksi lembut; warna perangkat tetap netral; artwork stiker tidak kehilangan saturasi secara berlebihan.

## 2. Kamera dan pose yang tersedia

Preset Back Flat Landscape, Back Portrait, 3/4 Side, Camera Detail. Zoom dibatasi agar pengguna tidak kehilangan konteks ukuran.

Kamera harus punya tombol **Reset View**, kontrol zoom dengan batas aman, dan petunjuk gesture singkat di awal. Posisi kamera tidak diperlakukan sebagai perubahan barang fisik.

## 3. Variabel produk yang boleh dipilih

- Model tablet yang didukung (ukuran fisik harus benar).
- Warna perangkat jika ada pada aset realistis; bukan parameter harga stiker kecuali barang dijual.
- Pilihan set stiker preset.
- Ukuran dan orientasi stiker.
- Layer order serta jumlah stiker yang dapat dicetak.

## 4. Struktur tab Bottom Sheet

| Urutan | Panel |
| --- | --- |
| 1 | Model Tablet |
| 2 | Paket Stiker |
| 3 | Tambah |
| 4 | Layer |
| 5 | Posisi |
| 6 | Ukuran |

Di atas panel selalu ada nama produk dan state editing. Ketika panel collapsed, pengguna melihat lebih banyak model; ketika expanded, scene masih bisa ditemukan dan kembali diperkecil.

## 5. Cara kerja Preset

Preset mengatur komposisi landscape; bila user ganti orientasi preview ke portrait, posisi dalam UV tetap melekat pada permukaan.

Preset harus diidentifikasi dengan nama yang mudah dikenali dan thumbnail statis. Perubahan preset tidak boleh menghapus custom tanpa konfirmasi jika pengguna sudah memodifikasinya.

## 6. Custom bebas dan kontrol sentuh

Drag stiker di belakang tablet dengan UV; tombol plus-minus untuk ukuran/rotasi, layer selection list untuk stiker tertutup.

- Interaksi langsung: tap untuk memilih, drag sesuai mode, gesture dua jari untuk zoom.
- Alternatif aksesibel: tombol step kiri/kanan/atas/bawah, rotasi ±, skala ±, dan pilihan anchor jika relevan.
- Panel kontrol hanya muncul saat objek atau pengaturan terkait aktif; hindari semua slider tampil sekaligus.

## 7. Anchor/surface dan aturan produksi

**Posisi dan koordinat:** Permukaan belakang UV; zona kamera dan tepi melengkung excluded; konversi ukuran ke mm terhadap model tablet.

**Batas valid:** Stiker tidak boleh menutup modul kamera dan melewati radius tepi; jaga minimum printable size; lapisan yang overlapping perlu kebijakan.

Jika pengguna melewati batas, sistem menunjukkan alasan singkat, tidak memindahkan objek ke lokasi acak, dan memungkinkan Undo.

## 8. Anggaran mobile dan fallback

Gunakan satu permukaan edit berbasis texture layer; batasi ukuran texture update saat drag agar FPS stabil. Saat melepas gesture, lakukan final higher-quality preview jika mampu.

Target FPS dan ukuran GLB harus ditentukan dari benchmark asset nyata; fallback gambar tetap tersedia. Jangan menggunakan render aktif di semua thumbnail sekaligus.

## 9. Kasus sulit dan state error

- Sticker hilang di balik kamera: auto select layer list.
- Preview UV meleset: reset map sesuai device model.
- Banyak stiker: pembatasan layer dan feedback performa.

## 10. Copy petunjuk

“Atur susunan di belakang tabletmu.”

## 11. Handoff owner / produksi

Owner menerima model tablet sebagai skala referensi, ukuran nyata setiap stiker, posisi UV, layer, dan artwork resolusi cetak. Tablet tidak otomatis dijual.

## 12. Acceptance test kategori

- [ ] Stiker tetap di tempat saat rotate portrait/landscape view.
- [ ] Tidak tembus zona kamera.
- [ ] Layer select bisa memilih stiker tertutup.
- [ ] Ukuran dan penempatan dapat diekspor sebagai data cetak.

## Referensi silang

- [Prinsip Studio bersama](00_PRINSIP_STUDIO.md)
- [Gesture dan alternatif tanpa drag](09_GESTURE_DAN_KONTROL.md)
- [Penyimpanan desain](10_DESAIN_SIMPAN_PREVIEW.md)
- [Kontras & token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md)
