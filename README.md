# ASCIIGEN <!-- omit in toc -->

A lightweight Python library for generating ASCII art from text.

[![PyPI version](https://img.shields.io/pypi/v/asciigen.svg?color=blue)](https://pypi.org/project/asciigen/)
[![Python Versions](https://img.shields.io/pypi/pyversions/asciigen.svg)](https://pypi.org/project/asciigen/)
[![License](https://img.shields.io/github/license/bhatishan2003/asciigen)](LICENSE)
[![Tests](https://github.com/bhatishan2003/asciigen/actions/workflows/tests.yml/badge.svg)](https://github.com/bhatishan2003/asciigen/actions)
[![Coverage](https://img.shields.io/codecov/c/github/bhatishan2003/asciigen)](https://codecov.io/gh/bhatishan2003/asciigen)

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
- [Usage](#usage)
  - [Basic Python Usage](#basic-python-usage)
  - [Command Line Usage](#command-line-usage)
- [Testing](#testing)
- [Development Notes](#development-notes)

---

## Installation

- Clone the repository:

  ```bash
  git clone https://github.com/bhatishan2003/asciigen.git
  cd asciigen
  ```

- Install the package:

  ```bash
  pip install .
  ```

- For development (editable mode):

  ```bash
  pip install -e .
  ```

## Usage

### Basic Python Usage

```python
import asciigen

# Test simple font
print("=== Simple Font ===")
print(asciigen.generate("Hello", font="simple"))

# === Simple Font ===
#  *  ** **** ****** *
# * **  *  ***  *  ***
# *** * *  *** *** ***
# * *  **  *** **  ***
# * ***  **** ****** *

print("\n=== Block Font ===")
print(asciigen.generate("Ishan", font="block"))

# === Block Font ===
#  █████╗ ███████╗ ██████╗██╗██╗ ██████╗ ███████╗███╗   ██╗
# ██╔══██╗██╔════╝██╔════╝██║██║██╔════╝ ██╔════╝████╗  ██║
# ███████║███████╗██║     ██║██║██║  ███╗█████╗  ██╔██╗ ██║
# ██╔══██║╚════██║██║     ██║██║██║   ██║██╔══╝  ██║╚██╗██║
# ██║  ██║███████║╚██████╗██║██║╚██████╔╝███████╗██║ ╚████║
# ╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝

print("\n=== Available Fonts ===")
print(asciigen.list_fonts())

# === Available Fonts ===
# ['block', 'simple']

```

### Command Line Usage

```bash
asciigen "Hello World"
asciigen "Hello World" --font block
asciigen --list-fonts
```

## Testing

Run all tests:

```bash
pytest -v
```

## Development Notes

- Pre-commit

  We use pre-commit to automate linting of our codebase.

  - Install hooks:
    ```bash
    pre-commit install
    ```
  - Run Hooks manually (optional):
    ```bash
    pre-commit run --all-files
    ```

- Ruff:

  - Lint and format:
    ```bash
    ruff check --fix
    ruff format
    ```
