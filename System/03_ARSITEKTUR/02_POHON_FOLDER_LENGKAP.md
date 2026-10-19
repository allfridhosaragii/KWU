# Pohon Folder dan Inventaris File Implementasi

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

> Daftar ini merupakan **target file**, belum dibuat pada root repo. File `System/*.md` adalah dokumen, bukan source code siap jalan.

```text
KWU/
├── .github/
│   ├── workflows/{ci,e2e,assets,deploy}.yml
│   ├── CODEOWNERS
│   └── PULL_REQUEST_TEMPLATE.md
├── apps/
│   └── web/
│       ├── public/{images,icons,posters}/
│       ├── src/
│       │   ├── app/
│       │   │   ├── (store)/
│       │   │   │   ├── page.tsx
│       │   │   │   ├── shop/page.tsx
│       │   │   │   ├── products/[slug]/page.tsx
│       │   │   │   ├── studio/page.tsx
│       │   │   │   ├── studio/[type]/[productId]/page.tsx
│       │   │   │   ├── cart/page.tsx
│       │   │   │   ├── checkout/page.tsx
│       │   │   │   ├── checkout/result/page.tsx
│       │   │   │   ├── help/page.tsx
│       │   │   │   ├── about/page.tsx
│       │   │   │   └── legal/[slug]/page.tsx
│       │   │   ├── (auth)/{login,register,forgot-password,reset-password}/page.tsx
│       │   │   ├── (account)/account/
│       │   │   │   ├── page.tsx
│       │   │   │   ├── designs/page.tsx
│       │   │   │   ├── wishlist/page.tsx
│       │   │   │   ├── orders/page.tsx
│       │   │   │   ├── orders/[id]/page.tsx
│       │   │   │   ├── addresses/page.tsx
│       │   │   │   └── profile/page.tsx
│       │   │   ├── (owner)/owner/
│       │   │   │   ├── layout.tsx
│       │   │   │   ├── page.tsx
│       │   │   │   ├── orders/page.tsx
│       │   │   │   ├── orders/[id]/page.tsx
│       │   │   │   ├── products/page.tsx
│       │   │   │   ├── products/new/page.tsx
│       │   │   │   ├── products/[id]/edit/page.tsx
│       │   │   │   ├── components/page.tsx
│       │   │   │   ├── assets/page.tsx
│       │   │   │   ├── inventory/page.tsx
│       │   │   │   ├── payments/page.tsx
│       │   │   │   ├── customers/page.tsx
│       │   │   │   ├── reports/page.tsx
│       │   │   │   └── settings/page.tsx
│       │   │   ├── api/
│       │   │   │   ├── auth/[...nextauth]/route.ts
│       │   │   │   ├── payment/create/route.ts
│       │   │   │   ├── payment/webhook/route.ts
│       │   │   │   ├── assets/sign-upload/route.ts
│       │   │   │   ├── designs/[id]/route.ts
│       │   │   │   └── health/route.ts
│       │   │   ├── layout.tsx
│       │   │   ├── error.tsx
│       │   │   ├── not-found.tsx
│       │   │   ├── loading.tsx
│       │   │   └── globals.css
│       │   ├── components/{layout,navigation,products,feedback,shared}/
│       │   ├── features/
│       │   │   ├── auth/
│       │   │   ├── catalog/
│       │   │   ├── customizer/
│       │   │   │   ├── components/{CustomizerClient,StudioCanvas,MobileControlSheet}.tsx
│       │   │   │   ├── store/customizer.store.ts
│       │   │   │   └── hooks/{useAutosave,useCustomizer}.ts
│       │   │   ├── cart/
│       │   │   ├── checkout/
│       │   │   ├── account/
│       │   │   └── owner/
│       │   ├── server/
│       │   │   ├── dal/{user,product,design,order}.ts
│       │   │   ├── actions/{cart,design,checkout}.ts
│       │   │   ├── services/{payment,asset,report}.ts
│       │   │   └── policies/{authorize,rateLimit}.ts
│       │   └── lib/{auth,env,storage,utils}.ts
│       ├── package.json
│       ├── next.config.ts
│       ├── eslint.config.mjs
│       └── tsconfig.json
├── packages/
│   ├── ui/src/{components,tokens,icons}/
│   ├── three-core/src/
│   │   ├── renderer/{ProductCanvas,RendererFallback,RendererEvents}.tsx
│   │   ├── camera/{ProductCamera,CameraController,CameraPresets}.ts(x)
│   │   ├── controls/{OrbitController,GestureController,DragController,TransformController}.ts(x)
│   │   ├── selection/{RaycastService,ObjectSelector}.ts
│   │   ├── rigging/{RigController,BoneController,PoseController,AttachmentResolver}.ts
│   │   ├── materials/{MaterialLibrary,MetalMaterial,SkinMaterial,PlasticMaterial}.ts
│   │   ├── lighting/{StudioLighting,EnvironmentMap,ShadowController}.ts(x)
│   │   ├── assets/{AssetLoader,AssetCache,AssetManifest,AssetDisposer,ModelPreloader}.ts
│   │   ├── optimization/{DeviceProfiler,QualityManager,FrameScheduler,VisibilityManager}.ts
│   │   ├── constraints/{AnchorConstraint,SurfaceConstraint,CollisionConstraint,TransformLimits}.ts
│   │   └── math/{coordinates,transforms,dimensions}.ts
│   ├── three-customizers/src/
│   │   ├── shared/{CustomizerScene,PresetApplicator,DesignSerializer,DesignHydrator,UndoRedoManager}.ts(x)
│   │   ├── jewelry/
│   │   │   ├── bracelet/{BraceletScene,HandMannequin,CharmRail,BraceletController}.ts(x)
│   │   │   ├── ring/{RingScene,FingerAnchors,FingerPoseController,RingController}.ts(x)
│   │   │   ├── necklace/{NecklaceScene,NeckMannequin,ChainController,PendantController}.ts(x)
│   │   │   └── bag-charm/{BagCharmScene,BagModel,HookAnchors,CharmController}.ts(x)
│   │   └── stickers/
│   │       ├── shared/{StickerRenderer,StickerEditor,UVPlacement,PrintableZone,SafeMargin}.ts(x)
│   │       ├── phone/{PhoneScene,CaseSwitcher,CaseColorController}.ts(x)
│   │       ├── tablet/{TabletScene,TabletSurface}.ts(x)
│   │       ├── macbook/{MacBookScene,HingeController,LidSurface}.ts(x)
│   │       └── bottle/{BottleScene,BottleColorController,CylindricalUVMapper}.ts(x)
│   ├── contracts/src/{auth,products,designs,orders,payments,assets}.schema.ts
│   ├── commerce/src/
│   │   ├── catalog/{product,category,variant}.service.ts
│   │   ├── pricing/{price-calculator,price-rules,price-quote}.ts
│   │   ├── cart/{cart.service,cart-validator}.ts
│   │   ├── inventory/{stock-reservation,inventory.service}.ts
│   │   ├── checkout/{checkout.service,checkout-validator}.ts
│   │   ├── orders/{order.service,order-snapshot,order-status}.ts
│   │   ├── payments/{midtrans.service,webhook-handler,payment-verifier}.ts
│   │   ├── production/{production-sheet,production-status}.ts
│   │   └── shipping/shipment.service.ts
│   ├── database/
│   │   ├── prisma/{schema.prisma,migrations/,seed.ts}
│   │   └── src/{client.ts,queries/,transactions/}
│   └── config/{typescript,eslint}/
├── assets/
│   ├── source/{mannequins,jewelry,devices,objects,ornaments,stickers}/
│   ├── manifests/{mannequins,jewelry,devices,ornaments,stickers}.json
│   ├── presets/{bracelet,ring,necklace,bag-charm,sticker}-presets.json
│   └── optimization/{quality-budgets,texture-profiles,asset-rules}.json
├── scripts/{optimize-assets,validate-assets,generate-previews,publish-assets}.ts
├── tests/{e2e,integration,visual,performance,security}/
├── infra/{docker,storage,monitoring}/
├── .env.example
├── .gitignore
├── package.json
├── pnpm-workspace.yaml
├── pnpm-lock.yaml
├── turbo.json
└── README.md
```

## Konvensi penting
Notasi `{fileA,fileB}` merupakan ringkasan dokumentasi, **bukan nama file literal**. Buat file aktual per item; `.ts(x)` berarti pilih `.ts` atau `.tsx` sesuai implementasi. `packages/*` harus memiliki `package.json` dan entrypoint. Folder kosong tidak otomatis ter-commit oleh Git.

## Keputusan unik
- Nama `Design Konsep` **tetap** dan jangan dipindah ketika membuat `System`.
- UI route studio `/studio/[type]/[productId]` konsisten dengan 34 halaman dalam dokumen desain, jangan ubah menjadi `/customize` tanpa memperbarui sitemap.
- API pembayaran ditulis `/api/payment/*` agar tidak ganda dengan `/api/payments/*`; status internal pembayaran tetap domain `payments`.
- Worker `apps/worker` belum diciptakan sebagai deployment sampai butuh antrean.
