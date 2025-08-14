# hpm/hpm/utils/pacman.py

import subprocess
import typer
from hpm.utils import log
from typing import List

def is_installed(package_name: str) -> bool:
    """
    Checks if a package is installed by querying the local pacman database.
    """
    try:
        subprocess.run(["pacman", "-Q", package_name], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        log.error("pacman was not found. Are you running this on Arch Linux or WSL with Arch?")
        typer.Exit(code=1)

def run_pacman_command(args: list, as_sudo: bool = False, dry_run: bool = False) -> bool:
    command = ["sudo", "pacman", "--noconfirm"] if as_sudo else ["pacman", "--noconfirm"]
    command.extend(args)

    if dry_run:
        log.info(f"[dry-run] Would have executed: {' '.join(command)}")
        return True

    try:
        log.debug(f"Running command: {' '.join(command)}")

        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )

        for line in process.stdout:
            print(line, end='')

        process.wait()
        return process.returncode == 0

    except FileNotFoundError:
        log.error("pacman was not found. Are you running this on Arch Linux or WSL with Arch?")
        raise typer.Exit(code=1)
    except Exception as e:
        log.error(f"Unexpected error: {e}")
        return False
