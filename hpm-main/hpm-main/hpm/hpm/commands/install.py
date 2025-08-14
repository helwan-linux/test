# hpm/commands/install.py

import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from hpm.utils import log
from hpm.commands.history_command import log_command_to_history

# We define PACMAN_PATH here to avoid the ImportError
PACMAN_PATH = "/usr/bin"
AUR_PATH = "/usr/bin/yay"

console = Console()

def install_main(packages: list[str], force: bool, local: bool, dry_run: bool):
    """
    Installs a package or a list of packages.
    """
    # Log the command to history first, regardless of dry_run
    log_command_to_history("install", packages)

    if dry_run:
        log.warning("Running in dry-run mode. No changes will be made to the system.")
        log.info(f"Preparing to install: {', '.join(packages)}")
        log.info("Would have executed: [bold cyan]sudo pacman -S --noconfirm[/bold cyan]")
        return
        
    log.info(f"Preparing to install: {', '.join(packages)}")

    cmd = []
    if local:
        cmd = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '--noconfirm', '-U'] + packages
    else:
        cmd = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '-S'] + packages
        if force:
            cmd = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '--noconfirm', '-S'] + packages
    
    # Check if the user wants to proceed
    if not Confirm.ask("Proceed with installation?", default=True):
        log.info("Installation aborted by user.")
        return

    try:
        log.debug(f"Executing command: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        log.success("Packages installed successfully.")
    except FileNotFoundError:
        log.error("Pacman or sudo was not found. Please check your system configuration.")
    except subprocess.CalledProcessError as e:
        log.error(f"Installation failed with error code: {e.returncode}")
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")
