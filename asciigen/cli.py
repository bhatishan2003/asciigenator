import argparse
import sys
from .core import generate, list_fonts

def main():
    parser = argparse.ArgumentParser(description="Generate ASCII art from text", prog="asciigen")
    parser.add_argument("text", nargs="?", help="Text to convert to ASCII art")
    parser.add_argument("-f", "--font", default="simple", help="Font to use (default: simple)")
    parser.add_argument("--list-fonts", action="store_true", help="List available fonts")
    args = parser.parse_args()

    if args.list_fonts:
        print("Available fonts:")
        for font in list_fonts():
            print(f"  {font}")
        return

    if not args.text:
        parser.print_help()
        return

    try:
        result = generate(args.text, args.font)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()