import asciigen


def test_generate_simple_font():
    result = asciigen.generate("Hello", font="simple")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Optionally, check for a known pattern in the output
    assert "*" in result  # Simple font uses asterisks


def test_generate_block_font():
    result = asciigen.generate("W1rld", font="block")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Optionally, check for a known pattern in the output
    assert "█" in result  # Block font uses block characters


def test_generate_empty_string():
    result = asciigen.generate("", font="simple")
    assert result.strip() == ""


def test_generate_with_color():
    """Test ASCII generation with color."""
    result = asciigen.generate("Hello", font="simple", color="red")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Check for ANSI color codes
    assert "\033[31m" in result  # Red color code
    assert "\033[0m" in result  # Reset code
    assert "*" in result  # Simple font pattern


def test_generate_with_border():
    """Test ASCII generation with border."""
    result = asciigen.generate("Hi", font="simple", border="#")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Check for border characters
    assert "#" in result
    assert "*" in result  # Original content should still be there
    lines = result.split("\n")
    # First and last lines should be all border characters
    assert all(char == "#" for char in lines[0])
    assert all(char == "#" for char in lines[-1])


def test_generate_with_color_and_border():
    """Test ASCII generation with both color and border."""
    result = asciigen.generate("Test", font="simple", color="blue", border="*")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Check for color codes
    assert "\033[34m" in result  # Blue color code
    assert "\033[0m" in result  # Reset code
    # Check for border
    assert "*" in result
    lines = result.split("\n")
    # Should have border lines
    assert len(lines) > 5  # Original content + border lines


def test_generate_block_font_with_border():
    """Test block font with border."""
    result = asciigen.generate("A", font="block", border="+")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Check for both block characters and border
    assert "█" in result or "╗" in result or "║" in result  # Block font characters
    assert "+" in result  # Border character
    lines = result.split("\n")
    # First and last lines should be all border characters
    assert all(char == "+" for char in lines[0])
    assert all(char == "+" for char in lines[-1])


def test_invalid_font():
    """Test error handling for invalid font."""
    try:
        asciigen.generate("Hello", font="invalid_font")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Font 'invalid_font' not available" in str(e)


def test_invalid_color():
    """Test error handling for invalid color."""
    try:
        asciigen.generate("Hello", font="simple", color="invalid_color")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Color 'invalid_color' not available" in str(e)


def test_list_fonts():
    """Test listing available fonts."""
    fonts = asciigen.list_fonts()
    assert isinstance(fonts, list)
    assert "simple" in fonts
    assert "block" in fonts
    assert len(fonts) >= 2


def test_list_colors():
    """Test listing available colors."""
    colors = asciigen.list_colors()
    assert isinstance(colors, list)
    assert "red" in colors
    assert "blue" in colors
    assert "green" in colors
    assert len(colors) >= 8  # Should have at least basic colors


def test_border_with_different_characters():
    """Test border with different border characters."""
    test_chars = ["#", "*", "=", "+", "-", "|"]

    for border_char in test_chars:
        result = asciigen.generate("X", font="simple", border=border_char)
        assert isinstance(result, str)
        assert border_char in result
        lines = result.split("\n")
        # First and last lines should contain the border character
        assert border_char in lines[0]
        assert border_char in lines[-1]


def test_empty_border():
    """Test that None border doesn't add border."""
    result_no_border = asciigen.generate("Test", font="simple")
    result_none_border = asciigen.generate("Test", font="simple", border=None)
    assert result_no_border == result_none_border


def test_case_insensitive():
    """Test that text is converted to uppercase properly."""
    result_lower = asciigen.generate("hello", font="simple")
    result_upper = asciigen.generate("HELLO", font="simple")
    assert result_lower == result_upper
