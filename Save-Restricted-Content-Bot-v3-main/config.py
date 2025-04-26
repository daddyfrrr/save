# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "25255466")
API_HASH = os.getenv("API_HASH", "aa797f1169fb6bbee3de4869d6b76165")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7734717991:AAG94Q_BHASQIEeLLdEm4wN3u82P1O8XVpk")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://daddyfrrr1:aGpA3J5QJqXi5Sq1@cluster0.li1zd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "7877249692").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "daddyfrrr1")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002542800168")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002542800168")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "50000"))
