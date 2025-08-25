import asciigen

# Test simple font
print("=== Simple Font ===")
print(asciigen.generate("ASCIIGEN", font="simple"))

print("\n=== Block Font ===")
print(asciigen.generate("ASCIIGEN", font="block"))

print("\n=== Available Fonts ===")
print(asciigen.list_fonts())
