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
    "1000794": {"name": "KINGDOM HEARTS INTEGRUM MASTERPIECE", "type": "sub", "target_price": 209.95, "target_discount": 50},
    "613830": {"name": "CHRONO TRIGGER", "type": "app", "target_price": 12.49, "target_discount": 75},
    "2966320": {"name": "Starsand Island", "type": "app", "target_price": 60.00, "target_discount": 40},
    "1730680": {"name": "Klonoa Phantasy Reverie Series", "type": "app", "target_price": 50.00, "target_discount": 75},
    "1689620": {"name": "BLEACH Rebirth of Souls", "type": "app", "target_price": 110.00, "target_discount": 60},
    "2244210": {"name": "Echoes of Aincrad", "type": "app", "target_price": 153.00, "target_discount": 50},
    "1340990": {"name": "Rise of the Ronin", "type": "app", "target_price": 90.00, "target_discount": 70},
    "1086940": {"name": "Baldur's Gate 3", "type": "app", "target_price": 120.00, "target_discount": 40},
    "1144200": {"name": "Ready or Not", "type": "app", "target_price": 50.00, "target_discount": 60},
    "351970": {"name": "Tales of Zestiria", "type": "app", "target_price": 9.09, "target_discount": 90},
    "597820": {"name": "BIOMUTANT", "type": "app", "target_price": 18.00, "target_discount": 80},
    "2060160": {"name": "The Farmer Was Replaced", "type": "app", "target_price": 20.00, "target_discount": 30},
    "2697000": {"name": "The Legend of Khiimori", "type": "app", "target_price": 75.00, "target_discount": 50}
}