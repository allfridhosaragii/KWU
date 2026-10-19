# Kontrak Data Desain 3D dan Migration

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Model desain konseptual
```json
{
  "schemaVersion": 1,
  "designId": "dsg_uuid",
  "productId": "bracelet-001",
  "variantId": "silver-M",
  "studioType": "bracelet",
  "assetVersion": "v1",
  "rulesVersion": 1,
  "presetId": "classic-silver",
  "elements": [
    {
      "id": "el_001",
      "componentId": "charm-heart",
      "anchorId": "bracelet-track",
      "placement": {"kind":"track","t":0.35,"rotationRadians":0,"scale":1}
    }
  ],
  "preview": {"thumbnailAssetId":"img_001"}
}
```

## Jenis koordinat berbeda
- `track`: parameter `t` 0..1 sepanjang jalur gelang/rantai.
- `anchor`: `anchorId` dan local offset terbatas (misal jari, kait tas).
- `surface_uv`: `u`, `v` ternormalisasi 0..1, rotasi radian, widthMm/heightMm untuk stiker; surface memiliki zone mask berversi.
- Jangan menyimpan `screenX/screenY` sebagai koordinat produksi. Resolusi dan aspek berubah antar perangkat.

## Wajib ada di schema
`designId`, `ownerUserId`, `schemaVersion`, `assetVersion`, `rulesVersion`, `productId`, `variantId`, `elements`, timestamps, `revision` untuk optimistic concurrency. Payload memiliki limit jumlah elemen. Jangan hanya simpan JSON jika laporan owner butuh query sering: simpan item komponen yang terindeks juga.

## Versioning/migrasi
- Saat membuka versi lama: `DesignMigrator(versionOld → versionNew)` mengubah bentuk schema yang valid.
- Jika model atau aturan pemasangan berubah dan tidak bisa dipetakan, desain tampil sebagai archived view dan pengguna diminta memilih preset pengganti, **tidak mengubah desain diam-diam**.
- Order snapshot tetap menunjuk data dan file versi saat transaksi, termasuk price breakdown dan production dimensions.
- Validasi server menggunakan metadata rule yang sesuai assetVersion dan rulesVersion.

## Konflik autosave
Client mengirim `revision` dan menerima revisi baru. Konflik memunculkan opsi muat versi terakhir/duplikat; tidak overwrite diam-diam dari perangkat lain. Autosave debounce, perubahan lokal tetap disimpan sementara bila offline (dengan pertimbangan privasi).
