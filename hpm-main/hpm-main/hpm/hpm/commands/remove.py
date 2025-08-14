# hpm/commands/remove.py
import subprocess
from typing import List
from hpm.utils import log
from hpm.i18n import get_translation

def remove_main(
    packages: List[str],
    force: bool,
    dry_run: bool
):
    """Removes a package."""
    translate = get_translation("en") # سنصلح هذه لاحقًا لتعمل تلقائيًا
    log.info(f"Preparing to remove: {', '.join(packages)}")

    if dry_run:
        log.warning("Running in dry-run mode. No changes will be made to the system.")
        log.info(f"Would run: sudo pacman -Rns" + (" --noconfirm" if force else "") + " " + " ".join(packages))
        return

    try:
        command = ["sudo", "pacman", "-Rns"]
        if force:
            command.append("--noconfirm")
        command.extend(packages)
        subprocess.run(command, check=True)
        log.success(f"Successfully removed packages: {', '.join(packages)}")
    except subprocess.CalledProcessError as e:
        log.error(f"Failed to remove packages. Error: {e}")
    except FileNotFoundError:
        log.error("The `pacman` command was not found. Are you on an Arch-based system?")
