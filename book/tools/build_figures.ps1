$ErrorActionPreference = "Stop"
$Source = Join-Path $PSScriptRoot "../figures/sources"
$Output = Join-Path $PSScriptRoot "../figures/generated"
New-Item -ItemType Directory -Force $Output | Out-Null

Push-Location $Source
try {
    latexmk -pdf -interaction=nonstopmode -halt-on-error tangent-line.tex
    latex -interaction=nonstopmode -halt-on-error tangent-line.tex
    dvisvgm --no-fonts -o "$Output/tangent-line.svg" tangent-line.dvi
    Copy-Item tangent-line.pdf "$Output/tangent-line.pdf" -Force
}
finally { Pop-Location }
