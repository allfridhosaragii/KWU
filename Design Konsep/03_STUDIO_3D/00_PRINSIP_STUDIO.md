# Prinsip Universal Studio 3D — Semua Delapan Produk

## Tujuan

Membuat pengguna dapat melihat detail realistis, mencoba preset, mengatur objek secara bebas dalam batas fisik yang masuk akal, menyimpan desain, dan menambah ke keranjang melalui HP. Studio harus dapat digunakan tanpa pengetahuan Blender/3D.

## Kategori dan file spesifik

| Tipe | Produk/Media | Dokumen |
|---|---|---|
| `bracelet` | Gelang pada tangan | [01](01_GELANG.md) |
| `ring` | Cincin pada lima jari | [02](02_CINCIN.md) |
| `necklace` | Kalung pada leher | [03](03_KALUNG.md) |
| `bag-charm` | Gantungan pada tas | [04](04_GANTUNGAN_TAS.md) |
| `phone-sticker` | HP + casing | [05](05_STIKER_HP.md) |
| `tablet-sticker` | Tablet Apple | [06](06_STIKER_TABLET.md) |
| `macbook-sticker` | MacBook | [07](07_STIKER_MACBOOK.md) |
| `bottle-sticker` | Botol stainless | [08](08_STIKER_BOTOL.md) |

## Komposisi mobile

1. **Top bar:** kembali, nama studio/produk, undo, simpan, overflow. Tidak lebih dari beberapa ikon terlihat sekaligus; sisanya masuk menu.
2. **Scene 3D:** area visual fleksibel, target sekitar 55–65% dari tinggi ruang kerja ketika sheet collapsed, bukan angka kaku pada semua HP.
3. **Petunjuk konteks:** satu kalimat pada penggunaan awal, kemudian memudar.
4. **Bottom sheet:** state peek/half/full; tab Preset, Komponen/Stiker, Bahan/Warna, Posisi, Ukuran sesuai kategori.
5. **Footer aksi:** ringkasan harga, Tambah ke Keranjang, dan indikasi perubahan belum tersimpan.

## Mode

| Mode | Perilaku | Label |
|---|---|---|
| Preset | Pilihan owner berisi konfigurasi valid, bisa dijadikan titik awal | “Preset” |
| Custom Bebas | Pengguna mengubah posisi, rotasi, skala, elemen dalam batas produksi | “Atur Sendiri” |
| Camera | Gestur memutar/zoom tampilan tanpa mengubah desain | “Lihat Produk” |
| Element Edit | Gestur pada objek mengubah konfigurasi, kamera terkunci selama drag | “Edit Ornamen/Stiker” |

## Anatomi kontrol bersama

- Orbit kamera dengan gesture sentuh, clamp sudut dan zoom agar objek tidak hilang.
- Tap pada objek yang bisa diedit menampilkan selection ring/outline dan panel kontekstual.
- Snap/hotspot hanya pada anchor valid; batas invalid menunjukkan alasan.
- Undo/redo mencatat perubahan desain; gerakan kamera sebaiknya tidak masuk riwayat undo desain.
- Reset View hanya mengembalikan posisi kamera, Reset Design berbeda dan membutuhkan konfirmasi.
- Save menghasilkan konfigurasi terstruktur plus thumbnail pratinjau.
- Add Cart menyimpan config snapshot, harga terbaru, dan komponen fisik yang dipesan.

## Performance dan visual realism

- Default Balanced/Auto; pertahankan preferensi kualitas pengguna bila kompatibel.
- Preview katalog/gateway statis; GLB hanya dimuat pada studio atau detail ketika diminta.
- Gunakan material PBR untuk metal, casing, kain/kulit, dan stainless dengan lighting netral terkontrol.
- Asset transfer model awal perlu anggaran yang disepakati lewat pengujian perangkat. Angka target 1–3 MB bukan janji universal.
- Saat scene diam, renderer boleh berhenti; saat manipulasi aktif, respons input harus diprioritaskan.
- Matikan efek dekoratif lebih dulu sebelum menurunkan ketepatan posisi/ukuran produk.
- Browser dengan WebGL unsupported mendapat pratinjau 2D serta pesan yang jujur.

## State universal

- **Loading:** tampil hero render fallback dengan skeleton yang ukurannya tetap dan progress bila ada.
- **No asset:** editor 3D tidak dijanjikan aktif; arahkan ke foto/detail, atau pilihan lain.
- **Invalid placement:** objek tetap terpilih, jelaskan batas, sediakan undo dan posisi sebelumnya.
- **Network offline:** perubahan lokal saat sesi dapat tertahan; save ke akun menunggu sinkronisasi. Jangan berkata “tersimpan” sebelum server mengonfirmasi.
- **GPU context loss:** tampil retry; desain tidak boleh hilang karena pergantian scene.
- **Unsaved exit:** konfirmasi simpan/buang/batal.

## Relasi ke proses bisnis

Konfigurasi yang dilihat customer harus dapat direkonstruksi owner, termasuk versi aset, pilihan bahan, ukuran, koordinat anchor/surface, urutan layer, dan thumbnail. Harga tidak dihitung dari pixel atau posisi layar; backend harus memvalidasi kombinasi dan harga.

Lihat juga [Gesture](09_GESTURE_DAN_KONTROL.md), [Design save](10_DESAIN_SIMPAN_PREVIEW.md), dan [Halaman Studio](../02_HALAMAN/01_TOKO_PUBLIK/05_CUSTOMIZER_3D.md).
