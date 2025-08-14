# hpm/commands/upgrade.py

import os
import subprocess
from hpm.utils import log
# We define PACMAN_PATH here to avoid the ImportError
PACMAN_PATH = "/usr/bin"

def upgrade_main(force: bool, dry_run: bool):
    """
    Upgrades all installed packages.
    """
    log.info("Starting system upgrade...")
    
    # We will run the upgrade command directly, similar to refresh.
    # This ensures proper interaction for the sudo password.
    cmd = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '-Syu']
    
    if dry_run:
        log.warning("Dry run: Would have upgraded all installed packages. No changes will be made.")
        return
    
    if force:
        cmd.append('--noconfirm')
    
    log.debug(f"Running command: {' '.join(cmd)}")
    
    try:
        # We run the command without capturing stdout/stderr so the user can interact.
        subprocess.run(cmd)
        
        log.success("System upgrade completed.")
        
    except FileNotFoundError:
        log.error("Pacman or sudo was not found. Please check your system configuration.")
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")
