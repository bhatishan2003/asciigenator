import asciigenator
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
from asciigenator import cli


# ============================================================================
# API Tests - Testing the core library functions
# ============================================================================


def test_generate_simple_font():
    """Test basic ASCII generation with simple font."""
    result = asciigenator.generate("Hello", font="simple")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    assert "*" in result  # Simple font uses asterisks


def test_generate_block_font():
    """Test ASCII generation with block font."""
    result = asciigenator.generate("W1rld", font="block")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    assert "█" in result  # Block font uses block characters


def test_generate_empty_string():
    """Test ASCII generation with empty string."""
    result = asciigenator.generate("", font="simple")
    assert result.strip() == ""


def test_generate_with_color():
    """Test ASCII generation with color."""
    result = asciigenator.generate("Hello", font="simple", color="red")
    assert isinstance(result, str)
    assert len(result.strip()) > 0
    # Check for ANSI color codes
    assert "\033[31m" in result  # Red color code
    assert "\033[0m" in result  # Reset code
    assert "*" in result  # Simple font pattern


def test_generate_with_border():
    """Test ASCII generation with border."""
    result = asciigenator.generate("Hi", font="simple", border="#")
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
    result = asciigenator.generate("Test", font="simple", color="blue", border="*")
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
    result = asciigenator.generate("A", font="block", border="+")
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
        asciigenator.generate("Hello", font="invalid_font")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Font 'invalid_font' not available" in str(e)


def test_invalid_color():
    """Test error handling for invalid color."""
    try:
        asciigenator.generate("Hello", font="simple", color="invalid_color")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "Color 'invalid_color' not available" in str(e)


def test_list_fonts():
    """Test listing available fonts."""
    fonts = asciigenator.list_fonts()
    assert isinstance(fonts, list)
    assert "simple" in fonts
    assert "block" in fonts
    assert len(fonts) >= 2


def test_list_colors():
    """Test listing available colors."""
    colors = asciigenator.list_colors()
    assert isinstance(colors, list)
    assert "red" in colors
    assert "blue" in colors
    assert "green" in colors
    assert len(colors) >= 8  # Should have at least basic colors


def test_border_with_different_characters():
    """Test border with different border characters."""
    test_chars = ["#", "*", "=", "+", "-", "|"]

    for border_char in test_chars:
        result = asciigenator.generate("X", font="simple", border=border_char)
        assert isinstance(result, str)
        assert border_char in result
        lines = result.split("\n")
        # First and last lines should contain the border character
        assert border_char in lines[0]
        assert border_char in lines[-1]


def test_empty_border():
    """Test that None border doesn't add border."""
    result_no_border = asciigenator.generate("Test", font="simple")
    result_none_border = asciigenator.generate("Test", font="simple", border=None)
    assert result_no_border == result_none_border


def test_case_insensitive():
    """Test that text is converted to uppercase properly."""
    result_lower = asciigenator.generate("hello", font="simple")
    result_upper = asciigenator.generate("HELLO", font="simple")
    assert result_lower == result_upper


# ============================================================================
# CLI Helper Function - Direct CLI testing without subprocess
# ============================================================================


def call_cli_function(args):
    """
    Helper to call CLI main function directly with args.
    This ensures proper coverage tracking for CLI code.
    """
    # Save original sys.argv
    original_argv = sys.argv[:]

    try:
        # Set up sys.argv as if called from command line
        sys.argv = ["asciigenator"] + args

        # Capture stdout and stderr
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()

        exit_code = 0

        with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
            try:
                cli.main()
            except SystemExit as e:
                exit_code = e.code if e.code is not None else 0

        return stdout_buffer.getvalue(), stderr_buffer.getvalue(), exit_code

    finally:
        # Restore original sys.argv
        sys.argv = original_argv


# ============================================================================
# CLI Tests - Testing command-line interface directly
# ============================================================================


def test_list_fonts_cli():
    """Test listing available fonts via CLI."""
    out, err, code = call_cli_function(["--list-fonts"])
    assert code == 0
    assert "simple" in out
    assert "block" in out


def test_list_colors_cli():
    """Test listing available colors via CLI."""
    out, err, code = call_cli_function(["--list-colors"])
    assert code == 0
    assert "Available colors:" in out
    assert "red" in out
    assert "blue" in out
    assert "green" in out


def test_generate_basic_text_cli():
    """Test basic text generation via CLI."""
    out, err, code = call_cli_function(["Hello"])
    assert code == 0
    assert len(out.strip()) > 0
    assert "*" in out  # Default simple font uses asterisks


def test_generate_with_font_cli():
    """Test font selection via CLI."""
    out, err, code = call_cli_function(["Test", "--font", "block"])
    assert code == 0
    assert "█" in out or "╗" in out or "║" in out  # Block font characters


def test_generate_with_font_short_cli():
    """Test font selection via CLI with short flag."""
    out, err, code = call_cli_function(["Test", "-f", "block"])
    assert code == 0
    assert "█" in out or "╗" in out or "║" in out  # Block font characters


def test_generate_with_color_cli():
    """Test ASCII generation with color via CLI."""
    out, err, code = call_cli_function(["Hi", "--color", "red"])
    assert code == 0
    assert "\033[31m" in out  # Red color code
    assert "\033[0m" in out  # Reset code


