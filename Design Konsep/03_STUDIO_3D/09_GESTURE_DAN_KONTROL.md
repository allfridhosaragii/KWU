# Gesture, Mode Interaksi, dan Aksesibilitas 3D

## Gesture matrix

| Konteks | Satu jari | Dua jari | Ketuk | Tombol alternatif |
|---|---|---|---|---|
| Ruang kosong scene | Orbit kamera | Zoom | Deselect objek | Panah view, Reset View |
| Ornamen tidak terpilih | Orbit atau tap-select tergantung hit target | Zoom | Memilih objek | Daftar elemen |
| Ornamen terpilih + mode Edit | Drag ornamen sepanjang anchor/surface | Zoom jika tidak bentrok | Pilih/ubah anchor | ± posisi/rotasi/scale |
| Bottom sheet | Scroll sheet | Tidak dipakai untuk scene | Pilih varian | Semua pilihan berupa tombol |
| MacBook hinge | Hanya pada kontrol hinge spesifik | Zoom | Toggle pose preset | Tombol Buka/Tutup |
| Cincin | Ketuk jari untuk pindah jika valid | Zoom | Pilih jari | Lima tombol jari |

## State machine konseptual

`idle -> camera-orbit -> idle`, `idle -> element-selected -> element-dragging -> element-selected`, `element-selected -> panel-open -> element-selected`. Ketika `element-dragging`, orbit kamera dinonaktifkan. Saat gesture batal atau pointer release, kontrol harus kembali stabil, termasuk saat sentuhan terputus di tepi browser.

## Tombol mobile

- Header: Back, Undo, Redo (overflow jika ruang sempit), Save, More.
- View: Reset View, Front, Side, Back bila relevan.
- Selected element: Putar kiri/kanan, Geser kiri/kanan, Perbesar/Perkecil, Hapus, Ganti.
- Semua tombol nondekoratif punya label aksesibel, target sentuh ideal 44 px.

## Kebiasaan satu tangan

Taruh aksi penting di area jangkauan bawah: pilihan ornamen, mode, dan Add Cart. Detail kamera/pose bisa berada pada rail samping dengan hitbox cukup besar atau sheet. Jangan menaruh seluruh kontrol di empat sudut canvas sehingga tangan harus terus berpindah jauh.

## Konfirmasi dan feedback

- Menempatkan elemen: tampil highlight subtil pada anchor valid.
- Konflik/overlap: tampil status teks dekat panel, bukan toast bertubi-tubi.
- Batas skala: tombol disabled dengan alasan atau hentikan gerakan di batas.
- Undo: kembali ke konfigurasi sebelumnya tanpa loncatan kamera jika kamera tidak berubah.

## Pengguna non-drag

WCAG 2.2 AA 2.5.7 mengharuskan alternatif single-pointer non-drag untuk fungsi drag tertentu. Karena itu, pemindahan stiker/charm harus bisa melalui tab Posisi, tombol ± atau pilihan anchor, dan kontrol numerik/preset yang dapat ditekan. Keyboard pada desktop tetap mendukung fokus/aksi jika terimplementasi.

## Safari iOS / Chrome Android

- Uji pinch saat bottom sheet collapsed/expanded.
- Cegah scroll body hanya ketika pointer berada dalam kontrol canvas yang sesuai.
- Hindari accidental pull-to-refresh saat drag dekat tepi atas.
- Cek perubahan orientasi dan resize saat toolbar browser muncul/hilang.
- Pastikan gestur dua jari tidak menimbulkan gerak objek yang tidak disengaja.

## Penyederhanaan tingkat kesulitan

Pertama kali membuka Studio tampil petunjuk satu kali 2–3 langkah. Setelah itu petunjuk tersedia lewat tombol `?` tanpa overlay selalu aktif. Pengguna berpengalaman bisa masuk dan mulai mengedit tanpa melewati tur panjang.
