# hpm/hpm/commands/alias.py

import typer
import subprocess
from typing import List, Optional
from hpm.utils import log, pacman, config

app = typer.Typer(help="Manages aliases for common pacman commands.")

@app.command(name="add", help="Adds a new alias for a pacman command.")
def add_alias(
    alias: str = typer.Argument(..., help="The alias to create."),
    command: List[str] = typer.Argument(..., help="The pacman command to alias.")
):
    """
    Adds a new alias to the configuration file.
    """
    conf = config.get_config()
    
    if alias in conf['aliases']:
        log.warning(f"Alias '{alias}' already exists. Updating...")
    
    conf['aliases'][alias] = command
    config.save_config(conf)
    log.success(f"Alias '{alias}' for 'pacman {' '.join(command)}' added successfully.")

@app.command(name="list", help="Lists all currently configured aliases.")
def list_aliases():
    """
    Lists all aliases from the configuration file.
    """
    conf = config.get_config()
    aliases = conf['aliases']

    if not aliases:
        log.info("No aliases configured yet.")
        return

    log.info("Available aliases:")
    for alias, command in aliases.items():
        log.info(f" - {alias} -> pacman {' '.join(command)}")

@app.command(name="remove", help="Removes an existing alias.")
def remove_alias(
    alias: str = typer.Argument(..., help="The alias to remove.")
):
    """
    Removes a configured alias.
    """
    conf = config.get_config()
    if alias in conf['aliases']:
        del conf['aliases'][alias]
        config.save_config(conf)
        log.success(f"Alias '{alias}' removed successfully.")
    else:
        log.error(f"Alias '{alias}' not found.")
        
@app.command(name="run", help="Runs an alias as if it were the original command.")
def run_alias(
    alias: str = typer.Argument(..., help="The alias to run."),
    extra_args: Optional[List[str]] = typer.Argument(None, help="Additional arguments for the alias command.")
):
    """
    Runs a configured alias with any additional arguments.
    """
    conf = config.get_config()
    if alias in conf['aliases']:
        pacman_command = conf['aliases'][alias]
        full_command = pacman_command + (extra_args if extra_args else [])
        
        # Determine if sudo is needed based on the command
        as_sudo = any(arg in full_command for arg in ['-S', '-R', '-U', '-Sc'])
        
        log.info(f"Executing alias '{alias}' -> pacman {' '.join(full_command)}")
        pacman.run_pacman_command(full_command, as_sudo=as_sudo)
    else:
        log.error(f"Alias '{alias}' not found.")
        typer.Exit(code=1)
