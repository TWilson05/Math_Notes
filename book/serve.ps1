param(
    [int]$Port = 8765,
    [switch]$SkipBuild
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "prototypes/.venv/Scripts/python.exe"
$Output = Join-Path $PSScriptRoot "_build/html"

if (-not (Test-Path $Python)) {
    throw "Create prototypes/.venv first; see CONTRIBUTING.md"
}

if (-not (Test-Path (Join-Path $PSScriptRoot "figures/generated/tangent-line.svg"))) {
    Write-Host "Generated figure assets are missing; building them first."
    & powershell -ExecutionPolicy Bypass -File (Join-Path $PSScriptRoot "tools/build_figures.ps1")
    if ($LASTEXITCODE -ne 0) {
        throw "Figure generation failed. Install LaTeX, latexmk, and dvisvgm, then try again."
    }
}

if (-not $SkipBuild) {
    & $Python -m sphinx -W --keep-going -b html $PSScriptRoot $Output
    if ($LASTEXITCODE -ne 0) {
        throw "The Sphinx build failed."
    }
}

Write-Host "Serving the textbook at http://127.0.0.1:$Port"
Write-Host "Press Ctrl+C to stop the server."
& $Python -m http.server $Port --bind 127.0.0.1 --directory $Output
