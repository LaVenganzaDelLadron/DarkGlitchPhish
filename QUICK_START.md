# WhPhisher Enhanced - Quick Start Guide

## 🚀 Quick Setup

### 1. Install Optional Dependencies (Recommended)
**Linux/Mac:**
```bash
chmod +x install_enhanced.sh
./install_enhanced.sh
```

**Windows:**
```cmd
install_enhanced.bat
```

Or manually:
```bash
pip install qrcode[pil]
```

### 2. Configure (Optional but Recommended)
Edit `whphisher_config.ini`:

**For Email Notifications:**
```ini
[SETTINGS]
email_enabled = True

[EMAIL]
to = your_email@gmail.com
from = your_email@gmail.com
password = your_app_password_here
```

**For Custom Port:**
```ini
[SETTINGS]
port = 8888
```

### 3. Run WhPhisher
```bash
python3 WhPhisher.py
```

---

## 🎯 New Features at a Glance

| Feature | Status | How to Access |
|---------|--------|---------------|
| **Timestamps** | Auto-enabled | Automatic on all captures |
| **Geolocation** | Auto-enabled | Shows with IP captures |
| **QR Codes** | Auto-enabled* | Shows after link generation |
| **JSON/CSV Export** | Auto-enabled | Saves to `capture_data.*` |
| **Email Alerts** | Manual setup | Edit config file |
| **Statistics** | Available | Press `x` then `s` |
| **Custom Port** | Manual setup | Edit config file |
| **Site Caching** | Auto-enabled | Speeds up reuse |

*Requires `qrcode` library for visual display

---

## 📊 What Gets Captured Now

### Before (Original)
- Username/password in plaintext
- IP address

### After (Enhanced)
- ✅ Username/password with timestamp
- ✅ IP address with geolocation
- ✅ Country, city, ISP
- ✅ GPS coordinates
- ✅ Session ID for tracking
- ✅ All data in JSON/CSV format
- ✅ Optional email alerts

---

## 🔍 Output Files Explained

| File | Content | Format |
|------|---------|--------|
| `usernames.txt` | Credentials (original) | Plain text |
| `ip.txt` | IP addresses (original) | Plain text |
| `capture_data.json` | All captures with metadata | JSON |
| `capture_data.csv` | All captures for Excel | CSV |
| `url_analytics.json` | Session and click tracking | JSON |
| `whphisher_config.ini` | Your settings | INI |

---

## 💡 Common Workflows

### Workflow 1: Quick Phishing (Same as Original)
```bash
python3 WhPhisher.py
# Select site number
# Copy generated link
# Wait for captures
```

### Workflow 2: Email Alerts Enabled
```bash
# 1. Configure email in whphisher_config.ini
# 2. Run: python3 WhPhisher.py
# 3. Generate link and share
# 4. Receive email when credentials captured
```

### Workflow 3: Data Analysis
```bash
# 1. Run campaign and capture data
# 2. Open capture_data.csv in Excel/Google Sheets
# 3. Analyze locations, times, patterns
# 4. Generate reports
```

### Workflow 4: View Statistics
```bash
# While WhPhisher is running:
# 1. Press Ctrl+C to stop capture
# 2. Press 'x' for About
# 3. Press 's' for Statistics
# 4. View all metrics
```

---

## 🛠️ Troubleshooting

### Problem: Email not sending
**Solution:**
- Use App Password, not regular password
- For Gmail: https://support.google.com/accounts/answer/185833
- Check SMTP server and port in config

### Problem: Geolocation not working
**Solution:**
- Check internet connection
- API has 45 requests/min limit
- Disable with `geolocation = False` in config

### Problem: QR Code showing error
**Solution:**
- Install library: `pip install qrcode[pil]`
- Or disable with `qr_code = False` in config

### Problem: Port already in use
**Solution:**
- Change port in config: `port = 8888`
- Or check what's using port: `lsof -i :8080`

---

## 🎨 Feature Toggle Cheat Sheet

Edit `whphisher_config.ini` and change True/False:

```ini
[SETTINGS]
email_enabled = False      # Email alerts
geolocation = True         # IP location lookup
qr_code = True            # QR code generation
auto_export = True        # JSON/CSV export
cache_sites = True        # Speed up reloads
```

---

## 📈 Statistics Dashboard

Press `x` then `s` to view:

```
========== STATISTICS & CONFIGURATION ==========

[Configuration]
  Port: 8080
  Geolocation: Enabled
  QR Code: Enabled
  Auto Export: Enabled
  Email Alerts: Disabled
  Cache Sites: Enabled

[Session Statistics]
  Total Clicks Tracked: 15
  Active Sessions: 3

[Output Files]
  usernames.txt: 1234 bytes
  ip.txt: 567 bytes
  capture_data.json: 2345 bytes
  capture_data.csv: 1890 bytes
```

---

## 🔐 Security Best Practices

1. **Secure Output Files** - Change permissions: `chmod 600 *.txt *.json *.csv`
2. **Protect Config** - Don't commit config with real passwords to Git
3. **Clean Up** - Delete captures after authorized testing
4. **Email Security** - Use app passwords, not main password
5. **Authorization** - Only use with written permission

---

## 📱 Mobile QR Code Usage

When QR code generation is enabled:
1. Generate phishing link as usual
2. QR code displays in terminal
3. Victim scans with phone camera
4. Opens phishing page on mobile
5. Better for mobile-targeted campaigns

---

## 🌍 Geolocation Data Example

```
Victim IP found! [2025-12-30 15:30:45]
[*] 123.456.789.012

Fetching geolocation data...
Location: New York, New York, United States
ISP: Comcast Cable Communications
Coordinates: 40.7128, -74.0060

Saved in ip.txt
Data exported to JSON and CSV with geolocation
```

---

## 📧 Email Notification Example

```
Subject: WhPhisher - Credentials Captured

Body:
Credentials captured at 2025-12-30 15:30:45:

Username: victim@email.com
Password: password123

---
Sent by WhPhisher Enhanced
```

---

## 🎓 Tips & Tricks

1. **Batch Testing** - Use CSV export to analyze multiple captures
2. **Geographic Targeting** - Use geolocation to verify victim location
3. **Time Analysis** - Check timestamps to find peak response times
4. **Session Correlation** - Use session IDs to match IPs with credentials
5. **Custom Ports** - Use non-standard ports to avoid conflicts
6. **Cache Everything** - Enable caching for faster repeated tests

---

## 📚 Documentation Files

- **ENHANCED_FEATURES.md** - Complete feature documentation
- **ENHANCEMENT_SUMMARY.md** - Technical details of changes
- **QUICK_START.md** - This guide
- **README.md** - Original documentation

---

## ⚡ Performance Tips

- Enable site caching (default: ON)
- Use custom port if 8080 is slow
- Disable geolocation if not needed
- Install qrcode library for faster generation
- Clear old captures regularly

---

## 🆘 Getting Help

1. Check configuration file syntax
2. Review error messages carefully
3. Check ENHANCED_FEATURES.md
4. Test each feature individually
5. Disable problematic features

---

## ✅ Post-Test Cleanup

```bash
# Remove sensitive data
rm -f usernames.txt ip.txt
rm -f capture_data.json capture_data.csv
rm -f url_analytics.json

# Keep configuration
# Keep cached sites in ~/.websites/
```

---

**Happy Enhanced Phishing!** 🎣

Remember: Use responsibly and legally! ⚖️
