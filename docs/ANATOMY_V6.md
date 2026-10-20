# KWU V6 — Detail Kulit pada Model Anatomi

## Keputusan produksi

Versi V6 menggunakan **mesh anatomi MakeHuman yang sudah digunakan proyek** sebagai dasar tangan, wajah, leher, dan bahu. Versi V6 tidak mengganti mesh anatomi dengan objek silinder, bola, atau bentuk geometris sederhana.

Model MakeHuman adalah aset artistik berlisensi CC0, **bukan hasil pemindaian orang nyata**. Target fotorealistik 1:1 belum bisa diklaim tanpa referensi pemindaian atau aset fotogrametri yang sesuai.

Sumber: https://github.com/makehumancommunity/makehuman/blob/master/LICENSE.md

## Perubahan V6

- Mesh bagian tubuh didensifikasi melalui subdivision satu kali jika memang diperlukan.
- Material kulit menggunakan albedo procedural hingga 2048 × 2048 piksel.
- Ditambahkan pola variasi warna kulit halus pada skala besar dan kecil.
- Warna sedikit lebih hangat pada bagian yang relevan.
- Material kulit menerapkan metallic = 0 dan roughness = 0.86 agar tidak terlihat seperti plastik mengilap.
- Tidak ditambahkan rambut atau bulu pada tangan.
- Model perhiasan, logika keranjang, posisi kamera, serta navigasi owner tetap dipertahankan.
- Preview foto render memakai beberapa sumber cahaya studio untuk membaca material secara benar.

## Proses build

1. `python tools/build_anatomical_cc0.py`
2. `python tools/skin_detail_postprocess_v6.py`
3. `KWU_PREVIEW_MODELS=bracelet,ring,necklace xvfb-run -a python tools/render_v5_previews.py`
4. `npm run build`
5. `python tools/check_models_v2.py`

## QA minimum

- GLB gelang, cincin, dan kalung harus berisi lebih dari satu mesh.
- Mesh tubuh tetap menjadi mesh pertama karena viewer saat ini menganggap mesh pertama sebagai badan utama.
- GLB harus memiliki tekstur albedo embedded.
- Tidak boleh ada kehilangan komponen perhiasan setelah export.
- File harus dapat dimuat ulang oleh trimesh dan browser.
- Situs harus tetap merender fallback 2D jika WebGL 2 tidak tersedia.

## Catatan kualitas

Model ini masih **prototype anatomi artistik dengan kulit lebih halus**, bukan bukti visual medis atau replika tubuh 1:1. Kualitas akhir harus dinilai dari screenshot 3D di browser dengan GPU nyata, bukan jumlah polygon atau ukuran file saja.
