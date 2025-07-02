# terminal_colors/__main__.py

from .colors import Color, printc

def main():
    """Demonstrates usage of the Color class and printc function."""
    printc("--- Terminal Colors Demo ---", foreground_color=Color.white.bold(), background_color=Color.black)
    printc("Hello, Red Text!", foreground_color=Color.red)
    printc("Bright Green Text!", foreground_color=Color.green.bold())
    printc("Green Background!", background_color=Color.green)
    printc("Bright Green Background!", background_color=Color.green.bold())

    printc("Yellow Text on Blue Background!",
           foreground_color=Color.yellow,
           background_color=Color.blue)

    printc("Bright Yellow Text on Bright Blue Background!",
           foreground_color=Color.yellow.bold(),
           background_color=Color.blue.bold())

    printc("Magenta text on Cyan background",
           foreground_color=Color.magenta,
           background_color=Color.cyan)
    printc("Black text, Bright Red Background",
           foreground_color=Color.black,
           background_color=Color.red.bold())
    printc("No color applied.", end="\n\n")

    # Demonstrating passing print kwargs
    printc("This is on a new line", foreground_color=Color.blue, end=" ", flush=True)
    printc("and this is after a space!", foreground_color=Color.cyan)

    # Example of invalid color name for Color class
    try:
        Color('orange')
    except ValueError as e:
        printc(f"Error creating color: {e}", foreground_color=Color.red.bold())

    # Example of passing wrong type to printc
    try:
        # Mypy will flag this, but for runtime demo it's fine
        printc("Error with type", foreground_color="red") # type: ignore
    except TypeError as e:
        printc(f"Error using printc: {e}", foreground_color=Color.red.bold())

    # Example of using a color object directly as a string (it won't apply color to itself)
    printc(f"Color object: {Color.red}", foreground_color=Color.blue)

if __name__ == "__main__":
    main()