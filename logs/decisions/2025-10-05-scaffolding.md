# 2025-10-05 — Jupyter Book scaffolding and CI setup

## Summary
- Added Jupyter Book config: `_config.yml`, `_toc.yml`, and `index.md`.
- Created `environment.yml` for local builds and reproducible runs.
- Added `CODE_OF_CONDUCT.md` and expanded root `README.md` with quickstart and badges.
- Introduced GitHub Actions workflow `.github/workflows/jupyter-book.yml` to build and deploy the site.

## Notes
- Update `repository.url` in `_config.yml` with the correct GitHub repository.
- After merging to `main`, enable GitHub Pages: Source = GitHub Actions.
- The ToC references existing chapters under `01-equations-of-motion/`, `02-conservation-law/`, and `appendices/` without extensions (Jupyter Book resolves `.md`/`.ipynb`).
- Binder/Colab badges use `YOUR_USERNAME`; replace with the real owner/org.

## Next steps
- Add CI job to execute notebooks (nbclient/nbmake) prior to book build.
- Add `glossary.md` and a notation/style guide.
- Create issue templates and PR template; open “help wanted” issues for unfinished chapters.
