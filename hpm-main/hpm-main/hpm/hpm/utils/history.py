# hpm/hpm/utils/history.py

import json
import os
from datetime import datetime
from hpm.utils import log

# Define the path to the history file
HISTORY_DIR = os.path.join(os.path.expanduser('~'), '.local', 'share', 'hpm')
HISTORY_FILE = os.path.join(HISTORY_DIR, 'history.json')

def get_history() -> list:
    """Reads the history from the file."""
    if not os.path.exists(HISTORY_FILE):
        return []
    
    with open(HISTORY_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            log.error("Failed to decode history file. It might be corrupted.")
            return []

def add_entry(command: str, action: str, packages: list):
    """Adds a new entry to the history file."""
    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)

    history_data = get_history()
    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "command": command,
        "action": action,
        "packages": packages
    }
    history_data.append(new_entry)
    
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history_data, f, indent=4)
