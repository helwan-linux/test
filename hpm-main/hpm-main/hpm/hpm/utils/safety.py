# hpm/hpm/utils/safety.py

import typer
from hpm.utils import log

def ask_confirmation(message: str) -> bool:
    """
    Asks the user for confirmation and returns True if they say 'yes', False otherwise.
    """
    log.info(message)
    response = typer.prompt("Continue? [y/n]", default="y")
    return response.lower() == 'y'
