"""Tests for Movie class."""
from movie import Movie


def run_tests():
    """Test Movie class."""

    # Test empty movie (defaults)
    print("Test empty movie:")
    default_movie = Movie()
    print(default_movie)
    assert default_movie.title == ""
    assert default_movie.category == ""
    assert default_movie.year == 0
    assert default_movie.is_watched is False

    # Test initial-value movie
    initial_movie = Movie("Thor: Ragnarok", 2017, "Comedy", True)
    print(initial_movie)
    assert initial_movie.title == "Thor: Ragnarok"
    assert initial_movie.year == 2017
    assert initial_movie.category == "Comedy"
    assert initial_movie.is_watched is True

    # Test mark_watched and mark_unwatched
    test_movie = Movie("Test", 2020, "Action")
    assert test_movie.is_watched is False
    test_movie.mark_watched()
    assert test_movie.is_watched is True
    test_movie.mark_unwatched()
    assert test_movie.is_watched is False

    print("All Movie tests passed!")


run_tests()