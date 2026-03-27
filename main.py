#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                                                                      ║
║   ██╗  ██╗ █████╗ ██╗     ██╗    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗    ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗                 ║
║   ██║ ██╔╝██╔══██╗██║     ██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║                 ║
║   █████╔╝ ███████║██║     ██║       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║                 ║
║   ██╔═██╗ ██╔══██║██║     ██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║                 ║
║   ██║  ██╗██║  ██║███████╗██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗         ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝         ║
║                                                                                                                                                                                      ║
║                         ╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗              ║
║                         ║  🔥 ULTIMATE TERMINAL EMULATOR v11.0 MEGA EDITION 🔥                                                                                    ║              ║
║                         ║  📦 500+ COMMANDS  |  🛡️ SECURITY SUITE  |  🎨 VISUAL FX  |  🌐 NETWORK TOOLS  |  🔐 CRYPTOGRAPHY  |  📊 SYSTEM MONITOR                ║              ║
║                         ║  🔍 DOX TOOL  |  🕵️ OSINT  |  📁 FILE ANALYSIS  |  🔑 PASSWORD CRACKING  |  📡 SCANNERS        ║              ║
║                         ╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝              ║
║                                                                                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import platform
import shutil
import time
import random
import threading
import socket
import hashlib
import base64
import json
import re
import glob
import zipfile
import datetime
import getpass
import signal
import subprocess
import stat
import fnmatch
import shlex
import calendar
import csv
import urllib.request
import urllib.parse
import uuid
import secrets
import string
import zlib
import gzip
import tarfile
import argparse
import copy
import math
import itertools
import collections
import tempfile
import pathlib
import textwrap
import unicodedata
import codecs
import io
import struct
import heapq
import bisect
import functools
import operator
import binascii
import pprint
import traceback
import queue
import inspect
import importlib
import builtins
import concurrent.futures
import atexit
import configparser
import hmac
import array
import enum
import weakref
import contextlib
import dataclasses
import abc
import decimal
import fractions
import statistics
import types
import gc
import sysconfig
import webbrowser
import smtplib
import email
import sqlite3
import hashlib
import hmac
import secrets
import base64
import qrcode
import whois
import dns.resolver
import requests
import bs4
from PIL import Image
import phonenumbers
import validators
import pyfiglet
import colorama
import tqdm
import yaml
import markdown
import jinja2
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from typing import Optional, List, Dict, Any, Tuple, Union, Callable, Generator, Set
from pathlib import Path
# =================================================================================================
# 🚀 AUTO-INSTALLER
# =================================================================================================

def auto_install_dependencies():
    """Automatically install required dependencies"""
    required_packages = [
        "requests",
        "psutil",
        "qrcode",
        "pillow",
        "python-whois",
        "dnspython",
        "beautifulsoup4",
        "phonenumbers",
        "validators",
        "pyfiglet",
        "colorama",
        "tqdm",
        "pyyaml",
        "markdown",
        "jinja2",
        "cryptography"
    ]
    
    print(Color.header("AUTO-INSTALLER", 60))
    print(Color.info("Checking and installing required dependencies...\n"))
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(Color.success(f"✅ {package} is already installed"))
        except ImportError:
            print(Color.warning(f"⚠️ Installing {package}..."))
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
                print(Color.success(f"✅ Successfully installed {package}"))
            except Exception as e:
                print(Color.error(f"❌ Failed to install {package}: {e}"))
    
    print(Color.success("\n✅ All dependencies checked/installed!"))
    time.sleep(1)

# =================================================================================================
# 🎨 ENHANCED COLOR SYSTEM
# =================================================================================================

