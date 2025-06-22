"""
CP1404/CP5632 Practical
State names in a dictionary
"""

# Dictionary containing state abbreviations and names
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

# Printing all states and names
for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

# Asking for user input
state_code = input("Enter short state: ").upper()  # Convert input to uppercase for case-insensitive matching
while state_code:
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()  # Convert input to uppercase for case-insensitive matching
