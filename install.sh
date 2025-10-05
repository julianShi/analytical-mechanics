#!/usr/bin/env bash
set -euo pipefail

# Simple installer for Analytical Mechanics notebooks (macOS/Linux)
# Creates a Python virtual environment and installs minimal dependencies.

PYTHON_BIN=${PYTHON_BIN:-python3}
VENV_DIR=${VENV_DIR:-.venv}

REQS=(
  "sympy>=1.12"
  "jupyter>=1.0.0"
  "notebook>=7.0.0"
  "numpy>=1.24.0"
  "matplotlib>=3.7.0"
  "scipy>=1.11.0"
)

command -v "$PYTHON_BIN" >/dev/null 2>&1 || {
  echo "Error: $PYTHON_BIN not found. Install Python 3.10+ first." >&2
  exit 1
}

# Create venv
"$PYTHON_BIN" -m venv "$VENV_DIR"
# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

python -m pip install --upgrade pip
python -m pip install "${REQS[@]}"

echo "\nSuccess! Activate with:"
echo "  source $VENV_DIR/bin/activate"
echo "Then launch Jupyter with:"
echo "  jupyter notebook"
