# Studio 08. Stiker Botol Stainless | Bottle Canvas

**Kategori:** `bottle-sticker`  
**Template halaman:** `/studio/[type]/[productId]`  
**Perangkat utama:** mobile, tap dan multi-touch.

## 1. Model, framing, dan scene default

Botol minum stainless model silinder dengan dua warna utama hitam dan abu-abu.

**Framing pertama:** Botol vertikal hampir memenuhi area scene; kamera tiga-perempat; bagian tengah badan menjadi area utama stiker. Saat edit, kamera mendekat tanpa memotong permukaan.

**Pencahayaan dan material:** Stainless hitam matte/graphite grey dengan highlight strip tipis; material tidak mengubah warna sticker menjadi cokelat. Shadow studio lembut.

## 2. Kamera dan pose yang tersedia

Preset Front, Side, Back, Full 360 Turn. Rotasi dibatasi agar produk selalu terbaca dan tutup tidak membuat viewer tersesat.

Kamera harus punya tombol **Reset View**, kontrol zoom dengan batas aman, dan petunjuk gesture singkat di awal. Posisi kamera tidak diperlakukan sebagai perubahan barang fisik.

## 3. Variabel produk yang boleh dipilih

- Warna botol: hitam dan abu-abu sebagai pilihan visual utama.
- Ukuran/bentuk botol hanya sesuai aset yang ada.
- Desain sticker die-cut/transparan bila benar-benar tersedia.
- Ukuran fisik dan jumlah stiker.
- Posisi horizontal mengelilingi silinder serta tinggi vertikal.

## 4. Struktur tab Bottom Sheet

| Urutan | Panel |
| --- | --- |
| 1 | Warna Botol |
| 2 | Preset |
| 3 | Tambah Stiker |
| 4 | Putar Botol |
| 5 | Posisi |
| 6 | Ukuran |

Di atas panel selalu ada nama produk dan state editing. Ketika panel collapsed, pengguna melihat lebih banyak model; ketika expanded, scene masih bisa ditemukan dan kembali diperkecil.

## 5. Cara kerja Preset

Preset menempatkan stiker pada bidang silinder yang valid, mempertahankan koordinat relatif jika warna botol berubah.

Preset harus diidentifikasi dengan nama yang mudah dikenali dan thumbnail statis. Perubahan preset tidak boleh menghapus custom tanpa konfirmasi jika pengguna sudah memodifikasinya.

## 6. Custom bebas dan kontrol sentuh

Stiker bisa digeser horizontal mengelilingi botol dan vertikal dalam batas. Pengguna bisa memakai slider derajat/posisi atau tombol kiri/kanan/atas/bawah.

- Interaksi langsung: tap untuk memilih, drag sesuai mode, gesture dua jari untuk zoom.
- Alternatif aksesibel: tombol step kiri/kanan/atas/bawah, rotasi ±, skala ±, dan pilihan anchor jika relevan.
- Panel kontrol hanya muncul saat objek atau pengaturan terkait aktif; hindari semua slider tampil sekaligus.

## 7. Anchor/surface dan aturan produksi

**Posisi dan koordinat:** Gunakan cylindrical UV yang memetakan sudut keliling dan tinggi. Seam UV ditangani agar stiker tidak terbelah ketika melewati batas 0°/360°.

**Batas valid:** Tidak mengenai area tutup, lekukan bawah, permukaan bertekstur tak layak tempel. Ukuran lebar stiker dibatasi keliling botol nyata; orientasi dan radius valid.

Jika pengguna melewati batas, sistem menunjukkan alasan singkat, tidak memindahkan objek ke lokasi acak, dan memungkinkan Undo.

## 8. Anggaran mobile dan fallback

Gunakan UV texture placement utama, bukan decal projected yang rawan distorsi pada bidang melengkung. Update tekstur efisien saat drag; hindari high-res render tiap frame.

Target FPS dan ukuran GLB harus ditentukan dari benchmark asset nyata; fallback gambar tetap tersedia. Jangan menggunakan render aktif di semua thumbnail sekaligus.

## 9. Kasus sulit dan state error

- Stiker melewati seam: remap tanpa flip/rusak.
- Permukaan tidak dapat ditempeli: hint arah zona valid.
- Refleksi berlebih pada hitam: quality downgrade material tidak merusak stiker.

## 10. Copy petunjuk

“Putar botol untuk melihat seluruh sisi.”

## 11. Handoff owner / produksi

Owner menerima warna media yang dipilih, model botol sebagai referensi, artwork, ukuran fisik, sudut/tinggi posisi stiker dan thumbnail. Jika yang dijual hanya sticker, botol tidak dihitung sebagai item.

## 12. Acceptance test kategori

- [ ] 360° tidak memotong sticker pada seam.
- [ ] Warna hitam dan abu berbeda akurat.
- [ ] Posisi sticker stabil setelah putaran penuh.
- [ ] Pilihan ukuran cetak sesuai keliling/tinggi real.
- [ ] Alternatif tanpa drag berfungsi.

## Referensi silang

- [Prinsip Studio bersama](00_PRINSIP_STUDIO.md)
- [Gesture dan alternatif tanpa drag](09_GESTURE_DAN_KONTROL.md)
- [Penyimpanan desain](10_DESAIN_SIMPAN_PREVIEW.md)
- [Kontras & token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md)
