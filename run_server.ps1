Write-Host "========================================================" -ForegroundColor Cyan
Write-Host " Bahasa Indonesia Knowledge Base - Local Server" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting server at http://localhost:8001 ..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop." -ForegroundColor Yellow
Write-Host ""

$env:PYTHONPATH = "$PSScriptRoot;$env:PYTHONPATH"
$env:PYTHONUTF8 = "1"

$exePath = "$PSScriptRoot\.venv\Scripts\zensical.exe"
if (Test-Path $exePath) {
    & $exePath serve -a localhost:8001
    exit
}

if (Get-Command zensical -ErrorAction SilentlyContinue) {
    zensical serve -a localhost:8001
    exit
}

Write-Host "[ERROR] zensical was not found in .venv." -ForegroundColor Red
Read-Host "Press Enter to exit..."
