@echo off
setlocal
cd /d "%~dp0"

set PYTHONUTF8=1

if not exist ".venv\Scripts\djlint.exe" (
    echo [ERROR] djlint could not be found in .venv.
    echo Please run: .\.venv\Scripts\pip.exe install djlint
    pause
    exit /b 1
)

if "%~1"=="" (
    echo Formatting HTML files in site/ ...
    ".venv\Scripts\djlint.exe" site --reformat
) else (
    echo Formatting %* ...
    ".venv\Scripts\djlint.exe" %* --reformat
)

echo Done.
