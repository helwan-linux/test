# hpm/commands/doctor.py

import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from hpm.utils import log
# We define PACMAN_PATH here to avoid the ImportError
PACMAN_PATH = "/usr/bin"

console = Console()

def check_orphans():
    """
    Checks for orphan packages and returns them as a list.
    """
    cmd = [os.path.join(PACMAN_PATH, 'pacman'), '-Qtdq']
    try:
        process = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        orphans = process.stdout.strip().split('\n')
        return [pkg for pkg in orphans if pkg]
    except Exception:
        return []

def check_broken_packages():
    """
    Checks for broken packages by verifying package files.
    Returns a list of broken packages.
    """
    cmd = [os.path.join(PACMAN_PATH, 'pacman'), '-Qk']
    try:
        process = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        # We look for lines that indicate an error
        broken = [line.split()[0] for line in process.stdout.split('\n') if "error" in line]
        return broken
    except Exception:
        return []

def doctor_main(dry_run: bool):
    """
    Performs a complete system health check.
    """
    log.info("Starting system health check...")
    
    if dry_run:
        log.warning("Dry run: Would have performed system diagnostics. No changes will be made.")
        return

    issues_found = False

    # Check for orphan packages
    log.info("Checking for orphan packages...")
    orphans = check_orphans()
    if orphans:
        issues_found = True
        panel_content = Text(f"Found {len(orphans)} orphan package(s).", style="bold red")
        panel_content.append("\nOrphan packages are dependencies that are no longer needed.")
        panel_content.append(f"\nTo fix, run:hpm orphans --remove")
        console.print(Panel(panel_content, title="[bold red]Orphan Packages Found[/bold red]", border_style="red"))
    else:
        log.success("No orphan packages found. Your system is clean!")

    # Check for broken packages
    log.info("Checking for broken packages...")
    broken_packages = check_broken_packages()
    if broken_packages:
        issues_found = True
        panel_content = Text(f"Found {len(broken_packages)} broken package(s).", style="bold red")
        panel_content.append("\nBroken packages have missing or modified files.")
        panel_content.append(f"\nTo fix, try reinstalling them manually: hpm install --force <package>")
        console.print(Panel(panel_content, title="[bold red]Broken Packages Found[/bold red]", border_style="red"))
    else:
        log.success("No broken packages found.")

    if not issues_found:
        console.print(Panel("[bold green]System health check completed successfully! No issues found.[/bold green]", title="[bold green]Health Check Summary[/bold green]", border_style="green"))
    else:
        log.warning("System health check completed with some issues. Please review the output above.")
