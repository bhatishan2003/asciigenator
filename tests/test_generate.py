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
