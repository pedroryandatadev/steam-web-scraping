import json
import os
from app.config import DB_FILE

# Database functions to load and save the history of sent alerts
def load_history():
    """Reads the history from the JSON file. Returns empty dict if file doesn't exist."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

# Saves the updated history dictionary to the JSON file.
def save_history(history):
    """Saves the updated history dictionary to the JSON file."""
    with open(DB_FILE, "w") as f:
        json.dump(history, f, indent=4) # indent=4 makes the JSON readable for humans