"""
Intermediate Exercises
File: hex_colours.py

This program allows users to look up hexadecimal color codes based on color names.
"""

# Constant dictionary of color names and their corresponding hexadecimal codes
HEX_COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "blanchedalmond": "#ffebcd",
    "blueviolet": "#8a2be2",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0"
}

def main():
    print("Welcome to the Hex Colours Lookup program.")
    print("Enter a color name to get its hexadecimal code, or leave blank to exit.")

    while True:
        color_name = input("Enter a color name (case-insensitive): ").strip().lower()
        if not color_name:
            print("Exiting the program.")
            break

        if color_name in HEX_COLOURS:
            print(f"{color_name.capitalize()}: {HEX_COLOURS[color_name]}")
        else:
            print("Invalid color name. Please try again.")

if __name__ == "__main__":
    main()