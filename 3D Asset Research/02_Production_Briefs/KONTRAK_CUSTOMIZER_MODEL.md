# Kontrak Runtime Customizer 3D

## Input minimum
- `kind` = salah satu: bracelet, ring, necklace, bag-charm, phone, tablet, macbook, bottle.
- `deviceModel` = ID spesifik Apple untuk phone/tablet/macbook, kosong untuk lain.
- `color` = HEX pilihan tampilan, diambil dari varian yang valid.
- `caseType` = plain atau clear khusus ponsel.
- `ornament` = heart, star, flower, pearl di demo.
- `placement` = nilai normalisasi 0–100.
- `scale` = 0.55–1.55; `rotation` = 0–360.
- `finger` = 0–4 untuk cincin.
- `pose` = 0–100 untuk sudut tampilan yang tersedia.

## Validasi mutlak sebelum backend produksi
- `deviceModel` harus milik kategori terpilih, bukan arbitrary path.
- Warna diizinkan harus tercantum dalam palette model atau palette casing.
- Metrik harga dihitung server, tidak boleh dipercayakan kepada preview JS.
- Area tempel bukan koordinat layar: simpan UV/material-space atau surface anchor.
- Saat `save`, sertakan `schemaVersion` dan `assetVersion`, serta snapshot pilihan untuk kompatibilitas ke depan.

## Batas demo saat ini
- Untuk stiker, renderer menggambar satu ornamen warna sebagai geometri datar dan simulasi penempelan; belum model multi-layer print-ready.
- `deviceModel` dikelola dalam dropdown kategori terkait; perubahan model me-reset warna ke default resmi perkiraan.
- Casing clear menggunakan overlay alpha sederhana, bukan simulasi transmission PBR.
