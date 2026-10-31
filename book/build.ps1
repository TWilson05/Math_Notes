param(
    [ValidateSet("html", "latex", "pdf", "check")]
    [string]$Target = "html"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Python = Join-Path $Root "prototypes/.venv/Scripts/python.exe"
if (-not (Test-Path $Python)) { throw "Create prototypes/.venv first; see CONTRIBUTING.md" }

switch ($Target) {
    "html" { & $Python -m sphinx -W --keep-going -b html "$PSScriptRoot" "$PSScriptRoot/_build/html" }
    "latex" { & $Python -m sphinx -W --keep-going -b latex "$PSScriptRoot" "$PSScriptRoot/_build/latex" }
    "pdf" {
        & $Python -m sphinx -W --keep-going -b latex "$PSScriptRoot" "$PSScriptRoot/_build/latex"
        & latexmk -pdf -interaction=nonstopmode -halt-on-error mathematics-notes.tex
    }
    "check" {
        & $Python "$PSScriptRoot/tools/validate_differential.py"
        & $Python -m sphinx -W --keep-going -b html "$PSScriptRoot" "$PSScriptRoot/_build/html"
        & $Python "$PSScriptRoot/tools/validate_book.py"
        & $Python -m sphinx -W --keep-going -b latex "$PSScriptRoot" "$PSScriptRoot/_build/latex"
    }
}
