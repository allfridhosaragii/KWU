# KWU V14 — Memperbaiki gambar 3D seperti 144p

## Diagnosis
- Viewer fallback 360 derajat memakai sprite 768 px untuk perhiasan dan 320 px untuk 18 model lain, lalu memperbesar sprite ketika pengguna zoom.
- Versi retina 1536 px hanya dimuat setelah diam selama 190 ms. Saat pengguna terus memutar model, tampilan tetap sprite.
- Geometri MakeHuman disubdivisi, tetapi bentuk dasar dan shading kulit masih menampilkan bidang bersudut.

## Solusi V14
1. Setelah model anatomi dan kuku selesai dibuat, pass Humphrey smoothing konservatif diterapkan hanya pada mesh kulit, tanpa merusak UV/PBR dan komponen perhiasan.
2. Mulai memuat retina 1536 px setelah 75 ms diam, lalu cache maksimum lima sudut termasuk tetangga kiri/kanan agar putaran berikutnya lebih cepat beresolusi tinggi.
3. Regenerasi atlas untuk semua 21 model memakai generator V11: 768 px per sudut untuk tiga kategori jewelry, 640 px untuk kategori lain (sebelumnya 320 px).
4. Perketat validasi workflow sehingga tidak dianggap lulus jika model lain masih memakai atlas 320 px.
5. Cache-busting versi v14-1 agar pengunjung mengambil viewer terbaru.

## Batas kualitas
Fallback masih berupa rangkaian gambar 360° dengan dua elevasi, bukan mesh 3D yang dirender per frame. Ketika rotasi sangat cepat, sprite awal tetap tampil untuk menjaga responsivitas. Model anatomis masih berdasarkan MakeHuman CC0, bukan scan tubuh manusia asli.

## Pengujian pra-deployment
- Script smoothing diuji pada 3 GLB lokal, material tekstur terjaga dan perpindahan vertex maksimum kurang dari 0.012 satuan dunia.
- Workflow memverifikasi seluruh 21 atlas, 720 frame retina, TypeScript build dan validitas model.
- FPS pada HP fisik belum dapat dijamin tanpa benchmark perangkat nyata.
