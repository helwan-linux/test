# hpm/commands/list.py

import os
import subprocess
from rich.console import Console
from rich.table import Table
from hpm.utils import log
# We define PACMAN_PATH here to avoid the ImportError
PACMAN_PATH = "/usr/bin"

console = Console()

def list_main(dry_run: bool):
    """
    Lists all installed packages on the system.
    """
    log.info("Listing all installed packages...")
    
    # We use 'pacman -Q' to query all installed packages.
    # This command does not require sudo.
    cmd = [os.path.join(PACMAN_PATH, 'pacman'), '-Q']
    
    if dry_run:
        log.warning("Dry run: Would have listed all installed packages. No changes will be made.")
        return
        
    try:
        log.debug(f"Running command: {' '.join(cmd)}")
        
        # Run the command and capture the output
        process = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        # Split the output into a list of packages
        packages = process.stdout.strip().split('\n')
        
        if not packages:
            log.info("No packages found on the system.")
            return

        # Create a rich table to display the packages
        table = Table(title="[bold blue]Installed Packages[/bold blue]", show_header=True, header_style="bold magenta")
        table.add_column("Package Name", style="bold cyan")
        table.add_column("Version", style="bold green")

        for pkg_line in packages:
            if pkg_line:
                # Pacman -Q output is typically "package-name version"
                parts = pkg_line.split()
                if len(parts) == 2:
                    table.add_row(parts[0], parts[1])
        
        console.print(table)
        
        log.success("Package listing completed successfully!")
        
    except FileNotFoundError:
        log.error("Pacman not found. Please check your system configuration.")
    except subprocess.CalledProcessError:
        log.error("An error occurred while trying to list packages.")
    except Exception as e:
        log.error(f"An unexpected error occurred: {e}")
