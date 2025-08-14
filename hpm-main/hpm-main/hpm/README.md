# hpm – A Friendly Frontend for Pacman

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Arch%20Linux-blue.svg)](https://archlinux.org)

`hpm` is a user-friendly and minimal CLI frontend for `pacman`, designed for Arch Linux users and derivatives. It simplifies common package management tasks through readable and intuitive commands.

---

## 🚀 Features

* 📦 Simple commands: `install`, `remove`, `upgrade`, etc.
* 🧹 System maintenance tools: cache cleaning and orphan management
* 🔍 Package search and info display
* 📜 Command history tracking
* 🌐 AUR support via `yay`
* 🩺 Full system health check (`doctor` command)
* 🧪 Dry-run mode (`--dry-run`) for safe testing
* 📁 Written in Python using `Typer` and `Rich`

---

## 🛠️ Installation

### From Source

```bash
git clone https://github.com/helwan-linux/helwan-pkg-manager.git
cd helwan-pkg-manager
pip install -e .
```

This will make the `hpm` command globally available in your terminal.

---

## 📚 Usage

### 📦 Install & Remove

```bash
sudo hpm install firefox
sudo hpm remove nano
```

### 🔄 Upgrade & Refresh

```bash
sudo hpm upgrade         # Upgrade all installed packages
sudo hpm refresh         # Sync databases + upgrade packages
```

### 🔍 Search & Info

```bash
hpm search terminal      # Search packages
hpm info htop            # Show detailed info
hpm list                 # List all installed packages
```

### 🧹 System Maintenance

```bash
sudo hpm clean
hpm orphans list
sudo hpm orphans remove
```

### 🌐 AUR Management

```bash
hpm aur install visual-studio-code-bin
```

### 🩺 System Health Check

```bash
hpm doctor
```

---

## 🧩 Global Options

* `--dry-run`, `-d`: Simulate actions without applying changes
* `--force`, `-f`: Skip confirmation prompts (for install/remove/upgrade)

---

## 🧪 Development

To run the app locally:

```bash
python main.py --help
```

To build a `.zst` package for Arch:

* Add a valid `PKGBUILD`
* Use `makepkg`

---

## 📄 License

MIT © Helwan Linux Team
