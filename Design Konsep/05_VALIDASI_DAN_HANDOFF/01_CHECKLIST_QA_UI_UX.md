# QA UI/UX — Audit Sebelum Handoff dan Rilis

## 1. Konsistensi visual

- [ ] 34 template halaman memakai token warna/typo/spacing yang sama.
- [ ] Semua heading editorial tidak mengorbankan keterbacaan.
- [ ] Harga, jumlah, nomor order, dan status memakai gaya Manrope yang konsisten.
- [ ] Tidak ada shadow/gradient/warna hardcode yang keluar dari design system tanpa alasan tercatat.
- [ ] Foto/render produk memakai arah cahaya dan framing yang konsisten.

## 2. Mobile dan responsive

- [ ] Uji 320, 360, 375, 390, 430, 768, 1024, 1440 CSS px.
- [ ] Bottom nav tidak menutupi konten; safe area iPhone terpenuhi.
- [ ] Keyboard tidak menutupi input dan CTA.
- [ ] Tidak ada horizontal overflow tak disengaja.
- [ ] Landscape Studio tetap dapat dimanipulasi.
- [ ] UI dapat digunakan pada pembesaran browser 200%.

## 3. Katalog dan pembelian

- [ ] Filter kategori, harga, bahan, warna, kompatibilitas berjalan; hasil dan chip tersinkron.
- [ ] Kembali dari detail memulihkan pilihan filter/scroll yang relevan.
- [ ] Produk stiker membedakan benda preview dari item yang dijual.
- [ ] Harga final terbaca sebelum checkout.
- [ ] Keranjang menyimpan thumbnail dan konfigurasi item.
- [ ] Checkout tidak kehilangan input setelah error/retry.
- [ ] Payment sukses/pending/gagal ditampilkan sesuai status terverifikasi.

## 4. Studio 3D

- [ ] Delapan kategori memiliki scene dan panel benar.
- [ ] Rotasi, zoom, reset view bekerja.
- [ ] Drag objek tidak ikut memutar kamera.
- [ ] Perubahan preset/custom tidak menggandakan atau menghilangkan komponen.
- [ ] Alternatif tanpa drag bisa mengubah posisi/rotasi/skala.
- [ ] Aturan anchor/collision/surface bekerja.
- [ ] Ganti varian material tidak merusak warna fisik secara berlebihan.
- [ ] Save/reload menjaga konfigurasi, versi, thumbnail, total harga.
- [ ] Graceful fallback saat WebGL/GLB/gpu context gagal.

## 5. Owner

- [ ] Akun pembeli tidak bisa membuka route owner.
- [ ] Dashboard menampilkan data periode dan status benar, tidak Rp0 palsu karena error.
- [ ] Owner bisa mencari dan memproses pesanan pada HP.
- [ ] Detail order berisi daftar produksi + visual final.
- [ ] Stok dan pembayaran mempunyai status terpisah.
- [ ] Publish produk memeriksa kesiapan aset/preset.

## 6. Aksesibilitas

- [ ] WCAG 2.2 AA kontras dicek pada halaman nyata.
- [ ] Target sentuh internal ideal 44 px untuk kontrol penting.
- [ ] Fokus keyboard dan screen reader label benar.
- [ ] Dragging alternatif satu-pointer tersedia.
- [ ] Reduced motion diterapkan.
- [ ] Loading/error/status diumumkan tanpa spam.

## 7. Performa nyata

- [ ] Uji FPS scene pada minimal satu iPhone dan satu Android kelas menengah/rendah.
- [ ] Pantau memori GPU setelah berpindah Studio 20 kali.
- [ ] Periksa ukuran asset transfer pertama dan total setelah memilih varian.
- [ ] LCP/INP/CLS diukur pada build produksi, bukan dari asumsi desain.
- [ ] Model Low/Auto benar-benar mengurangi biaya rendering.

## 8. Uji tugas manusia

- [ ] 5 orang dapat menemukan satu item dan membuka Studio tanpa instruksi.
- [ ] 5 orang dapat menaruh ornamen/stiker dan menyimpan desain.
- [ ] 5 orang dapat menemukan harga dan menyelesaikan checkout sandbox.
- [ ] Owner bisa membaca production sheet dan memperbarui status.

## Kriteria sign-off

Semua isu blocker pembayaran, akses role, kehilangan desain, area sticker invalid, dan crash 3D harus selesai. Temuan kosmetik minor boleh masuk backlog dengan tingkat prioritas jelas. Checklist yang belum diuji tetap dianggap **belum terverifikasi**, bukan otomatis lulus.
