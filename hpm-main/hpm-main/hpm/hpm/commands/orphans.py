# hpm/commands/orphans.py

import os
import subprocess
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from hpm.utils import log
# We define PACMAN_PATH here to avoid the ImportError
PACMAN_PATH = "/usr/bin"

console = Console()

def orphans_main(remove: bool, dry_run: bool):
    """
    Manages orphan packages.
    """
    log.info("Checking for orphan packages...")
    
    # We use 'pacman -Qtdq' to query all installed orphan packages.
    # This command does not require sudo.
    cmd_list_orphans = [os.path.join(PACMAN_PATH, 'pacman'), '-Qtdq']
    
    if dry_run:
        log.warning("Dry run: Would have checked for orphan packages. No changes will be made.")
        return
        
    try:
        log.debug(f"Running command: {' '.join(cmd_list_orphans)}")
        
        process = subprocess.run(
            cmd_list_orphans,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False # We don't want to raise an exception if no orphans are found
        )
        
        orphan_packages = process.stdout.strip().split('\n')
        
        # Check if there are any orphan packages
        if not orphan_packages or orphan_packages == ['']:
            log.info("No orphan packages found. Your system is clean!")
            return

        # Display the list in a table
        table = Table(title="[bold red]Orphan Packages Found[/bold red]", show_header=True, header_style="bold magenta")
        table.add_column("Package Name", style="bold cyan")

        for pkg in orphan_packages:
            if pkg:
                table.add_row(pkg)
        
        console.print(table)

        # Proceed to remove if the --remove flag is set
        if remove:
            response = console.input("[bold yellow]:: Proceed with removing these packages? [Y/n][/bold yellow] ")
            if response.lower() not in ['y', 'yes', '']:
                log.info("Removal aborted by user.")
                return

            log.info("Removing orphan packages...")
            cmd_remove = [os.path.join(PACMAN_PATH, 'sudo'), 'pacman', '-Rns', '--noconfirm'] + orphan_packages
            
            try:
                subprocess.run(cmd_remove)
                log.success("Orphan packages removed successfully!")
            except Exception as e:
                log.error(f"Failed to remove orphan packages: {e}")
        else:
            log.info("To remove these packages, run: python main.py orphans --remove")
            
    except FileNotFoundError:
        log.error("Pacman not found. Please check your system configuration.")
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")
