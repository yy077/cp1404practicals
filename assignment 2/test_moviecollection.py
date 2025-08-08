"""Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection.movies)
    assert movie_collection.movies == []

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies("movies.json")
    print(len(movie_collection.movies))
    assert len(movie_collection.movies) > 0

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    assert movie_collection.movies[-1].title == "Amazing Grace"

    # Test counting watched/unwatched
    unwatched = movie_collection.get_number_unwatched()
    watched = movie_collection.get_number_watched()
    print(f"Unwatched: {unwatched}, Watched: {watched}")
    assert unwatched + watched == len(movie_collection.movies)

    # Test sorting movies
    print("Test sorting - year:")
    movie_collection.sort("year")
    years = [movie.year for movie in movie_collection.movies]
    assert years == sorted(years)

    print("Test sorting - title:")
    movie_collection.sort("title")
    titles = [movie.title for movie in movie_collection.movies]
    assert titles == sorted(titles)

    # Test saving movies
    movie_collection.save_movies("test_movies.json")
    print("Movies saved to test_movies.json - check manually")

    print("All MovieCollection tests passed!")


run_tests()