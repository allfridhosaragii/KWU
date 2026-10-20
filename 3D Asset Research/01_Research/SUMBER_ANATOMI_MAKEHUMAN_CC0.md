# Sumber Anatomi Human Mesh — Lisensi dan Provenance

Sumber asli: https://github.com/makehumancommunity/makehuman/blob/master/makehuman/data/3dobjs/base.obj

File mesh di sumber tersebut menyatakan pelepasan CC0 pada September 2020. Ini digunakan untuk mengganti mannequin tangan dan bust leher KWU yang sebelumnya dibuat dari primitif geometris.

Langkah pemrosesan dalam `tools/build_anatomical_cc0.py`:
1. Memilih geometri tubuh, tidak menyertakan helper dan joint cubes.
2. Memotong model kanan di ujung lengan untuk menghasilkan tangan dan pergelangan yang memiliki lipatan anatomis.
3. Mengambil kepala, leher, bahu dan tulang selangka dalam satu permukaan mesh untuk halaman kalung.
4. Menyesuaikan orientasi/proporsi untuk viewer lama tanpa mengubah navigasi.
5. Menambahkan kalung/gelang/cincin terpisah.
6. Ekspor GLB dan poster yang baru.

Penting: MakeHuman merupakan karya pemodelan anatomi manusia, bukan scan fotogrametri pasien atau foto manusia asli. Hasil lebih anatomis daripada model silinder sebelumnya, tetapi label `hyperreal 1:1` membutuhkan evaluasi visual dan skin texture scanning, yang belum terpenuhi.

Target web: model 3D sebenarnya dimuat hanya ketika Studio dibuka, sementara katalog memakai poster WebP.
