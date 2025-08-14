# hpm/commands/aur.py

import os
import subprocess
from rich.console import Console
from hpm.utils import log
# We define PACMAN_PATH here to avoid the ImportError
PACMAN_PATH = "/usr/bin"

console = Console()

def find_aur_helper():
    """
    Finds an installed AUR helper (yay or paru) on the system.
    Returns the path to the helper if found, otherwise returns None.
    """
    aur_helpers = ["yay", "paru"]
    for helper in aur_helpers:
        helper_path = os.path.join(PACMAN_PATH, helper)
        if os.path.exists(helper_path):
            return helper_path
    return None

def aur_main(packages: list[str], dry_run: bool):
    """
    Manages packages from the Arch User Repository (AUR).
    This function primarily focuses on installing packages from the AUR.
    """
    log.info("Searching for AUR helper...")
    aur_helper = find_aur_helper()

    if not aur_helper:
        log.error("No AUR helper (yay or paru) found.")
        log.info("Please install an AUR helper to use this command.")
        return

    log.info(f"Using AUR helper: {os.path.basename(aur_helper)}")
    log.info(f"Attempting to install AUR package(s): {', '.join(packages)}")

    if dry_run:
        log.warning("Dry run: Would have installed the specified AUR packages.")
        return

    # The command to install AUR packages using the found helper
    cmd = [aur_helper, '-S'] + packages

    log.debug(f"Running command: {' '.join(cmd)}")

    try:
        # Run the command interactively so the user can see the progress and enter sudo password
        subprocess.run(cmd)
        log.success("AUR package installation completed.")
    except FileNotFoundError:
        log.error("AUR helper not found. This should not happen.")
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")
