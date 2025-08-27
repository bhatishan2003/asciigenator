"""
Core functionality for ASCII art generation with color support.
"""

from typing import Dict, List


class ASCIIGenerator:
    """ASCII Art Generator class with color support."""

    def __init__(self):
        """Initialize the generator with built-in fonts."""
        self.fonts = self._load_fonts()
        self.colors = {
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "bright_black": "\033[90m",
            "bright_red": "\033[91m",
            "bright_green": "\033[92m",
            "bright_yellow": "\033[93m",
            "bright_blue": "\033[94m",
            "bright_magenta": "\033[95m",
            "bright_cyan": "\033[96m",
            "bright_white": "\033[97m",
        }
        self.reset = "\033[0m"

    def _load_fonts(self) -> Dict[str, Dict[str, List[str]]]:
        """Load font definitions."""
        fonts = {
            "block": {
                "A": [" █████╗ ", "██╔══██╗", "███████║", "██╔══██║", "██║  ██║", "╚═╝  ╚═╝"],
                "B": ["██████╗ ", "██╔══██╗", "██████╔╝", "██╔══██╗", "██████╔╝", "╚═════╝ "],
                "C": [" ██████╗", "██╔════╝", "██║     ", "██║     ", "╚██████╗", " ╚═════╝"],
                "D": ["██████╗ ", "██╔══██╗", "██║  ██║", "██║  ██║", "██████╔╝", "╚═════╝ "],
                "E": ["███████╗", "██╔════╝", "█████╗  ", "██╔══╝  ", "███████╗", "╚══════╝"],
                "F": ["███████╗", "██╔════╝", "█████╗  ", "██╔══╝  ", "██║     ", "╚═╝     "],
                "G": [" ██████╗ ", "██╔════╝ ", "██║  ███╗", "██║   ██║", "╚██████╔╝", " ╚═════╝ "],
                "H": ["██╗  ██╗", "██║  ██║", "███████║", "██╔══██║", "██║  ██║", "╚═╝  ╚═╝"],
                "I": ["██╗", "██║", "██║", "██║", "██║", "╚═╝"],
                "J": ["     ██╗", "     ██║", "     ██║", "██   ██║", "╚█████╔╝", " ╚════╝ "],
                "K": ["██╗ ██╗", "██║██╔╝", "█████╔╝ ", "██╔═██╗ ", "██║  ██╗", "╚═╝  ╚═╝"],
                "L": ["██╗     ", "██║     ", "██║     ", "██║     ", "███████╗", "╚══════╝"],
                "M": ["███╗   ███╗", "████╗ ████║", "██╔████╔██║", "██║╚██╔╝██║", "██║ ╚═╝ ██║", "╚═╝     ╚═╝"],
                "N": ["███╗   ██╗", "████╗  ██║", "██╔██╗ ██║", "██║╚██╗██║", "██║ ╚████║", "╚═╝  ╚═══╝"],
                "O": [" ██████╗ ", "██╔═══██╗", "██║   ██║", "██║   ██║", "╚██████╔╝", " ╚═════╝ "],
                "P": ["██████╗ ", "██╔══██╗", "██████╔╝", "██╔═══╝ ", "██║     ", "╚═╝     "],
                "Q": [" ██████╗ ", "██╔═══██╗", "██║   ██║", "██║▄▄ ██║", "╚██████╔╝", " ╚══▀▀═╝ "],
                "R": ["██████╗ ", "██╔══██╗", "██████╔╝", "██╔══██╗", "██║  ██║", "╚═╝  ╚═╝"],
                "S": ["███████╗", "██╔════╝", "███████╗", "╚════██║", "███████║", "╚══════╝"],
                "T": ["████████╗", "╚══██╔══╝", "   ██║   ", "   ██║   ", "   ██║   ", "   ╚═╝   "],
                "U": ["██╗  ██╗", "██║  ██║", "██║  ██║", "██║  ██║", "╚██████╔╝", " ╚═════╝ "],
                "V": ["██╗  ██╗", "██║  ██║", "██║  ██║", "╚██╗██╔╝", " ╚████╔╝ ", "  ╚═══╝  "],
                "W": ["██╗    ██╗", "██║    ██║", "██║ █╗ ██║", "██║███╗██║", "╚███╔███╔╝", " ╚══╝╚══╝ "],
                "X": ["██╗  ██╗", "╚██╗██╔╝", " ╚███╔╝ ", " ██╔██╗ ", "██╔╝ ██╗", "╚═╝  ╚═╝"],
                "Y": ["██╗  ██╗", "╚██╗██╔╝", " ╚████╔╝ ", "  ╚██╔╝  ", "   ██║   ", "   ╚═╝   "],
                "Z": ["███████╗", "╚══███╔╝", "  ███╔╝ ", " ███╔╝  ", "███████╗", "╚══════╝"],
                " ": ["        ", "        ", "        ", "        ", "        ", "        "],
            },
            "simple": {
                "A": [" * ", "* *", "***", "* *", "* *"],
                "B": ["** ", "* *", "** ", "* *", "** "],
                "C": [" **", "* ", "* ", "* ", " **"],
                "D": ["** ", "* *", "* *", "* *", "** "],
                "E": ["***", "* ", "** ", "* ", "***"],
                "F": ["***", "* ", "** ", "* ", "* "],
                "G": [" **", "* ", "* *", "* *", " **"],
                "H": ["* *", "* *", "***", "* *", "* *"],
                "I": ["*", "*", "*", "*", "*"],
                "J": [" *", " *", " *", "* *", " * "],
                "K": ["* *", "** ", "* ", "** ", "* *"],
                "L": ["* ", "* ", "* ", "* ", "***"],
                "M": ["* *", "***", "* *", "* *", "* *"],
                "N": ["* *", "***", "***", "***", "* *"],
                "O": [" * ", "* *", "* *", "* *", " * "],
                "P": ["** ", "* *", "** ", "* ", "* "],
                "Q": [" * ", "* *", "* *", "***", " **"],
                "R": ["** ", "* *", "** ", "** ", "* *"],
                "S": [" **", "* ", " * ", " *", "** "],
                "T": ["***", " * ", " * ", " * ", " * "],
                "U": ["* *", "* *", "* *", "* *", " * "],
                "V": ["* *", "* *", "* *", " * ", " * "],
                "W": ["* *", "* *", "* *", "***", "* *"],
                "X": ["* *", " * ", " * ", " * ", "* *"],
                "Y": ["* *", "* *", " * ", " * ", " * "],
                "Z": ["***", " *", " * ", "* ", "***"],
                " ": [" ", " ", " ", " ", " "],
            },
        }
        return fonts

    def generate(self, text: str, font: str = "simple", color: str = None) -> str:
        """
        Generate ASCII art for the given text.

        Args:
            text (str): The text to convert to ASCII art
            font (str): The font to use ('simple' or 'block')
            color (str): The color to use for the text

        Returns:
            str: The ASCII art representation of the text

        Raises:
            ValueError: If the font is not available or color is invalid
        """
        if font not in self.fonts:
            raise ValueError(f"Font '{font}' not available. Available fonts: {list(self.fonts.keys())}")

        if color and color not in self.colors:
            raise ValueError(f"Color '{color}' not available. Available colors: {list(self.colors.keys())}")

        text = text.upper()
        font_data = self.fonts[font]

        # Get the height of the font
        if not text:
            return ""

        # Find a character that exists to get the height
        sample_char = None
        for char in text:
            if char in font_data:
                sample_char = char
                break

        if sample_char is None:
            # No valid characters found, try space
            if " " in font_data:
                sample_char = " "
            else:
                return ""

        height = len(font_data[sample_char])

        # Generate each line of the ASCII art
        lines = []
        for i in range(height):
            line = ""
            for char in text:
                if char in font_data:
                    if i < len(font_data[char]):
                        line += font_data[char][i]
                    else:
                        line += " " * len(font_data[char][0])
                else:
                    # For unsupported characters, use space
                    if " " in font_data:
                        if i < len(font_data[" "]):
                            line += font_data[" "][i]
                        else:
                            line += " " * len(font_data[" "][0])
                    else:
                        line += " "  # Default spacing
            lines.append(line.rstrip())

        result = "\n".join(lines)

        # Apply color if specified
        if color and result.strip():
            color_code = self.colors[color]
            result = f"{color_code}{result}{self.reset}"

        return result

    def list_fonts(self) -> List[str]:
        """
        List all available fonts.

        Returns:
            List[str]: List of available font names
        """
        return list(self.fonts.keys())

    def list_colors(self) -> List[str]:
        """
        List all available colors.

        Returns:
            List[str]: List of available color names
        """
        return list(self.colors.keys())


# Create a global instance
_generator = ASCIIGenerator()


# Public API functions
def generate(text: str, font: str = "simple", color: str = None) -> str:
    """
    Generate ASCII art for the given text.

    Args:
        text (str): The text to convert to ASCII art
        font (str): The font to use (default: 'simple')
        color (str): The color to use for the text

    Returns:
        str: The ASCII art representation of the text

    Example:
        >>> import asciigen
        >>> print(asciigen.generate("Hello", font="simple"))
        * *  *** * * *** * *
        * * *   * *  *  * *
        *** *** ***  *  ***
        * * *   * *  *  * *
        * * *** * * ***  *
        >>> print(asciigen.generate("Hello", font="simple", color="red"))
    """
    return _generator.generate(text, font, color)


def list_fonts() -> List[str]:
    """
    List all available fonts.

    Returns:
        List[str]: List of available font names

    Example:
        >>> import asciigen
        >>> asciigen.list_fonts()
        ['simple', 'block']
    """
    return _generator.list_fonts()


def list_colors() -> List[str]:
    """
    List all available colors.

    Returns:
        List[str]: List of available color names

    Example:
        >>> import asciigen
        >>> asciigen.list_colors()
        ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white']
    """
    return _generator.list_colors()
