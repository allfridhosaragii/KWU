# Studio 04. Gantungan Tas | The Bag Charm Atelier

**Kategori:** `bag-charm`  
**Template halaman:** `/studio/[type]/[productId]`  
**Perangkat utama:** mobile, tap dan multi-touch.

## 1. Model, framing, dan scene default

Model tas netral dengan beberapa titik pengait dan ornamen gantungan.

**Framing pertama:** Tas tiga-perempat, handle dan titik hook terlihat; charm mendapat ruang untuk menggantung di samping tanpa tertutup tas.

**Pencahayaan dan material:** Kulit/kain tas tidak terlalu mengkilap; bahan metal/akrilik gantungan jelas. Lighting netral dengan sedikit warm shadow.

## 2. Kamera dan pose yang tersedia

Preset Front 3/4, Side Hook, Back, Charm Macro. Rotasi tas dibatasi untuk tetap mudah dimengerti.

Kamera harus punya tombol **Reset View**, kontrol zoom dengan batas aman, dan petunjuk gesture singkat di awal. Posisi kamera tidak diperlakukan sebagai perubahan barang fisik.

## 3. Variabel produk yang boleh dipilih

- Model tas preview sesuai aset yang disediakan.
- Titik pengait A/B bila relevan.
- Model gantungan/charm A/B/C/D.
- Warna komponen dan susunan charm.
- Panjang gantungan jika opsi fisiknya tersedia.

## 4. Struktur tab Bottom Sheet

| Urutan | Panel |
| --- | --- |
| 1 | Model Tas |
| 2 | Gantungan |
| 3 | Titik Pengait |
| 4 | Ornamen |
| 5 | Warna |
| 6 | Susunan |

Di atas panel selalu ada nama produk dan state editing. Ketika panel collapsed, pengguna melihat lebih banyak model; ketika expanded, scene masih bisa ditemukan dan kembali diperkecil.

## 5. Cara kerja Preset

Tap preset gantungan A/B/C/D langsung mengganti objek terpasang, menampilkan nama dan perubahan harga yang benar.

Preset harus diidentifikasi dengan nama yang mudah dikenali dan thumbnail statis. Perubahan preset tidak boleh menghapus custom tanpa konfirmasi jika pengguna sudah memodifikasinya.

## 6. Custom bebas dan kontrol sentuh

Pengguna bisa memindahkan gantungan ke hook yang valid dan menyusun charm pada rantai. Drag tidak membuat rantai terlepas secara visual; ada tombol pilih titik pengait.

- Interaksi langsung: tap untuk memilih, drag sesuai mode, gesture dua jari untuk zoom.
- Alternatif aksesibel: tombol step kiri/kanan/atas/bawah, rotasi ±, skala ±, dan pilihan anchor jika relevan.
- Panel kontrol hanya muncul saat objek atau pengaturan terkait aktif; hindari semua slider tampil sekaligus.

## 7. Anchor/surface dan aturan produksi

**Posisi dan koordinat:** Bag-hook anchor pada handle/ring; sub-anchor untuk komponen rantai. Gantungan tetap terhubung ke tas ketika kamera berputar.

**Batas valid:** Titik hook harus mampu menerima ukuran komponen, jumlah elemen dibatasi, aksesori tidak menembus badan tas.

Jika pengguna melewati batas, sistem menunjukkan alasan singkat, tidak memindahkan objek ke lokasi acak, dan memungkinkan Undo.

## 8. Anggaran mobile dan fallback

Gantungan animasi ayunan pendek terbatas atau pre-baked; jangan menjalankan physics engine berat untuk semua ornamen.

Target FPS dan ukuran GLB harus ditentukan dari benchmark asset nyata; fallback gambar tetap tersedia. Jangan menggunakan render aktif di semua thumbnail sekaligus.

## 9. Kasus sulit dan state error

- Hook tidak kompatibel: tampil alasan.
- Gantungan terlalu panjang: tampil batas susunan.
- Model tas preview hilang: tampil produk gantungan sendiri dengan konteks.

## 10. Copy petunjuk

“Pilih gantungan, lalu tentukan posisinya.”

## 11. Handoff owner / produksi

Owner melihat item gantungan yang dibeli, tas media preview jika bukan SKU, hook, susunan, material, dan ukuran.

## 12. Acceptance test kategori

- [ ] Gantungan A/B/C/D berganti tanpa duplikat objek lama.
- [ ] Bisa pindah minimal dua hook jika tersedia.
- [ ] Ornamen tidak melayang/tembus tas.
- [ ] Harga tepat setelah pergantian preset.

## Referensi silang

- [Prinsip Studio bersama](00_PRINSIP_STUDIO.md)
- [Gesture dan alternatif tanpa drag](09_GESTURE_DAN_KONTROL.md)
- [Penyimpanan desain](10_DESAIN_SIMPAN_PREVIEW.md)
- [Kontras & token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md)
