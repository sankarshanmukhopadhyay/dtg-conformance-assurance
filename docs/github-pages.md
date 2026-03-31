# Publishing docs with GitHub Pages

This repository is Pages-ready using the `/docs` folder as the site source.

## Recommended setup

In GitHub:

1. Go to **Settings → Pages**
2. Under **Build and deployment**
3. Select **Deploy from a branch**
4. Choose:
   - Branch: `main`
   - Folder: `/docs`

GitHub Pages will build a simple Jekyll site from the Markdown files in `/docs`.

## Notes

- The landing page is `docs/index.md`.
- If you do not want Jekyll processing, add a `.nojekyll` file to `/docs`. (Not recommended unless you know why.)

- Experimental profiles that should appear on the docs site need a `/docs` landing page. The AIS-1 profile is surfaced via `docs/ais1-experimental-assurance-profile.md`.
