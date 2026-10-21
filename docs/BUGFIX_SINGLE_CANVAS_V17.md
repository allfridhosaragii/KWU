# KWU V17: Perbaikan Tangan Terpotong Saat Zoom/Rotasi

## Laporan pengguna
Screenshot 21 Oktober 2026 memperlihatkan ujung jari terpisah dan sebagian tangan terpotong pada mode 360°.

## Penyebab yang diaudit
Pada V16 ada dua permukaan gambar sekaligus: sprite atlas 768 px pada canvas yang diperbesar dan `<img>` HD 1536 px terpisah yang juga diperbesar. Selisih pemuatan, ukuran kotak, atau sudut antar-lapisan dapat menghasilkan jari duplikat/terputus pada layar.

## Perbaikan
- HD di-decode dan di-cache, **tanpa ditambahkan ke DOM**.
- Canvas atlas yang sama menggambar frame 768 atau frame HD 1536. Hanya ada satu objek visual yang menerima transform zoom.
- Saat frame baru belum selesai dimuat, canvas menampilkan atlas dasar untuk sudut yang aktif, bukan menumpuk gambar HD dari sudut lama.
- Cache dibersihkan saat model, tone kulit, atau mode kualitas berubah.
- Klik dua kali pada area produk mengembalikan sudut dan zoom.
- Versi URL aset naik ke V17 untuk mencegah cache JavaScript V16.
- Detail 1536 px tetap dipertahankan. Tidak ada perubahan pada 21 GLB, role owner, atau default tone Sawo Matang.

## Bukti validasi
TypeScript/build dan tes regresi statis otomatis dijalankan oleh GitHub Actions. Perilaku GPU dan gesture Safari di HP fisik tetap harus diverifikasi terpisah.

## Catatan
Saat zoom besar sebagian tangan memang keluar dari bingkai sebagaimana kamera close-up. Gunakan Reset atau klik dua kali untuk kembali ke tampilan penuh. Namun ujung jari tidak boleh tampak terpisah akibat tumpukan dua lapisan.
