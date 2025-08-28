"""
Core functionality for ASCII art generation with color and border support.
"""

from typing import Dict, List


class ASCIIGenerator:
    """ASCII Art Generator class with color and border support."""

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

    def _add_border(self, text: str, border_char: str, padding: int = 1) -> str:
        """
        Add a border around the text.

        Args:
            text (str): The ASCII art text
            border_char (str): Character to use for the border
            padding (int): Padding around the text inside the border

        Returns:
            str: Text with border added
        """
        if not text or not text.strip():
            return text

        # Split into lines and find the maximum width
        lines = text.split("\n")
        if not lines:
            return text

        # Remove ANSI color codes when calculating width
        import re

        ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

        max_width = 0
        clean_lines = []
        for line in lines:
            clean_line = ansi_escape.sub("", line)
            clean_lines.append(clean_line)
            max_width = max(max_width, len(clean_line))

        if max_width == 0:
            return text

        # Calculate border dimensions
        inner_width = max_width + (2 * padding)
        border_width = inner_width + 2  # +2 for left and right border chars

        # Create the border
        top_border = border_char * border_width
        bottom_border = border_char * border_width

        # Create bordered content
        bordered_lines = [top_border]

        # Add empty padding lines at top if padding > 0
        for _ in range(padding):
            padding_line = border_char + " " * inner_width + border_char
            bordered_lines.append(padding_line)

        # Add content lines with padding
        for i, line in enumerate(lines):
            clean_line = clean_lines[i]
            # Calculate padding needed to center the content
            left_pad = " " * padding
            right_pad_needed = inner_width - padding - len(clean_line)
            right_pad = " " * max(0, right_pad_needed)

            bordered_line = border_char + left_pad + line + right_pad + border_char
            bordered_lines.append(bordered_line)

        # Add empty padding lines at bottom if padding > 0
        for _ in range(padding):
            padding_line = border_char + " " * inner_width + border_char
            bordered_lines.append(padding_line)

        bordered_lines.append(bottom_border)

        return "\n".join(bordered_lines)

    def generate(self, text: str, font: str = "simple", color: str = None, border: str = None) -> str:
        """
        Generate ASCII art for the given text.

        Args:
            text (str): The text to convert to ASCII art
            font (str): The font to use ('simple' or 'block')
            color (str): The color to use for the text
            border (str): Character to use for border (None for no border)

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

        # Add border if specified
        if border and result.strip():
            result = self._add_border(result, border)

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
def generate(text: str, font: str = "simple", color: str = None, border: str = None) -> str:
    """
    Generate ASCII art for the given text.

    Args:
        text (str): The text to convert to ASCII art
        font (str): The font to use (default: 'simple')
        color (str): The color to use for the text
        border (str): Character to use for border (None for no border)

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
        >>> print(asciigen.generate("Hello", font="simple", color="red", border="#"))
    """
    return _generator.generate(text, font, color, border)


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
