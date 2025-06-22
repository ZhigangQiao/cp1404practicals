"""
Hexadecimal Colour Codes
Estimate: 30 minutes
Actual: 40 minutes
"""

# Define a dictionary of colour names and their corresponding hexadecimal codes
COLORS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


def lookup_color():
    """
    Allows the user to look up hexadecimal color codes.
    """
    while True:
        color_name = input("Enter a color name (blank to stop): ").strip().capitalize()
        if color_name == "":
            break
        color_code = COLORS.get(color_name)
        if color_code:
            print(f"The hexadecimal code for {color_name} is {color_code}.")
        else:
            print("Invalid color name. Please try again.")


if __name__ == "__main__":
    lookup_color()
