# hpm/commands/clean.py

import os
import subprocess
from hpm.utils import log
# We define PACMAN_PATH here to avoid the ImportError
PACMAN_PATH = "/usr/bin"

def clean_main(all_cache: bool, dry_run: bool):
    """
    Cleans the package cache and removes orphan packages.
    """
    log.info("Starting system cleanup...")
    
    # First, let's remove orphan packages.
    log.info("Checking for and removing orphan packages...")
    
    cmd_list_orphans = [os.path.join(PACMAN_PATH, 'pacman'), '-Qtdq']
    
    if not dry_run:
        try:
            # Get the list of orphan packages, but don't raise an error if none are found.
            orphans_list_process = subprocess.run(cmd_list_orphans, capture_output=True, text=True)
            orphans_list = orphans_list_process.stdout.strip().splitlines()

            if orphans_list:
                # If there are orphan packages, remove them
                cmd_remove_orphans = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '-Rns', '--noconfirm'] + orphans_list
                subprocess.run(cmd_remove_orphans, check=True)
                log.info("Orphan packages removed.")
            else:
                log.info("No orphan packages to remove.")
        except subprocess.CalledProcessError as e:
            log.error(f"Failed to remove orphan packages: {e}")

    # Second, let's clean the package cache.
    log.info("Cleaning package cache...")
    
    # Check if we should remove all cache files or just unused ones
    if all_cache:
        cmd_clean_cache = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '-Scc']
    else:
        cmd_clean_cache = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '-Sc']
    
    if dry_run:
        log.info("Dry run: Would have cleaned package cache.")
    else:
        try:
            subprocess.run(cmd_clean_cache, check=True)
        except subprocess.CalledProcessError as e:
            log.error(f"Failed to clean cache: {e}")
    
    log.success("System cleanup completed.")