def test_generate_with_color_short_cli():
    """Test ASCII generation with color via CLI using short flag."""
    out, err, code = call_cli_function(["Hi", "-c", "red"])
    assert code == 0
    assert "\033[31m" in out  # Red color code
    assert "\033[0m" in out  # Reset code


def test_generate_with_border_cli():
    """Test border generation via CLI."""
    out, err, code = call_cli_function(["Hi", "--border", "#"])
    assert code == 0
    lines = out.splitlines()
    assert "#" in out
    assert len([line for line in lines if line.strip()]) > 0
    # Check that border appears in output
    assert any("#" in line for line in lines)


def test_generate_with_border_short_cli():
    """Test border generation via CLI with short flag."""
    out, err, code = call_cli_function(["Hi", "-b", "#"])
    assert code == 0
    lines = out.splitlines()
    assert "#" in out
    assert any("#" in line for line in lines)


def test_generate_with_all_options_cli():
    """Test generation with all options combined."""
    out, err, code = call_cli_function(["Test", "--font", "simple", "--color", "blue", "--border", "*"])
    assert code == 0
    assert "\033[34m" in out  # Blue color code
    assert "\033[0m" in out  # Reset code
    assert "*" in out  # Border and/or font character


def test_no_arguments_shows_help():
    """Test that running CLI with no arguments shows help."""
    out, err, code = call_cli_function([])
    assert code == 0
    assert "usage:" in out or "Generate ASCII art from text" in out


def test_help_flag():
    """Test help flag."""
    out, err, code = call_cli_function(["--help"])
    assert code == 0
    assert "usage:" in out
    assert "--font" in out
    assert "--color" in out
    assert "--border" in out


def test_help_short_flag():
    """Test short help flag."""
    out, err, code = call_cli_function(["-h"])
    assert code == 0
    assert "usage:" in out
    assert "--font" in out
    assert "--color" in out
    assert "--border" in out


def test_cli_invalid_font_error():
    """Test CLI error handling for invalid font."""
    out, err, code = call_cli_function(["Test", "-f", "nonexistent_font"])
    assert code == 1
    assert "Error:" in err
    assert "Font 'nonexistent_font' not available" in err


def test_cli_invalid_color_error():
    """Test CLI error handling for invalid color."""
    out, err, code = call_cli_function(["Test", "-c", "nonexistent_color"])
    assert code == 1
    assert "Error:" in err
    assert "Color 'nonexistent_color' not available" in err


def test_version_flag():
    """Test version flag if it exists."""
    try:
        out, err, code = call_cli_function(["--version"])
        # If version flag exists, it should exit with code 0
        if code == 0:
            assert len(out.strip()) > 0
    except SystemExit:
        # If version flag doesn't exist or behaves differently, that's okay
        pass


def test_special_characters_cli():
    """Test CLI with special characters."""
    out, err, code = call_cli_function(["A1B"])
    assert code == 0
    assert len(out.strip()) > 0


def test_empty_text_cli():
    """Test CLI with empty text."""
    out, err, code = call_cli_function([""])
    assert code == 0
    # Empty text should produce minimal output


# ============================================================================
# Integration Tests - Testing API and CLI consistency
# ============================================================================


def test_api_cli_consistency_simple():
    """Test that API and CLI produce the same output for simple cases."""
    api_result = asciigenator.generate("Test", font="simple")
    cli_out, cli_err, cli_code = call_cli_function(["Test", "-f", "simple"])

    assert cli_code == 0
    # Strip trailing whitespace for comparison
    assert api_result.strip() == cli_out.strip()


def test_api_cli_consistency_with_color():
    """Test API and CLI consistency with color."""
    api_result = asciigenator.generate("Hi", font="simple", color="red")
    cli_out, cli_err, cli_code = call_cli_function(["Hi", "-f", "simple", "-c", "red"])

    assert cli_code == 0
    assert api_result.strip() == cli_out.strip()


def test_api_cli_consistency_with_border():
    """Test API and CLI consistency with border."""
    api_result = asciigenator.generate("X", font="simple", border="#")
    cli_out, cli_err, cli_code = call_cli_function(["X", "-f", "simple", "-b", "#"])

    assert cli_code == 0
    assert api_result.strip() == cli_out.strip()


def test_api_cli_font_list_consistency():
    """Test that API and CLI return the same font list."""
    api_fonts = set(asciigenator.list_fonts())

    cli_out, cli_err, cli_code = call_cli_function(["--list-fonts"])
    assert cli_code == 0

    # Extract font names from CLI output
    cli_fonts = set()
    for line in cli_out.split("\n"):
        line = line.strip()
        if line and not line.startswith("Available") and ":" not in line:
            cli_fonts.add(line)

    # At minimum, both should contain 'simple' and 'block'
    assert "simple" in api_fonts
    assert "simple" in cli_out
    assert "block" in api_fonts
    assert "block" in cli_out


def test_api_cli_color_list_consistency():
    """Test that API and CLI return consistent color information."""
    api_colors = set(asciigenator.list_colors())

    cli_out, cli_err, cli_code = call_cli_function(["--list-colors"])
    assert cli_code == 0

    # Basic colors should be present in both
    basic_colors = ["red", "blue", "green", "yellow"]
    for color in basic_colors:
        assert color in api_colors
        assert color in cli_out
