import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
DASHBOARD_KEY = os.getenv("DASHBOARD_KEY", "ultra123")

DOWNLOAD_DIR = "downloads"

HEADERS = "User-Agent: Mozilla/5.0\r\nReferer: https://hindibhaskarbyamarnathapi.akamai.net.in\r\n"

