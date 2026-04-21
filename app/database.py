import json
import os
from app.config import DB_FILE

# Loads the history of sent alerts from the JSON file. If the file doesn't exist, it returns an empty dictionary.
def load_history():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Saves the updated history dictionary to the JSON file.
def save_history(history):
    with open(DB_FILE, "w") as f:
        json.dump(history, f, indent=4) # indent=4 makes the JSON readable for humans