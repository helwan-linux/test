# hpm/commands/refresh.py

import os
import subprocess
from hpm.utils import log
# The PACMAN_PATH constant was not defined in hpm.constants,
# causing an ImportError. We define it here to fix the issue.
PACMAN_PATH = "/usr/bin"

def refresh_main(force: bool, dry_run: bool):
    """
    Synchronizes package databases and upgrades all packages.
    """
    log.info("Starting a full system refresh...")
    
    # We use a single, direct subprocess call to run the refresh command.
    # This allows the user to interact directly with the command line
    # for sudo password and pacman prompts.
    cmd = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '-Syu']
    
    if dry_run:
        log.info("Performing a dry run. No changes will be made.")
    
    if force:
        cmd.append('--noconfirm')
    
    log.debug(f"Running command: {' '.join(cmd)}")
    
    try:
        # We run the command without capturing stdout/stderr so the user can interact.
        subprocess.run(cmd)
        
        log.success("System refresh completed.")
        
    except FileNotFoundError:
        log.error("Pacman or sudo was not found. Please check your system configuration.")
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")
