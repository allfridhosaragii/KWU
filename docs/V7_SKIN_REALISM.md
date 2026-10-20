# V7 — Realisme anatomi dan pilihan tone kulit

## Diterapkan
- Material PBR kulit dengan albedo sawo matang, normal map mikro, dan roughness map.
- Dasar bentuk anatomi dari mesh MakeHuman CC0 pada pipeline GitHub, bukan hasil scan manusia.
- Lima pilihan tone: Sawo Matang (default), Kuning Langsat, Light Beige, Medium Tan, dan Deep Brown.
- Material kulit dibedakan dari perhiasan agar perubahan warna tidak mengecat logam/ornamen.
- Studio gelang, cincin, dan kalung mempertahankan penyimpanan desain.
- Aset 3D dimuat saat dibutuhkan, rendering berjalan on-demand.

## Pemeriksaan
- TypeScript: berhasil.
- Validasi 21 GLB dan katalog: berhasil pada paket kerja lokal.
- E2E tone kulit pada empat viewport: 64 pemeriksaan berhasil.
- E2E varian perangkat Apple: 105 pemeriksaan berhasil.

## Batas yang belum teruji
Model ini adalah aset 3D artistik yang ditingkatkan, bukan rekonstruksi anatomi 1:1 dari scan medis/fotogrametri. Tidak ada bukti performa 60 FPS pada GPU HP fisik dari lingkungan pengujian ini. Harga, akun, dan transaksi pada GitHub Pages masih demonstrasi.
