"""
Name: Yang Ruishen
Date started: 2025/08/04
GitHub URL:
"""

"""Console program for managing movies using classes."""
from movie import Movie
from moviecollection import MovieCollection


def main():
    """Run the console-based movie manager."""
    print("Movies To Watch 2.0 - by <Your Name>")

    movie_collection = MovieCollection()
    movie_collection.load_movies("movies.json")

    print(f"{len(movie_collection.movies)} movies loaded")

    while True:
        print("\nMenu:")
        print("L - List movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")

        choice = input(">>> ").upper()

        if choice == "L":
            list_movies(movie_collection)
        elif choice == "A":
            add_movie(movie_collection)
        elif choice == "W":
            watch_movie(movie_collection)
        elif choice == "Q":
            movie_collection.save_movies("movies.json")
            print(f"{len(movie_collection.movies)} movies saved to movies.json")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def list_movies(movie_collection):
    """Display all movies with their details."""
    if not movie_collection.movies:
        print("No movies in collection")
        return

    unwatched_count = movie_collection.get_number_unwatched()

    for i, movie in enumerate(movie_collection.movies, 1):
        status = "*" if not movie.is_watched else " "
        print(f"{i}. {status} {movie}")

    print(f"\n{unwatched_count} movies to watch")


def add_movie(movie_collection):
    """Add a new movie to the collection."""
    title = input("Title: ").strip()
    while not title:
        print("Input cannot be blank")
        title = input("Title: ").strip()

    while True:
        try:
            year = int(input("Year: "))
            if year < 0:
                print("Number must be >= 0")
                continue
            break
        except ValueError:
            print("Invalid input; enter a valid number")

    category = input("Category: ").strip()
    while not category:
        print("Input cannot be blank")
        category = input("Category: ").strip()

    movie_collection.add_movie(Movie(title, year, category))
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(movie_collection):
    """Mark a movie as watched."""
    unwatched_count = movie_collection.get_number_unwatched()
    if unwatched_count == 0:
        print("No more movies to watch!")
        return

    list_movies(movie_collection)

    while True:
        try:
            choice = int(input("Enter the number of a movie to mark as watched: "))
            if choice < 1 or choice > len(movie_collection.movies):
                print("Invalid movie number")
                continue

            movie = movie_collection.movies[choice - 1]
            if movie.is_watched:
                print(f"You have already watched {movie.title}")
                continue

            movie.mark_watched()
            print(f"{movie.title} from {movie.year} watched")
            break
        except ValueError:
            print("Invalid input; enter a valid number")


if __name__ == '__main__':
    main()