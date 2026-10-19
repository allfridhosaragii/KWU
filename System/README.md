# SYSTEM — KWU Digital Atelier

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Tujuan dokumen
Folder `System/` merupakan **single source of truth untuk keputusan engineering** website KWU: e-commerce mobile-first dengan 3D customizer yang realistis dan tetap efisien untuk perangkat menengah. Dokumen ini mengarahkan pengembangan; **bukan klaim kode sudah dibuat, layanan sudah terpasang, atau performa sudah terbukti**.

## Kontrak produk yang tidak boleh berubah diam-diam
- Tepat dua jenis akun: `BUYER` dan `OWNER`. Guest boleh menjelajah katalog, sedangkan menyimpan desain ke akun dan checkout memerlukan autentikasi pada rancangan awal.
- Delapan tipe customizer: gelang, cincin lima jari, kalung, gantungan tas, stiker HP dengan casing polos/transparan, stiker tablet Apple, stiker MacBook, stiker botol stainless hitam/abu-abu.
- Sistem **hybrid preset + custom bebas terikat aturan fisik**: objek tidak boleh melayang, overlap yang dilarang, atau keluar dari area produksi.
- Dua kelompok barang dagangan: aksesori dan stiker. HP/tablet/MacBook/botol menjadi **media tampilan** kecuali owner secara eksplisit menambahkannya sebagai SKU dengan stok dan harga. Casing juga tidak otomatis dijual.
- Template UI: **34** (11 publik, 4 auth, 7 akun buyer, 12 owner). Banyaknya URL dapat lebih besar karena satu template dapat melayani beberapa URL dan delapan tipe studio.
- Bahasa UI dan dokumen: Indonesia; harga rupiah/IDR; zona waktu operasional Asia/Jakarta; waktu disimpan UTC di database.
- Rancangan visual **harus mengikuti** folder saudara [`../Design Konsep/`](../Design%20Konsep/README.md), khususnya warna, tipografi, navigasi, aksesibilitas, dan per-page behavior.

## Keputusan teknologi rekomendasi
**TypeScript** utama untuk full-stack, React + Next.js App Router, Tailwind CSS, React Three Fiber + Three.js + Drei, Zustand untuk state editor, Blender untuk authoring aset, GLB/glTF 2.0 + Meshopt/KTX2 untuk distribusi, PostgreSQL + Prisma, Zod, Auth.js, Midtrans Sandbox, Cloudflare R2/CDN, pnpm workspaces + Turborepo, Vitest + Playwright, CI GitHub Actions. Tidak memerlukan Laravel, Express API mandiri, atau Next.js dan Laravel sekaligus pada MVP.

## Cara membaca
1. `00_MASTER_INDEX.md`, `01_FONDASI/01_KEPUTUSAN_DAN_NON_GOALS.md`, `02_BAHASA_DAN_STACK/01_BAHASA_PEMROGRAMAN.md`.
2. `03_ARSITEKTUR/01_MONOREPO_DAN_ATURAN_PACKAGE.md`, `03_ARSITEKTUR/02_POHON_FOLDER_LENGKAP.md`.
3. `04_ENGINE_3D/` sebelum menulis customizer apapun, lalu `05_BISNIS_BACKEND/` untuk transaksi.
4. `06_KUALITAS_OPERASIONAL/` untuk test, keamanan, deployment, dan acceptance gate.
5. `07_RUJUKAN_DAN_KEPUTUSAN/` mencatat justifikasi dan sumber resmi.

## Definisi selesai
Dokumen dianggap siap implementasi jika istilah konsisten dengan `Design Konsep`; kontrak data dan hak akses jelas; rute dan paket tidak menggandakan tanggung jawab; setiap kategori 3D punya kontrak input/output; setiap risiko mempunyai pengujian; harga dan stok ditegakkan server. **Benchmark FPS dan Core Web Vitals adalah target, bukan hasil.**

## Prinsip biaya dan skalabilitas
Mulai satu aplikasi Next.js + database + R2. **Worker terpisah**, antrean, dan physics engine bukan kebutuhan awal; tambah setelah ada pengukuran beban atau kebutuhan proses asinkron yang nyata. Mode sandbox pembayaran dahulu sebelum koneksi produksi.
