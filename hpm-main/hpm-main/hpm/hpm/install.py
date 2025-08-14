# hpm/hpm/commands/install.py

import typer
import subprocess
from typing import List
from hpm.utils import log, pacman, safety

def install_main(packages: List[str], force: bool, dry_run: bool = False):
    log.info(f"Preparing to install: {', '.join(packages)}")
    
    if not force and not dry_run:
        if not safety.ask_confirmation("Proceed with installation?"):
            log.info("Installation cancelled.")
            return

    # Call the pacman command with the dry_run flag
    result = pacman.run_pacman_command(['-S'] + packages, as_sudo=True, dry_run=dry_run)
    
    if isinstance(result, subprocess.CalledProcessError):
        log.error("Installation failed. See the error details above.")
        return

    log.success("Packages installed successfully.")

# Note: The command decorator in cli.py is already handled
