# hpm/hpm/utils/pacman.py

import subprocess
import typer
from hpm.utils import log
from typing import Optional

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
        raise typer.Exit(code=1)

def run_pacman_command(args: list, as_sudo: bool = False) -> Optional[subprocess.CompletedProcess]:
    """
    Runs a pacman command with the given arguments and returns the result object.
    Returns None on failure.
    """
    command = ["sudo", "pacman"] if as_sudo else ["pacman"]
    command.extend(args)

    try:
        log.debug(f"Running command: {' '.join(command)}")
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        log.error(f"Command failed with exit code {e.returncode}")
        if e.stderr:
            print(e.stderr)
        return None
    except FileNotFoundError:
        log.error("pacman was not found. Are you running this on Arch Linux or WSL with Arch?")
        raise typer.Exit(code=1)
