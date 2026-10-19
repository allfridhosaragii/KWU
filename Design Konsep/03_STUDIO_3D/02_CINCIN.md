# Studio 02. Cincin | The Ring Atelier

**Kategori:** `ring`  
**Template halaman:** `/studio/[type]/[productId]`  
**Perangkat utama:** mobile, tap dan multi-touch.

## 1. Model, framing, dan scene default

Manekin tangan dengan kelima jari dapat dipilih.

**Framing pertama:** Tangan dari sisi punggung dengan semua jari cukup terlihat; cincin pada jari default, lalu close-up objek ketika memilih jari.

**Pencahayaan dan material:** Skintone netral dan pencahayaan studio. Detail bevel metal dan batu diprioritaskan saat close-up. Outline pilihan jari sangat tipis, bukan neon.

## 2. Kamera dan pose yang tersedia

Preset: Hand Overview, Finger Focus, Side Ring Detail, Gem Detail. Jangan membuat kamera melewati kulit/mesh ketika zoom.

Kamera harus punya tombol **Reset View**, kontrol zoom dengan batas aman, dan petunjuk gesture singkat di awal. Posisi kamera tidak diperlakukan sebagai perubahan barang fisik.

## 3. Variabel produk yang boleh dipilih

- Posisi jari: ibu jari, telunjuk, tengah, manis, kelingking.
- Model cincin: band/plain/ornamental sesuai daftar nyata.
- Material: silver/gold/steel yang ada.
- Batu atau ukiran/ornamen tambahan jika barang dapat dibuat.
- Ukuran mengikuti ukuran cincin per jari, bukan satu ukuran otomatis.

## 4. Struktur tab Bottom Sheet

| Urutan | Panel |
| --- | --- |
| 1 | Jari |
| 2 | Model |
| 3 | Bahan |
| 4 | Batu/Ornamen |
| 5 | Ukuran |
| 6 | Sudut Lihat |

Di atas panel selalu ada nama produk dan state editing. Ketika panel collapsed, pengguna melihat lebih banyak model; ketika expanded, scene masih bisa ditemukan dan kembali diperkecil.

## 5. Cara kerja Preset

Preset memadukan jari awal dan model cincin; pilihan ukuran tidak boleh berubah sendiri ketika pindah jari.

Preset harus diidentifikasi dengan nama yang mudah dikenali dan thumbnail statis. Perubahan preset tidak boleh menghapus custom tanpa konfirmasi jika pengguna sudah memodifikasinya.

## 6. Custom bebas dan kontrol sentuh

Pengguna ketuk jari atau memilih tombol bernama lima jari. Cincin berpindah mengikuti anchor tulang jari, bukan posisi screen. Bila multi-ring dijual, batas maksimum dan aturan tiap jari jelas.

- Interaksi langsung: tap untuk memilih, drag sesuai mode, gesture dua jari untuk zoom.
- Alternatif aksesibel: tombol step kiri/kanan/atas/bawah, rotasi ±, skala ±, dan pilihan anchor jika relevan.
- Panel kontrol hanya muncul saat objek atau pengaturan terkait aktif; hindari semua slider tampil sekaligus.

## 7. Anchor/surface dan aturan produksi

**Posisi dan koordinat:** Anchor tiap jari pada lokasi pangkal cincin yang benar; orientasi sumbu cincin mengikuti pose tulang, bukan hanya mesh depan.

**Batas valid:** Cincin tidak menembus jari, ukuran harus cocok pada anchor, area batu tidak masuk kulit, kombinasi multi-ring sesuai produksi.

Jika pengguna melewati batas, sistem menunjukkan alasan singkat, tidak memindahkan objek ke lokasi acak, dan memungkinkan Undo.

## 8. Anggaran mobile dan fallback

Hindari rig deformasi rumit saat hanya berpindah jari; pose tangan dapat berupa preset ringan. Texture 1K pada tangan mobile, detail lebih tajam hanya di cincin.

Target FPS dan ukuran GLB harus ditentukan dari benchmark asset nyata; fallback gambar tetap tersedia. Jangan menggunakan render aktif di semua thumbnail sekaligus.

## 9. Kasus sulit dan state error

- Jari tidak kompatibel ukuran: tampil pilih ukuran dan tahan perpindahan.
- Zoom terlalu dekat: batas minimum jarak kamera.
- Model batu gagal: tampil band plain dengan label pratinjau terbatas.

## 10. Copy petunjuk

“Pilih jari untuk mencoba.” “Sesuaikan ukuran cincin sebelum memesan.”

## 11. Handoff owner / produksi

Owner melihat jari target (sebagai preview), ukuran fisik ring, material, batu, varian serta catatan produksi.

## 12. Acceptance test kategori

- [ ] Semua lima jari dapat dipilih melalui tombol.
- [ ] Anchor per jari tetap benar saat pose berubah.
- [ ] Harga mengikuti pilihan batu/material.
- [ ] Ring tidak melayang atau menembus kulit pada view umum.
- [ ] Mode tanpa drag dapat digunakan.

## Referensi silang

- [Prinsip Studio bersama](00_PRINSIP_STUDIO.md)
- [Gesture dan alternatif tanpa drag](09_GESTURE_DAN_KONTROL.md)
- [Penyimpanan desain](10_DESAIN_SIMPAN_PREVIEW.md)
- [Kontras & token](../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md)
