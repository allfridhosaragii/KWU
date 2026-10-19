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
