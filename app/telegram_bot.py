import requests
from app.config import TELEGRAM_TOKEN, CHAT_ID

# Function to send a message to Telegram using the Bot API
def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID, # The chat ID where the message will be sent
        "text": message,  # The message content to be sent
        "parse_mode": "Markdown", # Use Markdown for formatting the message (e.g., bold, italics)
        "disable_web_page_preview": False # Set to True to disable link previews, False to show them
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Failed to send Telegram message: {e}")