# Studio 03. Kalung | The Pendant Atelier

**Kategori:** `necklace`  
**Template halaman:** `/studio/[type]/[productId]`  
**Perangkat utama:** mobile, tap dan multi-touch.

## 1. Model, framing, dan scene default

Manekin leher dan bahu dengan kalung, rantai, serta liontin.

**Framing pertama:** Close-up leher dengan bahu sebagai konteks. Rantai tampak jatuh secara alami; liontin tidak tertutup panel.

**Pencahayaan dan material:** Material skin/neck netral. Rantai mendapat detail silhouette, pendant metal memiliki pantulan studio; jangan menumpuk efek glossy.

## 2. Kamera dan pose yang tersedia

Preset: Front Neck, 3/4 Neck, Side, Pendant Macro. Kontrol pose leher hanya sebatas gerak halus yang tidak mengubah desain fisik.

Kamera harus punya tombol **Reset View**, kontrol zoom dengan batas aman, dan petunjuk gesture singkat di awal. Posisi kamera tidak diperlakukan sebagai perubahan barang fisik.

## 3. Variabel produk yang boleh dipilih

- Jenis rantai sesuai katalog nyata.
- Panjang rantai dalam cm atau pilihan ukuran jelas.
- Material/warna logam.
- Model liontin dan charm tambahan.
- Penempatan liontin di titik yang valid.

## 4. Struktur tab Bottom Sheet

| Urutan | Panel |
| --- | --- |
| 1 | Rantai |
| 2 | Panjang |
| 3 | Liontin |
| 4 | Warna |
| 5 | Susun Ornamen |
| 6 | Sudut Pandang |

Di atas panel selalu ada nama produk dan state editing. Ketika panel collapsed, pengguna melihat lebih banyak model; ketika expanded, scene masih bisa ditemukan dan kembali diperkecil.

## 5. Cara kerja Preset

Preset menyatukan rantai, panjang, dan liontin. Saat preset diganti, animasi transisi tidak boleh mengubah panjang tanpa konfirmasi visual.

Preset harus diidentifikasi dengan nama yang mudah dikenali dan thumbnail statis. Perubahan preset tidak boleh menghapus custom tanpa konfirmasi jika pengguna sudah memodifikasinya.

## 6. Custom bebas dan kontrol sentuh

Liontin bisa diganti, urutan/posisi elemen pada rantai diubah dalam batas produksi. Geser mengikuti track rantai atau pilih anchor kiri/tengah/kanan jika jenis rantai mendukung.

- Interaksi langsung: tap untuk memilih, drag sesuai mode, gesture dua jari untuk zoom.
- Alternatif aksesibel: tombol step kiri/kanan/atas/bawah, rotasi ±, skala ±, dan pilihan anchor jika relevan.
- Panel kontrol hanya muncul saat objek atau pengaturan terkait aktif; hindari semua slider tampil sekaligus.

## 7. Anchor/surface dan aturan produksi

**Posisi dan koordinat:** Chain curve anchor mengikuti leher, liontin berada di depan tubuh dengan offset fisik realistis. Attachment yang bergerak mengikuti anchor neck rig.

**Batas valid:** Panjang minimal/maksimal, jumlah liontin, jarak aman, panjang rantai vs ukuran leher, simetri sesuai model.

Jika pengguna melewati batas, sistem menunjukkan alasan singkat, tidak memindahkan objek ke lokasi acak, dan memungkinkan Undo.

## 8. Anggaran mobile dan fallback

Gunakan chain segment teroptimasi atau pose terhitung sederhana; physics realtime penuh tidak wajib di HP.

Target FPS dan ukuran GLB harus ditentukan dari benchmark asset nyata; fallback gambar tetap tersedia. Jangan menggunakan render aktif di semua thumbnail sekaligus.

## 9. Kasus sulit dan state error

- Liontin tembus leher saat pose: koreksi anchor/pose bukan membiarkan glitch.
- Panjang tidak valid: tampil rentang ukuran.
- Animasi rantai berat: fallback pose statis.

## 10. Copy petunjuk

“Ubah panjang untuk melihat jatuhnya kalung.”

## 11. Handoff owner / produksi

Owner melihat jenis dan panjang rantai, model liontin, material, jumlah elemen, serta susunan akhir.

## 12. Acceptance test kategori

- [ ] Panjang rantai tampak berubah masuk akal.
- [ ] Liontin tetap pada posisi konsisten saat kamera diputar.
- [ ] Tidak terjadi clipping pada pose yang tersedia.
- [ ] Semua varian dapat dipreview dan disimpan.

## Referensi silang

- [Prinsip Studio bersama](00_PRINSIP_STUDIO.md)
- [Gesture dan alternatif tanpa drag](09_GESTURE_DAN_KONTROL.md)
- [Penyimpanan desain](10_DESAIN_SIMPAN_PREVIEW.md)
- [Kontras & token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md)
