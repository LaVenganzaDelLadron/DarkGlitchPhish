#!/bin/bash

# Enhanced WhPhisher - Optional Dependencies Installer
# This script installs optional Python packages for enhanced features

echo "=================================="
echo "WhPhisher Enhanced - Dependencies"
echo "=================================="
echo ""

# Check Python version
if command -v python3 &> /dev/null; then
    PYTHON=python3
    PIP=pip3
elif command -v python &> /dev/null; then
    PYTHON=python
    PIP=pip
else
    echo "[ERROR] Python is not installed!"
    exit 1
fi

echo "[*] Python found: $PYTHON"
echo ""

# Install QR Code library
echo "[+] Installing QR Code library..."
$PIP install qrcode[pil] 2>&1 | grep -v "already satisfied" || echo "[✓] QR Code library ready"

echo ""
echo "=================================="
echo "[✓] Installation Complete!"
echo "=================================="
echo ""
echo "Features enabled:"
echo "  ✓ QR Code generation"
echo "  ✓ Timestamp logging"
echo "  ✓ IP Geolocation"
echo "  ✓ JSON/CSV export"
echo "  ✓ Email notifications"
echo "  ✓ Session tracking"
echo "  ✓ Statistics dashboard"
echo ""
echo "Configuration file: whphisher_config.ini"
echo "Documentation: ENHANCED_FEATURES.md"
echo ""
echo "Run: python3 WhPhisher.py"
echo ""
