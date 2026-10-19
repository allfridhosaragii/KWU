# Strategi Performa Mobile dan Adaptive Quality

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Performance budget awal (hipotesis)
| Ukuran | Budget uji awal | Catatan |
|---|---|---|
| FPS Low | >= 30 saat kontrol aktif | pada perangkat uji kelas rendah, dinilai per scene |
| FPS Balanced | target 60 bila mampu | tidak menjamin konstan semua perangkat |
| Frame time 60fps | ~16.7 ms | total JS, render, GPU |
| Frame time 30fps | ~33.3 ms | tidak mengorbankan input responsif |
| Model inti scene mobile | target 1–3 MB transfer | tergantung aset; ukuran final dari benchmark |
| Draw calls | diupayakan <100 | hitung menggunakan `renderer.info.render.calls` |
| Triangle aktif | target awal 75k–150k | bukan batas mutlak; bergantung material/rig |
| Texture primary | 512–1024 untuk low, sampai 2048 terpilih | cek VRAM dan resolusi layar |
| DPR mobile | Low ~0.75–1, Balanced ~1–1.5 | adaptive dan jangan berasumsi DPR fisik |

## Profil Low/Balanced/High
- **Low**: shadow baked, transparansi sederhana, KTX2 512–1K, resolusi rendah, animasi kosmetik dibatasi, opsional tanpa DOF/post-processing.
- **Balanced**: PBR standar, satu HDR environment terkompresi/optimal, shadow hemat, 1K/2K tekstur terpilih.
- **High**: detail geometri/tekstur dan refleksi lebih baik hanya untuk perangkat yang sanggup, tetap batasi draw calls.
- Adaptasi kualitas memakai hysteresis agar tidak naik-turun terus saat FPS berfluktuasi. Catat mode manual user dan automatic fallback.

## Teknik wajib
1. Tidak load Three.js pada beranda/katalog; poster/WebP/AVIF saja.
2. Lazy scene per kategori, jangan import seluruh delapan sekaligus.
3. Use `frameloop="demand"`, `invalidate` ketika perlu; hentikan saat tab hidden.
4. Instancing untuk banyak charm identik, reuse geometry/material, hindari membuat `new Material()` per frame.
5. KTX2 texture compression + Meshopt geometry compression; pastikan transcoder benar-benar terpakai.
6. Resize canvas via ResizeObserver, batasi DPR dan ukuran render buffer.
7. Dispose `geometry`, `material`, `texture`, render targets yang tidak digunakan lagi; hormati asset cache shared refs.
8. Hindari `gl.readPixels`, synchronous framebuffer, shader compile saat drag.
9. Prefetch **satu** kandidat item berikutnya bila jaringan memungkinkan, jangan unduh semua variasi.
10. Pindah scene berkali-kali harus lulus memory stress test, tidak hanya FPS awal.

## Benchmark lab
Device low/medium/high, Android Chrome dan iOS Safari; uji WiFi, 4G throttle, mode hemat daya, setelah perangkat panas, masing-masing scene setidaknya 2 menit dan 20 kali change variant. Catat FPS median, p5, device temp (bila tersedia), `renderer.info`, transfer size, total heap estimate, durasi load hingga interactive.

## Sumber
https://r3f.docs.pmnd.rs/advanced/scaling-performance
https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices
