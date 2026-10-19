# Studio 05. Stiker HP | Phone Canvas

**Kategori:** `phone-sticker`  
**Template halaman:** `/studio/[type]/[productId]`  
**Perangkat utama:** mobile, tap dan multi-touch.

## 1. Model, framing, dan scene default

HP 3D dengan pilihan casing polos atau transparan dan beberapa warna casing polos.

**Framing pertama:** HP berorientasi portrait, punggung menghadap pengguna dengan sedikit sudut tiga-perempat; area kamera terlihat jelas; ketika edit stiker kamera mendekati belakang secara ortografis/mendekati orthographic.

**Pencahayaan dan material:** Case transparan punya transmission/fallback alpha yang dapat dibaca; desain stiker tetap jelas. Latar netral agar warna case tidak berubah hangat.

## 2. Kamera dan pose yang tersedia

Preset Back Flat, 3/4 Back, Side Edge, Detail Camera Area. Rotasi memudahkan melihat casing transparan tanpa salah mengira material solid.

Kamera harus punya tombol **Reset View**, kontrol zoom dengan batas aman, dan petunjuk gesture singkat di awal. Posisi kamera tidak diperlakukan sebagai perubahan barang fisik.

## 3. Variabel produk yang boleh dipilih

- Jenis case: Polos atau Transparan, bukan pilihan kaca bertekstur fiktif.
- Warna case polos dari katalog; transparan tetap transparan.
- Model/ukuran HP yang memang didukung oleh aset.
- Desain stiker A/B/C dan variasi ukuran cetak.
- Jumlah stiker dan opsi layer kalau benar-benar dapat diproduksi.

## 4. Struktur tab Bottom Sheet

| Urutan | Panel |
| --- | --- |
| 1 | Model HP |
| 2 | Casing |
| 3 | Warna |
| 4 | Tambah Stiker |
| 5 | Posisi |
| 6 | Ukuran & Rotasi |

Di atas panel selalu ada nama produk dan state editing. Ketika panel collapsed, pengguna melihat lebih banyak model; ketika expanded, scene masih bisa ditemukan dan kembali diperkecil.

## 5. Cara kerja Preset

Preset dapat menyusun 1–3 stiker pada area belakang yang valid sesuai model dan tipe casing. Preset tidak mengubah warna casing yang dipilih secara tak terlihat.

Preset harus diidentifikasi dengan nama yang mudah dikenali dan thumbnail statis. Perubahan preset tidak boleh menghapus custom tanpa konfirmasi jika pengguna sudah memodifikasinya.

## 6. Custom bebas dan kontrol sentuh

User mengetuk stiker, drag pada permukaan, dua jari zoom saat tidak drag, gunakan handle/tombol rotasi & scale. Stiker tidak bergerak melewati cutout kamera, tombol/pinggiran case.

- Interaksi langsung: tap untuk memilih, drag sesuai mode, gesture dua jari untuk zoom.
- Alternatif aksesibel: tombol step kiri/kanan/atas/bawah, rotasi ±, skala ±, dan pilihan anchor jika relevan.
- Panel kontrol hanya muncul saat objek atau pengaturan terkait aktif; hindari semua slider tampil sekaligus.

## 7. Anchor/surface dan aturan produksi

**Posisi dan koordinat:** Surface UV untuk punggung casing; kamera cutout dan bibir/edge diberi polygon exclusion zone. Ukuran desain dikonversi ke mm untuk produksi stiker.

**Batas valid:** Tidak menempel di kamera/bibir tombol; stiker tidak diluar casing; skala min/maks sesuai stok/cetak; overlapping jika boleh harus eksplisit dan berurutan.

Jika pengguna melewati batas, sistem menunjukkan alasan singkat, tidak memindahkan objek ke lokasi acak, dan memungkinkan Undo.

## 8. Anggaran mobile dan fallback

Bahan transparan dapat mahal untuk GPU, pakai material alternatif pada Low; satu model HP aktif per scene; preload varian kecil yang paling mungkin.

Target FPS dan ukuran GLB harus ditentukan dari benchmark asset nyata; fallback gambar tetap tersedia. Jangan menggunakan render aktif di semua thumbnail sekaligus.

## 9. Kasus sulit dan state error

- Sticker out-of-bounds: snap balik ke posisi valid dan hint area tempel.
- Model HP beda rasio: hitung ulang UV/area valid, jangan reuse transform mentah.
- Transparansi tidak didukung baik: tampil fallback visual dan label.

## 10. Copy petunjuk

“Coba pada casing favoritmu.” “Perangkat pada gambar hanya untuk pratinjau.”

## 11. Handoff owner / produksi

Owner menerima tipe casing sebagai media atau SKU yang dibeli sesuai katalog, model HP, stiker, ukuran cetak, warna, posisi dan thumbnail. Jika yang dijual hanya stiker, jelaskan bahwa HP/casing hanya preview.

## 12. Acceptance test kategori

- [ ] Ganti polos/transparan tanpa kehilangan stiker saat kompatibel.
- [ ] Sticker tidak bisa menutupi kamera.
- [ ] Ornamen bisa dipindah via tombol non-drag.
- [ ] Ukuran sticker memiliki satuan fisik.
- [ ] Owner mendapat artwork yang sesuai.

## Referensi silang

- [Prinsip Studio bersama](00_PRINSIP_STUDIO.md)
- [Gesture dan alternatif tanpa drag](09_GESTURE_DAN_KONTROL.md)
- [Penyimpanan desain](10_DESAIN_SIMPAN_PREVIEW.md)
- [Kontras & token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md)
