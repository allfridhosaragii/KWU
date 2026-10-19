# Production Backlog: Required Before Real Sales

## Priority P0: safe business foundation

- Next.js + React/R3F application on server-capable hosting, with shared TypeScript validation, functional backend APIs and error monitoring.
- PostgreSQL + Prisma migrations: `users`, `roles`, `products`, `variants`, `3d_assets`, `components`, `designs`, `cart`, `orders`, `order_items`, `payments`, `shipments`, `inventory_movements`.
- Auth.js or equivalent verified server-side sessions and RBAC; owner must be protected by backend rules, NOT demo role toggles.
- Prices, taxes, shipping, component compatibility, reservations and inventory validated in server transaction. Client may only submit product IDs and design payloads, never a trusted final amount.
- Midtrans sandbox integration, server-created transactions, signature-checked idempotent webhook handler, reconciliation, duplicate prevention, expiration/refund logic. Production keys only in server environment.
- Cloudflare R2 upload management with narrow signed URLs, immutable hashed asset versions, CORS rules and file validation.
- Real courier/shipping rates and tracking or clearly documented manual shipping.
- Privacy policy and contact support with correct real-world company details.

## Priority P1: photoreal and mobile 3D

- Replace primitive GLBs with Blender-sculpted / manufacturer-verified models, e.g. high-quality skinned hand with correct nail proportions and joint hierarchy.
- Physically validated dimensions, mesh normals, UV islands, color-managed PBR materials, roughness/normal maps, optional KTX2 and Meshopt.
- Ring geometry/pose to follow every finger bone; necklace simulation/lightweight constraints; bag charm joints; laptop open/close hinge.
- A production sticker engine: exact UV-space placement, bleed/safe margins, collision zones, separate print-ready file and mm units.
- Move native experimental viewer to Three.js + React Three Fiber, compare real FPS against native renderer.
- LOD, frustum culling, reusable geometry/material, effective DPR adaptivity, context-loss recovery, memory instrumentation.
- Browser tests on real Safari iOS, Android Chrome, iPad Safari, laptop Chromium/Firefox.

## Priority P2: business refinement

- Product CRUD, media asset moderation, variants, bundle offers, design order previews, fulfillment print sheet and refunds.
- Analytics dashboard backed by trusted server-side facts.
- Automated CI: type checking, unit tests, visual snapshots, browser workflows, security and performance gates.
- Image rights/brand review for representations of trademarked devices.

## Definition of production ready

No demo wording, no unverified payment, server authorization enforced, load and performance tests passing, real device GPU verification, real SKU/stock/pricing and actual sample products validated physically.
