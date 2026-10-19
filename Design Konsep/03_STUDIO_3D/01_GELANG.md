# Studio 01. Gelang | The Charm Atelier

**Kategori:** `bracelet`  
**Template halaman:** `/studio/[type]/[productId]`  
**Perangkat utama:** mobile, tap dan multi-touch.

## 1. Model, framing, dan scene default

Manekin tangan realistis dengan gelang di pergelangan.

**Framing pertama:** Pergelangan dalam komposisi diagonal 3/4; gelang mengisi sekitar 30–45% lebar area scene awal supaya tangan memberi konteks ukuran.

**Pencahayaan dan material:** Kulit tangan tekstur natural tetapi tidak lebih tajam daripada gelang. Metal PBR dengan highlight lembut; hindari sparkle berlebihan. Hand rig tidak memengaruhi ukuran asli gelang.

## 2. Kamera dan pose yang tersedia

Preset: front wrist, 3/4 wrist, side wrist, detail clasp. Orbit clamp menghindari tangan terbalik atau gelang menghilang; tombol Fokus Gelang dan Reset View.

Kamera harus punya tombol **Reset View**, kontrol zoom dengan batas aman, dan petunjuk gesture singkat di awal. Posisi kamera tidak diperlakukan sebagai perubahan barang fisik.

## 3. Variabel produk yang boleh dipilih

- Jenis gelang: rantai, bangle, tali bila benar-benar tersedia.
- Warna bahan: silver/gold/varian owner; jangan dipaksa sama warna UI brand.
- Ukuran: S/M/L atau cm sesuai ukuran fisik yang ditetapkan.
- Charm: hati, bintang, bunga, inisial sesuai komponen katalog.

## 4. Struktur tab Bottom Sheet

| Urutan | Panel |
| --- | --- |
| 1 | Preset |
| 2 | Jenis Gelang |
| 3 | Charm |
| 4 | Warna Bahan |
| 5 | Ukuran |
| 6 | Atur Posisi |

Di atas panel selalu ada nama produk dan state editing. Ketika panel collapsed, pengguna melihat lebih banyak model; ketika expanded, scene masih bisa ditemukan dan kembali diperkecil.

## 5. Cara kerja Preset

Preset menempatkan 0–N charm pada posisi valid sepanjang gelang. Pilihan preset harus bisa dimodifikasi tanpa mengganti model dasar secara tidak sengaja.

Preset harus diidentifikasi dengan nama yang mudah dikenali dan thumbnail statis. Perubahan preset tidak boleh menghapus custom tanpa konfirmasi jika pengguna sudah memodifikasinya.

## 6. Custom bebas dan kontrol sentuh

Saat charm dipilih, tampil outline halus, drag mengikuti rail gelang; pilihan ± posisi sepanjang rail serta rotasi/scale bila kompatibel. Perubahan terasa langsung, tidak ada gerakan kamera saat drag.

- Interaksi langsung: tap untuk memilih, drag sesuai mode, gesture dua jari untuk zoom.
- Alternatif aksesibel: tombol step kiri/kanan/atas/bawah, rotasi ±, skala ±, dan pilihan anchor jika relevan.
- Panel kontrol hanya muncul saat objek atau pengaturan terkait aktif; hindari semua slider tampil sekaligus.

## 7. Anchor/surface dan aturan produksi

**Posisi dan koordinat:** Charm mengikuti `bracelet-track`; snap ke titik valid, jaga jarak minimum antarcharm dan tidak masuk ke pengait/area lipatan. Mengikuti deformasi pergelangan/manekin jika pose berubah.

**Batas valid:** Batas jumlah charm, jarak antar elemen, ukuran pengait, tidak boleh melayang/tembus tangan, warna bahan konsisten dengan stok.

Jika pengguna melewati batas, sistem menunjukkan alasan singkat, tidak memindahkan objek ke lokasi acak, dan memungkinkan Undo.

## 8. Anggaran mobile dan fallback

Default tidak perlu simulation cloth/chain berat; gunakan animation poses sederhana. Kurangi polygon tangan di mobile, pertahankan detail charm saat zoom.

Target FPS dan ukuran GLB harus ditentukan dari benchmark asset nyata; fallback gambar tetap tersedia. Jangan menggunakan render aktif di semua thumbnail sekaligus.

## 9. Kasus sulit dan state error

- Charm pada rail invalid: kembali ke posisi terakhir, tampil hint area valid.
- Model tangan gagal: fallback foto produk dan ringkasan komponen.
- Banyak charm membebani: instancing/reuse geometri dengan kualitas adaptif.

## 10. Copy petunjuk

“Geser charm mengikuti gelang.” “Pilih bahan dan ukuranmu.”

## 11. Handoff owner / produksi

Owner menerima model gelang, jenis rantai, panjang/ukuran, daftar charm, urutan rail, bahan, harga dan thumbnail.

## 12. Acceptance test kategori

- [ ] Dua charm dipindahkan ke lokasi berurutan tanpa overlap fatal.
- [ ] Gelang tetap mengikuti wrist saat pose diubah.
- [ ] Undo/redo memulihkan posisi semua charm.
- [ ] Preview dari empat sudut tetap akurat.
- [ ] Alternatif posisi tanpa drag berjalan.

## Referensi silang

- [Prinsip Studio bersama](00_PRINSIP_STUDIO.md)
- [Gesture dan alternatif tanpa drag](09_GESTURE_DAN_KONTROL.md)
- [Penyimpanan desain](10_DESAIN_SIMPAN_PREVIEW.md)
- [Kontras & token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md)
