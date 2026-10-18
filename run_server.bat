@echo off
setlocal
cd /d "%~dp0"

echo ========================================================
echo  Bahasa Indonesia Knowledge Base - Local Server
echo ========================================================
echo.
echo Starting server at http://localhost:8001 ...
echo Press Ctrl+C to stop.
echo.

set PYTHONPATH=%CD%;%PYTHONPATH%
set PYTHONUTF8=1

if exist ".venv\Scripts\zensical.exe" (
    ".venv\Scripts\zensical.exe" serve -a localhost:8001
    exit /b
)

where zensical >nul 2>nul
if %errorlevel% equ 0 (
    zensical serve -a localhost:8001
    exit /b
)

echo [ERROR] zensical could not be found in .venv.
pause
