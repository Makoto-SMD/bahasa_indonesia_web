[CmdletBinding()]
param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$TargetPaths
)

$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$djlintPath = Join-Path $ScriptDir ".venv\Scripts\djlint.exe"

if (-not (Test-Path $djlintPath)) {
    Write-Host "[ERROR] djlint not found in .venv." -ForegroundColor Red
    Write-Host "Please run: .\.venv\Scripts\pip.exe install djlint" -ForegroundColor Yellow
    exit 1
}

if (-not $TargetPaths -or $TargetPaths.Count -eq 0) {
    $TargetPaths = @("site")
}

Write-Host "Formatting HTML files: $($TargetPaths -join ' ')..." -ForegroundColor Cyan
& $djlintPath $TargetPaths --reformat

if ($LASTEXITCODE -eq 0) {
    Write-Host "Formatting completed successfully." -ForegroundColor Green
} else {
    Write-Host "Formatting completed with code $LASTEXITCODE."
}
