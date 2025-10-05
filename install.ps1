# Simple installer for Analytical Mechanics notebooks (Windows PowerShell)
# Creates a Python virtual environment and installs minimal dependencies.
Param(
  [string]$PythonBin = "py",
  [string]$VenvDir = ".venv"
)

# Check Python
$pythonFound = $false
try {
  & $PythonBin -V | Out-Null
  $pythonFound = $true
} catch {
  $pythonFound = $false
}
if (-not $pythonFound) {
  Write-Error "Python not found. Install Python 3.10+ and ensure '$PythonBin' is on PATH."
  exit 1
}

# Create venv
& $PythonBin -m venv $VenvDir

# Activate venv
$activate = Join-Path $VenvDir "Scripts/Activate.ps1"
if (-not (Test-Path $activate)) {
  Write-Error "Failed to locate venv activation script at $activate"
  exit 1
}
. $activate

# Install packages
$reqs = @(
  'sympy>=1.12',
  'jupyter>=1.0.0',
  'notebook>=7.0.0',
  'numpy>=1.24.0',
  'matplotlib>=3.7.0',
  'scipy>=1.11.0'
)
python -m pip install --upgrade pip
python -m pip install @reqs

Write-Host "`nSuccess! Activate with:" -ForegroundColor Green
Write-Host "  . $activate"
Write-Host "Then launch Jupyter with:"
Write-Host "  jupyter notebook"
