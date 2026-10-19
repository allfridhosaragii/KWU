# GitHub Pages Deployment

Repository: `allfridhosaragii/KWU`, default branch `main`.

## Published build

- Static artifacts: `site/`.
- GitHub Pages path: `/KWU/`.
- Script and image base path: detected at runtime (`window.KWU_BASE`).
- Deep links: `site/404.html` contains the application shell and boots the route for client-side rendering. Direct visits may technically return HTTP 404 before SPA rendering; a server-capable host with rewrite rules solves this.
- Workflow: `.github/workflows/pages.yml` uses official Pages upload/deploy actions.

## Activation

1. Open repository **Settings → Pages**.
2. Select **GitHub Actions** as the build/deployment source.
3. Open **Actions** and run `Publish KWU demo to GitHub Pages` if it has not run automatically.
4. Inspect workflow logs for build and deploy success.
5. Open `https://allfridhosaragii.github.io/KWU/` and perform device checks.

The GitHub connector may not have permissions to modify GitHub Pages settings. If Pages is disabled, the workflow and files can be pushed but activation requires the repository owner.

## Domain and security

Use HTTPS. There are no secrets in the frontend. Do not commit payment keys. Real production architecture must be hosted separately and must not trust localStorage for authorization or payment state.


## First deployment attempt result (20 Oct 2026)

GitHub Actions run \`39304564764\` finished with \`validate=success\`, \`deploy=failure\`. The failed step was \`actions/configure-pages@v5\` with \`Get Pages site failed: Not Found\`. This confirms repository Pages has not been activated. Source compilation CI run \`39304564663\` finished successfully.

The owner must open **Settings → Pages → Build and deployment → Source → GitHub Actions**, save, and rerun the failed deployment workflow. The GitHub App available to the assistant cannot enable repository Pages settings. Until this is done, \`https://allfridhosaragii.github.io/KWU/\` is a target URL, not a verified live site.
