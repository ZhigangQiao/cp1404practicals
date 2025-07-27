class Band:
    """Band class"""

    def __init__(self, name):
        """Construct a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({len(self.musicians)} members)"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing."""
        if not self.musicians:
            return "The band needs members!"
        playing_info = []
        for musician in self.musicians:
            playing_info.append(musician.play())
        return "\n".join(playing_info)
