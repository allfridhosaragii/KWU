# Motion System dan Microinteractions

## Prinsip

Gerakan untuk menunjukkan hubungan sebab-akibat, orientasi spasial, atau feedback. Jangan menambahkan animasi hanya supaya halaman “terlihat Awwwards”. Prioritas: respon input cepat, kemudian kualitas transisi.

## Token waktu awal

| Token | Durasi | Contoh |
|---|---:|---|
| `instant` | 0–80 ms | Highlight tekan/selection |
| `fast` | 120–180 ms | Tombol, icon, chip |
| `standard` | 200–280 ms | Bottom sheet, tab transition |
| `gentle` | 320–500 ms | Kamera berpindah ke close-up objek |
| `editorial` | 500–700 ms | Reveal satu gambar kampanye, sekali saja |

Easing UI bisa memakai ease-out; perpindahan objek 3D memakai interpolasi halus yang tidak menimbulkan perasaan kendali tertunda. Angka perlu diuji pada HP nyata.

## Motion penting

- **Variant selected:** objek berubah, kamera tidak meloncat, swatch menunjukkan pilihan.
- **Sticker placed:** snap subtil ke area valid; batas merah/teks jika tidak valid.
- **Saved:** tombol memberi state proses dan sukses, thumbnail desain diperbarui.
- **Add to cart:** feedback singkat dan badge keranjang bertambah.
- **Payment status:** jangan memakai animasi centang sebagai bukti sukses sebelum server terverifikasi.

## Batas performa

- Hanya properti transform dan opacity untuk animasi UI yang mungkin; hindari animasi layout berat dan filter blur besar.
- Canvas 3D harus dapat berhenti rendering saat diam; saat pengguna drag tetap responsif.
- Jangan memuat Lottie besar pada setiap kartu atau status.
- Saat tab tidak terlihat atau baterai/performa turun, hentikan gerakan ambient.

## Reduced motion

Ikuti `prefers-reduced-motion`: matikan parallax, kurangi transisi nonesensial, jangan melakukan auto-rotate manekin. Gerakan yang diperlukan untuk menjelaskan fungsi tetap dapat diganti snap/crossfade cepat.

## Aturan UX 3D

- Input langsung → visual feedback sesegera mungkin.
- Jika ornamen di-drag, kamera tidak berputar pada saat bersamaan.
- Kembalikan mode kamera setelah selesai memilih/menggeser.
- Undo/redo menjaga kesinambungan orientasi dan kondisi desain.

## QA motion

Uji pada 30 FPS, 60 FPS, jaringan lambat, Safari iOS dan Chrome Android. Pastikan tidak ada animasi yang mengubah harga/produk tanpa interaksi sadar pengguna.
