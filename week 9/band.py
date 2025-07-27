from musician import Musician


class Band:
    """Band class that aggregates(zero or more) Musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string like: 'BandName (Musician1(...), Musician2(...), ...)'"""
        return f"{self.name} ({', '.join(str(m) for m in self.musicians)})"

    def add(self, musician: Musician):
        """Add a Musician to this band."""
        self.musicians.append(musician)

    def play(self):
        """Return multi-line string of each musician playing."""
        lines = [musician.play() for musician in self.musicians]
        return "\n".join(lines)