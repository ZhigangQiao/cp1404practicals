"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?
# A ValueError will occur if the input for either numerator or denominator cannot be converted to an integer.
# When will a ZeroDivisionError occur?
# A ZeroDivisionError will occur if the user enters 0 as the denominator.
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes, we can avoid the possibility of a ZeroDivisionError by adding a conditional statement to check if the
# denominator is zero before performing the division.

# Here's the updated code to avoid the possibility of a ZeroDivisionError:
try:
    numerator = int(input("Enter the numerator: "))
    while True:
        try:
            denominator = int(input("Enter the denominator: "))
            if denominator == 0:
                print("Cannot divide by zero! Please try again.")
            else:
                break
        except ValueError:
            print("Denominator must be a valid number! Please try again.")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator must be a valid number!")
print("Finished.")
