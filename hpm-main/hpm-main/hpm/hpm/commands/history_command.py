# hpm/commands/history_command.py

import os
import typer
from rich.console import Console
from rich.table import Table
from datetime import datetime
from hpm.utils import log

# This is a temporary file path to store the history.
# We'll use a path in the user's local application data directory.
HISTORY_DIR = os.path.join(os.path.expanduser('~'), '.local/share/hpm')
HISTORY_FILE = os.path.join(HISTORY_DIR, 'history.log')

console = Console()

def log_command_to_history(command_name: str, args: list):
    """
    Logs a command and its arguments to a history file.
    """
    # Ensure the directory exists
    os.makedirs(HISTORY_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    command_str = f"hpm {command_name} {' '.join(args)}"
    log_entry = f"[{timestamp}] {command_str}\n"

    try:
        with open(HISTORY_FILE, 'a') as f:
            f.write(log_entry)
        log.debug(f"Command logged to history: {command_str}")
    except Exception as e:
        log.error(f"Failed to log command to history file: {e}")

def history_main(dry_run: bool):
    """
    Displays the command history from the history file.
    """
    if dry_run:
        log.warning("Running in dry-run mode. No changes will be made to the system.")
    
    log.info("Displaying command history...")
    
    if not os.path.exists(HISTORY_FILE) or os.path.getsize(HISTORY_FILE) == 0:
        log.info("No command history found. Start using hpm to generate a history.")
        return

    try:
        table = Table(title="[bold blue]Command History[/bold blue]", show_header=True, header_style="bold magenta")
        table.add_column("Timestamp", style="cyan", no_wrap=True)
        table.add_column("Command", style="green")

        with open(HISTORY_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        timestamp_str, command_str = line.split('] ', 1)
                        table.add_row(timestamp_str.strip('['), command_str)
                    except ValueError:
                        # Handle malformed lines gracefully
                        log.warning(f"Skipping malformed history line: {line}")
        
        console.print(table)
        log.success("History displayed successfully.")

    except Exception as e:
        log.error(f"An error occurred while reading history: {e}")
