# 34 Page Templates and Eight Studio Scenes

Public (11): `/`, `/shop`, `/products/:slug`, `/studio`, `/studio/:kind/:productId`, `/cart`, `/checkout`, `/checkout/result`, `/help`, `/about`, `/legal/:slug`.

Auth (4): `/login`, `/register`, `/forgot-password`, `/reset-password`.

Buyer (7): `/account`, `/account/designs`, `/account/wishlist`, `/account/orders`, `/account/orders/:id`, `/account/addresses`, `/account/profile`.

Owner (12): `/owner`, `/owner/orders`, `/owner/orders/:id`, `/owner/products`, `/owner/products/new` (and editor same template), `/owner/components`, `/owner/assets`, `/owner/inventory`, `/owner/payments`, `/owner/customers`, `/owner/reports`, `/owner/settings`.

Studio scene ids (8): `bracelet`, `ring`, `necklace`, `bag-charm`, `phone`, `tablet`, `macbook`, `bottle`.

- Every route uses shared typography/color tokens from `Design Konsep/`.
- Route templates include dynamic paths; dynamic values are not separate templates.
- Owner links render a demo access gate if role has not been chosen in the local demo.
- Actual database-backed owner access control and real checkout remain in the production backlog.
