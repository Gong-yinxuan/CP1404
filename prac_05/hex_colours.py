HEX_COLOURS = {"Absolute Zero": "#0048ba",
               "Acid Green": "#b0bf1a",
               "AliceBlue": "#f0f8ff",
               "Alizarin crimson": "#e32636",
               "Amaranth": "#e52b50",
               "Amber": "#e74c3c",
               "Amethyst": "#ffbf00",
               "AntiqueWhite": "#9966cc",
               "AntiqueWhite2": "#66c2a5",
               "AntiqueWhite3": "#66c2a5",}

print(HEX_COLOURS)

colour_input = input("Enter the colour name:")
while colour_input != "":
    if colour_input in HEX_COLOURS:
        print(colour_input, "is", HEX_COLOURS[colour_input])
    else:
        print("Invalid short state")
    colour_input = input("Enter short state: ")


