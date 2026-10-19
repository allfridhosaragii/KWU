# Arsitektur Renderer, Scene, Kamera, dan Lifecycle

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Runtime 3D pilihan
Browser memakai WebGL 2 melalui Three.js + React Three Fiber; Drei menyediakan helpers (`useGLTF`, controls, environment, performance monitor). Hanya mount satu Canvas utama saat editor aktif. WebGPU adalah eksperimen lanjutan, bukan syarat dapat checkout.

## Alur mount
1. Halaman server mengambil DTO produk, variant, manifest, rules, auth state.
2. Poster 2D tampil terlebih dahulu, lalu `CustomizerClient` dimuat dengan dynamic import.
3. Feature detect WebGL, kemampuan hardware, `prefers-reduced-motion`, data saver. Pilih profil Low/Balanced/High.
4. Runtime load GLB base, mannequin, lingkungan studio ringan; ornamen opsional di-load setelah user memilih.
5. Siapkan kamera target berdasarkan bounds objek dan category preset.
6. Interaction controller mengendalikan kamera atau item aktif. Editor menyimpan transform logis, renderer mengikuti model itu.
7. Saat keluar route, cancel async loaders, hapus listeners, release non-shared GPU resources, stop loop, dan unmount Canvas.

## Scene graph rekomendasi
```text
Scene
  EnvironmentLight
  ProductRoot
    MannequinOrDevice
    BaseProduct
    Attachments
      Element_1
      Element_2
  Controls / Selection overlay
  ContactShadow (conditional)
CameraRig
```
Jangan letakkan informasi UI/harga di mesh; tampilkan melalui React DOM overlay.

## State/render lifecycle
`frameloop='demand'` ketika scene diam; `invalidate()` saat kontrol imperatif, perubahan rig atau animasi. Selama drag aktif, render terjadwal; setelah selesai berhenti. Gunakan `Suspense` dan poster fallback agar layout tidak meloncat.

## Interaksi standar
- Drag kosong = orbit, tap objek = select, drag objek = transform bila terpilih. Gesture controller membedakan pointer capture dan dua sentuhan.
- Batasi zoom min/max untuk mencegah camera clipping dan penetrasi mesh.
- Simpan kamera/view preset terpisah dari konfigurasi barang; rotasi camera tidak memengaruhi order.

## Error recovery
Gagal glTF/decoder: retry sekali/penjelasan; WebGL context lost: stop loop, tampilkan fallback, coba restore saat tersedia; tidak ada WebGL: poster 2D + opsi katalog. Jangan memaksa pembayaran gagal akibat renderer mati.

## Sumber
https://r3f.docs.pmnd.rs/advanced/scaling-performance
https://threejs.org/docs/pages/GLTFLoader.html
