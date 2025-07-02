# Terminal Colors

A simple and user-friendly Python package for printing colored and styled text to the terminal,
with excellent IDE autocompletion support.

## Features

- **Intuitive Color Objects:** Define colors using `Color.red`, `Color.blue.bold()`, etc., for clear and readable code.
- **IDE Friendly:** Provides strong type hints and static attributes for excellent code completion (IntelliSense) in your editor.
- **Seamless `print` Integration:** The `printc` function acts as an enhanced `print` that accepts `Color` objects via `fg` (foreground) and `bg` (background) arguments, while supporting all standard `print` arguments (`end`, `sep`, `file`, `flush`).

- **Cross-Platform Compatibility:** Uses standard ANSI escape codes, which are widely supported by modern terminals.

## Installation

You can install this package directly from its Git repository.

```bash
pip install git+https://github.com/hotpocket/terminal_colors.git
```

If you need to install a specific branch, tag, or commit, or if it's a private repository (using SSH), consult pip's documentation for "Installing from VCS." For example, to install from the `dev` branch:

```bash
pip install git+https://github.com/hotpocket/terminal_colors.git@dev
```

## Usage

```python
from terminal_colors import Color, printc

# Print text in a specific foreground color
printc("This is red text!", fg=Color.red)

# Print text with a bold background color
printc("Green background!", bg=Color.green.bold())

# Combine foreground and background colors
printc("Blue text on a yellow background.",
       fg=Color.blue,
       bg=Color.yellow)

# Make text bold (bright)
printc("This text is bold magenta.", fg=Color.magenta.bold())

# Use standard print arguments
printc("Part 1: ", fg=Color.cyan, end="")
printc("Part 2.", fg=Color.cyan.bold())

# Example with all colors
printc("Black", fg=Color.black)
printc("Red", fg=Color.red)
printc("Green", fg=Color.green)
printc("Yellow", fg=Color.yellow)
printc("Blue", fg=Color.blue)
printc("Magenta", fg=Color.magenta)
printc("Cyan", fg=Color.cyan)
printc("White", fg=Color.white)
printc("Bold Red", fg=Color.red.bold())

printc("On Red Background", bg=Color.red)
printc("On Bold Green Background", bg=Color.green.bold())
```

## Running the Demo

After installation, you can run the built-in demo script:

```bash
python -m terminal_colors
```

## Project Structure
```
terminal_colors/
├── setup.py
├── README.md
├── src/
│   ├── __init__.py
│   ├── colors.py
│   └── __main__.py
├── tests/
└── docs/
```
## License
This project is licensed under the MIT License. See the LICENSE file for details.