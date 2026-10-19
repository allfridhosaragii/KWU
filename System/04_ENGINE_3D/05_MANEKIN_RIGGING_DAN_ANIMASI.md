# Rigging Manekin Tangan, Jari, Leher, dan Pose

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Kebutuhan bentuk
- `HandMannequin`: tangan sampai pergelangan/lengan sedikit; skeleton mencakup wrist dan tulang lima jari yang digunakan untuk anchor cincin.
- `NeckMannequin`: bagian leher dan bahu, rig minimal untuk pose yaw/pitch terbatas, tidak ada skinning kompleks yang tidak terlihat.
- Animasi bukan sekadar putar mesh: user dapat memutar kamera independen dan memilih pose rig. Keputusan ini penting untuk menjaga posisi produk menempel.

## Hierarki rig yang direkomendasikan
```text
root
└── armature_hand
    ├── wrist
    ├── thumb_{1,2,3}
    ├── index_{1,2,3}
    ├── middle_{1,2,3}
    ├── ring_{1,2,3}
    └── pinky_{1,2,3}
```
Anchor cincin dipasang pada bone/spatial transform yang benar, bukan ke screen pixel. Gelang mengikuti wrist dengan offset ke area pergelangan, tanpa deformation gelang yang tidak realistis.

## Pose
Preset: neutral/front/side/palm-relaxed (untuk tangan), neutral/left/right (leher). Motion range dibatasi agar cincin tidak tembus kulit dan rantai tidak memotong bahu. Setelah pose berubah, update world matrix, transform anchor, re-evaluate collision dan request redraw.

## SkinnedMesh
Skinning untuk manekin hanya; charm/cincin biasanya rigid object yang terikat bone transform/anchor. Jangan skinning semua charm karena mahal dan tidak diperlukan.

## Detail ergonomi
User tap jari → highlight ring anchor dan gerakkan kamera, pilih satu jari, cek ring size. Bila UI memindah cincin ke jari lain, desain perlu menyimpan `fingerId` dan size compatibility.

## Test
Semua pose dengan semua jari, zoom maksimum, attach/detach 50 kali, rotate camera+pose bersamaan, GPU asset cleanup, fallback screenshot; tidak boleh ada floating ring, skin popping mencolok atau culling terbalik.
