"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

result = None  # Initialize result variable
is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # If the user enters a valid integer, set is_finished to True to exit the loop
        is_finished = True
    except ValueError:  # Catch the ValueError exception
        print("Please enter a valid integer.")

if result is not None:
    print("Valid result is:", result)
