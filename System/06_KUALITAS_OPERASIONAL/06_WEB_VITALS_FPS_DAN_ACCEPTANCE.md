# Target Performa, Benchmark, dan Gate Rilis

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Web Core Vitals
Untuk publik/commerce, target `LCP <= 2.5s`, `INP <= 200ms`, `CLS <= 0.1` pada persentil 75. Ini nilai good thresholds standar; diuji via CrUX/RUM atau lapangan setelah ada trafik, dan lab Lighthouse sebagai sinyal. Saat belum ada data nyata, tulis 'belum diukur'.

## Metrik customizer 3D
| Metrik | Target awal | Alat |
|---|---|---|
| Interactive-ready studio | diukur per kelas jaringan dan category | Performance API + custom mark |
| Frame rate aktif low | >= 30 FPS dengan kualitas Low di device target | profiler device nyata |
| Frame rate balanced | mendekati 60 FPS bila device mampu | profiler iOS/Android |
| Drawcall & triangle budget | target <100 calls dan 75k–150k tris mobile | renderer.info |
| Context recovery | preview 2D atau restore tidak menghilangkan desain | manual stress |
| Memory after 30 scene switches | tidak terus naik tanpa batas, lihat GC | device profiler |
| Battery and heat | tidak membuat frame loop idle terus aktif | observation + profiler |

## Batas klaim
Ukuran aset 1–3MB dan 30/60 FPS adalah **budget pengembangan**, bukan klaim semua device. Matrik budget boleh dinaikkan/diturunkan berdasarkan bukti dan bukti revisi disimpan.

## Test matrix
- Viewport: 320, 360, 375, 390, 430, 768, 1024, 1440 CSS px.
- Device: setidaknya satu Android midrange/low dan satu iPhone nyata.
- Browser: Chrome Android, Safari iOS, Chrome desktop, Edge; perhatikan iOS WebGL restrictions.
- Network: WiFi, 4G throttled, offline sementara, reload setelah timeout.
- Scenes: semua 8; rotate, pinch, placement, save, reload, cart, owner replay.

## Release gate
Tidak boleh rilis jika: checkout dapat dibypass nominal, owner role dapat diakses buyer, order preview tidak cocok konfigurasi, 3D menyebabkan crash konsisten di device target, tidak ada 2D fallback, error pesan kosong, storage private leakage.

## Sumber
https://web.dev/articles/vitals
https://r3f.docs.pmnd.rs/advanced/scaling-performance
