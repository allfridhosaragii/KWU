# Perbaikan viewer 3D V9

## Akar masalah pengujian
Pengujian browser terdahulu memakai fallback 2D karena konteks WebGL tidak tersedia. Keberhasilan UI test tidak membuktikan bahwa 3D dapat diputar pada GPU nyata.

## Perbaikan
- WebGL2 sebagai prioritas, WebGL1 sebagai fallback bila tersedia OES_vertex_array_object dan OES_element_index_uint.
- Konversi shader untuk WebGL1. Normal mikro diganti shading sederhana hanya di jalur kompatibilitas.
- Fallback pembacaan tekstur dengan HTMLImageElement bila createImageBitmap tidak tersedia.
- Gagal decode satu tekstur tidak mematikan keseluruhan rendering geometri.
- Pemulihan saat context lost / context restored.
- Tombol putar kiri/kanan 45° dan zoom masuk/keluar untuk HP/desktop.
- Label mode menunjukkan 3D Aktif (WebGL1/2) atau Preview 2D saat tidak ada GPU.
- Tone kulit sawo matang, menu owner, dan 21 aset GLB dipertahankan.

## Pemeriksaan yang dilakukan
- Kompilasi TypeScript lokal: berhasil.
- Pemeriksaan GLB dan site: berhasil.
- Pengujian browser 390 px untuk kontrol kamera, shader legacy, dan fallback: 11/11 berhasil.
- Keterbatasan: lingkungan tes tidak mempunyai WebGL/GPU aktif, sehingga hasil rendering dan FPS pada HP asli belum terverifikasi.
