# Cloudflare R2, CDN, Signed Upload, dan Akses Privat

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Klasifikasi aset
| Data | Akses | Lokasi |
|---|---|---|
| GLB katalog public | publik read | public R2 bucket dengan custom domain/CDN |
| Poster katalog/product foto | publik read | CDN |
| Thumbnail desain buyer private | restricted | private bucket/key dengan signed access atau proxy |
| File master stiker milik buyer | private | private R2 bucket |
| Data order/PII | DB private | bukan CDN |
| `.blend` master modeling | terbatas developer | Git LFS/private storage; jangan pada public CDN |

## Upload pipeline
Owner mengirim request sign ke backend → server check OWNER/allowlist file/size/quota → buat presigned PUT pendek dan key acak → browser upload langsung ke R2 → server verifikasi metadata/object → asset processing/validation → publish manifest immutable. Jangan mengambil path dari input user sebagai key final.

## CDN
Attach custom domain ke R2 bucket untuk caching Cloudflare. `.r2.dev` bukan pilihan cache/WAF setara custom domain. Tetapkan `Content-Type`, CORS spesifik origin aplikasi, security headers, immutable hashed key, dan cache policy untuk `.glb`, `.ktx2`, `.webp`.

## Validasi file
Periksa ekstensi dan MIME serta magic/parse konten, dimensi/vertices/texture budget, sanitizer SVG jika dibolehkan, scanning bila layanan tersedia. Jangan percaya nama file. Rate-limit uploads.

## Privasi dan retensi
Hapus desain pengguna sesuai kebijakan produk dan kewajiban transaksi; order snapshot tetap sesuai periode retensi yang sah. Private preview tidak boleh bisa dibaca pembeli lain melalui guessable URL.

## Sumber
https://developers.cloudflare.com/cache/interaction-cloudflare-products/r2/
https://developers.cloudflare.com/r2/
