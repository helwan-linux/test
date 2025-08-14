# hpm/hpm/utils/log.py

from rich.console import Console

console = Console()

def info(message: str):
    console.print(f"ℹ {message}", style="bold cyan")

def success(message: str):
    console.print(f"✔ {message}", style="bold green")

def warning(message: str):
    console.print(f"⚠ {message}", style="bold yellow")

def error(message: str):
    console.print(f"✖ {message}", style="bold red")

def debug(message: str):
    console.print(f"[DEBUG] {message}", style="dim")
