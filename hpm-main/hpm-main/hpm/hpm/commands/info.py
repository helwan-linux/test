# hpm/hpm/commands/info.py

import typer
import subprocess
import re
from typing import List
from typing_extensions import Annotated
from hpm.utils import log
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="Displays detailed information about a package.")
console = Console()

def parse_pacman_info(raw_output: str) -> dict:
    """
    Parses the raw output from a pacman info command into a dictionary.
    """
    info = {}
    lines = raw_output.strip().split('\n')
    current_key = None
    
    for line in lines:
        match = re.match(r"^(.*?)\s*:\s*(.*)$", line)
        if match:
            key, value = match.groups()
            key = key.strip()
            value = value.strip()
            if key in info:
                info[key] += f", {value}"
            else:
                info[key] = value
            current_key = key
        else:
            if current_key and line.strip():
                # Handle multi-line values
                info[current_key] += f"\n{line.strip()}"
    return info

@app.command()
def info_main(
    packages: Annotated[List[str], typer.Argument(help="One or more package names", metavar="PACKAGE...")],
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would be done without executing")] = False
):
    """
    Main function to fetch and display package information.
    """
    for package in packages:
        log.info(f"Fetching information for: {package}")
        
        if dry_run:
            log.debug(f"[dry-run] Would run pacman info for: {package}")
            continue

        try:
            # Check if the package is installed first
            is_installed_result = subprocess.run(
                ["pacman", "-Qi", package],
                check=False,
                capture_output=True,
                text=True
            )
            
            # Use the correct command based on installation status
            if is_installed_result.returncode == 0:
                command = ["pacman", "-Qi", package]
            else:
                command = ["pacman", "-Si", package]

            log.debug(f"Running command: {' '.join(command)}")
            result = subprocess.run(command, check=True, capture_output=True, text=True)

            # The command was successful, so parse the stdout
            info_dict = parse_pacman_info(result.stdout)
            
            # Create a two-column rich Table for displaying the results
            table = Table(title=f"Package Information: {info_dict.get('Name', 'N/A')}", title_style="bold cyan")
            table.add_column("Key", style="bold green", no_wrap=True)
            table.add_column("Value", style="white")

            for key, value in info_dict.items():
                table.add_row(key, value)
            
            console.print(table)
            console.print("\n")
            
            log.success(f"Information for '{package}' fetched successfully.")

        except subprocess.CalledProcessError as e:
            log.error(f"Could not find package '{package}'.")
            if e.stderr:
                log.debug(f"Command failed with error: {e.stderr.decode('utf-8')}")
        except FileNotFoundError:
            log.error("pacman was not found. Are you running this on Arch Linux or WSL with Arch?")
            raise typer.Exit(code=1)
        except Exception as e:
            log.error(f"An unexpected error occurred while fetching info for '{package}': {e}")
