# Runbook Operasional, Backup, dan Recovery

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Insiden prioritas 1
Website tidak dapat checkout, role data bocor, webhook memproses pembayaran ganda, atau order paid hilang. Hentikan operasi berisiko melalui flag/maintenance, pertahankan bukti log, batasi akses, identifikasi penyebab, koreksi data melalui transaksi audit dan umumkan status secara proporsional.

## Prioritas 2
CDN GLB 404, satu scene crash, preview berbeda atau performance regression. Aktifkan poster 2D fallback atau roll back asset manifest, pertahankan checkout non-3D bila aman dan sesuai komitmen produk.

## Backup
DB daily snapshot dan backup sebelum migration besar; atur retensi sesuai kebutuhan/aturan bisnis. Uji **restore**, bukan hanya cek file backup tersedia. Aset immutable versioned perlu backup/retensi matching order history. Dokumentasikan RPO/RTO sesuai kemampuan operasional sesungguhnya.

## Payment recovery
Jika webhook gagal: lihat event table, validasi manual dengan provider status API server-to-server, jalankan reconciliation idempotent. Jangan mengubah DB langsung melalui console tanpa audit koreksi.

## Rollback
Deployment sebelumnya dapat dipulihkan, DB schema kompatibel mundur selama release transition, asset manifest previous version tersedia. Bila migrasi irreversible, siapkan forward fix dan backup restore plan.

## Alert hygiene
Alert yang relevan: request 5xx rate, PSP webhook rejected/signature anomaly, payment stuck pending, DB errors, asset upload failure, 3D context lost spike. Data pengguna sensitif tidak boleh masuk error reporter.
