"""Movie class to represent a single movie."""

class Movie:
    """Represent a Movie object."""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """Initialize a Movie instance."""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Return string representation of movie."""
        status = "watched" if self.is_watched else "unwatched"
        return f"{self.title} ({self.year}) - {self.category} ({status})"

    def mark_watched(self):
        """Mark the movie as watched."""
        self.is_watched = True

    def mark_unwatched(self):
        """Mark the movie as unwatched."""
        self.is_watched = False