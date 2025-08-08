"""MovieCollection class to manage a collection of movies."""

import json
from operator import attrgetter
from movie import Movie


class MovieCollection:
    """Represent a collection of Movie objects."""

    def __init__(self):
        """Initialize an empty movie collection."""
        self.movies = []

    def add_movie(self, movie):
        """Add a Movie object to the collection."""
        self.movies.append(movie)

    def get_number_unwatched(self):
        """Return the number of unwatched movies."""
        return sum(1 for movie in self.movies if not movie.is_watched)

    def get_number_watched(self):
        """Return the number of watched movies."""
        return sum(1 for movie in self.movies if movie.is_watched)

    def load_movies(self, filename):
        """Load movies from a JSON file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.movies = [Movie(**movie_data) for movie_data in data]
        except FileNotFoundError:
            self.movies = []

    def save_movies(self, filename):
        """Save movies to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([movie.__dict__ for movie in self.movies], file, indent=2)

    def sort(self, key):
        """Sort movies by the given key, then by title."""
        self.movies.sort(key=attrgetter(key, 'title'))