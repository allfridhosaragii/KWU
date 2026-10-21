# KWU 3D Viewer V15: gambar HD selama rotasi

## Penyebab kualitas tampak 144p
Fallback 360° menampilkan atlas berukuran 768 × 768 px per sudut ketika model digeser. Gambar WebP 1536 × 1536 px baru dimuat setelah jeda 75 ms ketika berhenti. Saat pengguna memutar cepat atau zoom, sprite 768 terlihat pecah. Mesh anatomi artistik MakeHuman juga belum menyerupai hasil scan manusia 1:1.

## Perbaikan yang diterapkan
- Hapus jeda 75 ms untuk mengunduh frame 1536p.
- Prefetch frame tetangga sesuai arah putar dan gunakan cache LRU maksimum 7 frame untuk menjaga memori mobile.
- Tampilkan frame 1536p seketika saat sudah ada di cache. Jika belum siap, atlas 768p tetap memberi feedback rotasi tanpa membekukan browser.
- Simpan screenshot dari frame 1536p aktif jika sudah tersedia, alih-alih selalu mengambil sprite 768p.
- Cache asset frontend menggunakan v15-1.
- Pertahankan 5 tone kulit, default Sawo Matang, dan 21 model dalam navigasi owner.

## Pemeriksaan wajib setelah deploy
1. Studio gelang/cincin/kalung: setiap drag mengubah sudut dan setelah gambar HD dimuat tampil lebih tajam.
2. Zoom dan pergantian tone: model tidak kembali ke sprite secara permanen.
3. Safari iPhone dan Chrome Android: cek pemakaian memori, lag, serta kestabilan tab.
4. Lakukan hard refresh atau buka versi v15-1 bila JS lama masih tersimpan.

## Batas kualitas
Ini tetap fallback interaktif berbasis urutan render kamera, bukan geometri WebGL real-time. Mengganti 768p menjadi 1536p tidak membuat bentuk tangan otomatis fotorealistis. Akurasi anatomi/skin perlu pipeline scan 3D yang sesuai, dan FPS perangkat fisik belum diuji oleh CI.
