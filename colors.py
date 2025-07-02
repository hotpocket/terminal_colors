# terminal_colors/colors.py

from typing import Optional, Any

class Color:
    """
    Represents an ANSI color with a name and a bright/bold setting.
    Provides static factory methods for base colors and a method to get
    bright versions.
    """
    _color_map = {
        "black": 0, "red": 1, "green": 2, "yellow": 3,
        "blue": 4, "magenta": 5, "cyan": 6, "white": 7,
    }

    # Type hints for static instances for base colors
    black: 'Color'
    red: 'Color'
    green: 'Color'
    yellow: 'Color'
    blue: 'Color'
    magenta: 'Color'
    cyan: 'Color'
    white: 'Color'

    def __init__(self, name: str, bold: bool = False):
        """
        Initializes a Color object.

        Args:
            name (str): The name of the color (e.g., 'red', 'blue').
                        Valid names: 'black', 'red', 'green', 'yellow',
                        'blue', 'magenta', 'cyan', 'white'.
            bold (bool, optional): If True, the color will be its bright version.
                                     Defaults to False.

        Raises:
            ValueError: If an invalid color name is provided.
        """
        if name.lower() not in self._color_map:
            raise ValueError(f"Invalid color name: '{name}'. "
                             f"Valid names are: {', '.join(self._color_map.keys())}")
        self.name = name.lower()
        self.bold = bold

    def get_foreground_code(self) -> int:
        """
        Gets the ANSI escape code for the foreground (text) color.
        """
        base_code = self._color_map[self.name]
        return 30 + base_code if not self.bold else 90 + base_code

    def get_background_code(self) -> int:
        """
        Gets the ANSI escape code for the background color.
        """
        base_code = self._color_map[self.name]
        return 40 + base_code if not self.bold else 100 + base_code

    def bold(self) -> 'Color':
        """
        Returns a new Color object that is the bright version of this color.
        If the color is already bright, it returns a new identical bright color.

        Returns:
            Color: A new Color instance with bright set to True.
        """
        return Color(self.name, bold=True)

    def __str__(self) -> str:
        """String representation for debugging."""
        return f"Color(name='{self.name}', bold={self.bold})"

    def __repr__(self) -> str:
        return self.__str__()

# Initialize static color instances after the class definition
for _name in Color._color_map.keys():
    setattr(Color, _name, Color(_name))

def printc(text: str, foreground_color: Optional[Color] = None,
           background_color: Optional[Color] = None, **kwargs: Any) -> None:
    """
    Prints the given text to the console with ANSI escape codes for the specified
    foreground and background colors.

    Args:
        text (str): The text to print.
        foreground_color (Optional[Color]): A Color object representing the foreground color.
                                            Defaults to None (no foreground color change).
        background_color (Optional[Color]): A Color object representing the background color.
                                            Defaults to None (no background color change).
        **kwargs: Additional keyword arguments to pass directly to the built-in print() function,
                  such as 'end', 'sep', 'file', 'flush'.

    Returns:
        None

    Raises:
        TypeError: If foreground_color or background_color are not None or Color instances.

    Examples:
        >>> printc("Hello, Red Text!", foreground_color=Color.red)
        \033[31mHello, Red Text!\0033[0m

        >>> printc("Bright Green Text!", foreground_color=Color.green.bold())
        \033[92mBright Green Text!\0033[0m

        >>> printc("Blue text on Yellow background",
        ...        foreground_color=Color.blue,
        ...        background_color=Color.yellow.bold(),
        ...        end=" -- The End\\n")
        \033[34;103mBlue text on Yellow background\0033[0m -- The End
    """
    color_codes = []

    if foreground_color is not None:
        if not isinstance(foreground_color, Color):
            raise TypeError("foreground_color must be a Color instance or None.")
        color_codes.append(str(foreground_color.get_foreground_code()))

    if background_color is not None:
        if not isinstance(background_color, Color):
            raise TypeError("background_color must be a Color instance or None.")
        color_codes.append(str(background_color.get_background_code()))

    if not color_codes:
        # If no colors specified, just print the text directly
        print(text, **kwargs)
        return

    color_string = ";".join(color_codes)
    colored_text = f"\033[{color_string}m{text}\033[0m"
    print(colored_text, **kwargs)