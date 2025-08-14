# hpm/hpm/commands/sync.py

import typer
import subprocess
from hpm.utils import log, pacman

app = typer.Typer(help="Synchronizes package databases with the repositories.")

@app.command(name="sync", help="Synchronizes package databases with the repositories.")
def sync_main():
    """
    Synchronizes package databases using pacman.
    """
    log.info("Synchronizing package databases...")
    
    # Run pacman -Sy to synchronize the databases
    result = pacman.run_pacman_command(['-Sy'])
    
    if isinstance(result, subprocess.CalledProcessError):
        log.error("Failed to synchronize databases. Please check your internet connection.")
        return

    log.success("Databases have been successfully synchronized.")
