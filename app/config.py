import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
DB_FILE = "price_history.json"

# Keywords to identify special editions in package names
EDITION_KEYWORDS = ["deluxe", "gold", "ultimate", "premium", "complete"]

# Product wishlist
GAMES = {
    "1245620": {"name": "Elden Ring", "type": "app", "target_price": 150.00, "target_discount": 40},
    "1903340": {"name": "Clair Obscur: Expedition 33", "type": "app", "target_price": 159.20, "target_discount": 20},
    "1790600": {"name": "Dragon Ball: Sparking! Zero", "type": "app", "target_price": 141.25, "target_discount": 50},
    "1954200": {"name": "Kena: Bridge of Spirits", "type": "app", "target_price": 47.97, "target_discount": 70},
    "1000794": {"name": "KINGDOM HEARTS INTEGRUM MASTERPIECE", "type": "sub", "target_price": 209.95, "target_discount": 50}
}