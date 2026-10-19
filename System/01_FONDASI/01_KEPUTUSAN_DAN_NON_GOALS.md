# Keputusan Pokok, Batas Proyek, dan Non-Goals

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Tujuan fungsional
1. Buyer mencari produk, memilih variasi, mengustomisasi secara 3D, menyimpan desain, memasukkan konfigurasi ke cart, checkout, melihat riwayat, dan melacak status.
2. Owner mengelola produk, kategori, preset, komponen, model GLB, titik pemasangan, stok, pembayaran, pesanan, produksi, pelanggan dan laporan.
3. Status desain, harga dan pesanan konsisten sejak preview sampai owner menerima spesifikasi produksi.
4. UX memprioritaskan layar sentuh 320–430 px, kemudian tablet/desktop.

## Sumber kebenaran
- `Design Konsep` = semua keputusan antarmuka, urutan konten, warna, tipografi, copy dan gesture yang terlihat.
- `System` = keputusan teknis, folder kode, kontrak, security, API, data, asset pipeline, performance, deployment.
- Katalog/varian/stok/price rule milik database dan commerce server; UI tidak menyimpan harga final sebagai otoritas.
- Aturan area valid 3D dipublikasikan sebagai metadata berversi; editor melakukan validasi cepat dan server mengecek ulang.

## Keputusan arsitektur yang dipilih
- **Modular monolith** pada Next.js App Router, bukan microservices. Monorepo digunakan untuk batas modul dan kemungkinan scaling.
- **WebGL 2** sebagai jalur produksi default; WebGPU dipelajari terpisah, tidak menjadi dependensi rilis mobile.
- 3D dijalankan hanya dalam Client Component yang dimuat malas di route studio atau preview detail pesanan saat diminta.
- Rigging tulang dan animasi terbatas, bukan simulasi fisika full-body; gerak rantai dibatasi agar ringan.
- Sticker placement: UV surface sebagai kontrak penyimpanan; DecalGeometry hanya opsi tampilan pada area hampir datar.
- `Auth.js` memudahkan sesi. Password email/credential perlu desain provider dan verifikasi aman; akun OWNER dibuat oleh proses administrasi, bukan register publik.
- Aset GLB/texture dilayani melalui public CDN yang terversi; desain privat dan data pengguna jangan berada pada public bucket.

## Non-goals MVP
- AR kamera langsung, face/hand tracking live, multiplayer editor, undo tanpa batas, photoreal ray tracing, 3D setiap kartu katalog, AI pembuat model, marketplace multi-owner, multi-currency, aplikasi iOS native, pembayaran produksi tanpa uji sandbox.
- Semua 34 halaman harus terdokumentasi, tetapi implementasi bertahap diperbolehkan dengan prioritas funnel kritis.

## Risiko bisnis
- Preview bukan jaminan ukuran nyata; perbedaan layar dan pencahayaan dapat memengaruhi persepsi warna.
- Cincin pada jari berbeda harus sesuai ukuran kompatibel; ukuran aktual ditentukan dari SKU/size chart.
- Stiker yang dibeli harus jelas kuantitas, bahan, ukuran cetak, dan cara pemasangan. Media preview bukan otomatis bagian transaksi.
