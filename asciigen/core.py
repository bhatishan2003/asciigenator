"""
Core functionality for ASCII art generation.
"""

from typing import Dict, List


class ASCIIGenerator:
    """ASCII Art Generator class."""

    def __init__(self):
        """Initialize the generator with built-in fonts."""
        self.fonts = self._load_fonts()

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
                "K": ["██╗  ██╗", "██║ ██╔╝", "█████╔╝ ", "██╔═██╗ ", "██║  ██╗", "╚═╝  ╚═╝"],
                "L": ["██╗     ", "██║     ", "██║     ", "██║     ", "███████╗", "╚══════╝"],
                "M": ["███╗   ███╗", "████╗ ████║", "██╔████╔██║", "██║╚██╔╝██║", "██║ ╚═╝ ██║", "╚═╝     ╚═╝"],
                "N": ["███╗   ██╗", "████╗  ██║", "██╔██╗ ██║", "██║╚██╗██║", "██║ ╚████║", "╚═╝  ╚═══╝"],
                "O": [" ██████╗ ", "██╔═══██╗", "██║   ██║", "██║   ██║", "╚██████╔╝", " ╚═════╝ "],
                "P": ["██████╗ ", "██╔══██╗", "██████╔╝", "██╔═══╝ ", "██║     ", "╚═╝     "],
                "Q": [" ██████╗ ", "██╔═══██╗", "██║   ██║", "██║▄▄ ██║", "╚██████╔╝", " ╚══▀▀═╝ "],
                "R": ["██████╗ ", "██╔══██╗", "██████╔╝", "██╔══██╗", "██║  ██║", "╚═╝  ╚═╝"],
                "S": ["███████╗", "██╔════╝", "███████╗", "╚════██║", "███████║", "╚══════╝"],
                "T": ["████████╗", "╚══██╔══╝", "   ██║   ", "   ██║   ", "   ██║   ", "   ╚═╝   "],
                "U": ["██╗   ██╗", "██║   ██║", "██║   ██║", "██║   ██║", "╚██████╔╝", " ╚═════╝ "],
                "V": ["██╗   ██╗", "██║   ██║", "██║   ██║", "╚██╗ ██╔╝", " ╚████╔╝ ", "  ╚═══╝  "],
                "W": ["██╗    ██╗", "██║    ██║", "██║ █╗ ██║", "██║███╗██║", "╚███╔███╔╝", " ╚══╝╚══╝ "],
                "X": ["██╗  ██╗", "╚██╗██╔╝", " ╚███╔╝ ", " ██╔██╗ ", "██╔╝ ██╗", "╚═╝  ╚═╝"],
                "Y": ["██╗   ██╗", "╚██╗ ██╔╝", " ╚████╔╝ ", "  ╚██╔╝  ", "   ██║   ", "   ╚═╝   "],
                "Z": ["███████╗", "╚══███╔╝", "  ███╔╝ ", " ███╔╝  ", "███████╗", "╚══════╝"],
                " ": ["   ", "   ", "   ", "   ", "   ", "   "],
            },
            "simple": {
                "A": [" * ", "* *", "***", "* *", "* *"],
                "B": ["** ", "* *", "** ", "* *", "** "],
                "C": [" **", "*  ", "*  ", "*  ", " **"],
                "D": ["** ", "* *", "* *", "* *", "** "],
                "E": ["***", "*  ", "** ", "*  ", "***"],
                "F": ["***", "*  ", "** ", "*  ", "*  "],
                "G": [" **", "*  ", "* *", "* *", " **"],
                "H": ["* *", "* *", "***", "* *", "* *"],
                "I": ["*", "*", "*", "*", "*"],
                "J": ["  *", "  *", "  *", "* *", " * "],
                "K": ["* *", "** ", "*  ", "** ", "* *"],
                "L": ["*  ", "*  ", "*  ", "*  ", "***"],
                "M": ["* *", "***", "* *", "* *", "* *"],
                "N": ["* *", "***", "***", "***", "* *"],
                "O": [" * ", "* *", "* *", "* *", " * "],
                "P": ["** ", "* *", "** ", "*  ", "*  "],
                "Q": [" * ", "* *", "* *", "***", " **"],
                "R": ["** ", "* *", "** ", "** ", "* *"],
                "S": [" **", "*  ", " * ", "  *", "** "],
                "T": ["***", " * ", " * ", " * ", " * "],
                "U": ["* *", "* *", "* *", "* *", " * "],
                "V": ["* *", "* *", "* *", " * ", " * "],
                "W": ["* *", "* *", "* *", "***", "* *"],
                "X": ["* *", " * ", " * ", " * ", "* *"],
                "Y": ["* *", "* *", " * ", " * ", " * "],
                "Z": ["***", "  *", " * ", "*  ", "***"],
                " ": ["  ", "  ", "  ", "  ", "  "],
            },
        }
        return fonts

    def generate(self, text: str, font: str = "simple") -> str:
        """
        Generate ASCII art for the given text.

        Args:
            text (str): The text to convert to ASCII art
            font (str): The font to use ('simple' or 'block')

        Returns:
            str: The ASCII art representation of the text

        Raises:
            ValueError: If the font is not available
        """
        if font not in self.fonts:
            raise ValueError(f"Font '{font}' not available. Available fonts: {list(self.fonts.keys())}")

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
                        line += "   "  # Default spacing
            lines.append(line.rstrip())

        return "\n".join(lines)

    def list_fonts(self) -> List[str]:
        """
        List all available fonts.

        Returns:
            List[str]: List of available font names
        """
        return list(self.fonts.keys())


# Create a global instance
_generator = ASCIIGenerator()


# Public API functions
def generate(text: str, font: str = "simple") -> str:
    """
    Generate ASCII art for the given text.

    Args:
        text (str): The text to convert to ASCII art
        font (str): The font to use (default: 'simple')

    Returns:
        str: The ASCII art representation of the text

    Example:
        >>> import asciigen
        >>> print(asciigen.generate("Hello", font="simple"))
        * *      ***   *    *    ***
        * *       *    *    *    *  *
        ***       *    *    *    *  *
        * *       *    *    *    *  *
        * *      ***    ****     ***
    """
    return _generator.generate(text, font)


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
