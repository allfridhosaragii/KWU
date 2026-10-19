# GitHub Actions: CI/CD, Quality Gates, dan Release

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Workflow file rencana
- `.github/workflows/ci.yml`: install frozen lockfile, lint, typecheck, unit tests, build.
- `.github/workflows/e2e.yml`: preview deployment + Playwright buyer/owner flows, no production PSP.
- `.github/workflows/assets.yml`: validate changed manifests/GLB metadata, ensure budgets and glTF decode.
- `.github/workflows/deploy.yml`: deploy after main merge, environment approvals untuk production.

## Quality gates wajib
| Tahap | Harus lolos |
|---|---|
| PR static | format/lint/typecheck dan secret scan |
| Unit | pricing, design constraint, RBAC, state transitions |
| Integration | DB transaction, webhook idempotency, storage signed URL policy |
| E2E | buyer design→cart→checkout sandbox, owner order processing |
| Asset validation | GLB/manifest sizes, anchor names, dimensions, texture upper limits |
| Performance regression | Web Vitals + FPS device lab berkala, bukan angka palsu di CI headless |

## Secret policy
CI hanya memakai nonproduction secrets; sandbox key disimpan pada Secrets, jangan output. Pull request dari fork tidak boleh mendapat prod credentials. Production deploy memerlukan approval dan health checks.

## Rollback
Simpan versi deploy sebelumnya; DB migration harus backward-compatible bila rollback aplikasi. Aset model memakai versioned URL sehingga rollback manifest tidak menghapus file lama.

## Evidence
Pipeline menyimpan test reports/artifacts dan ringkasan outcome. Jangan memberi status passed jika uji mobile manual belum dijalankan.
