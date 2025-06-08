"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False


    for char in password:
        if char.islower():
            has_lowercase = True
        elif char.isupper():
            has_uppercase = True
        elif char.isdigit():
            has_digit = True
        elif SPECIAL_CHARS_REQUIRED and char in SPECIAL_CHARACTERS:
            has_special = True


    if not has_lowercase or not has_uppercase or not has_digit:
        return False
    if SPECIAL_CHARS_REQUIRED and not has_special:
        return False

    return True
