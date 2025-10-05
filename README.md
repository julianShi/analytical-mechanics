# Analytical Mechanics

[![Build Book](https://github.com/julianShi/analytical-mechanics/actions/workflows/jupyter-book.yml/badge.svg)](https://github.com/julianShi/analytical-mechanics/actions/workflows/jupyter-book.yml)

Open textbook for teaching Analytical Mechanics with reproducible notebooks and interactive visualizations.

## Quickstart

- View the site: (will appear after first successful deploy)
- Run locally:
  ```bash
  conda env create -f environment.yml  # or: pip install -r requirements.txt
  conda activate analytical-mechanics
  jupyter-book build .
  python -m http.server -d _build/html 8000
  ```

## Launch online

- Binder: [Launch Binder](https://mybinder.org/v2/gh/julianShi/analytical-mechanics/HEAD)
- Colab: open notebooks from the repo directly in Colab.

## Contributing

We welcome contributions! Please see `CONTRIBUTING.md` and adhere to the `CODE_OF_CONDUCT.md`.

### Style

- Use MyST Markdown (`.md`) for chapters; Jupyter notebooks (`.ipynb`) are supported.
- Use consistent notation; add terms to `glossary.md` (to be added).
- Include 3–5 exercises per chapter where possible.

## License

- Text and figures: CC‑BY 4.0
- Code: MIT
