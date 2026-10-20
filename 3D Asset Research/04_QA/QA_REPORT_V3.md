# QA Aset 3D V3 dan Navigasi Owner

Tanggal: 20 Oktober 2026
Status: prototipe prosedural, **belum 1:1** dengan benda fisik

## Perbaikan fungsional
- Navigasi model 3D owner dipertahankan pada seluruh halaman owner.
- Desktop: 21 tautan model 3D pada sidebar serta horizontal quick-access.
- Mobile: tombol `Model 3D` pada navigasi bawah dan horizontal quick-access yang bisa digeser.
- Library 3D menyediakan delapan model kategori dan 13 varian Apple, preview dan link GLB individual.
- Pergantian pilihan model menggunakan satu route `/owner/assets?model=<id>`.
- Library 3D hanya membuka satu canvas untuk model yang dipilih.

## Peningkatan aset
- Model hard-surface iPhone/iPad/MacBook kini memakai cap vertices terpisah dari side bevel untuk menghilangkan artefak shading berbentuk X pada bidang datar.
- Ransel memiliki tambahan detail jahitan, zipper-pull, dan piping pada kantong depan.
- Botol stainless memiliki gasket tutup dan cincin detail leher tambahan.
- GLB dan poster WebP diregenerasi dari pipeline sumber `tools/make_models_v2.py`.
- Material shader dirancang lebih berbeda antara permukaan matte dan logam, menggunakan pencahayaan key/fill dengan spesular terkendali; **tidak setara PBR lengkap**.

## Strategi performa browser
- Renderer tetap render-on-demand saat terdapat perubahan, bukan 60 FPS kontinu sepanjang waktu.
- DPR mobile otomatis dibatasi hingga sekitar 1,25 (mode High hingga 1,6).
- Preserve drawing buffer dimatikan untuk mengurangi kebutuhan memori.
- Poster WebP dan pesan fallback 2D saat WebGL 2 tidak tersedia.
- Model 3D di library owner dimuat hanya untuk satu model terpilih.

## Pengujian otomatis yang telah dijalankan
- `npx tsc -p tsconfig.json`
- `python tools/check_site.py`
- `python tools/check_models_v2.py`
- `python tests/run_matrix.py` (320/390/768/1440 px)
- `python tests/model_variants_e2e.py`
- `python tests/owner_model_nav_e2e.py` (21 varian × 4 viewport, jumlah cek ada di `qa-owner-models.json`)

## Batas pengujian dan kualitas yang belum lulus
- Browser headless di lingkungan pengujian tidak mengekspos WebGL 2, jadi **rendering GPU real-time, gesture 3D, suhu perangkat, dan FPS HP nyata belum dapat divalidasi**.
- Proses pengujian ini memeriksa halaman, navigasi, fallback, data pilihan model, integritas GLB, dan flow demo, bukan ketepatan fisik atau reproduksi optik fotoreal.
- Model tangan bukan 3D scan manusia dengan rig anatomis penuh.
- Model tas dan botol menggunakan satu foto depan sehingga bentuk belakang serta dimensi fisiknya belum terverifikasi.
- Model Apple disusun menurut proporsi ukuran resmi dan warna yang didekati, bukan CAD resmi atau replika akurat sampai tingkat detail mikro.
- Website GitHub Pages masih frontend demo, bukan transaksi produksi dan autentikasi aman.

## Kriteria penerimaan untuk rilis photoreal 1:1 berikutnya
1. Referensi multi-angle terukur atau scan 3D setiap objek.
2. Model master UV-textured dan material PBR melalui pipeline Blender.
3. Rig/manekin diselesaikan dengan pengujian deformasi jari dan pergelangan.
4. Optimasi GLB dan tekstur KTX2 serta uji visual setara pada HP nyata.
5. Selisih siluet, dimensi, warna, dan material diperiksa terhadap referensi fisik terukur.
6. Benchmark FPS dan memori pada sekurang-kurangnya tiga kelas perangkat HP serta beberapa browser.
