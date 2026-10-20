# KWU Viewer V10 — Putar objek tanpa WebGL

## Masalah pengguna
Setelah V8/V9, halaman Studio masih menampilkan gambar statis yang tidak bisa diputar. Browser yang tidak menyediakan GPU/WebGL tetap masuk jalur fallback 2D. Pengujian UI sebelum V10 tidak menjamin gerakan rendering.

## Perbaikan teknis
1. Menambahkan fallback turntable interaktif yang benar-benar dibentuk dari model GLB, diputar offline melalui VTK, dan diekspor dalam satu atlas WebP per model.
2. 21 model mendapat 360° multi-view (24 sudut horizontal untuk gelang, cincin dan kalung, 16 sudut untuk model lain), dengan dua elevasi.
3. Tangan, cincin, kalung mendapat 5 opsi tone kulit pada fallback, default `Sawo Matang`.
4. Gestur geser horizontal mengubah azimuth dan geser vertikal mengubah elevasi; pinch, mousewheel dan tombol +/- mengatur zoom. Tombol ↶ ↷ serta reset juga bekerja.
5. Kontrol `360°` disediakan untuk beralih manual ke mode kompatibel jika realtime WebGL tidak berjalan meski konteks terbentuk.
6. GitHub Actions menghasilkan atlas setelah membangun GLB terbaru, lalu menyimpannya ke GitHub Pages dan repository.
7. Cache HTML, app.js, viewer.js dan turntable.js memakai V10-1 supaya browser mengambil versi baru.

## Batasan yang dinyatakan jelas
Mode GPU-independen **bukan WebGL 3D real-time**. Mode ini adalah foto hasil render objek GLB dari berbagai sudut, sehingga user tetap bisa memutar/zoom namun tidak mendapatkan sudut kamera yang benar-benar kontinu, perhitungan realtime ornamen, atau simulasi material di GPU. Jika WebGL berfungsi, viewer tetap menampilkan 3D real-time.

## Audit
- WebGL GPU tidak tersedia pada Chromium CI di lingkungan ini.
- Mode 360 tanpa GPU diuji dengan klik, drag, zoom, reset, dan status pada 320, 390, 768, dan 1440 px, 20 cek interaksi berhasil.
- 21 atlas disiapkan dan ditemukan, serta tone kulit default Sawo Matang dipertahankan.
- Kinerja pada HP pengguna tetap perlu diverifikasi langsung setelah Pages diterbitkan.
