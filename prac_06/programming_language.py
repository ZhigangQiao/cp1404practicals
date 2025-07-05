"""
It is 2024 - 03 - 19 9: 00:00.

Time Estimate: 15 minutes
Time Taken: 12 minutes

"""


class ProgrammingLanguage:
    """Class for representing programming languages."""

    def __init__(self, name, typing, reflection, year):
        """Initialize ProgrammingLanguage object with provided attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of the ProgrammingLanguage object."""
        reflection_str = "Reflection=True" if self.reflection else "Reflection=False"
        return f"{self.name}, {self.typing} Typing, {reflection_str}, First appeared in {self.year}"
