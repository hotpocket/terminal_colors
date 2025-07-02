from .colors import Color, printc

def main():
    """Demonstrates usage of the Color class and printc function."""
    printc("--- Terminal Colors Demo ---", fg=Color.white.bolded(), bg=Color.black)
    printc("Hello, Red Text!", fg=Color.red)
    printc("Bold Green Text!", fg=Color.green.bolded())
    printc("Green Background!", bg=Color.green)
    printc("Bold Green Background!", bg=Color.green.bolded())

    printc("Yellow Text on Blue Background!",
           fg=Color.yellow,
           bg=Color.blue)

    printc("Bold Yellow Text on Bold Blue Background!",
           fg=Color.yellow.bolded(),
           bg=Color.blue.bolded())

    printc("Magenta text on Cyan background",
           fg=Color.magenta,
           bg=Color.cyan)
    printc("Black text, Bold Red Background",
           fg=Color.black,
           bg=Color.red.bolded())
    printc("No color applied.", end="\n\n")

    # Demonstrating passing print kwargs
    printc("This is on a new line", fg=Color.blue, end=" ", flush=True)
    printc("and this is after a space!", fg=Color.cyan)

    # Example of invalid color name for Color class
    try:
        Color('orange')
    except ValueError as e:
        printc(f"Error creating color: {e}", fg=Color.red.bolded())

    # Example of passing wrong type to printc
    try:
        # Mypy will flag this, but for runtime demo it's fine
        printc("Error with type", fg="red") # type: ignore
    except TypeError as e:
        printc(f"Error using printc: {e}", fg=Color.red.bolded())

    # Example of using a color object directly as a string (it won't apply color to itself)
    printc(f"Color object: {Color.red}", fg=Color.blue)

if __name__ == "__main__":
    main()