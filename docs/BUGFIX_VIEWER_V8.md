# Bugfix V8: Rotasi tangan 3D dan drag gambar

## Latar belakang
Laporan pengguna 2026-10-20 menunjukkan permukaan tangan bersudut ketika diputar, charm terlihat melayang di depan pergelangan, dan thumbnail transparan muncul saat pointer digeser.

## Perubahan
1. Normal permukaan skin pada vertex duplikat di UV seam digabung berdasarkan posisi spasial, tanpa mengubah bentuk anatomi maupun mesh hard-surface perangkat Apple.
2. Native drag gambar/long-press selection dicegah pada viewer; fallback 2D memakai img draggable=false dan pointer-events:none.
3. Anchor ornamen gelang disesuaikan dengan y=-1.10, z=.355; ukuran ornamen dikurangi agar berada dekat gelang. Anchor liontin diturunkan ke z=.615.
4. pointermove/pointerdown mencegah perilaku native default; lostpointercapture membersihkan state drag.
5. Listener visibilitychange dibersihkan saat viewer dibuang agar tidak menumpuk di setiap navigasi.

## Yang sengaja dipertahankan
- Lima tone kulit, default Sawo Matang.
- Delapan kategori Studio dan 21 model di halaman owner.
- Model GLB dan tekstur PBR saat ini.
- Mode fallback 2D apabila WebGL2 tidak tersedia.

## Pengujian
Patch diuji lokal melalui TypeScript compile, check_site.py untuk 21 model, dan 64 pemeriksaan perubahan tone kulit pada 4 lebar viewport. Perlu pengujian tambahan pada WebGL2 perangkat fisik untuk memverifikasi kehalusan shading saat rotasi dan FPS.