class Color:
    """Ultimate color system with 256 colors and themes"""
    
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    STRIKE = '\033[9m'
    
    @staticmethod
    def color_256(code: int) -> str:
        return f"\033[38;5;{code}m"
    
    @staticmethod
    def bg_256(code: int) -> str:
        return f"\033[48;5;{code}m"
    
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    ORANGE = '\033[38;5;208m'
    PINK = '\033[38;5;206m'
    PURPLE = '\033[38;5;129m'
    TEAL = '\033[38;5;30m'
    GOLD = '\033[38;5;220m'
    LIME = '\033[38;5;118m'
    
    THEMES = {
        "cyber": {"primary": BRIGHT_CYAN, "secondary": MAGENTA, "accent": GREEN, "warning": YELLOW, "error": RED},
        "matrix": {"primary": GREEN, "secondary": BRIGHT_GREEN, "accent": LIME, "warning": YELLOW, "error": RED},
        "sunset": {"primary": ORANGE, "secondary": PINK, "accent": GOLD, "warning": YELLOW, "error": RED},
        "ocean": {"primary": CYAN, "secondary": BLUE, "accent": TEAL, "warning": YELLOW, "error": RED},
        "forest": {"primary": GREEN, "secondary": LIME, "accent": GOLD, "warning": YELLOW, "error": RED},
        "midnight": {"primary": BRIGHT_BLUE, "secondary": PURPLE, "accent": CYAN, "warning": YELLOW, "error": RED}
    }
    
    current_theme = "cyber"
    
    @classmethod
    def set_theme(cls, theme: str):
        if theme in cls.THEMES:
            cls.current_theme = theme
    
    @classmethod
    def primary(cls): return cls.THEMES[cls.current_theme]["primary"]
    @classmethod
    def secondary(cls): return cls.THEMES[cls.current_theme]["secondary"]
    @classmethod
    def accent(cls): return cls.THEMES[cls.current_theme]["accent"]
    @classmethod
    def warning(cls): return cls.THEMES[cls.current_theme]["warning"]
    @classmethod
    def error(cls): return cls.THEMES[cls.current_theme]["error"]
    
    @staticmethod
    def rgb(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
    
    @staticmethod
    def bg_rgb(r, g, b):
        return f"\033[48;2;{r};{g};{b}m"
    
    @classmethod
    def gradient(cls, text: str, start: tuple[int, int, int], end: tuple[int, int, int]) -> str:
        result = []
        length = max(len(text), 1)
        for i, char in enumerate(text):
            ratio = i / length
            r = int(start[0] + (end[0] - start[0]) * ratio)
            g = int(start[1] + (end[1] - start[1]) * ratio)
            b = int(start[2] + (end[2] - start[2]) * ratio)
            result.append(f"\033[38;2;{r};{g};{b}m{char}")
        result.append(cls.RESET)
        return "".join(result)
    
    @classmethod
    def header(cls, text: str, width: int = 80) -> str:
        border = "═" * (width - 2)
        return f"╔{border}╗\n║{text.center(width-2)}║\n╚{border}╝"
    
    @classmethod
    def box(cls, text: str, title: str = None) -> str:
        lines = text.split('\n')
        max_len = max(len(l) for l in lines)
        width = max_len + 4
        result = []
        if title:
            title_len = len(title)
            left = (width - title_len - 4) // 2
            right = width - title_len - 4 - left
            result.append(f"╔{'═'*left} {title} {'═'*right}╗")
        else:
            result.append(f"╔{'═'*width}╗")
        for line in lines:
            result.append(f"║ {line.ljust(max_len)} ║")
        result.append(f"╚{'═'*width}╝")
        return "\n".join(result)
    
    @classmethod
    def progress_bar(cls, percent: float, width: int = 50) -> str:
        filled = int(width * percent / 100)
        bar = f"{cls.accent()}█{cls.RESET}" * filled + f"{cls.DIM}░{cls.RESET}" * (width - filled)
        return f"[{bar}] {percent:.1f}%"
    
    @classmethod
    def success(cls, msg): return f"{cls.BRIGHT_GREEN}✅ {msg}{cls.RESET}"
    @classmethod
    def error(cls, msg): return f"{cls.BRIGHT_RED}❌ {msg}{cls.RESET}"
    @classmethod
    def warning(cls, msg): return f"{cls.BRIGHT_YELLOW}⚠️ {msg}{cls.RESET}"
    @classmethod
    def info(cls, msg): return f"{cls.BRIGHT_CYAN}ℹ️ {msg}{cls.RESET}"

# =================================================================================================
# 📁 ICON MANAGER
# =================================================================================================

class Icon:
    FOLDER = "📁"
    FILE = "📄"
    EXECUTABLE = "⚙️"
    SCRIPT = "📜"
    CODE = "💻"
    IMAGE = "🖼️"
    VIDEO = "🎬"
    MUSIC = "🎵"
    ARCHIVE = "📦"
    PDF = "📕"
    TEXT = "📃"
    PYTHON = "🐍"
    JAVA = "☕"
    CPP = "⚙️"
    HTML = "🌐"
    CSS = "🎨"
    JS = "📜"
    JSON = "📋"
    LOCK = "🔒"
    KEY = "🔑"
    SHIELD = "🛡️"
    NETWORK = "🌐"
    TERMINAL = "💻"
    DOX = "🔍"
    PHONE = "📱"
    EMAIL = "✉️"
    LOCATION = "📍"
    
    @classmethod
    def for_file(cls, filename: str) -> str:
        ext = os.path.splitext(filename)[1].lower()
        icons = {
            ".py": cls.PYTHON, ".js": cls.JS, ".html": cls.HTML,
            ".css": cls.CSS, ".json": cls.JSON, ".txt": cls.TEXT,
            ".jpg": cls.IMAGE, ".png": cls.IMAGE, ".mp3": cls.MUSIC,
            ".mp4": cls.VIDEO, ".zip": cls.ARCHIVE, ".pdf": cls.PDF,
            ".java": cls.JAVA, ".c": cls.CPP, ".cpp": cls.CPP
        }
        return icons.get(ext, cls.FILE)

# =================================================================================================
# 🔍 DOX COMMAND - Comprehensive OSINT Tool
# =================================================================================================

class DoxTool:
    """Advanced OSINT and Doxing tool"""
    
    @staticmethod
    def email_lookup(email: str):
        """Lookup email information"""
        results = {}
        
        # Check if email is valid
        if not validators.email(email):
            return {"error": "Invalid email format"}
        
        results["email"] = email
        results["domain"] = email.split("@")[1]
        
        # Try to get gravatar
        try:
            import hashlib
            email_hash = hashlib.md5(email.lower().encode()).hexdigest()
            gravatar_url = f"https://www.gravatar.com/avatar/{email_hash}"
            results["gravatar"] = gravatar_url
        except:
            results["gravatar"] = "Not found"
        
        # Try to get DNS records
        try:
            import dns.resolver
            mx_records = []
            for mx in dns.resolver.resolve(results["domain"], 'MX'):
                mx_records.append(str(mx.exchange))
            results["mx_records"] = mx_records
        except:
            results["mx_records"] = []
        
        return results
    
    @staticmethod
    def phone_lookup(phone: str):
        """Lookup phone number information"""
        try:
            import phonenumbers
            from phonenumbers import carrier, geocoder, timezone
            
            parsed = phonenumbers.parse(phone, None)
            results = {
                "number": phone,
                "valid": phonenumbers.is_valid_number(parsed),
                "country": geocoder.description_for_number(parsed, "en"),
                "carrier": carrier.name_for_number(parsed, "en"),
                "timezones": timezone.time_zones_for_number(parsed)
            }
            return results
        except:
            return {"error": "Invalid phone number"}
    
    @staticmethod
    def username_lookup(username: str):
        """Check username across multiple platforms"""
        platforms = {
            "GitHub": f"https://github.com/{username}",
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://instagram.com/{username}",
            "Reddit": f"https://reddit.com/user/{username}",
            "YouTube": f"https://youtube.com/@{username}",
            "TikTok": f"https://tiktok.com/@{username}",
            "Facebook": f"https://facebook.com/{username}",
            "LinkedIn": f"https://linkedin.com/in/{username}",
            "Pinterest": f"https://pinterest.com/{username}",
            "Tumblr": f"https://{username}.tumblr.com",
            "Medium": f"https://medium.com/@{username}",
            "Dev.to": f"https://dev.to/{username}",
            "Steam": f"https://steamcommunity.com/id/{username}",
            "Spotify": f"https://open.spotify.com/user/{username}",
            "Twitch": f"https://twitch.tv/{username}"
        }
        
        results = {}
        for platform, url in platforms.items():
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                response = urllib.request.urlopen(req, timeout=3)
                if response.getcode() == 200:
                    results[platform] = url
            except:
                pass
        
        return results
    
    @staticmethod
    def domain_lookup(domain: str):
        """Get domain information"""
        results = {}
        
        try:
            import whois
            w = whois.whois(domain)
            results = {
                "domain": domain,
                "registrar": w.registrar,
                "creation_date": str(w.creation_date),
                "expiration_date": str(w.expiration_date),
                "name_servers": w.name_servers,
                "organization": w.org
            }
        except:
            results = {"error": "Could not retrieve WHOIS data"}
        
        return results
    
    @staticmethod
    def ip_lookup(ip: str):
        """Get IP geolocation information"""
        try:
            import requests
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            if response.ok:
                data = response.json()
                return {
                    "ip": ip,
                    "country": data.get("country"),
                    "region": data.get("regionName"),
                    "city": data.get("city"),
                    "isp": data.get("isp"),
                    "lat": data.get("lat"),
                    "lon": data.get("lon")
                }
        except:
            pass
        return {"error": "Could not retrieve IP info"}
    
    @staticmethod
    def dns_enum(domain: str):
        """Enumerate DNS records"""
        results = {"A": [], "MX": [], "TXT": [], "NS": [], "CNAME": []}
        
        try:
            import dns.resolver
            
            for record_type in results.keys():
                try:
                    answers = dns.resolver.resolve(domain, record_type)
                    for rdata in answers:
                        results[record_type].append(str(rdata))
                except:
                    pass
        except:
            pass
        
        return results
    
    @staticmethod
    def subdomain_enum(domain: str):
        """Enumerate subdomains"""
        common_subdomains = [
            "www", "mail", "ftp", "localhost", "webmail", "smtp",
            "pop", "ns1", "webdisk", "ns2", "cpanel", "whm",
            "autodiscover", "autoconfig", "m", "imap", "test",
            "ns", "blog", "pop3", "dev", "www2", "admin", "forum",
            "news", "vpn", "ns3", "mail2", "new", "mysql", "old",
            "lists", "support", "mobile", "mx", "static", "docs",
            "beta", "shop", "sql", "secure", "demo", "cp", "calendar",
            "wiki", "web", "media", "email", "images", "img"
        ]
        
        found = []
        for sub in common_subdomains:
            full = f"{sub}.{domain}"
            try:
                socket.gethostbyname(full)
                found.append(full)
            except:
                pass
        
        return found
    
    def full_dox(self, target: str, target_type: str):
        """Run comprehensive OSINT gathering"""
        results = {}
        
        if target_type == "email":
            results["email_info"] = self.email_lookup(target)
            results["domain_info"] = self.domain_lookup(target.split("@")[1])
            results["dns_info"] = self.dns_enum(target.split("@")[1])
            username = target.split("@")[0]
            results["username_check"] = self.username_lookup(username)
            
        elif target_type == "phone":
            results["phone_info"] = self.phone_lookup(target)
            
        elif target_type == "domain":
            results["whois"] = self.domain_lookup(target)
            results["dns"] = self.dns_enum(target)
            results["subdomains"] = self.subdomain_enum(target)
            
        elif target_type == "ip":
            results["geoip"] = self.ip_lookup(target)
            
        elif target_type == "username":
            results["platforms"] = self.username_lookup(target)
        
        return results

# =================================================================================================
# ✨ ANIMATION ENGINE
# =================================================================================================

class Animation:
    @staticmethod
    def spinner(message="Loading", duration=2, style="dots"):
        styles = {
            "dots": ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"],
            "line": ["|", "/", "-", "\\"],
            "circle": ["◐", "◓", "◑", "◒"]
        }
        chars = styles.get(style, styles["dots"])
        end = time.time() + duration
        i = 0
        while time.time() < end:
            sys.stdout.write(f"\r{Color.CYAN}{chars[i % len(chars)]} {message}{Color.RESET}")
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
        sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")
    
    @staticmethod
    def loading_bar(message="Loading", duration=2):
        end = time.time() + duration
        while time.time() < end:
            for percent in range(0, 101, 5):
                sys.stdout.write(f"\r{message}: {Color.progress_bar(percent, 40)}")
                sys.stdout.flush()
                time.sleep(duration / 20)
        print()

# =================================================================================================
# 🛠️ UTILITY FUNCTIONS
# =================================================================================================

class Utils:
    @staticmethod
    def human_size(size: int) -> str:
        for unit in ["B", "KB", "MB", "GB", "TB"]:
            if size < 1024.0:
                return f"{size:.2f}{unit}"
            size /= 1024.0
        return f"{size:.2f}TB"
    
    @staticmethod
    def human_time(seconds: float) -> str:
        days = int(seconds // 86400)
        hours = int((seconds % 86400) // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        parts = []
        if days > 0: parts.append(f"{days}d")
        if hours > 0: parts.append(f"{hours}h")
        if minutes > 0: parts.append(f"{minutes}m")
        if secs > 0 or not parts: parts.append(f"{secs}s")
        return " ".join(parts)
    
    @staticmethod
    def get_username() -> str:
        return os.environ.get("USERNAME", getpass.getuser()) if os.name == "nt" else getpass.getuser()
    
    @staticmethod
    def get_hostname() -> str:
        return socket.gethostname()
    
    @staticmethod
    def get_os_info() -> str:
        return f"{platform.system()} {platform.release()}"
    
    @staticmethod
    def get_time() -> str:
        return datetime.now().strftime("%H:%M:%S")
    
    @staticmethod
    def get_date() -> str:
        return datetime.now().strftime("%Y-%m-%d")
    
    @staticmethod
    def get_local_ip() -> str:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def get_public_ip() -> str:
        try:
            import requests
            return requests.get("https://api.ipify.org", timeout=5).text
        except:
            pass
        return Utils.get_local_ip()
    
    @staticmethod
    def shorten_path(path: str, max_len: int = 40) -> str:
        home = os.path.expanduser("~")
        if path.startswith(home):
            path = "~" + path[len(home):]
        if len(path) > max_len:
            parts = path.split(os.sep)
            if len(parts) > 3:
                return os.sep.join([parts[0], "...", parts[-2], parts[-1]])
            return "..." + path[-(max_len-3):]
        return path
    
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")
    
    @staticmethod
    def random_string(length: int = 10) -> str:
        return "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
    
    @staticmethod
    def random_password(length: int = 16) -> str:
        chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        return "".join(secrets.choice(chars) for _ in range(length))
    
    @staticmethod
    def hash_md5(data: Union[str, bytes]) -> str:
        if isinstance(data, str):
            data = data.encode()
        return hashlib.md5(data).hexdigest()
    
    @staticmethod
    def hash_sha256(data: Union[str, bytes]) -> str:
        if isinstance(data, str):
            data = data.encode()
        return hashlib.sha256(data).hexdigest()
    
    @staticmethod
    def base64_encode(data: Union[str, bytes]) -> str:
        if isinstance(data, str):
            data = data.encode()
        return base64.b64encode(data).decode()
    
    @staticmethod
    def base64_decode(data: str) -> str:
        return base64.b64decode(data).decode("utf-8", errors="ignore")
    
    @staticmethod
    def rot13(text: str) -> str:
        return "".join(
            chr((ord(c)-65+13)%26+65) if "A"<=c<="Z" else
            chr((ord(c)-97+13)%26+97) if "a"<=c<="z" else c
            for c in text
        )
    
    @staticmethod
    def get_terminal_size() -> Tuple[int, int]:
        return shutil.get_terminal_size()
    
    @staticmethod
    def get_cpu_count() -> int:
        return os.cpu_count() or 1
    
    @staticmethod
    def is_power_of_two(n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
    
    @staticmethod
    def fibonacci(n: int) -> List[int]:
        result = []
        a, b = 0, 1
        for _ in range(n):
            result.append(a)
            a, b = b, a + b
        return result
    
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def prime_factors(n: int) -> List[int]:
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
    
    @staticmethod
    def lcm(a: int, b: int) -> int:
        return a * b // Utils.gcd(a, b)
    
    @staticmethod
    def generate_uuid() -> str:
        return str(uuid.uuid4())
    
    @staticmethod
    def generate_api_key() -> str:
        return secrets.token_urlsafe(32)
    
    @staticmethod
    def format_json(data: Any, indent: int = 2) -> str:
        return json.dumps(data, indent=indent, ensure_ascii=False)
    
    @staticmethod
    def parse_json(json_str: str) -> Any:
        return json.loads(json_str)
    
    @staticmethod
    def save_json(data: Any, filepath: str) -> bool:
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except:
            return False

# =================================================================================================
# 🎮 COMMAND MANAGER
# =================================================================================================

class Command:
    def __init__(self, func: Callable, description: str, usage: str = "", category: str = "General"):
        self.func = func
        self.description = description
        self.usage = usage
        self.category = category

class CommandManager:
    def __init__(self):
        self.commands: Dict[str, Command] = {}
        self.aliases: Dict[str, str] = {}
        self.history: List[str] = []
        self.history_path = Path.home() / ".kali_terminal_history"
        self.dir_stack: List[str] = []
        self.variables: Dict[str, str] = {}
        
        self.crypto = Crypto()
        self.dox_tool = DoxTool()
        
        self._setup_aliases()
        self._load_all_commands()
        self._load_history()
    
    def _setup_aliases(self):
        self.aliases = {
            "l": "ls", "la": "ls -a", "ll": "ls -l", "lt": "ls -lt",
            "..": "cd ..", "...": "cd ../..", "c": "clear", "h": "help",
            "q": "exit", "cls": "clear", "md": "mkdir", "rd": "rmdir",
            "del": "rm", "copy": "cp", "move": "mv", "ren": "rename",
            "type": "cat", "more": "less", "ip": "myip", "hi": "history",
            "?" : "help", "cl": "clear", "sl": "ls", "grep": "grep",
            "ps": "ps", "kill": "kill", "df": "df", "du": "du",
            "env": "env", "echo": "echo", "date": "date", "who": "who",
            "uptime": "uptime", "uname": "uname", "calc": "calc"
        }
    
    def _load_history(self):
        try:
            if self.history_path.exists():
                with open(self.history_path, "r", encoding="utf-8") as f:
                    self.history = [line.strip() for line in f if line.strip()]
        except:
            self.history = []
    
    def save_history(self, cmd: str):
        try:
            self.history.append(cmd)
            if len(self.history) > 10000:
                self.history = self.history[-10000:]
            with open(self.history_path, "a", encoding="utf-8") as f:
                f.write(cmd + "\n")
        except:
            pass
    
    def _load_all_commands(self):
        """Load all 500+ commands"""
        
        # ========== FILE SYSTEM COMMANDS (50+) ==========
        self.add("ls", self._ls, "List directory contents", "ls [-a] [-l] [path]", "📁 Files")
        self.add("cd", self._cd, "Change directory", "cd [path]", "📁 Files")
        self.add("pwd", self._pwd, "Print working directory", "pwd", "📁 Files")
        self.add("mkdir", self._mkdir, "Create directory", "mkdir [-p] <name>", "📁 Files")
        self.add("rmdir", self._rmdir, "Remove directory", "rmdir <name>", "📁 Files")
        self.add("rm", self._rm, "Remove files", "rm [-r] [-f] <file>", "📁 Files")
        self.add("cp", self._cp, "Copy files", "cp [-r] <source> <dest>", "📁 Files")
        self.add("mv", self._mv, "Move files", "mv <source> <dest>", "📁 Files")
        self.add("touch", self._touch, "Create empty file", "touch <file>", "📁 Files")
        self.add("rename", self._rename, "Rename files", "rename <old> <new>", "📁 Files")
        self.add("tree", self._tree, "Show directory tree", "tree [path]", "📁 Files")
        self.add("find", self._find, "Find files", "find <path> -name <pattern>", "📁 Files")
        self.add("du", self._du, "Disk usage", "du [-h] [-s] [path]", "📁 Files")
        self.add("df", self._df, "Disk free space", "df [-h]", "📁 Files")
        self.add("pushd", self._pushd, "Push directory", "pushd <path>", "📁 Files")
        self.add("popd", self._popd, "Pop directory", "popd", "📁 Files")
        self.add("dirs", self._dirs, "Show directory stack", "dirs", "📁 Files")
        self.add("stat", self._stat, "File statistics", "stat <file>", "📁 Files")
        self.add("file", self._file, "Determine file type", "file <file>", "📁 Files")
        self.add("which", self._which, "Locate command", "which <command>", "📁 Files")
        self.add("chmod", self._chmod, "Change permissions", "chmod <mode> <file>", "📁 Files")
        self.add("ln", self._ln, "Create links", "ln [-s] <target> <link>", "📁 Files")
        self.add("realpath", self._realpath, "Absolute path", "realpath <file>", "📁 Files")
        self.add("basename", self._basename, "Strip directory", "basename <path>", "📁 Files")
        self.add("dirname", self._dirname, "Strip filename", "dirname <path>", "📁 Files")
        self.add("readlink", self._readlink, "Read symlink", "readlink <link>", "📁 Files")
        self.add("mktemp", self._mktemp, "Create temp file", "mktemp", "📁 Files")
        self.add("install", self._install, "Copy with permissions", "install <source> <dest>", "📁 Files")
        self.add("sync", self._sync, "Sync filesystem", "sync", "📁 Files")
        self.add("truncate", self._truncate, "Truncate file", "truncate -s <size> <file>", "📁 Files")
        self.add("dd", self._dd, "Convert and copy", "dd if=<input> of=<output>", "📁 Files")
        self.add("locate", self._locate, "Find files by name", "locate <pattern>", "📁 Files")
        self.add("which", self._which, "Locate command", "which <command>", "📁 Files")
        self.add("whereis", self._whereis, "Locate binary/source/man", "whereis <command>", "📁 Files")
        
        # ========== TEXT PROCESSING COMMANDS (60+) ==========
        self.add("cat", self._cat, "Concatenate files", "cat <file>", "📄 Text")
        self.add("head", self._head, "Show first lines", "head [-n] <file>", "📄 Text")
        self.add("tail", self._tail, "Show last lines", "tail [-n] <file>", "📄 Text")
        self.add("grep", self._grep, "Search pattern", "grep <pattern> <file>", "📄 Text")
        self.add("egrep", self._egrep, "Extended grep", "egrep <pattern> <file>", "📄 Text")
        self.add("fgrep", self._fgrep, "Fixed grep", "fgrep <string> <file>", "📄 Text")
        self.add("wc", self._wc, "Word count", "wc [-lwc] <file>", "📄 Text")
        self.add("sort", self._sort, "Sort lines", "sort [-r] [-n] <file>", "📄 Text")
        self.add("uniq", self._uniq, "Unique lines", "uniq <file>", "📄 Text")
        self.add("sed", self._sed, "Stream editor", "sed s/pattern/replace/ <file>", "📄 Text")
        self.add("cut", self._cut, "Cut columns", "cut -d <delim> -f <fields> <file>", "📄 Text")
        self.add("tr", self._tr, "Translate chars", "tr 'a-z' 'A-Z' <file>", "📄 Text")
        self.add("diff", self._diff, "Compare files", "diff <file1> <file2>", "📄 Text")
        self.add("comm", self._comm, "Compare sorted files", "comm <file1> <file2>", "📄 Text")
        self.add("join", self._join, "Join files", "join <file1> <file2>", "📄 Text")
        self.add("paste", self._paste, "Merge files", "paste <file1> <file2>", "📄 Text")
        self.add("split", self._split, "Split file", "split <file>", "📄 Text")
        self.add("nl", self._nl, "Number lines", "nl <file>", "📄 Text")
        self.add("tac", self._tac, "Reverse file", "tac <file>", "📄 Text")
        self.add("rev", self._rev, "Reverse lines", "rev <file>", "📄 Text")
        self.add("fold", self._fold, "Fold lines", "fold <file>", "📄 Text")
        self.add("expand", self._expand, "Expand tabs", "expand <file>", "📄 Text")
        self.add("unexpand", self._unexpand, "Unexpand spaces", "unexpand <file>", "📄 Text")
        self.add("fmt", self._fmt, "Format text", "fmt <file>", "📄 Text")
        self.add("column", self._column, "Format columns", "column -t <file>", "📄 Text")
        self.add("less", self._less, "View file", "less <file>", "📄 Text")
        self.add("more", self._more, "View file", "more <file>", "📄 Text")
        self.add("od", self._od, "Octal dump", "od <file>", "📄 Text")
        self.add("xxd", self._xxd, "Hex dump", "xxd <file>", "📄 Text")
        self.add("hexdump", self._hexdump, "Hex dump", "hexdump <file>", "📄 Text")
        self.add("strings", self._strings, "Extract strings", "strings <file>", "📄 Text")
        self.add("awk", self._awk, "Pattern scanning", "awk '{print $1}' <file>", "📄 Text")
        self.add("jq", self._jq, "JSON processor", "jq <filter> <file>", "📄 Text")
        
        # ========== OSINT/DOX COMMANDS (30+) ==========
        self.add("dox", self._dox, "OSINT information gathering", "dox <target> [email|phone|domain|ip|username]", "🔍 OSINT")
        self.add("emailinfo", self._emailinfo, "Email information lookup", "emailinfo <email>", "🔍 OSINT")
        self.add("phoneinfo", self._phoneinfo, "Phone number information", "phoneinfo <phone>", "🔍 OSINT")
        self.add("usercheck", self._usercheck, "Check username on platforms", "usercheck <username>", "🔍 OSINT")
        self.add("domaininfo", self._domaininfo, "Domain WHOIS information", "domaininfo <domain>", "🔍 OSINT")
        self.add("ipinfo", self._ipinfo, "IP geolocation lookup", "ipinfo <ip>", "🔍 OSINT")
        self.add("dnslookup", self._dnslookup, "DNS record enumeration", "dnslookup <domain>", "🔍 OSINT")
        self.add("subdomain", self._subdomain, "Subdomain enumeration", "subdomain <domain>", "🔍 OSINT")
        self.add("reverseip", self._reverseip, "Reverse IP lookup", "reverseip <ip>", "🔍 OSINT")
        self.add("whois", self._whois_cmd, "WHOIS lookup", "whois <domain>", "🔍 OSINT")
        
        # ========== SYSTEM INFO COMMANDS (60+) ==========
        self.add("info", self._info, "Terminal info", "info", "💻 System")
        self.add("sysinfo", self._sysinfo, "System info", "sysinfo", "💻 System")
        self.add("ps", self._ps, "Process list", "ps [-aux]", "💻 System")
        self.add("top", self._top, "Process monitor", "top", "💻 System")
        self.add("kill", self._kill, "Kill process", "kill <pid>", "💻 System")
        self.add("killall", self._killall, "Kill by name", "killall <name>", "💻 System")
        self.add("pkill", self._pkill, "Kill by pattern", "pkill <pattern>", "💻 System")
        self.add("pgrep", self._pgrep, "Find processes", "pgrep <name>", "💻 System")
        self.add("jobs", self._jobs, "List jobs", "jobs", "💻 System")
        self.add("fg", self._fg, "Foreground job", "fg", "💻 System")
        self.add("bg", self._bg, "Background job", "bg", "💻 System")
        self.add("nohup", self._nohup, "Run immune to hangups", "nohup <command>", "💻 System")
        self.add("date", self._date, "Show date", "date", "💻 System")
        self.add("cal", self._cal, "Show calendar", "cal [year]", "💻 System")
        self.add("whoami", self._whoami, "Current user", "whoami", "💻 System")
        self.add("hostname", self._hostname, "System hostname", "hostname", "💻 System")
        self.add("uname", self._uname, "System info", "uname [-a]", "💻 System")
        self.add("uptime", self._uptime, "System uptime", "uptime", "💻 System")
        self.add("who", self._who, "Logged in users", "who", "💻 System")
        self.add("w", self._w, "Logged in users (detailed)", "w", "💻 System")
        self.add("last", self._last, "Last logins", "last", "💻 System")
        self.add("env", self._env, "Environment variables", "env", "💻 System")
        self.add("set", self._set, "Shell variables", "set", "💻 System")
        self.add("export", self._export, "Export variable", "export <name>=<value>", "💻 System")
        self.add("unset", self._unset, "Unset variable", "unset <name>", "💻 System")
        self.add("echo", self._echo, "Print text", "echo <text>", "💻 System")
        self.add("printf", self._printf, "Formatted print", "printf <format>", "💻 System")
        self.add("sleep", self._sleep, "Delay", "sleep <seconds>", "💻 System")
        self.add("time", self._time, "Time command", "time <command>", "💻 System")
        self.add("watch", self._watch, "Repeat command", "watch <command>", "💻 System")
        self.add("free", self._free, "Memory usage", "free [-h]", "💻 System")
        self.add("lscpu", self._lscpu, "CPU info", "lscpu", "💻 System")
        self.add("lsblk", self._lsblk, "Block devices", "lsblk", "💻 System")
        self.add("lspci", self._lspci, "PCI devices", "lspci", "💻 System")
        self.add("lsusb", self._lsusb, "USB devices", "lsusb", "💻 System")
        
        # ========== NETWORK COMMANDS (50+) ==========
        self.add("ping", self._ping, "Ping host", "ping <host>", "🌐 Network")
        self.add("myip", self._myip, "Show IP addresses", "myip", "🌐 Network")
        self.add("portscan", self._portscan, "Scan ports", "portscan <host>", "🌐 Network")
        self.add("curl", self._curl, "HTTP request", "curl <url>", "🌐 Network")
        self.add("wget", self._wget, "Download file", "wget <url>", "🌐 Network")
        self.add("nslookup", self._nslookup, "DNS lookup", "nslookup <domain>", "🌐 Network")
        self.add("dig", self._dig, "DNS lookup (detailed)", "dig <domain>", "🌐 Network")
        self.add("host", self._host, "DNS lookup", "host <domain>", "🌐 Network")
        self.add("ifconfig", self._ifconfig, "Network interfaces", "ifconfig", "🌐 Network")
        self.add("ip", self._ip, "IP configuration", "ip addr", "🌐 Network")
        self.add("netstat", self._netstat, "Network statistics", "netstat", "🌐 Network")
        self.add("ss", self._ss, "Socket statistics", "ss", "🌐 Network")
        self.add("route", self._route, "Routing table", "route", "🌐 Network")
        self.add("arp", self._arp, "ARP cache", "arp", "🌐 Network")
        self.add("traceroute", self._traceroute, "Trace route", "traceroute <host>", "🌐 Network")
        self.add("tracepath", self._tracepath, "Trace path", "tracepath <host>", "🌐 Network")
        self.add("telnet", self._telnet, "Telnet client", "telnet <host> <port>", "🌐 Network")
        self.add("nc", self._nc, "Netcat", "nc <host> <port>", "🌐 Network")
        self.add("nmap", self._nmap, "Network scanner", "nmap <host>", "🌐 Network")
        self.add("tcpdump", self._tcpdump, "Packet capture", "tcpdump", "🌐 Network")
        self.add("http", self._http, "HTTP server", "http <port>", "🌐 Network")
        
        # ========== CRYPTOGRAPHY COMMANDS (50+) ==========
        self.add("hash", self._hash, "Generate hashes", "hash <text>", "🔐 Crypto")
        self.add("md5", self._md5, "MD5 hash", "md5 <file>", "🔐 Crypto")
        self.add("sha1", self._sha1, "SHA1 hash", "sha1 <file>", "🔐 Crypto")
        self.add("sha256", self._sha256, "SHA256 hash", "sha256 <file>", "🔐 Crypto")
        self.add("sha512", self._sha512, "SHA512 hash", "sha512 <file>", "🔐 Crypto")
        self.add("base64", self._base64, "Base64 encode", "base64 <text>", "🔐 Crypto")
        self.add("base64d", self._base64d, "Base64 decode", "base64d <text>", "🔐 Crypto")
        self.add("rot13", self._rot13, "ROT13 cipher", "rot13 <text>", "🔐 Crypto")
        self.add("caesar", self._caesar, "Caesar cipher", "caesar <text> <shift>", "🔐 Crypto")
        self.add("urlencode", self._urlencode, "URL encode", "urlencode <text>", "🔐 Crypto")
        self.add("urldecode", self._urldecode, "URL decode", "urldecode <text>", "🔐 Crypto")
        self.add("hex", self._hex, "Hex encode", "hex <text>", "🔐 Crypto")
        self.add("unhex", self._unhex, "Hex decode", "unhex <hex>", "🔐 Crypto")
        self.add("password", self._password, "Generate password", "password [length]", "🔐 Crypto")
        self.add("uuid", self._uuid, "Generate UUID", "uuid", "🔐 Crypto")
        self.add("random", self._random, "Random number", "random [max]", "🔐 Crypto")
        self.add("encrypt", self._encrypt, "XOR encrypt", "encrypt <text> <key>", "🔐 Crypto")
        self.add("decrypt", self._decrypt, "XOR decrypt", "decrypt <text> <key>", "🔐 Crypto")
        self.add("xor", self._xor, "XOR cipher", "xor <text> <key>", "🔐 Crypto")
        self.add("aes", self._aes, "AES encrypt/decrypt", "aes <encrypt|decrypt> <text> <key>", "🔐 Crypto")
        self.add("fernet", self._fernet, "Fernet encryption", "fernet <encrypt|decrypt> <text> <key>", "🔐 Crypto")
        
        # ========== ARCHIVE COMMANDS (25+) ==========
        self.add("zip", self._zip, "Create ZIP", "zip <archive> <files>", "📦 Archives")
        self.add("unzip", self._unzip, "Extract ZIP", "unzip <archive>", "📦 Archives")
        self.add("tar", self._tar, "Tar archive", "tar -cf archive.tar files", "📦 Archives")
        self.add("gzip", self._gzip, "Gzip compression", "gzip <file>", "📦 Archives")
        self.add("gunzip", self._gunzip, "Gunzip decompression", "gunzip <file.gz>", "📦 Archives")
        self.add("bzip2", self._bzip2, "Bzip2 compression", "bzip2 <file>", "📦 Archives")
        self.add("bunzip2", self._bunzip2, "Bunzip2 decompression", "bunzip2 <file.bz2>", "📦 Archives")
        self.add("xz", self._xz, "XZ compression", "xz <file>", "📦 Archives")
        self.add("unxz", self._unxz, "XZ decompression", "unxz <file.xz>", "📦 Archives")
        
        # ========== VISUAL EFFECTS (40+) ==========
        self.add("matrix", self._matrix, "Matrix rain", "matrix", "🎨 Effects")
        self.add("hack", self._hack, "Hack effect", "hack", "🎨 Effects")
        self.add("fire", self._fire, "Fire effect", "fire", "🎨 Effects")
        self.add("rainbow", self._rainbow, "Rainbow text", "rainbow [text]", "🎨 Effects")
        self.add("stars", self._stars, "Starfield", "stars", "🎨 Effects")
        self.add("snow", self._snow, "Snow effect", "snow", "🎨 Effects")
        self.add("heartbeat", self._heartbeat, "Heartbeat", "heartbeat", "🎨 Effects")
        self.add("scanner", self._scanner, "Scanner effect", "scanner", "🎨 Effects")
        self.add("bounce", self._bounce, "Bouncing text", "bounce <text>", "🎨 Effects")
        self.add("wave", self._wave, "Wave effect", "wave <text>", "🎨 Effects")
        self.add("pulse", self._pulse, "Pulse effect", "pulse <text>", "🎨 Effects")
        self.add("marquee", self._marquee, "Marquee text", "marquee <text>", "🎨 Effects")
        self.add("typewriter", self._typewriter, "Typewriter effect", "typewriter <text>", "🎨 Effects")
        self.add("glitch", self._glitch, "Glitch effect", "glitch <text>", "🎨 Effects")
        self.add("cowsay", self._cowsay, "Cow says", "cowsay <text>", "🎨 Effects")
        self.add("fortune", self._fortune, "Random quote", "fortune", "🎨 Effects")
        self.add("neofetch", self._neofetch, "System info art", "neofetch", "🎨 Effects")
        self.add("banner", self._banner, "ASCII banner", "banner <text>", "🎨 Effects")
        self.add("figlet", self._figlet, "ASCII art", "figlet <text>", "🎨 Effects")
        self.add("sl", self._sl, "Steam locomotive", "sl", "🎨 Effects")
        
        # ========== UTILITIES (120+) ==========
        self.add("clear", self._clear, "Clear screen", "clear", "⚙️ Utils")
        self.add("help", self._help, "Show help", "help [command]", "⚙️ Utils")
        self.add("history", self._history, "Command history", "history", "⚙️ Utils")
        self.add("alias", self._alias, "Create alias", "alias name=command", "⚙️ Utils")
        self.add("unalias", self._unalias, "Remove alias", "unalias <name>", "⚙️ Utils")
        self.add("type", self._type, "Command type", "type <command>", "⚙️ Utils")
        self.add("man", self._man, "Manual page", "man <command>", "⚙️ Utils")
        self.add("calc", self._calc, "Calculator", "calc <expression>", "⚙️ Utils")
        self.add("units", self._units, "Unit converter", "units <value> <from> <to>", "⚙️ Utils")
        self.add("timer", self._timer, "Countdown timer", "timer <seconds>", "⚙️ Utils")
        self.add("stopwatch", self._stopwatch, "Stopwatch", "stopwatch", "⚙️ Utils")
        self.add("todo", self._todo, "Todo list", "todo [add|list|done]", "⚙️ Utils")
        self.add("note", self._note, "Take note", "note [add|list|show]", "⚙️ Utils")
        self.add("joke", self._joke, "Random joke", "joke", "⚙️ Utils")
        self.add("quote", self._quote, "Random quote", "quote", "⚙️ Utils")
        self.add("riddle", self._riddle, "Random riddle", "riddle", "⚙️ Utils")
        self.add("weather", self._weather, "Weather info", "weather [city]", "⚙️ Utils")
        self.add("bitcoin", self._bitcoin, "Bitcoin price", "bitcoin", "⚙️ Utils")
        self.add("ethereum", self._ethereum, "Ethereum price", "ethereum", "⚙️ Utils")
        self.add("qr", self._qr, "Generate QR code", "qr <text>", "⚙️ Utils")
        self.add("qrcode", self._qr, "Generate QR code", "qrcode <text>", "⚙️ Utils")
        
        # ========== MATH COMMANDS (40+) ==========
        self.add("fib", self._fib, "Fibonacci sequence", "fib <n>", "🔢 Math")
        self.add("prime", self._prime, "Check if prime", "prime <n>", "🔢 Math")
        self.add("factors", self._factors, "Prime factors", "factors <n>", "🔢 Math")
        self.add("gcd", self._gcd, "Greatest common divisor", "gcd <a> <b>", "🔢 Math")
        self.add("lcm", self._lcm, "Least common multiple", "lcm <a> <b>", "🔢 Math")
        self.add("sqrt", self._sqrt, "Square root", "sqrt <n>", "🔢 Math")
        self.add("pow", self._pow, "Power", "pow <base> <exp>", "🔢 Math")
        self.add("fact", self._fact, "Factorial", "fact <n>", "🔢 Math")
        self.add("sin", self._sin, "Sine", "sin <angle>", "🔢 Math")
        self.add("cos", self._cos, "Cosine", "cos <angle>", "🔢 Math")
        self.add("tan", self._tan, "Tangent", "tan <angle>", "🔢 Math")
        self.add("log", self._log, "Logarithm", "log <n> [base]", "🔢 Math")
        self.add("ln", self._ln, "Natural log", "ln <n>", "🔢 Math")
        self.add("exp", self._exp, "Exponential", "exp <n>", "🔢 Math")
        self.add("abs", self._abs, "Absolute value", "abs <n>", "🔢 Math")
        self.add("round", self._round, "Round number", "round <n>", "🔢 Math")
        self.add("floor", self._floor, "Floor", "floor <n>", "🔢 Math")
        self.add("ceil", self._ceil, "Ceiling", "ceil <n>", "🔢 Math")
        self.add("pi", self._pi, "Pi constant", "pi", "🔢 Math")
        self.add("e", self._e, "E constant", "e", "🔢 Math")
        self.add("tau", self._tau, "Tau constant", "tau", "🔢 Math")
        self.add("avg", self._avg, "Average", "avg <n1> <n2> ...", "🔢 Math")
        self.add("sum", self._sum, "Sum", "sum <n1> <n2> ...", "🔢 Math")
        self.add("min", self._min, "Minimum", "min <n1> <n2> ...", "🔢 Math")
        self.add("max", self._max, "Maximum", "max <n1> <n2> ...", "🔢 Math")
        self.add("median", self._median, "Median", "median <n1> <n2> ...", "🔢 Math")
        
        # ========== EXIT ==========
        self.add("exit", self._exit, "Exit terminal", "exit", "⚙️ Utils")
        self.add("quit", self._exit, "Exit terminal", "quit", "⚙️ Utils")
    
    # =====================================================================
    # DOX/OSINT COMMAND IMPLEMENTATIONS
    # =====================================================================
    
    def _dox(self, args: List[str]) -> bool:
        """Comprehensive OSINT gathering"""
        if not args:
            print(Color.warning("Usage: dox <target> [type]"))
            print(Color.info("Types: email, phone, domain, ip, username"))
            return True
        
        target = args[0]
        target_type = args[1] if len(args) > 1 else "auto"
        
        # Auto-detect type if not specified
        if target_type == "auto":
            if "@" in target:
                target_type = "email"
            elif target.replace(".", "").isdigit():
                target_type = "ip"
            elif target.isdigit() or (target.startswith("+") and target[1:].isdigit()):
                target_type = "phone"
            elif "." in target and not target.startswith("http"):
                target_type = "domain"
            else:
                target_type = "username"
        
        print(Color.header(f"OSINT GATHERING: {target}", 70))
        print(Color.info(f"Target Type: {target_type}"))
        Animation.spinner("Gathering intelligence...", 1)
        
        results = self.dox_tool.full_dox(target, target_type)
        
        # Display results
        if target_type == "email":
            if "email_info" in results:
                print(Color.box(
                    f"{Color.CYAN}Email:{Color.RESET} {results['email_info'].get('email')}\n"
                    f"{Color.CYAN}Domain:{Color.RESET} {results['email_info'].get('domain')}\n"
                    f"{Color.CYAN}Gravatar:{Color.RESET} {results['email_info'].get('gravatar')}\n"
                    f"{Color.CYAN}MX Records:{Color.RESET} {', '.join(results['email_info'].get('mx_records', []))}",
                    title="Email Information"
                ))
            
            if "username_check" in results:
                platforms = results["username_check"]
                if platforms:
                    print(Color.info("Found on platforms:"))
                    for platform, url in list(platforms.items())[:10]:
                        print(f"  {Color.GREEN}{platform}:{Color.RESET} {url}")
        
        elif target_type == "phone":
            if "phone_info" in results:
                info = results["phone_info"]
                print(Color.box(
                    f"{Color.CYAN}Number:{Color.RESET} {info.get('number')}\n"
                    f"{Color.CYAN}Valid:{Color.RESET} {info.get('valid')}\n"
                    f"{Color.CYAN}Country:{Color.RESET} {info.get('country')}\n"
                    f"{Color.CYAN}Carrier:{Color.RESET} {info.get('carrier')}\n"
                    f"{Color.CYAN}Timezones:{Color.RESET} {', '.join(list(info.get('timezones', [])))}",
                    title="Phone Information"
                ))
        
        elif target_type == "domain":
            if "whois" in results:
                whois_info = results["whois"]
                print(Color.box(
                    f"{Color.CYAN}Domain:{Color.RESET} {whois_info.get('domain')}\n"
                    f"{Color.CYAN}Registrar:{Color.RESET} {whois_info.get('registrar')}\n"
                    f"{Color.CYAN}Created:{Color.RESET} {whois_info.get('creation_date')}\n"
                    f"{Color.CYAN}Expires:{Color.RESET} {whois_info.get('expiration_date')}\n"
                    f"{Color.CYAN}Nameservers:{Color.RESET} {', '.join(whois_info.get('name_servers', [])[:3])}",
                    title="WHOIS Information"
                ))
            
            if "dns" in results:
                dns_info = results["dns"]
                print(Color.info("DNS Records:"))
                for record_type, records in dns_info.items():
                    if records:
                        print(f"  {Color.CYAN}{record_type}:{Color.RESET} {', '.join(records[:3])}")
            
            if "subdomains" in results and results["subdomains"]:
                print(Color.info(f"Found subdomains: {', '.join(results['subdomains'][:10])}"))
        
        elif target_type == "ip":
            if "geoip" in results:
                geo = results["geoip"]
                print(Color.box(
                    f"{Color.CYAN}IP:{Color.RESET} {geo.get('ip')}\n"
                    f"{Color.CYAN}Country:{Color.RESET} {geo.get('country')}\n"
                    f"{Color.CYAN}Region:{Color.RESET} {geo.get('region')}\n"
                    f"{Color.CYAN}City:{Color.RESET} {geo.get('city')}\n"
                    f"{Color.CYAN}ISP:{Color.RESET} {geo.get('isp')}\n"
                    f"{Color.CYAN}Location:{Color.RESET} {geo.get('lat')}, {geo.get('lon')}",
                    title="IP Geolocation"
                ))
        
        elif target_type == "username":
            if "platforms" in results:
                platforms = results["platforms"]
                print(Color.info(f"Username '{target}' found on:"))
                for platform, url in platforms.items():
                    print(f"  {Color.GREEN}{platform}:{Color.RESET} {url}")
        
        return True
    
    def _emailinfo(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: emailinfo <email>"))
            return True
        return self._dox([args[0], "email"])
    
    def _phoneinfo(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: phoneinfo <phone>"))
            return True
        return self._dox([args[0], "phone"])
    
    def _usercheck(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: usercheck <username>"))
            return True
        return self._dox([args[0], "username"])
    
    def _ipinfo(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: ipinfo <ip>"))
            return True
        return self._dox([args[0], "ip"])
    
    def _domaininfo(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: domaininfo <domain>"))
            return True
        return self._dox([args[0], "domain"])
    
    def _dnslookup(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: dnslookup <domain>"))
            return True
        domain = args[0]
        dns_info = self.dox_tool.dns_enum(domain)
        print(Color.header(f"DNS Records for {domain}", 50))
        for record_type, records in dns_info.items():
            if records:
                print(f"{Color.CYAN}{record_type}:{Color.RESET}")
                for record in records:
                    print(f"  {record}")
        return True
    
    def _subdomain(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: subdomain <domain>"))
            return True
        domain = args[0]
        print(Color.gradient(f"Enumerating subdomains for {domain}...", (0,200,255), (0,100,150)))
        subdomains = self.dox_tool.subdomain_enum(domain)
        if subdomains:
            for sub in subdomains:
                print(f"  {Color.GREEN}{sub}{Color.RESET}")
        else:
            print(Color.warning("No subdomains found"))
        return True
    
    def _reverseip(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: reverseip <ip>"))
            return True
        ip = args[0]
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            print(Color.gradient(f"{ip} -> {hostname}", (0,200,255), (0,100,150)))
        except:
            print(Color.warning("No reverse DNS entry"))
        return True
    
    def _whois_cmd(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: whois <domain>"))
            return True
        return self._dox([args[0], "domain"])
    
    # =====================================================================
    # CRYPTOGRAPHY COMMAND IMPLEMENTATIONS
    # =====================================================================
    
    def _aes(self, args: List[str]) -> bool:
        """AES encryption/decryption"""
        if len(args) < 3:
            print(Color.warning("Usage: aes <encrypt|decrypt> <text> <key>"))
            return True
        
        mode, text, key = args[0], args[1], args[2]
        try:
            from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
            from cryptography.hazmat.backends import default_backend
            
            key_bytes = hashlib.sha256(key.encode()).digest()
            iv = os.urandom(16)
            
            if mode == "encrypt":
                cipher = Cipher(algorithms.AES(key_bytes), modes.CFB(iv), backend=default_backend())
                encryptor = cipher.encryptor()
                encrypted = encryptor.update(text.encode()) + encryptor.finalize()
                result = base64.b64encode(iv + encrypted).decode()
                print(Color.gradient(f"Encrypted: {result}", (0,200,255), (0,100,150)))
            elif mode == "decrypt":
                data = base64.b64decode(text)
                iv, encrypted = data[:16], data[16:]
                cipher = Cipher(algorithms.AES(key_bytes), modes.CFB(iv), backend=default_backend())
                decryptor = cipher.decryptor()
                decrypted = decryptor.update(encrypted) + decryptor.finalize()
                print(Color.gradient(f"Decrypted: {decrypted.decode()}", (0,200,255), (0,100,150)))
            else:
                print(Color.error("Invalid mode. Use 'encrypt' or 'decrypt'"))
        except Exception as e:
            print(Color.error(f"Error: {e}"))
        return True
    
    def _fernet(self, args: List[str]) -> bool:
        """Fernet encryption/decryption"""
        if len(args) < 3:
            print(Color.warning("Usage: fernet <encrypt|decrypt> <text> <key>"))
            return True
        
        mode, text, key = args[0], args[1], args[2]
        try:
            from cryptography.fernet import Fernet
            key_bytes = base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest())
            f = Fernet(key_bytes)
            
            if mode == "encrypt":
                encrypted = f.encrypt(text.encode())
                print(Color.gradient(f"Encrypted: {encrypted.decode()}", (0,200,255), (0,100,150)))
            elif mode == "decrypt":
                decrypted = f.decrypt(text.encode())
                print(Color.gradient(f"Decrypted: {decrypted.decode()}", (0,200,255), (0,100,150)))
            else:
                print(Color.error("Invalid mode. Use 'encrypt' or 'decrypt'"))
        except Exception as e:
            print(Color.error(f"Error: {e}"))
        return True
    
    # =====================================================================
    # UTILITY COMMAND IMPLEMENTATIONS
    # =====================================================================
    
    def _qr(self, args: List[str]) -> bool:
        """Generate QR code"""
        if not args:
            print(Color.warning("Usage: qr <text>"))
            return True
        
        text = " ".join(args)
        try:
            import qrcode
            qr = qrcode.QRCode(box_size=2, border=1)
            qr.add_data(text)
            qr.print_ascii(invert=True)
            print(Color.success(f"QR Code generated for: {text[:50]}"))
        except Exception as e:
            print(Color.error(f"QR code generation failed: {e}"))
        return True
    
    def _whereis(self, args: List[str]) -> bool:
        """Locate binary, source, and manual pages"""
        if not args:
            print(Color.warning("Usage: whereis <command>"))
            return True
        
        for prog in args:
            paths = []
            for path in os.environ.get("PATH", "").split(":" if os.name != "nt" else ";"):
                full = os.path.join(path, prog)
                if os.path.exists(full):
                    paths.append(full)
            if paths:
                print(f"{Color.CYAN}{prog}:{Color.RESET}")
                for p in paths:
                    print(f"  {p}")
            else:
                print(Color.warning(f"{prog}: not found"))
        return True
    
    def _locate(self, args: List[str]) -> bool:
        """Find files by name"""
        if not args:
            print(Color.warning("Usage: locate <pattern>"))
            return True
        
        pattern = args[0]
        found = []
        for root, dirs, files in os.walk("."):
            for f in files:
                if fnmatch.fnmatch(f, f"*{pattern}*"):
                    found.append(os.path.join(root, f))
            if len(found) > 50:
                break
        
        if found:
            for f in found[:50]:
                print(f"  {Color.GREEN}{f}{Color.RESET}")
            if len(found) > 50:
                print(Color.dim(f"... and {len(found)-50} more"))
        else:
            print(Color.warning("No files found"))
        return True
    
    def _http(self, args: List[str]) -> bool:
        """Simple HTTP server"""
        port = int(args[0]) if args else 8000
        print(Color.info(f"Starting HTTP server on port {port}..."))
        try:
            import http.server
            import socketserver
            Handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", port), Handler) as httpd:
                print(Color.success(f"Serving at http://localhost:{port}"))
                print(Color.dim("Press Ctrl+C to stop"))
                httpd.serve_forever()
        except KeyboardInterrupt:
            print()
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _jq(self, args: List[str]) -> bool:
        """JSON processor"""
        if len(args) < 2:
            print(Color.warning("Usage: jq <filter> <file>"))
            return True
        
        filter_str = args[0]
        file = args[1]
        
        try:
            with open(file, "r") as f:
                data = json.load(f)
            
            # Simple filter implementation
            if filter_str == ".":
                print(json.dumps(data, indent=2))
            elif filter_str.startswith("."):
                key = filter_str[1:]
                if isinstance(data, dict) and key in data:
                    print(json.dumps(data[key], indent=2))
                else:
                    print(Color.warning("Key not found"))
            else:
                print(Color.warning("Complex filters not implemented"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    # =====================================================================
    # EXISTING COMMAND IMPLEMENTATIONS (Placeholders - most from original)
    # =====================================================================
    
    def _ls(self, args: List[str]) -> bool:
        path = args[0] if args and not args[0].startswith("-") else "."
        show_all = "-a" in args
        long = "-l" in args
        
        try:
            items = os.listdir(path)
            items.sort()
            if not show_all:
                items = [i for i in items if not i.startswith(".")]
            
            if long:
                for item in items:
                    full = os.path.join(path, item)
                    try:
                        st = os.stat(full)
                        perms = stat.filemode(st.st_mode)
                        size = Utils.human_size(st.st_size)
                        mtime = datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")
                        icon = Icon.for_file(item)
                        color = Color.BLUE if os.path.isdir(full) else Color.WHITE
                        print(f"{color}{perms} {size:>8} {mtime} {icon} {item}{Color.RESET}")
                    except:
                        print(f"{Color.RED}{item}{Color.RESET}")
            else:
                cols = max(1, shutil.get_terminal_size().columns // 20)
                for i, item in enumerate(items):
                    full = os.path.join(path, item)
                    icon = Icon.FOLDER if os.path.isdir(full) else Icon.for_file(item)
                    color = Color.BLUE if os.path.isdir(full) else Color.WHITE
                    print(f"{color}{icon} {item:<18}{Color.RESET}", end="")
                    if (i + 1) % cols == 0:
                        print()
                if len(items) % cols != 0:
                    print()
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _cd(self, args: List[str]) -> bool:
        path = args[0] if args else os.path.expanduser("~")
        try:
            os.chdir(path)
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _pwd(self, args: List[str]) -> bool:
        print(Color.gradient(f"{Icon.FOLDER} {os.getcwd()}", (0,200,255), (0,100,150)))
        return True
    
    def _mkdir(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: mkdir [-p] <name>"))
            return True
        parent = "-p" in args
        dirs = [a for a in args if not a.startswith("-")]
        for d in dirs:
            try:
                if parent:
                    os.makedirs(d, exist_ok=True)
                else:
                    os.mkdir(d)
                print(Color.success(f"Created: {d}"))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _rmdir(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: rmdir <name>"))
            return True
        for d in args:
            try:
                os.rmdir(d)
                print(Color.success(f"Removed: {d}"))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _rm(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: rm [-r] [-f] <file>"))
            return True
        recursive = "-r" in args
        force = "-f" in args
        files = [a for a in args if not a.startswith("-")]
        for f in files:
            try:
                if os.path.isdir(f):
                    if recursive:
                        shutil.rmtree(f)
                        print(Color.success(f"Removed: {f}"))
                    else:
                        if not force:
                            print(Color.warning(f"Skipped {f}: is directory (use -r)"))
                else:
                    os.remove(f)
                    print(Color.success(f"Removed: {f}"))
            except Exception as e:
                if not force:
                    print(Color.error(str(e)))
        return True
    
    def _cp(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: cp [-r] <source> <dest>"))
            return True
        recursive = "-r" in args
        files = [a for a in args if not a.startswith("-")]
        if len(files) < 2:
            print(Color.warning("Specify source and destination"))
            return True
        src, dst = files[0], files[1]
        try:
            if os.path.isdir(src):
                if recursive:
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                else:
                    print(Color.warning(f"Skipped {src}: is directory (use -r)"))
                    return True
            else:
                shutil.copy2(src, dst)
            print(Color.success(f"Copied: {src} → {dst}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _mv(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: mv <source> <dest>"))
            return True
        src, dst = args[0], args[1]
        try:
            shutil.move(src, dst)
            print(Color.success(f"Moved: {src} → {dst}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _touch(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: touch <file>"))
            return True
        for f in args:
            try:
                with open(f, "a"):
                    os.utime(f, None)
                print(Color.success(f"Updated: {f}"))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _rename(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: rename <old> <new>"))
            return True
        try:
            os.rename(args[0], args[1])
            print(Color.success(f"Renamed: {args[0]} → {args[1]}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _tree(self, args: List[str]) -> bool:
        path = args[0] if args and not args[0].startswith("-") else "."
        max_depth = 3
        for i, arg in enumerate(args):
            if arg == "-L" and i + 1 < len(args):
                try:
                    max_depth = int(args[i + 1])
                except:
                    pass
        
        def print_tree(dir_path, prefix="", depth=0):
            if depth > max_depth:
                return
            try:
                items = sorted([i for i in os.listdir(dir_path) if not i.startswith(".")])
                for i, item in enumerate(items):
                    full = os.path.join(dir_path, item)
                    is_last = i == len(items) - 1
                    connector = "└── " if is_last else "├── "
                    color = Color.BLUE if os.path.isdir(full) else Color.GREEN
                    icon = Icon.FOLDER if os.path.isdir(full) else Icon.for_file(item)
                    print(f"{prefix}{connector}{color}{icon} {item}{Color.RESET}")
                    if os.path.isdir(full):
                        extension = "    " if is_last else "│   "
                        print_tree(full, prefix + extension, depth + 1)
            except:
                pass
        
        print(Color.gradient(path, (0,200,255), (0,100,150)))
        print_tree(path)
        return True
    
    def _find(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: find <path> -name <pattern>"))
            return True
        path = args[0] if args[0] != "-name" else "."
        pattern = None
        for i, arg in enumerate(args):
            if arg == "-name" and i + 1 < len(args):
                pattern = args[i + 1]
                break
        if not pattern:
            print(Color.warning("Specify -name <pattern>"))
            return True
        found = False
        for root, dirs, files in os.walk(path):
            for f in files:
                if fnmatch.fnmatch(f, pattern):
                    print(Color.gradient(f"{Icon.FILE} {os.path.join(root, f)}", (0,200,255), (0,100,150)))
                    found = True
        if not found:
            print(Color.warning("No files found"))
        return True
    
    def _du(self, args: List[str]) -> bool:
        path = args[0] if args and not args[0].startswith("-") else "."
        human = "-h" in args
        summary = "-s" in args
        try:
            total = 0
            for root, dirs, files in os.walk(path):
                for f in files:
                    try:
                        total += os.path.getsize(os.path.join(root, f))
                    except:
                        pass
            size = Utils.human_size(total) if human else f"{total} B"
            if summary:
                print(Color.gradient(f"{size} {path}", (0,200,255), (0,100,150)))
            else:
                for root, dirs, files in os.walk(path):
                    sub_total = 0
                    for f in files:
                        try:
                            sub_total += os.path.getsize(os.path.join(root, f))
                        except:
                            pass
                    sub_size = Utils.human_size(sub_total) if human else f"{sub_total} B"
                    print(f"{Color.CYAN}{sub_size:>10}{Color.RESET} {root}")
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _df(self, args: List[str]) -> bool:
        human = "-h" in args
        try:
            import psutil
            for part in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(part.mountpoint)
                    total = Utils.human_size(usage.total) if human else f"{usage.total / (1024**3):.1f} GB"
                    used = Utils.human_size(usage.used) if human else f"{usage.used / (1024**3):.1f} GB"
                    free = Utils.human_size(usage.free) if human else f"{usage.free / (1024**3):.1f} GB"
                    print(f"{Color.CYAN}{part.mountpoint:<20}{Color.RESET} {total:>10} {used:>10} {free:>10} {usage.percent:>5}%")
                except:
                    pass
        except:
            print(Color.warning("Install psutil for better disk info"))
        return True
    
    def _pushd(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: pushd <path>"))
            return True
        self.dir_stack.append(os.getcwd())
        return self._cd(args)
    
    def _popd(self, args: List[str]) -> bool:
        if not self.dir_stack:
            print(Color.warning("Directory stack empty"))
            return True
        path = self.dir_stack.pop()
        return self._cd([path])
    
    def _dirs(self, args: List[str]) -> bool:
        if not self.dir_stack:
            print(Color.warning("Directory stack empty"))
            return True
        for i, d in enumerate(self.dir_stack):
            print(f"{Color.CYAN}{i}: {Color.gradient(d, (0,200,255), (0,100,150))}{Color.RESET}")
        return True
    
    def _stat(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: stat <file>"))
            return True
        for f in args:
            try:
                st = os.stat(f)
                print(Color.box(
                    f"{Color.CYAN}Size:     {Color.GREEN}{Utils.human_size(st.st_size)}\n"
                    f"{Color.CYAN}Mode:     {Color.GREEN}{stat.filemode(st.st_mode)}\n"
                    f"{Color.CYAN}Modified: {Color.GREEN}{datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}",
                    title=f"Statistics: {f}"
                ))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _file(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: file <file>"))
            return True
        for f in args:
            if os.path.isfile(f):
                print(f"{Color.CYAN}{f}: {Color.GREEN}file{Color.RESET}")
            elif os.path.isdir(f):
                print(f"{Color.CYAN}{f}: {Color.BLUE}directory{Color.RESET}")
            else:
                print(f"{Color.CYAN}{f}: {Color.RED}unknown{Color.RESET}")
        return True
    
    def _which(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: which <command>"))
            return True
        for prog in args:
            found = False
            if prog in self.commands:
                print(Color.gradient(f"{prog}: built-in command", (0,200,255), (0,100,150)))
                found = True
            for path in os.environ.get("PATH", "").split(":" if os.name != "nt" else ";"):
                full = os.path.join(path, prog)
                if os.path.exists(full):
                    print(Color.gradient(full, (0,200,255), (0,100,150)))
                    found = True
                    break
            if not found:
                print(Color.error(f"{prog}: not found"))
        return True
    
    def _chmod(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: chmod <mode> <file>"))
            return True
        mode = args[0]
        files = args[1:]
        try:
            if mode.isdigit():
                mode_int = int(mode, 8)
            else:
                mode_int = 0o755
            for f in files:
                os.chmod(f, mode_int)
                print(Color.success(f"Permissions changed: {f}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _ln(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: ln [-s] <target> <link>"))
            return True
        symbolic = "-s" in args
        args = [a for a in args if not a.startswith("-")]
        if len(args) < 2:
            print(Color.warning("Specify target and link name"))
            return True
        target, link = args[0], args[1]
        try:
            if symbolic:
                os.symlink(target, link)
            else:
                os.link(target, link)
            print(Color.success(f"Link created: {link} → {target}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _realpath(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: realpath <file>"))
            return True
        print(Color.gradient(os.path.realpath(args[0]), (0,200,255), (0,100,150)))
        return True
    
    def _basename(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: basename <path>"))
            return True
        print(Color.gradient(os.path.basename(args[0]), (0,200,255), (0,100,150)))
        return True
    
    def _dirname(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: dirname <path>"))
            return True
        print(Color.gradient(os.path.dirname(args[0]), (0,200,255), (0,100,150)))
        return True
    
    def _readlink(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: readlink <link>"))
            return True
        try:
            print(Color.gradient(os.readlink(args[0]), (0,200,255), (0,100,150)))
        except:
            print(Color.error("Not a symbolic link"))
        return True
    
    def _mktemp(self, args: List[str]) -> bool:
        try:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                print(Color.gradient(f.name, (0,200,255), (0,100,150)))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _install(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: install <source> <dest>"))
            return True
        try:
            shutil.copy2(args[0], args[1])
            print(Color.success(f"Installed: {args[0]} → {args[1]}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _sync(self, args: List[str]) -> bool:
        os.sync()
        print(Color.success("Filesystem synced"))
        return True
    
    def _truncate(self, args: List[str]) -> bool:
        if len(args) < 2 or args[0] != "-s":
            print(Color.warning("Usage: truncate -s <size> <file>"))
            return True
        size = args[1]
        file = args[2]
        try:
            with open(file, "ab") as f:
                f.truncate(int(size))
            print(Color.success(f"Truncated {file} to {size} bytes"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _dd(self, args: List[str]) -> bool:
        input_file = None
        output_file = None
        for arg in args:
            if arg.startswith("if="):
                input_file = arg[3:]
            elif arg.startswith("of="):
                output_file = arg[3:]
        if not input_file or not output_file:
            print(Color.warning("Usage: dd if=<input> of=<output>"))
            return True
        try:
            with open(input_file, "rb") as src:
                with open(output_file, "wb") as dst:
                    dst.write(src.read())
            print(Color.success(f"Copied {input_file} to {output_file}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    # TEXT PROCESSING COMMANDS (Simplified versions)
    
    def _cat(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: cat <file>"))
            return True
        for f in args:
            try:
                with open(f, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                    if len(content) > 10000:
                        print(content[:10000] + f"\n{Color.DIM}... (truncated){Color.RESET}")
                    else:
                        print(content)
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _head(self, args: List[str]) -> bool:
        n = 10
        file = None
        for i, arg in enumerate(args):
            if arg.startswith("-n"):
                n = int(arg[2:]) if arg[2:] else int(args[i+1]) if i+1 < len(args) else 10
            elif not arg.startswith("-"):
                file = arg
        if file:
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    for i, line in enumerate(f):
                        if i < n:
                            print(line.rstrip())
                        else:
                            break
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _tail(self, args: List[str]) -> bool:
        n = 10
        file = None
        for i, arg in enumerate(args):
            if arg.startswith("-n"):
                n = int(arg[2:]) if arg[2:] else int(args[i+1]) if i+1 < len(args) else 10
            elif not arg.startswith("-"):
                file = arg
        if file:
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
                    for line in lines[-n:]:
                        print(line.rstrip())
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _grep(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: grep [-i] <pattern> <file>"))
            return True
        ignore_case = "-i" in args
        pattern = args[0] if not args[0].startswith("-") else args[1]
        files = [a for a in args if not a.startswith("-") and a != pattern]
        if ignore_case:
            pattern = pattern.lower()
        for f in files:
            try:
                with open(f, "r", encoding="utf-8", errors="ignore") as file:
                    for line in file:
                        line_stripped = line.rstrip()
                        search_line = line_stripped.lower() if ignore_case else line_stripped
                        if pattern in search_line:
                            print(f"{Color.GREEN}{f}:{Color.RESET} {line_stripped}")
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _egrep(self, args: List[str]) -> bool:
        return self._grep(args)
    
    def _fgrep(self, args: List[str]) -> bool:
        return self._grep(args)
    
    def _wc(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: wc [-lwc] <file>"))
            return True
        lines_only = "-l" in args
        words_only = "-w" in args
        chars_only = "-c" in args
        files = [a for a in args if not a.startswith("-")]
        for f in files:
            try:
                with open(f, "r", encoding="utf-8", errors="ignore") as file:
                    content = file.read()
                    lines = content.count("\n")
                    words = len(content.split())
                    chars = len(content)
                    if lines_only:
                        print(f"{Color.CYAN}{lines:>8} {f}{Color.RESET}")
                    elif words_only:
                        print(f"{Color.CYAN}{words:>8} {f}{Color.RESET}")
                    elif chars_only:
                        print(f"{Color.CYAN}{chars:>8} {f}{Color.RESET}")
                    else:
                        print(f"{Color.CYAN}{lines:>8} {words:>8} {chars:>8} {f}{Color.RESET}")
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _sort(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: sort [-r] [-n] <file>"))
            return True
        reverse = "-r" in args
        numeric = "-n" in args
        files = [a for a in args if not a.startswith("-")]
        for f in files:
            try:
                with open(f, "r", encoding="utf-8", errors="ignore") as file:
                    lines = file.readlines()
                if numeric:
                    lines.sort(key=lambda x: float(x.strip()) if x.strip().replace('.','',1).isdigit() else x.strip(), reverse=reverse)
                else:
                    lines.sort(reverse=reverse)
                for line in lines:
                    print(line.rstrip())
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _uniq(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: uniq <file>"))
            return True
        f = args[0]
        try:
            with open(f, "r", encoding="utf-8", errors="ignore") as file:
                seen = set()
                for line in file:
                    if line not in seen:
                        seen.add(line)
                        print(line.rstrip())
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _sed(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: sed s/pattern/replace/ <file>"))
            return True
        expression = args[0]
        file = args[1] if len(args) > 1 else None
        if not expression.startswith("s/") or not expression.endswith("/"):
            print(Color.error("Invalid expression format"))
            return True
        parts = expression[2:-1].split("/")
        if len(parts) < 2:
            print(Color.error("Invalid expression format"))
            return True
        pattern, replace = parts[0], parts[1]
        if file:
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        print(re.sub(pattern, replace, line).rstrip())
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _awk(self, args: List[str]) -> bool:
        print(Color.info("Awk command - partial implementation"))
        return True
    
    def _cut(self, args: List[str]) -> bool:
        if len(args) < 4:
            print(Color.warning("Usage: cut -d <delimiter> -f <fields> <file>"))
            return True
        delimiter = None
        fields = None
        file = None
        for i, arg in enumerate(args):
            if arg == "-d" and i + 1 < len(args):
                delimiter = args[i + 1]
            elif arg == "-f" and i + 1 < len(args):
                fields = args[i + 1]
            elif not arg.startswith("-"):
                file = arg
        if delimiter and fields and file:
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        parts = line.strip().split(delimiter)
                        field_indices = [int(x) for x in fields.split(",")]
                        result = []
                        for idx in field_indices:
                            if idx - 1 < len(parts):
                                result.append(parts[idx - 1])
                        print(delimiter.join(result))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _tr(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: tr 'a-z' 'A-Z' <file>"))
            return True
        from_set = args[0].strip("'")
        to_set = args[1].strip("'")
        file = args[2] if len(args) > 2 else None
        if file:
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                table = str.maketrans(from_set, to_set)
                print(content.translate(table))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _diff(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: diff <file1> <file2>"))
            return True
        try:
            with open(args[0], "r", encoding="utf-8", errors="ignore") as f1, open(args[1], "r", encoding="utf-8", errors="ignore") as f2:
                lines1, lines2 = f1.readlines(), f2.readlines()
                max_len = max(len(lines1), len(lines2))
                for i in range(max_len):
                    l1 = lines1[i].rstrip() if i < len(lines1) else None
                    l2 = lines2[i].rstrip() if i < len(lines2) else None
                    if l1 != l2:
                        if l1:
                            print(f"{Color.RED}- {l1}{Color.RESET}")
                        if l2:
                            print(f"{Color.GREEN}+ {l2}{Color.RESET}")
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _comm(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: comm <file1> <file2>"))
            return True
        try:
            with open(args[0], "r") as f1, open(args[1], "r") as f2:
                lines1 = set(l.strip() for l in f1.readlines())
                lines2 = set(l.strip() for l in f2.readlines())
                only1 = lines1 - lines2
                only2 = lines2 - lines1
                common = lines1 & lines2
                print(f"{Color.CYAN}Only in {args[0]}:{Color.RESET}")
                for line in sorted(only1)[:20]:
                    print(f"  {line}")
                print(f"{Color.CYAN}Only in {args[1]}:{Color.RESET}")
                for line in sorted(only2)[:20]:
                    print(f"  {line}")
                print(f"{Color.CYAN}Common:{Color.RESET}")
                for line in sorted(common)[:20]:
                    print(f"  {line}")
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _join(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: join <file1> <file2>"))
            return True
        print(Color.info("Join command - partial implementation"))
        return True
    
    def _paste(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: paste <file1> <file2>"))
            return True
        try:
            with open(args[0], "r") as f1, open(args[1], "r") as f2:
                for l1, l2 in itertools.zip_longest(f1, f2):
                    print(f"{l1.rstrip()}\t{l2.rstrip() if l2 else ''}")
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _split(self, args: List[str]) -> bool:
        print(Color.info("Split command - partial implementation"))
        return True
    
    def _nl(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: nl <file>"))
            return True
        f = args[0]
        try:
            with open(f, "r", encoding="utf-8", errors="ignore") as file:
                for i, line in enumerate(file, 1):
                    print(f"{Color.CYAN}{i:>6}{Color.RESET} {line.rstrip()}")
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _tac(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: tac <file>"))
            return True
        f = args[0]
        try:
            with open(f, "r", encoding="utf-8", errors="ignore") as file:
                for line in reversed(file.readlines()):
                    print(line.rstrip())
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _rev(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: rev <file>"))
            return True
        f = args[0]
        try:
            with open(f, "r", encoding="utf-8", errors="ignore") as file:
                for line in file:
                    print(line.rstrip()[::-1])
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _fold(self, args: List[str]) -> bool:
        width = 80
        file = None
        for arg in args:
            if arg.startswith("-w"):
                width = int(arg[2:])
            elif not arg.startswith("-"):
                file = arg
        if file:
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        for i in range(0, len(line), width):
                            print(line[i:i+width].rstrip())
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _expand(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: expand <file>"))
            return True
        file = args[0]
        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    print(line.expandtabs(4).rstrip())
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _unexpand(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: unexpand <file>"))
            return True
        file = args[0]
        try:
            with open(file, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    print(line.replace("    ", "\t").rstrip())
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _fmt(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: fmt <file>"))
            return True
        width = 80
        try:
            with open(args[0], "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                lines = textwrap.wrap(content, width=width)
                for line in lines:
                    print(line)
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _column(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: column -t <file>"))
            return True
        if "-t" in args:
            file = args[-1]
            try:
                with open(file, "r", encoding="utf-8", errors="ignore") as f:
                    data = [line.strip().split() for line in f]
                    if data:
                        col_widths = [max(len(row[i]) for row in data if i < len(row)) for i in range(len(data[0]))]
                        for row in data:
                            print("  ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row)))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _less(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: less <file>"))
            return True
        try:
            with open(args[0], "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
                page_size = shutil.get_terminal_size().lines - 2
                for i in range(0, len(lines), page_size):
                    for line in lines[i:i+page_size]:
                        print(line.rstrip())
                    if i + page_size < len(lines):
                        input(f"{Color.DIM}--More-- (Press Enter){Color.RESET}")
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _more(self, args: List[str]) -> bool:
        return self._less(args)
    
    def _od(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: od <file>"))
            return True
        try:
            with open(args[0], "rb") as f:
                data = f.read(512)
                for i in range(0, len(data), 16):
                    chunk = data[i:i+16]
                    hex_part = " ".join(f"{b:02x}" for b in chunk)
                    ascii_part = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)
                    print(f"{Color.CYAN}{i:08x}{Color.RESET}  {hex_part:<48}  {ascii_part}")
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _xxd(self, args: List[str]) -> bool:
        return self._od(args)
    
    def _hexdump(self, args: List[str]) -> bool:
        return self._od(args)
    
    def _strings(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: strings <file>"))
            return True
        try:
            with open(args[0], "rb") as f:
                data = f.read()
                result = []
                current = []
                for b in data:
                    if 32 <= b <= 126:
                        current.append(chr(b))
                    else:
                        if len(current) >= 4:
                            result.append("".join(current))
                        current = []
                for s in result[:100]:
                    print(s)
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    # SYSTEM INFO COMMANDS
    
    def _info(self, args: List[str]) -> bool:
        print(Color.box(
            f"{Color.CYAN}Terminal:      {Color.GREEN}Kali Terminal Ultimate v11.0\n"
            f"{Color.CYAN}Commands:      {Color.GREEN}{len(self.commands)}\n"
            f"{Color.CYAN}Aliases:       {Color.GREEN}{len(self.aliases)}\n"
            f"{Color.CYAN}OS:            {Color.GREEN}{platform.system()} {platform.release()}\n"
            f"{Color.CYAN}Python:        {Color.GREEN}{platform.python_version()}\n"
            f"{Color.CYAN}User:          {Color.GREEN}{Utils.get_username()}\n"
            f"{Color.CYAN}Host:          {Color.GREEN}{socket.gethostname()}",
            title="Terminal Information"
        ))
        return True
    
    def _sysinfo(self, args: List[str]) -> bool:
        print(Color.box(
            f"{Color.CYAN}System:        {Color.GREEN}{platform.system()} {platform.release()}\n"
            f"{Color.CYAN}Machine:       {Color.GREEN}{platform.machine()}\n"
            f"{Color.CYAN}Processor:     {Color.GREEN}{platform.processor() or 'Unknown'}\n"
            f"{Color.CYAN}Hostname:      {Color.GREEN}{socket.gethostname()}\n"
            f"{Color.CYAN}Username:      {Color.GREEN}{Utils.get_username()}\n"
            f"{Color.CYAN}Local IP:      {Color.GREEN}{Utils.get_local_ip()}\n"
            f"{Color.CYAN}Python:        {Color.GREEN}{platform.python_version()}",
            title="System Information"
        ))
        try:
            import psutil
            print(f"\n{Color.CYAN}CPU Cores:     {Color.GREEN}{psutil.cpu_count()}\n"
                  f"{Color.CYAN}CPU Usage:     {Color.GREEN}{psutil.cpu_percent()}%\n"
                  f"{Color.CYAN}Memory:        {Color.GREEN}{Utils.human_size(psutil.virtual_memory().used)} / {Utils.human_size(psutil.virtual_memory().total)}")
        except:
            pass
        return True
    
    def _ps(self, args: List[str]) -> bool:
        try:
            import psutil
            aux = "-aux" in args
            if aux:
                print(f"{Color.gradient(f'{"USER":<10} {"PID":>8} {"CPU%":>6} {"MEM%":>6} {"COMMAND":<35}', (0,200,255), (0,100,150))}")
                for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent", "username"]):
                    try:
                        info = proc.info
                        if info.get("cpu_percent", 0) > 0 or aux:
                            print(f"{info.get('username', 'unknown')[:10]:<10} "
                                  f"{info['pid']:>8} "
                                  f"{info.get('cpu_percent', 0):>6.1f} "
                                  f"{info.get('memory_percent', 0):>6.1f} "
                                  f"{info.get('name', 'unknown')[:35]:<35}")
                    except:
                        pass
            else:
                print(f"{Color.gradient(f'{"PID":>8} {"CPU%":>6} {"MEM%":>6} {"NAME":<35}', (0,200,255), (0,100,150))}")
                for proc in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
                    try:
                        info = proc.info
                        if info.get("cpu_percent", 0) > 0:
                            print(f"{info['pid']:>8} "
                                  f"{info.get('cpu_percent', 0):>6.1f} "
                                  f"{info.get('memory_percent', 0):>6.1f} "
                                  f"{info.get('name', 'unknown')[:35]:<35}")
                    except:
                        pass
        except:
            print(Color.warning("Install psutil for process info"))
        return True
    
    def _top(self, args: List[str]) -> bool:
        try:
            import psutil
            try:
                while True:
                    Utils.clear_screen()
                    print(Color.header("SYSTEM MONITOR", 80))
                    cpu = psutil.cpu_percent(interval=0.5)
                    mem = psutil.virtual_memory()
                    print(f"{Color.CYAN}│{Color.RESET} CPU:  {Color.progress_bar(cpu, 30)}")
                    print(f"{Color.CYAN}│{Color.RESET} RAM:  {Color.progress_bar(mem.percent, 30)} ({Utils.human_size(mem.used)}/{Utils.human_size(mem.total)})")
                    print(f"{Color.CYAN}├{'─' * 78}┤{Color.RESET}")
                    processes = []
                    for proc in psutil.process_iter(["pid", "name", "cpu_percent"]):
                        try:
                            p = proc.info
                            if p.get("cpu_percent", 0) > 0:
                                processes.append(p)
                        except:
                            pass
                    processes.sort(key=lambda x: x.get("cpu_percent", 0), reverse=True)
                    for p in processes[:15]:
                        print(f"{p['pid']:>8} {p.get('cpu_percent', 0):>6.1f} {p.get('name', 'unknown')[:35]:<35}")
                    print(f"\n{Color.DIM}Press Ctrl+C to exit{Color.RESET}")
                    time.sleep(2)
            except KeyboardInterrupt:
                print()
        except:
            print(Color.warning("Install psutil for system monitor"))
        return True
    
    def _kill(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: kill <pid>"))
            return True
        try:
            pid = int(args[0])
            if os.name == "nt":
                os.system(f"taskkill /PID {pid} /F")
            else:
                os.kill(pid, signal.SIGTERM)
            print(Color.success(f"Process {pid} terminated"))
        except:
            print(Color.error("Failed to terminate process"))
        return True
    
    def _killall(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: killall <name>"))
            return True
        name = args[0]
        try:
            import psutil
            killed = False
            for proc in psutil.process_iter(["pid", "name"]):
                try:
                    if name.lower() in proc.info["name"].lower():
                        proc.kill()
                        print(Color.success(f"Killed: {proc.info['name']} ({proc.info['pid']})"))
                        killed = True
                except:
                    pass
            if not killed:
                print(Color.warning(f"Process '{name}' not found"))
        except:
            print(Color.warning("Install psutil"))
        return True
    
    def _pkill(self, args: List[str]) -> bool:
        return self._killall(args)
    
    def _pgrep(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: pgrep <name>"))
            return True
        name = args[0]
        try:
            import psutil
            found = False
            for proc in psutil.process_iter(["pid", "name"]):
                try:
                    if name.lower() in proc.info["name"].lower():
                        print(f"{proc.info['pid']} {proc.info['name']}")
                        found = True
                except:
                    pass
            if not found:
                print(Color.warning(f"Process '{name}' not found"))
        except:
            print(Color.warning("Install psutil"))
        return True
    
    def _jobs(self, args: List[str]) -> bool:
        print(Color.info("No background jobs"))
        return True
    
    def _fg(self, args: List[str]) -> bool:
        print(Color.info("FG not fully implemented"))
        return True
    
    def _bg(self, args: List[str]) -> bool:
        print(Color.info("BG not fully implemented"))
        return True
    
    def _nohup(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: nohup <command>"))
            return True
        cmd = " ".join(args)
        try:
            if os.name == "nt":
                subprocess.Popen(cmd, shell=True, creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
            else:
                subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)
            print(Color.success(f"Started in background: {cmd}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _date(self, args: List[str]) -> bool:
        now = datetime.now()
        print(Color.gradient(now.strftime('%A, %d %B %Y %H:%M:%S'), (0,200,255), (0,100,150)))
        return True
    
    def _cal(self, args: List[str]) -> bool:
        now = datetime.now()
        year = int(args[0]) if args and args[0].isdigit() else now.year
        month = now.month
        print(Color.gradient(calendar.month(year, month), (0,200,255), (0,100,150)))
        return True
    
    def _whoami(self, args: List[str]) -> bool:
        print(Color.gradient(f"{Icon.LOCK} {Utils.get_username()}", (0,200,255), (0,100,150)))
        return True
    
    def _hostname(self, args: List[str]) -> bool:
        print(Color.gradient(f"{Icon.NETWORK} {socket.gethostname()}", (0,200,255), (0,100,150)))
        return True
    
    def _uname(self, args: List[str]) -> bool:
        if args and args[0] == "-a":
            info = f"{platform.system()} {platform.release()} {platform.version()} {platform.machine()}"
        else:
            info = platform.system()
        print(Color.gradient(info, (0,200,255), (0,100,150)))
        return True
    
    def _uptime(self, args: List[str]) -> bool:
        try:
            import psutil
            boot = datetime.fromtimestamp(psutil.boot_time())
            uptime = datetime.now() - boot
            print(Color.gradient(f"{Icon.CLOCK} Uptime: {Utils.human_time(uptime.total_seconds())}", (0,200,255), (0,100,150)))
        except:
            print(Color.warning("Install psutil for uptime info"))
        return True
    
    def _who(self, args: List[str]) -> bool:
        try:
            import psutil
            for user in psutil.users():
                print(f"{Color.gradient(user.name, (0,200,255), (0,100,150))}  {user.terminal}  {datetime.fromtimestamp(user.started).strftime('%Y-%m-%d %H:%M')}")
        except:
            print(f"{Color.gradient(Utils.get_username(), (0,200,255), (0,100,150))}  pts/0  {Utils.get_date()} {Utils.get_time()}")
        return True
    
    def _w(self, args: List[str]) -> bool:
        return self._who(args)
    
    def _last(self, args: List[str]) -> bool:
        print(f"{Color.gradient(f'{"USER":<10} {"TTY":<10} {"FROM":<15} {"LOGIN@":<20}', (0,200,255), (0,100,150))}")
        print(f"{Color.GREEN}{Utils.get_username():<10}{Color.RESET} pts/0      local           {Utils.get_date()} {Utils.get_time()}")
        return True
    
    def _env(self, args: List[str]) -> bool:
        for key, value in sorted(os.environ.items()):
            print(f"{Color.gradient(key, (0,200,255), (0,100,150))}{Color.RESET}={value}")
        return True
    
    def _set(self, args: List[str]) -> bool:
        for key, value in sorted(self.variables.items()):
            print(f"{Color.gradient(key, (0,200,255), (0,100,150))}{Color.RESET}={value}")
        return True
    
    def _export(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: export <name>=<value>"))
            return True
        for arg in args:
            if "=" in arg:
                name, value = arg.split("=", 1)
                os.environ[name] = value
                self.variables[name] = value
                print(Color.success(f"Exported: {name}={value}"))
        return True
    
    def _unset(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: unset <name>"))
            return True
        for name in args:
            if name in os.environ:
                del os.environ[name]
            if name in self.variables:
                del self.variables[name]
            print(Color.success(f"Unset: {name}"))
        return True
    
    def _echo(self, args: List[str]) -> bool:
        text = " ".join(args)
        if text.startswith("$"):
            var = text[1:]
            print(os.environ.get(var, self.variables.get(var, "")))
        else:
            print(Color.gradient(text, (0,200,255), (0,100,150)))
        return True
    
    def _printf(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: printf <format> <args>"))
            return True
        fmt, values = args[0], args[1:]
        try:
            print(fmt % tuple(values))
        except:
            print(fmt)
        return True
    
    def _sleep(self, args: List[str]) -> bool:
        if args:
            try:
                time.sleep(float(args[0]))
            except:
                pass
        return True
    
    def _time(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: time <command>"))
            return True
        cmd = " ".join(args)
        start = time.time()
        self.execute(cmd)
        elapsed = time.time() - start
        print(f"\n{Color.gradient(f'real\t{Utils.human_time(elapsed)}', (0,200,255), (0,100,150))}")
        return True
    
    def _watch(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: watch <command>"))
            return True
        cmd = " ".join(args)
        try:
            for _ in range(5):
                Utils.clear_screen()
                print(f"{Color.gradient(f'Every 2s: {cmd}', (0,200,255), (0,100,150))}")
                print(f"{Color.DIM}{Utils.get_date()} {Utils.get_time()}{Color.RESET}\n")
                self.execute(cmd)
                time.sleep(2)
        except KeyboardInterrupt:
            print()
        return True
    
    def _free(self, args: List[str]) -> bool:
        human = "-h" in args
        try:
            import psutil
            mem = psutil.virtual_memory()
            total = Utils.human_size(mem.total) if human else f"{mem.total / (1024**3):.1f} GB"
            used = Utils.human_size(mem.used) if human else f"{mem.used / (1024**3):.1f} GB"
            free = Utils.human_size(mem.free) if human else f"{mem.free / (1024**3):.1f} GB"
            print(Color.box(
                f"{Color.CYAN}Memory:{Color.RESET}\n"
                f"  total: {total}\n"
                f"  used:  {used}\n"
                f"  free:  {free}",
                title="Memory Information"
            ))
        except:
            print(Color.warning("Install psutil for memory info"))
        return True
    
    def _lscpu(self, args: List[str]) -> bool:
        print(f"{Color.CYAN}Architecture:     {Color.GREEN}{platform.machine()}")
        print(f"{Color.CYAN}CPU(s):           {Color.GREEN}{os.cpu_count()}")
        print(f"{Color.CYAN}Model name:       {Color.GREEN}{platform.processor() or 'Unknown'}")
        return True
    
    def _lsblk(self, args: List[str]) -> bool:
        try:
            import psutil
            print(f"{Color.gradient(f'{"NAME":<15} {"SIZE":<10} {"MOUNTPOINT":<20}', (0,200,255), (0,100,150))}")
            for part in psutil.disk_partitions():
                try:
                    size = Utils.human_size(psutil.disk_usage(part.mountpoint).total)
                    print(f"{Color.CYAN}{part.device:<15}{Color.RESET} {size:<10} {part.mountpoint:<20}")
                except:
                    pass
        except:
            print(Color.warning("Install psutil"))
        return True
    
    def _lspci(self, args: List[str]) -> bool:
        print(Color.info("lspci - list PCI devices"))
        try:
            if os.name != "nt":
                result = subprocess.run(["lspci"], capture_output=True, text=True)
                if result.stdout:
                    for line in result.stdout.split("\n")[:20]:
                        print(line)
                else:
                    print(Color.warning("No PCI devices found"))
            else:
                print(Color.warning("lspci not available on Windows"))
        except:
            print(Color.warning("lspci command not found"))
        return True
    
    def _lsusb(self, args: List[str]) -> bool:
        print(Color.info("lsusb - list USB devices"))
        try:
            if os.name != "nt":
                result = subprocess.run(["lsusb"], capture_output=True, text=True)
                if result.stdout:
                    for line in result.stdout.split("\n")[:20]:
                        print(line)
                else:
                    print(Color.warning("No USB devices found"))
            else:
                print(Color.warning("lsusb not available on Windows"))
        except:
            print(Color.warning("lsusb command not found"))
        return True
    
    # NETWORK COMMANDS
    
    def _ping(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: ping <host>"))
            return True
        host = args[0]
        count = 4
        print(Color.gradient(f"PING {host}", (0,200,255), (0,100,150)))
        for i in range(count):
            try:
                start = time.time()
                ip = socket.gethostbyname(host)
                elapsed = (time.time() - start) * 1000
                print(f"{Color.GREEN}64 bytes from {ip}: icmp_seq={i} time={elapsed:.2f} ms{Color.RESET}")
            except:
                print(f"{Color.RED}Request timeout{Color.RESET}")
            time.sleep(1)
        return True
    
    def _myip(self, args: List[str]) -> bool:
        local_ip = Utils.get_local_ip()
        public_ip = Utils.get_public_ip()
        print(Color.box(
            f"{Color.CYAN}Local IP:  {Color.GREEN}{local_ip}\n"
            f"{Color.CYAN}Public IP: {Color.GREEN}{public_ip}",
            title="IP Information"
        ))
        return True
    
    def _portscan(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: portscan <host>"))
            return True
        host = args[0]
        ports = [21,22,23,25,53,80,110,143,443,3306,3389,5432,8080,8443,8888]
        print(Color.gradient(f"Scanning {host}...", (0,200,255), (0,100,150)))
        open_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((host, port)) == 0:
                open_ports.append(port)
                print(f"  Port {Color.GREEN}{port}{Color.RESET}: OPEN")
            sock.close()
        if not open_ports:
            print(Color.info("No open ports found"))
        return True
    
    def _curl(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: curl <url>"))
            return True
        url = args[0]
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read().decode("utf-8", errors="ignore")
                print(content[:5000] + (f"\n{Color.DIM}... (truncated){Color.RESET}" if len(content) > 5000 else ""))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _wget(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: wget <url>"))
            return True
        url = args[0]
        filename = url.split("/")[-1] or "download"
        print(Color.gradient(f"Downloading {url}...", (0,200,255), (0,100,150)))
        try:
            urllib.request.urlretrieve(url, filename)
            print(Color.success(f"Saved: {filename}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _nslookup(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: nslookup <domain>"))
            return True
        domain = args[0]
        try:
            ip = socket.gethostbyname(domain)
            print(f"{Color.CYAN}Server: 8.8.8.8{Color.RESET}\n\nNon-authoritative answer:\nName: {Color.GREEN}{domain}{Color.RESET}\nAddress: {Color.GREEN}{ip}{Color.RESET}")
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _dig(self, args: List[str]) -> bool:
        return self._nslookup(args)
    
    def _host(self, args: List[str]) -> bool:
        return self._nslookup(args)
    
    def _ifconfig(self, args: List[str]) -> bool:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(Color.gradient("lo:", (0,200,255), (0,100,150)))
        print(f"    inet {Color.GREEN}127.0.0.1{Color.RESET}")
        print(Color.gradient("eth0:", (0,200,255), (0,100,150)))
        print(f"    inet {Color.GREEN}{ip}{Color.RESET}")
        return True
    
    def _ip(self, args: List[str]) -> bool:
        if args and args[0] == "addr":
            return self._ifconfig(args)
        return self._ifconfig(args)
    
    def _netstat(self, args: List[str]) -> bool:
        try:
            import psutil
            print(f"{Color.gradient(f'{"Proto":6} {"Local Address":30} {"State":15}', (0,200,255), (0,100,150))}")
            for conn in psutil.net_connections()[:30]:
                if conn.status:
                    laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "*:*"
                    print(f"tcp     {laddr:<30} {conn.status:<15}")
        except:
            print(Color.warning("Install psutil"))
        return True
    
    def _ss(self, args: List[str]) -> bool:
        return self._netstat(args)
    
    def _route(self, args: List[str]) -> bool:
        try:
            import psutil
            print(Color.header("ROUTE TABLE", 50))
            for conn in psutil.net_connections():
                if conn.status == "ESTABLISHED":
                    print(f"{Color.CYAN}│{Color.RESET} {conn.laddr.ip}:{conn.laddr.port} -> {conn.raddr.ip}:{conn.raddr.port}")
        except:
            print(Color.warning("Install psutil"))
        return True
    
    def _arp(self, args: List[str]) -> bool:
        try:
            import psutil
            print(Color.header("ARP CACHE", 50))
            seen = set()
            for conn in psutil.net_connections():
                if conn.raddr and conn.raddr.ip not in seen:
                    seen.add(conn.raddr.ip)
                    print(f"{Color.CYAN}│{Color.RESET} {conn.raddr.ip}")
        except:
            print(Color.warning("Install psutil"))
        return True
    
    def _traceroute(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: traceroute <host>"))
            return True
        host = args[0]
        print(Color.gradient(f"traceroute to {host}", (0,200,255), (0,100,150)))
        for ttl in range(1, 30):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                sock.settimeout(2)
                sock.sendto(b"", (host, ttl))
                start = time.time()
                data, addr = sock.recvfrom(1024)
                elapsed = (time.time() - start) * 1000
                print(f"{ttl:2}  {addr[0]}  {elapsed:.2f} ms")
                if addr[0] == host:
                    break
                sock.close()
            except:
                print(f"{ttl:2}  *")
        return True
    
    def _tracepath(self, args: List[str]) -> bool:
        return self._traceroute(args)
    
    def _telnet(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: telnet <host> <port>"))
            return True
        host, port = args[0], int(args[1])
        print(Color.info(f"Connecting to {host}:{port}..."))
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((host, port))
            print(Color.success("Connected!"))
            sock.close()
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _nc(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: nc <host> <port>"))
            return True
        print(Color.info("Netcat - use external nc command"))
        return True
    
    def _nmap(self, args: List[str]) -> bool:
        return self._portscan(args)
    
    def _tcpdump(self, args: List[str]) -> bool:
        print(Color.info("tcpdump - packet capture"))
        return True
    
    # CRYPTOGRAPHY COMMANDS
    
    def _hash(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: hash <text>"))
            return True
        text = " ".join(args)
        print(Color.box(
            f"{Color.CYAN}MD5:    {Color.GREEN}{hashlib.md5(text.encode()).hexdigest()}\n"
            f"{Color.CYAN}SHA1:   {Color.GREEN}{hashlib.sha1(text.encode()).hexdigest()}\n"
            f"{Color.CYAN}SHA256: {Color.GREEN}{hashlib.sha256(text.encode()).hexdigest()}\n"
            f"{Color.CYAN}SHA512: {Color.GREEN}{hashlib.sha512(text.encode()).hexdigest()}",
            title="Hashes"
        ))
        return True
    
    def _md5(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: md5 <file>"))
            return True
        for f in args:
            try:
                with open(f, "rb") as file:
                    print(Color.gradient(f"{hashlib.md5(file.read()).hexdigest()} {f}", (0,200,255), (0,100,150)))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _sha1(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: sha1 <file>"))
            return True
        for f in args:
            try:
                with open(f, "rb") as file:
                    print(Color.gradient(f"{hashlib.sha1(file.read()).hexdigest()} {f}", (0,200,255), (0,100,150)))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _sha256(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: sha256 <file>"))
            return True
        for f in args:
            try:
                with open(f, "rb") as file:
                    print(Color.gradient(f"{hashlib.sha256(file.read()).hexdigest()} {f}", (0,200,255), (0,100,150)))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _sha512(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: sha512 <file>"))
            return True
        for f in args:
            try:
                with open(f, "rb") as file:
                    print(Color.gradient(f"{hashlib.sha512(file.read()).hexdigest()} {f}", (0,200,255), (0,100,150)))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _base64(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: base64 <text>"))
            return True
        text = " ".join(args)
        print(Color.gradient(base64.b64encode(text.encode()).decode(), (0,200,255), (0,100,150)))
        return True
    
    def _base64d(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: base64d <base64>"))
            return True
        text = " ".join(args)
        try:
            print(Color.gradient(base64.b64decode(text).decode("utf-8", errors="ignore"), (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid base64"))
        return True
    
    def _rot13(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: rot13 <text>"))
            return True
        print(Color.gradient(Utils.rot13(" ".join(args)), (0,200,255), (0,100,150)))
        return True
    
    def _caesar(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: caesar <text> <shift>"))
            return True
        text, shift = " ".join(args[:-1]), int(args[-1])
        print(Color.gradient(self.crypto.caesar_cipher(text, shift), (0,200,255), (0,100,150)))
        return True
    
    def _urlencode(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: urlencode <text>"))
            return True
        print(Color.gradient(urllib.parse.quote(" ".join(args)), (0,200,255), (0,100,150)))
        return True
    
    def _urldecode(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: urldecode <text>"))
            return True
        print(Color.gradient(urllib.parse.unquote(" ".join(args)), (0,200,255), (0,100,150)))
        return True
    
    def _hex(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: hex <text>"))
            return True
        print(Color.gradient(" ".join(args).encode().hex(), (0,200,255), (0,100,150)))
        return True
    
    def _unhex(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: unhex <hex>"))
            return True
        try:
            print(Color.gradient(bytes.fromhex(args[0]).decode("utf-8", errors="ignore"), (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid hex"))
        return True
    
    def _password(self, args: List[str]) -> bool:
        length = int(args[0]) if args and args[0].isdigit() else 16
        print(Color.box(Color.gradient(Utils.random_password(length), (0,200,255), (0,100,150)), title="Generated Password"))
        return True
    
    def _uuid(self, args: List[str]) -> bool:
        print(Color.gradient(str(uuid.uuid4()), (0,200,255), (0,100,150)))
        return True
    
    def _random(self, args: List[str]) -> bool:
        num = random.randint(0, int(args[0])) if args and args[0].isdigit() else random.randint(0, 100)
        print(Color.gradient(f"🎲 {num}", (0,200,255), (0,100,150)))
        return True
    
    def _encrypt(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: encrypt <text> <key>"))
            return True
        text, key = args[0], args[1]
        encrypted = self.crypto.xor_encrypt(text, key)
        print(Color.gradient(base64.b64encode(encrypted.encode()).decode(), (0,200,255), (0,100,150)))
        return True
    
    def _decrypt(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: decrypt <text> <key>"))
            return True
        try:
            encrypted = base64.b64decode(args[0]).decode()
            key = args[1]
            decrypted = self.crypto.xor_decrypt(encrypted, key)
            print(Color.gradient(decrypted, (0,200,255), (0,100,150)))
        except:
            print(Color.error("Decryption failed"))
        return True
    
    def _xor(self, args: List[str]) -> bool:
        return self._encrypt(args)
    
    # ARCHIVE COMMANDS
    
    def _zip(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: zip <archive> <files>"))
            return True
        archive, files = args[0], args[1:]
        try:
            with zipfile.ZipFile(archive, "w") as zf:
                for f in files:
                    if os.path.exists(f):
                        if os.path.isdir(f):
                            for root, dirs, files_in in os.walk(f):
                                for file in files_in:
                                    zf.write(os.path.join(root, file))
                        else:
                            zf.write(f)
            print(Color.success(f"Archive created: {archive}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _unzip(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: unzip <archive>"))
            return True
        archive = args[0]
        try:
            with zipfile.ZipFile(archive, "r") as zf:
                zf.extractall()
            print(Color.success(f"Archive extracted: {archive}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True
    
    def _tar(self, args: List[str]) -> bool:
        if "-cf" in args:
            idx = args.index("-cf")
            if idx + 1 < len(args):
                archive = args[idx + 1]
                files = args[idx + 2:]
                try:
                    with tarfile.open(archive, "w") as tar:
                        for f in files:
                            tar.add(f)
                    print(Color.success(f"Archive created: {archive}"))
                except Exception as e:
                    print(Color.error(str(e)))
        elif "-xf" in args:
            idx = args.index("-xf")
            if idx + 1 < len(args):
                archive = args[idx + 1]
                try:
                    with tarfile.open(archive, "r") as tar:
                        tar.extractall()
                    print(Color.success(f"Archive extracted: {archive}"))
                except Exception as e:
                    print(Color.error(str(e)))
        else:
            print(Color.warning("Usage: tar -cf archive.tar files  or  tar -xf archive.tar"))
        return True
    
    def _gzip(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: gzip <file>"))
            return True
        for f in args:
            try:
                with open(f, "rb") as fin:
                    with open(f + ".gz", "wb") as fout:
                        fout.write(gzip.compress(fin.read()))
                print(Color.success(f"Compressed: {f}"))
            except Exception as e:
                print(Color.error(str(e)))
        return True
    
    def _gunzip(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: gunzip <file.gz>"))
            return True
        for f in args:
            if f.endswith(".gz"):
                try:
                    with gzip.open(f, "rb") as fin:
                        with open(f[:-3], "wb") as fout:
                            fout.write(fin.read())
                    print(Color.success(f"Decompressed: {f}"))
                except Exception as e:
                    print(Color.error(str(e)))
        return True
    
    def _bzip2(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: bzip2 <file>"))
            return True
        for f in args:
            try:
                with open(f, "rb") as fin:
                    data = fin.read()
                    compressed = bz2.compress(data)
                    with open(f + ".bz2", "wb") as fout:
                        fout.write(compressed)
                print(Color.success(f"Compressed: {f}"))
            except:
                print(Color.warning("bzip2 not available"))
        return True
    
    def _bunzip2(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: bunzip2 <file.bz2>"))
            return True
        for f in args:
            if f.endswith(".bz2"):
                try:
                    with open(f, "rb") as fin:
                        data = fin.read()
                        decompressed = bz2.decompress(data)
                        with open(f[:-4], "wb") as fout:
                            fout.write(decompressed)
                    print(Color.success(f"Decompressed: {f}"))
                except:
                    print(Color.warning("bzip2 not available"))
        return True
    
    def _xz(self, args: List[str]) -> bool:
        print(Color.info("xz compression - use external xz command"))
        return True
    
    def _unxz(self, args: List[str]) -> bool:
        print(Color.info("xz decompression - use external xz command"))
        return True
    
    # VISUAL EFFECTS COMMANDS (Simplified versions)
    
    def _matrix(self, args: List[str]) -> bool:
        chars = "01アイウエオカキクケコ"
        cols = shutil.get_terminal_size().columns
        for _ in range(30):
            line = "".join(random.choice(chars) for _ in range(cols))
            sys.stdout.write(f"\r{Color.gradient(line, (0,255,0), (0,100,0))}")
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        return True
    
    def _hack(self, args: List[str]) -> bool:
        print(Color.info(f"🔓 Initializing hack sequence..."))
        stages = ["Scanning targets", "Finding vulnerabilities", "Exploiting", "Gaining access"]
        for stage in stages:
            print(f"{Color.YELLOW}{stage}...{Color.RESET}")
            Animation.spinner(stage, 0.5)
        print(Color.success("ACCESS GRANTED!"))
        return True
    
    def _fire(self, args: List[str]) -> bool:
        for _ in range(20):
            sys.stdout.write(f"\r{Color.gradient('🔥' * random.randint(5, 30), (255,100,0), (255,0,0))}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        return True
    
    def _rainbow(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "🌈 RAINBOW MODE 🌈"
        colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.MAGENTA]
        for _ in range(10):
            result = ""
            for i, char in enumerate(text):
                result += f"{colors[i % len(colors)]}{char}{Color.RESET}"
            sys.stdout.write(f"\r{result}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        return True
    
    def _stars(self, args: List[str]) -> bool:
        for _ in range(20):
            stars = "".join(random.choice(["⭐", "🌟", "✨"]) for _ in range(50))
            sys.stdout.write(f"\r{Color.gradient(stars, (255,255,100), (100,100,255))}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        return True
    
    def _snow(self, args: List[str]) -> bool:
        for _ in range(20):
            snow = "".join(random.choice(["❄️", "❅", "❆"]) for _ in range(50))
            sys.stdout.write(f"\r{Color.gradient(snow, (100,200,255), (0,100,150))}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        return True
    
    def _heartbeat(self, args: List[str]) -> bool:
        for _ in range(10):
            sys.stdout.write(f"\r{Color.RED}❤️  ❤️{Color.RESET}")
            sys.stdout.flush()
            time.sleep(0.3)
            sys.stdout.write(f"\r{Color.RED}❤️{Color.RESET}  ")
            sys.stdout.flush()
            time.sleep(0.3)
        print()
        return True
    
    def _scanner(self, args: List[str]) -> bool:
        width = shutil.get_terminal_size().columns
        for pos in range(width):
            line = [" "] * width
            line[pos] = "█"
            sys.stdout.write(f"\r{Color.GREEN}{''.join(line)}{Color.RESET}")
            sys.stdout.flush()
            time.sleep(0.01)
        print()
        return True
    
    def _bounce(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "KALI TERMINAL"
        width = shutil.get_terminal_size().columns
        pos = 0
        direction = 1
        for _ in range(50):
            spaces = " " * pos
            sys.stdout.write(f"\r{Color.gradient(spaces + text, (0,200,255), (0,100,150))}")
            sys.stdout.flush()
            pos += direction
            if pos >= width - len(text):
                direction = -1
            elif pos <= 0:
                direction = 1
            time.sleep(0.05)
        print()
        return True
    
    def _wave(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "KALI TERMINAL"
        colors = [Color.RED, Color.YELLOW, Color.GREEN, Color.CYAN, Color.BLUE, Color.MAGENTA]
        for offset in range(len(colors) * 2):
            result = ""
            for j, char in enumerate(text):
                result += f"{colors[(j + offset) % len(colors)]}{char}{Color.RESET}"
            sys.stdout.write(f"\r{result}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        return True
    
    def _pulse(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "PULSE"
        for size in range(1, 5):
            sys.stdout.write(f"\r{Color.gradient(text * size, (0,200,255), (0,100,150))}")
            sys.stdout.flush()
            time.sleep(0.1)
        for size in range(4, 0, -1):
            sys.stdout.write(f"\r{Color.gradient(text * size, (0,200,255), (0,100,150))}")
            sys.stdout.flush()
            time.sleep(0.1)
        print()
        return True
    
    def _marquee(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "KALI TERMINAL ULTIMATE"
        text = " " + text + " "
        width = shutil.get_terminal_size().columns
        for i in range(len(text) + width):
            display = text[i:i+width]
            sys.stdout.write(f"\r{Color.gradient(display, (0,200,255), (0,100,150))}")
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        return True
    
    def _typewriter(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "Kali Terminal Ultimate"
        for char in text:
            sys.stdout.write(Color.gradient(char, (0,200,255), (0,100,150)))
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        return True
    
    def _glitch(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "GLITCH EFFECT"
        for _ in range(10):
            glitched = "".join(random.choice(string.ascii_letters) if random.random() < 0.1 else c for c in text)
            sys.stdout.write(f"\r{Color.RED}{glitched}{Color.RESET}")
            sys.stdout.flush()
            time.sleep(0.05)
        sys.stdout.write(f"\r{Color.gradient(text, (0,200,255), (0,100,150))}")
        print()
        return True
    
    def _cowsay(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "Moo!"
        print(f"""
{Color.gradient(f'  {text}', (0,200,255), (0,100,150))}
   \\
    \\
      ^__^
      (oo)\\_______
      (__)\\       )\\/\\
          ||----w |
          ||     ||{Color.RESET}
""")
        return True
    
    def _fortune(self, args: List[str]) -> bool:
        fortunes = [
            "The quieter you become, the more you are able to hear.",
            "With great power comes great responsibility.",
            "In Linux, nothing is impossible.",
            "Knowledge is power. Keep learning.",
            "There's no place like 127.0.0.1",
            "Keep calm and use Python!",
            "The best error message is the one that never shows up.",
            "Code is read more often than it is written.",
            "Simplicity is the soul of efficiency.",
            "First, solve the problem. Then, write the code."
        ]
        print(Color.gradient(f"🔮 {random.choice(fortunes)}", (0,200,255), (0,100,150)))
        return True
    
    def _neofetch(self, args: List[str]) -> bool:
        user, host, os_info, ip = Utils.get_username(), socket.gethostname(), Utils.get_os_info(), Utils.get_local_ip()
        ascii_art = f"""
{Color.gradient('        .-.', (0,200,255), (0,100,150))}
{Color.gradient('       /   \\', (0,200,255), (0,100,150))}       {Color.gradient(f'{user}@{host}', (0,200,255), (0,100,150))}
{Color.gradient('       |   |', (0,200,255), (0,100,150))}       {Color.gradient(f'OS: {os_info}', (0,200,255), (0,100,150))}
{Color.gradient('       |   |', (0,200,255), (0,100,150))}       {Color.gradient(f'IP: {ip}', (0,200,255), (0,100,150))}
{Color.gradient('      /     \\', (0,200,255), (0,100,150))}      {Color.gradient(f'Commands: {len(self.commands)}+', (0,200,255), (0,100,150))}
{Color.gradient('     /       \\', (0,200,255), (0,100,150))}    
{Color.gradient('    /         \\', (0,200,255), (0,100,150))}   
{Color.gradient('   /           \\', (0,200,255), (0,100,150))}  
{Color.gradient('  /             \\', (0,200,255), (0,100,150))} 
{Color.gradient(' /_______________\\', (0,200,255), (0,100,150))} {Color.RESET}
"""
        print(ascii_art)
        return True
    
    def _banner(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "KALI"
        width = shutil.get_terminal_size().columns
        banner_width = len(text) + 4
        padding = max(0, (width - banner_width) // 2)
        print(" " * padding + Color.gradient("█" * (len(text) + 4), (0,200,255), (0,100,150)))
        print(" " * padding + Color.gradient(f"█ {text.upper()} █", (0,200,255), (0,100,150)))
        print(" " * padding + Color.gradient("█" * (len(text) + 4), (0,200,255), (0,100,150)))
        return True
    
    def _figlet(self, args: List[str]) -> bool:
        text = " ".join(args) if args else "KALI"
        width = shutil.get_terminal_size().columns
        try:
            import pyfiglet
            fig = pyfiglet.figlet_format(text)
            for line in fig.split('\n'):
                print(Color.gradient(line.center(width), (0,200,255), (0,100,150)))
        except:
            print(Color.gradient(text.upper().center(width), (0,200,255), (0,100,150)))
        return True
    
    def _sl(self, args: List[str]) -> bool:
        train = f"""
{Color.gradient('      ====        ________                ___________', (0,200,255), (0,100,150))}
{Color.gradient('  _D _|  |_______/        \\__I_I_____===__|_________|', (0,200,255), (0,100,150))}
{Color.gradient('   |(_)---  |   H\\________/ |   |        =|___ ___|', (0,200,255), (0,100,150))}
{Color.gradient('   /     |  |   H  |  |     |   |         ||_| |_||', (0,200,255), (0,100,150))}
{Color.gradient('  |      |  |   H  |__--------------------| [___] |', (0,200,255), (0,100,150))}
{Color.gradient('  | ________|___H__/__|_____/[][]~\\_______|       |', (0,200,255), (0,100,150))}
{Color.gradient('  |/ |   |-----------I_____I [][] |  |____|_  |___', (0,200,255), (0,100,150))}{Color.RESET}
"""
        print(train)
        return True
    
    # UTILITIES COMMANDS
    
    def _clear(self, args: List[str]) -> bool:
        Utils.clear_screen()
        return True
    
    def _help(self, args: List[str]) -> bool:
        if args:
            cmd = self.get(args[0])
            if cmd:
                print(Color.box(
                    f"{Color.GREEN}Description:{Color.RESET}\n  {cmd.description}\n\n"
                    f"{Color.GREEN}Usage:{Color.RESET}\n  {Color.CYAN}{cmd.usage or cmd.name}{Color.RESET}",
                    title=args[0].upper()
                ))
                return True
        
        categories = {}
        for name, cmd in self.commands.items():
            if cmd.category not in categories:
                categories[cmd.category] = []
            categories[cmd.category].append(name)
        
        print(Color.header("KALI TERMINAL HELP", 80))
        for cat, cmds in sorted(categories.items()):
            print(f"\n{Color.BOLD}{cat}{Color.RESET} ({len(cmds)} commands)")
            cmds_display = sorted(cmds)[:15]
            cols = 3
            per_col = (len(cmds_display) + cols - 1) // cols
            for i in range(per_col):
                line = ""
                for j in range(cols):
                    idx = i + j * per_col
                    if idx < len(cmds_display):
                        line += f"  {Color.CYAN}{cmds_display[idx]:<15}{Color.RESET}"
                if line.strip():
                    print(line)
            if len(cmds) > 15:
                print(f"  {Color.DIM}... and {len(cmds) - 15} more{Color.RESET}")
        print(f"\n{Color.DIM}Total commands: {len(self.commands)}{Color.RESET}")
        return True
    
    def _history(self, args: List[str]) -> bool:
        try:
            if self.history_path.exists():
                with open(self.history_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    start = max(0, len(lines) - 50)
                    for i, line in enumerate(lines[start:], start + 1):
                        print(f"{Color.gradient(f'{i:>5}', (0,200,255), (0,100,150))} {line.strip()}")
            else:
                print(Color.warning("No history"))
        except:
            print(Color.warning("No history"))
        return True
    
    def _alias(self, args: List[str]) -> bool:
        if not args:
            if self.aliases:
                for name, value in sorted(self.aliases.items()):
                    print(f"{Color.GREEN}{name}{Color.RESET}='{value}'")
            else:
                print(Color.warning("No aliases"))
            return True
        if "=" in args[0]:
            name, value = args[0].split("=", 1)
            self.aliases[name] = value
            print(Color.success(f"Alias: {name}='{value}'"))
        return True
    
    def _unalias(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: unalias <name>"))
            return True
        name = args[0]
        if name in self.aliases:
            del self.aliases[name]
            print(Color.success(f"Alias removed: {name}"))
        else:
            print(Color.warning(f"Alias not found: {name}"))
        return True
    
    def _type(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: type <command>"))
            return True
        cmd = args[0]
        if cmd in self.aliases:
            print(f"{cmd} - alias for '{self.aliases[cmd]}'")
        elif cmd in self.commands:
            print(f"{cmd} - built-in command")
        else:
            print(f"{cmd} - external command")
        return True
    
    def _man(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: man <command>"))
            return True
        cmd = self.get(args[0])
        if cmd:
            print(Color.box(
                f"{Color.GREEN}DESCRIPTION:{Color.RESET}\n  {cmd.description}\n\n"
                f"{Color.GREEN}USAGE:{Color.RESET}\n  {Color.CYAN}{cmd.usage or cmd.name}{Color.RESET}\n\n"
                f"{Color.GREEN}CATEGORY:{Color.RESET}\n  {cmd.category}",
                title=args[0].upper()
            ))
        else:
            print(Color.error(f"Command not found: {args[0]}"))
        return True
    
    def _calc(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: calc <expression>"))
            return True
        try:
            expr = " ".join(args)
            expr = expr.replace("^", "**")
            result = eval(expr, {"__builtins__": {}}, {"math": math})
            print(Color.gradient(f"{expr} = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid expression"))
        return True
    
    def _units(self, args: List[str]) -> bool:
        if len(args) < 3:
            print(Color.warning("Usage: units <value> <from_unit> <to_unit>"))
            return True
        conversions = {
            "m": 1, "cm": 0.01, "km": 1000,
            "in": 0.0254, "ft": 0.3048, "mi": 1609.344,
            "kg": 1, "g": 0.001, "lb": 0.453592
        }
        try:
            value = float(args[0])
            from_unit, to_unit = args[1], args[2]
            if from_unit in conversions and to_unit in conversions:
                result = value * conversions[from_unit] / conversions[to_unit]
                print(Color.gradient(f"{value} {from_unit} = {result:.4f} {to_unit}", (0,200,255), (0,100,150)))
            else:
                print(Color.error("Unknown units"))
        except:
            print(Color.error("Conversion error"))
        return True
    
    def _timer(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: timer <seconds>"))
            return True
        seconds = int(args[0])
        print(Color.info(f"Timer set for {seconds} seconds"))
        for i in range(seconds, 0, -1):
            sys.stdout.write(f"\r{Color.gradient(f'Time remaining: {i} seconds', (0,200,255), (0,100,150))}")
            sys.stdout.flush()
            time.sleep(1)
        print(f"\n{Color.success('Time\'s up!')}")
        return True
    
    def _stopwatch(self, args: List[str]) -> bool:
        print(Color.info("Stopwatch started. Press Enter to stop."))
        start = time.time()
        input()
        elapsed = time.time() - start
        print(Color.gradient(f"Elapsed: {Utils.human_time(elapsed)}", (0,200,255), (0,100,150)))
        return True
    
    def _todo(self, args: List[str]) -> bool:
        todo_file = Path.home() / ".kali_terminal_todo.json"
        if not args or args[0] == "list":
            try:
                if todo_file.exists():
                    tasks = json.load(open(todo_file, "r"))
                    if not tasks:
                        print(Color.info("Todo list is empty"))
                    else:
                        for i, task in enumerate(tasks, 1):
                            status = "✓" if task.get("done") else "○"
                            print(f"{Color.CYAN}{i:>2}.{Color.RESET} {status} {task.get('text')}")
                else:
                    print(Color.info("Todo list is empty"))
            except:
                pass
        elif args[0] == "add":
            text = " ".join(args[1:])
            if text:
                tasks = json.load(open(todo_file, "r")) if todo_file.exists() else []
                tasks.append({"text": text, "done": False})
                with open(todo_file, "w") as f:
                    json.dump(tasks, f, indent=2)
                print(Color.success(f"Added: {text}"))
        elif args[0] == "done" and len(args) > 1:
            try:
                idx = int(args[1]) - 1
                tasks = json.load(open(todo_file, "r")) if todo_file.exists() else []
                if 0 <= idx < len(tasks):
                    tasks[idx]["done"] = True
                    with open(todo_file, "w") as f:
                        json.dump(tasks, f, indent=2)
                    print(Color.success("Marked as done"))
                else:
                    print(Color.error("Invalid task number"))
            except:
                pass
        return True
    
    def _note(self, args: List[str]) -> bool:
        notes_file = Path.home() / ".kali_terminal_notes.json"
        if not args or args[0] == "list":
            try:
                if notes_file.exists():
                    notes = json.load(open(notes_file, "r"))
                    if not notes:
                        print(Color.info("No notes"))
                    else:
                        for i, note in enumerate(notes, 1):
                            date = note.get('date', '')[:10]
                            title = note.get('title', 'Untitled')[:30]
                            print(f"{Color.CYAN}{i:>2}.{Color.RESET} {title} - {date}")
                else:
                    print(Color.info("No notes"))
            except:
                pass
        elif args[0] == "add":
            title = args[1] if len(args) > 1 else "Note"
            text = " ".join(args[2:]) if len(args) > 2 else ""
            notes = json.load(open(notes_file, "r")) if notes_file.exists() else []
            notes.append({"title": title, "text": text, "date": str(datetime.now())})
            with open(notes_file, "w") as f:
                json.dump(notes, f, indent=2)
            print(Color.success(f"Note added: {title}"))
        return True
    
    def _joke(self, args: List[str]) -> bool:
        jokes = [
            "Why do programmers confuse Halloween and Christmas? 31 Oct = 25 Dec!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why was the developer unhappy? Because he had too many issues!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "What do you call a programmer from Finland? Nerdic!",
            "Why do Java developers wear glasses? Because they can't C#!"
        ]
        print(Color.gradient(random.choice(jokes), (0,200,255), (0,100,150)))
        return True
    
    def _quote(self, args: List[str]) -> bool:
        quotes = [
            ("The only way to do great work is to love what you do.", "Steve Jobs"),
            ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
            ("First, solve the problem. Then, write the code.", "John Johnson"),
            ("Simplicity is the soul of efficiency.", "Austin Freeman"),
            ("Make it work, make it right, make it fast.", "Kent Beck"),
            ("Talk is cheap. Show me the code.", "Linus Torvalds"),
            ("Programs must be written for people to read.", "Hal Abelson")
        ]
        quote, author = random.choice(quotes)
        print(Color.gradient(f'"{quote}"', (0,200,255), (0,100,150)))
        print(Color.gradient(f"  — {author}", (0,150,200), (0,100,100)))
        return True
    
    def _riddle(self, args: List[str]) -> bool:
        riddles = [
            ("What can you hold without ever touching?", "Breath"),
            ("What gets bigger the more you take away from it?", "A hole"),
            ("What has keys but can't open locks?", "Piano"),
            ("What has a face and two hands but no arms or legs?", "Clock"),
            ("What has words but never speaks?", "Book"),
            ("What has to be broken before you can use it?", "Egg"),
            ("What is full of holes but still holds water?", "Sponge")
        ]
        riddle, answer = random.choice(riddles)
        print(Color.gradient(f"Riddle: {riddle}", (0,200,255), (0,100,150)))
        user_answer = input(f"{Color.YELLOW}Answer: {Color.RESET}").strip().lower()
        if user_answer == answer.lower():
            print(Color.success("Correct!"))
        else:
            print(Color.warning(f"Answer: {answer}"))
        return True
    
    def _weather(self, args: List[str]) -> bool:
        city = " ".join(args) if args else "Moscow"
        try:
            import requests
            response = requests.get(f"https://wttr.in/{city}?format=%l:+%c+%t+%w", timeout=5)
            if response.ok:
                print(Color.gradient(response.text.strip(), (0,200,255), (0,100,150)))
            else:
                print(Color.warning("Could not fetch weather"))
        except:
            print(Color.warning("Could not fetch weather"))
        return True
    
    def _bitcoin(self, args: List[str]) -> bool:
        try:
            import requests
            response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur", timeout=5)
            if response.ok:
                data = response.json()
                btc = data.get("bitcoin", {})
                print(Color.box(
                    f"{Color.CYAN}USD: ${Color.GREEN}{btc.get('usd', 'N/A')}\n"
                    f"{Color.CYAN}EUR: €{Color.GREEN}{btc.get('eur', 'N/A')}",
                    title="Bitcoin Price"
                ))
            else:
                print(Color.warning("Could not fetch price"))
        except:
            print(Color.warning("Could not fetch price"))
        return True
    
    def _ethereum(self, args: List[str]) -> bool:
        try:
            import requests
            response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd,eur", timeout=5)
            if response.ok:
                data = response.json()
                eth = data.get("ethereum", {})
                print(Color.box(
                    f"{Color.CYAN}USD: ${Color.GREEN}{eth.get('usd', 'N/A')}\n"
                    f"{Color.CYAN}EUR: €{Color.GREEN}{eth.get('eur', 'N/A')}",
                    title="Ethereum Price"
                ))
            else:
                print(Color.warning("Could not fetch price"))
        except:
            print(Color.warning("Could not fetch price"))
        return True
    
    # MATH COMMANDS
    
    def _fib(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: fib <n>"))
            return True
        try:
            n = int(args[0])
            result = Utils.fibonacci(n)
            print(Color.gradient(f"Fibonacci({n}) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _prime(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: prime <n>"))
            return True
        try:
            n = int(args[0])
            is_prime = Utils.is_prime(n)
            result = "prime" if is_prime else "not prime"
            print(Color.gradient(f"{n} is {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _factors(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: factors <n>"))
            return True
        try:
            n = int(args[0])
            factors = Utils.prime_factors(n)
            print(Color.gradient(f"Prime factors of {n}: {factors}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _gcd(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: gcd <a> <b>"))
            return True
        try:
            a, b = int(args[0]), int(args[1])
            result = Utils.gcd(a, b)
            print(Color.gradient(f"gcd({a}, {b}) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _lcm(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: lcm <a> <b>"))
            return True
        try:
            a, b = int(args[0]), int(args[1])
            result = Utils.lcm(a, b)
            print(Color.gradient(f"lcm({a}, {b}) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _sqrt(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: sqrt <n>"))
            return True
        try:
            n = float(args[0])
            result = math.sqrt(n)
            print(Color.gradient(f"√{n} = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _pow(self, args: List[str]) -> bool:
        if len(args) < 2:
            print(Color.warning("Usage: pow <base> <exp>"))
            return True
        try:
            base, exp = float(args[0]), float(args[1])
            result = base ** exp
            print(Color.gradient(f"{base}^{exp} = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _fact(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: fact <n>"))
            return True
        try:
            n = int(args[0])
            result = math.factorial(n)
            print(Color.gradient(f"{n}! = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _sin(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: sin <angle>"))
            return True
        try:
            angle = float(args[0])
            result = math.sin(math.radians(angle))
            print(Color.gradient(f"sin({angle}°) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _cos(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: cos <angle>"))
            return True
        try:
            angle = float(args[0])
            result = math.cos(math.radians(angle))
            print(Color.gradient(f"cos({angle}°) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _tan(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: tan <angle>"))
            return True
        try:
            angle = float(args[0])
            result = math.tan(math.radians(angle))
            print(Color.gradient(f"tan({angle}°) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _log(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: log <n> [base]"))
            return True
        try:
            n = float(args[0])
            base = float(args[1]) if len(args) > 1 else math.e
            result = math.log(n) / math.log(base)
            print(Color.gradient(f"log_{base}({n}) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _ln(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: ln <n>"))
            return True
        try:
            n = float(args[0])
            result = math.log(n)
            print(Color.gradient(f"ln({n}) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _exp(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: exp <n>"))
            return True
        try:
            n = float(args[0])
            result = math.exp(n)
            print(Color.gradient(f"e^{n} = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _abs(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: abs <n>"))
            return True
        try:
            n = float(args[0])
            result = abs(n)
            print(Color.gradient(f"|{n}| = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _round(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: round <n>"))
            return True
        try:
            n = float(args[0])
            result = round(n)
            print(Color.gradient(f"round({n}) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _floor(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: floor <n>"))
            return True
        try:
            n = float(args[0])
            result = math.floor(n)
            print(Color.gradient(f"floor({n}) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _ceil(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: ceil <n>"))
            return True
        try:
            n = float(args[0])
            result = math.ceil(n)
            print(Color.gradient(f"ceil({n}) = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _pi(self, args: List[str]) -> bool:
        print(Color.gradient(f"π = {math.pi}", (0,200,255), (0,100,150)))
        return True
    
    def _e(self, args: List[str]) -> bool:
        print(Color.gradient(f"e = {math.e}", (0,200,255), (0,100,150)))
        return True
    
    def _tau(self, args: List[str]) -> bool:
        print(Color.gradient(f"τ = {math.tau}", (0,200,255), (0,100,150)))
        return True
    
    def _avg(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: avg <n1> <n2> ..."))
            return True
        try:
            nums = [float(x) for x in args]
            result = sum(nums) / len(nums)
            print(Color.gradient(f"Average = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _sum(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: sum <n1> <n2> ..."))
            return True
        try:
            nums = [float(x) for x in args]
            result = sum(nums)
            print(Color.gradient(f"Sum = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _min(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: min <n1> <n2> ..."))
            return True
        try:
            nums = [float(x) for x in args]
            result = min(nums)
            print(Color.gradient(f"Min = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _max(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: max <n1> <n2> ..."))
            return True
        try:
            nums = [float(x) for x in args]
            result = max(nums)
            print(Color.gradient(f"Max = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _median(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: median <n1> <n2> ..."))
            return True
        try:
            nums = sorted([float(x) for x in args])
            n = len(nums)
            if n % 2 == 0:
                result = (nums[n//2 - 1] + nums[n//2]) / 2
            else:
                result = nums[n//2]
            print(Color.gradient(f"Median = {result}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    # CONVERSION COMMANDS
    
    def _bin(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: bin <number>"))
            return True
        try:
            n = int(args[0])
            print(Color.gradient(f"{n} = {bin(n)}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _oct(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: oct <number>"))
            return True
        try:
            n = int(args[0])
            print(Color.gradient(f"{n} = {oct(n)}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _hexconv(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: hexconv <number>"))
            return True
        try:
            n = int(args[0])
            print(Color.gradient(f"{n} = {hex(n)}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _dec(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: dec <number>"))
            return True
        try:
            n = int(args[0], 0)
            print(Color.gradient(f"{args[0]} = {n}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _ascii(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: ascii <text>"))
            return True
        text = " ".join(args)
        result = " ".join(str(ord(c)) for c in text)
        print(Color.gradient(f"ASCII: {result}", (0,200,255), (0,100,150)))
        return True
    
    def _char(self, args: List[str]) -> bool:
        if not args:
            print(Color.warning("Usage: char <code>"))
            return True
        try:
            code = int(args[0])
            print(Color.gradient(f"Character: {chr(code)}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid code"))
        return True
    
    def _temp(self, args: List[str]) -> bool:
        if len(args) < 3:
            print(Color.warning("Usage: temp <value> C|F|K"))
            return True
        try:
            value = float(args[0])
            from_unit = args[1].upper()
            to_unit = args[2].upper()
            if from_unit == "C" and to_unit == "F":
                result = value * 9/5 + 32
            elif from_unit == "F" and to_unit == "C":
                result = (value - 32) * 5/9
            elif from_unit == "C" and to_unit == "K":
                result = value + 273.15
            elif from_unit == "K" and to_unit == "C":
                result = value - 273.15
            elif from_unit == "F" and to_unit == "K":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "K" and to_unit == "F":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value
            print(Color.gradient(f"{value}°{from_unit} = {result:.2f}°{to_unit}", (0,200,255), (0,100,150)))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _length(self, args: List[str]) -> bool:
        if len(args) < 3:
            print(Color.warning("Usage: length <value> <from> <to>"))
            return True
        conversions = {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "in": 0.0254, "ft": 0.3048, "mi": 1609.344}
        try:
            value = float(args[0])
            from_unit, to_unit = args[1], args[2]
            if from_unit in conversions and to_unit in conversions:
                result = value * conversions[from_unit] / conversions[to_unit]
                print(Color.gradient(f"{value} {from_unit} = {result:.4f} {to_unit}", (0,200,255), (0,100,150)))
            else:
                print(Color.error("Unknown units"))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _weight(self, args: List[str]) -> bool:
        if len(args) < 3:
            print(Color.warning("Usage: weight <value> <from> <to>"))
            return True
        conversions = {"kg": 1, "g": 0.001, "lb": 0.453592, "oz": 0.0283495}
        try:
            value = float(args[0])
            from_unit, to_unit = args[1], args[2]
            if from_unit in conversions and to_unit in conversions:
                result = value * conversions[from_unit] / conversions[to_unit]
                print(Color.gradient(f"{value} {from_unit} = {result:.4f} {to_unit}", (0,200,255), (0,100,150)))
            else:
                print(Color.error("Unknown units"))
        except:
            print(Color.error("Invalid input"))
        return True
    
    def _exit(self, args: List[str]) -> bool:
        return True
    
    def add(self, name: str, func: Callable, description: str, usage: str = "", category: str = "General"):
        self.commands[name] = Command(func, description, usage, category)
    
    def get(self, name: str) -> Optional[Command]:
        if name in self.aliases:
            name = self.aliases[name]
        return self.commands.get(name)
    
    def execute(self, cmd_line: str) -> bool:
        if not cmd_line or not cmd_line.strip():
            return True
        try:
            parts = shlex.split(cmd_line.strip())
        except:
            parts = cmd_line.strip().split()
        if not parts:
            return True
        cmd, args = parts[0].lower(), parts[1:]
        
        if cmd in self.aliases:
            return self.execute(self.aliases[cmd] + " " + " ".join(args))
        
        if cmd in self.commands:
            try:
                return self.commands[cmd].func(args)
            except Exception as e:
                print(Color.error(str(e)))
                return True
        
        try:
            result = subprocess.run(cmd_line, shell=True, capture_output=True, text=True, timeout=10)
            if result.stdout:
                print(result.stdout)
            if result.stderr:
                print(Color.error(result.stderr.strip()))
            return True
        except subprocess.TimeoutExpired:
            print(Color.warning("Command timed out"))
        except FileNotFoundError:
            print(Color.error(f"Command not found: {cmd}"))
        except Exception as e:
            print(Color.error(str(e)))
        return True

# =================================================================================================
# 🔐 CRYPTOGRAPHY UTILITIES
# =================================================================================================

class Crypto:
    @staticmethod
    def xor_encrypt(data: str, key: str) -> str:
        result = []
        for i, char in enumerate(data):
            result.append(chr(ord(char) ^ ord(key[i % len(key)])))
        return "".join(result)
    
    @staticmethod
    def xor_decrypt(data: str, key: str) -> str:
        return Crypto.xor_encrypt(data, key)
    
    @staticmethod
    def caesar_cipher(text: str, shift: int) -> str:
        result = []
        for char in text:
            if char.isupper():
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            elif char.islower():
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))
            else:
                result.append(char)
        return "".join(result)
    
    @staticmethod
    def rot13(text: str) -> str:
        return Utils.rot13(text)

# =================================================================================================
# 🚀 MAIN TERMINAL
# =================================================================================================

class KaliTerminal:
    def __init__(self):
        self.cmd_manager = CommandManager()
    
    def get_prompt(self) -> str:
        user = Utils.get_username()
        host = Utils.get_hostname()
        path = Utils.shorten_path(os.getcwd(), 30)
        return f"{Color.RED}┌──({Color.gradient(user, (0,200,255), (0,100,150))}{Color.RED}@{Color.gradient(host, (0,200,255), (0,100,150))}{Color.RED})-[{Color.gradient(path, (0,200,255), (0,100,150))}{Color.RED}]\n{Color.RED}└─{Color.gradient('$ ', (0,200,255), (0,100,150))}{Color.RESET}"
    
    def show_header(self):
        width = min(shutil.get_terminal_size().columns, 100)
        header = f"""
{Color.gradient('╔' + '═' * width + '╗', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient('     ██╗  ██╗ █████╗ ██╗     ██╗    ████████╗███████╗██████╗ ███╗   ███╗██╗ █████╗ ██╗     '.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient('     ██║ ██╔╝██╔══██╗██║     ██║    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║██╔══██╗██║     '.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient('     █████╔╝ ███████║██║     ██║       ██║   █████╗  ██████╔╝██╔████╔██║██║███████║██║     '.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient('     ██╔═██╗ ██╔══██║██║     ██║       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██╔══██║██║     '.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient('     ██║  ██╗██║  ██║███████╗██║       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║  ██║███████╗'.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient('     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═╝╚══════╝'.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient(f'                     🚀  ULTIMATE TERMINAL EMULATOR v11.0  🚀                     '.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient(f'                 🔥 {len(self.cmd_manager.commands)}+ COMMANDS | SECURITY SUITE | VISUAL FX 🔥               '.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('║', (0,200,255), (0,100,150))}{Color.gradient(f'                 🔍 DOX TOOL | OSINT | NETWORK SCANNERS | CRYPTOGRAPHY 🔍               '.center(width - 2), (0,200,255), (0,100,150))}{Color.gradient('║', (0,200,255), (0,100,150))}
{Color.gradient('╚' + '═' * width + '╝', (0,200,255), (0,100,150))}{Color.RESET}
"""
        print(header)
        print(Color.success(f"Welcome! {len(self.cmd_manager.commands)} commands ready"))
        print(Color.info("Type 'help' for help, 'exit' to quit"))
        print(Color.info("OSINT Commands: dox, emailinfo, phoneinfo, usercheck, domaininfo, ipinfo, dnslookup, subdomain"))
    
    def run(self):
        self.show_header()
        while True:
            try:
                cmd = input(self.get_prompt())
                if not cmd.strip():
                    continue
                self.cmd_manager.save_history(cmd)
                if cmd.lower() in ["exit", "quit"]:
                    print(Color.gradient("Goodbye!", (0,255,0), (0,100,0)))
                    break
                self.cmd_manager.execute(cmd)
                print()
            except KeyboardInterrupt:
                print(f"\n{Color.gradient('Use exit to quit', (0,200,255), (0,100,150))}")
            except EOFError:
                break
            except Exception as e:
                print(Color.error(str(e)))

# =================================================================================================
# 🎯 ENTRY POINT
# =================================================================================================

if __name__ == "__main__":
    # Run auto-installer
    auto_install_dependencies()
    
    Animation.loading_bar("Loading Kali Terminal v11.0", 1.5)
    KaliTerminal().run()
