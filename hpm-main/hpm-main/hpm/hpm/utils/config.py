# hpm/hpm/utils/config.py

import json
import os
from hpm.utils import log

# Define the path to the configuration file
CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config', 'hpm')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'config.json')

def get_config():
    """Reads the configuration from the config file."""
    if not os.path.exists(CONFIG_FILE):
        return {"aliases": {}}
    
    with open(CONFIG_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            log.error("Failed to decode config file. It might be corrupted.")
            return {"aliases": {}}

def save_config(config: dict):
    """Saves the configuration to the config file."""
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)

    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)
