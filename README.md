# ELTechnical Pacman GUI

**ELTechnical Pacman GUI** is a simple, user-friendly Qt-based graphical interface for installing well-known packages available via `pacman` on Arch Linux.

## Features

- Clean Qt UI
- Lists popular packages only
- Allows multi-selection using `Ctrl` key
- No support for AUR or drivers — only official `pacman` packages

## Requirements

- Python 3
- PyQt5
- Arch Linux (or any Arch-based distro)

## Installation

Clone this repository and build the package:

```bash
git clone https://github.com/eltechnical/eltechnical-pacman-gui.git
cd eltechnical-pacman-gui
makepkg -si
