import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    SKRYFALL_BASE_URL = "https://api.scryfall.com"
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"