# hpm/hpm/commands/search.py

import typer
import subprocess
import re
from typing import List, Union
from typing_extensions import Annotated
from hpm.utils import log
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="Searches for packages in the repositories.")
console = Console()

def parse_search_output(raw_output: str) -> List[dict]:
    """
    Parses the raw output from a pacman search command into a list of dictionaries.
    This version correctly handles multi-line descriptions and ensures each package is
    a separate entry.
    """
    packages = []
    current_package = None
    lines = raw_output.strip().split('\n')

    package_header_pattern = re.compile(r"^(?P<repo>[^/]+)/(?P<name>[^ ]+)\s+(?P<version>.+)$")

    for line in lines:
        match = package_header_pattern.match(line)
        if match:
            # New package found, save the previous one if it exists
            if current_package:
                packages.append(current_package)

            # Start a new package dictionary
            current_package = {
                'Repo': match.group('repo').strip(),
                'Name': match.group('name').strip(),
                'Version': match.group('version').strip(),
                'Description': ''
            }
        elif current_package:
            # Append subsequent lines to the current package's description
            if current_package['Description']:
                current_package['Description'] += ' ' + line.strip()
            else:
                current_package['Description'] = line.strip()

    # Append the last package after the loop
    if current_package:
        packages.append(current_package)

    return packages

@app.command()
def search_main(
    packages: Annotated[List[str], typer.Argument(help="One or more search terms", metavar="QUERY...")],
    dry_run: Annotated[bool, typer.Option("--dry-run", help="Show what would be done without executing")] = False
):
    """
    Main function to search for packages.
    """
    if not packages:
        log.error("Please provide a search term.")
        raise typer.Exit(code=1)

    query_term = " ".join(packages)
    log.info(f"Searching for: {query_term}")
    
    if dry_run:
        log.debug(f"[dry-run] Would run pacman search for: {query_term}")
        return

    try:
        # We ensure 'packages' is a list before building the command
        if isinstance(packages, str):
            command_args = [packages]
        else:
            command_args = packages

        command = ["pacman", "-Ss"] + command_args
        log.debug(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        if result.returncode != 0:
            log.error(f"Search command failed with exit code {result.returncode}")
            return
            
        # If the output is empty, no packages were found
        if not result.stdout.strip():
            log.warning(f"No packages found matching '{query_term}'.")
            return
            
        # Parse the output and print it
        found_packages = parse_search_output(result.stdout)
        
        console.print(f"[bold cyan]──────────────── Search Results for: {query_term} ────────────────[/bold cyan]\n")

        for pkg in found_packages:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Key", style="bold green", no_wrap=True)
            table.add_column("Value", style="white")

            table.add_row("Repo", pkg.get('Repo', 'N/A'))
            table.add_row("Name", pkg.get('Name', 'N/A'))
            table.add_row("Version", pkg.get('Version', 'N/A'))
            table.add_row("Description", pkg.get('Description', 'N/A'))
            
            console.print(table)
            console.print("\n") # Add a line break for separation
        
        log.success(f"Search for '{query_term}' completed successfully.")

    except subprocess.CalledProcessError as e:
        log.error(f"Search failed with exit code {e.returncode}.")
        if e.stderr:
            log.debug(f"Error: {e.stderr.decode('utf-8')}")
    except FileNotFoundError:
        log.error("pacman was not found. Are you running this on Arch Linux or WSL with Arch?")
        raise typer.Exit(code=1)
    except Exception as e:
        log.error(f"An unexpected error occurred while searching for '{query_term}': {e}")
