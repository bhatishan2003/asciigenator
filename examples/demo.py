import asciigenator

# Test simple font
print("=== Simple Font ===")
print(asciigenator.generate("asciigenator", font="simple"))

print("\n=== Block Font ===")
print(asciigenator.generate("asciigenator", font="block"))

print("\n=== Available Fonts ===")
print(asciigenator.list_fonts())
