"""
Name: Yang Ruishen
Date started: 2025/06/18
GitHub URL: https://github.com/yy077/cp1404practicals/tree/main/assignment%201
"""

# Constants
WATCHED = 'w'
UNWATCHED = 'u'
MENU = """Menu:
D - Display movies
A - Add new movie
W - Watch a movie
Q - Quit"""

def main():
    """Main function to run the movie list program."""
    print("Must-See Movies 1.0 - by YourName")
    movies = load_movies('movies.csv')
    print(f"{len(movies)} movies loaded from movies.csv")

    while True:
        print(MENU)
        choice = input(">>> ").strip().lower()
        if choice == 'd':
            display_movies(movies)
        elif choice == 'a':
            add_movie(movies)
        elif choice == 'w':
            watch_movie(movies)
        elif choice == 'q':
            save_movies(movies, 'movies.csv')
            print(f"{len(movies)} movies saved to movies.csv")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def load_movies(filename):
    """Load movies from a CSV file and return a list of movies."""
    movies = []
    with open(filename, 'r') as file:
        for line in file:
            title, year, category, status = line.strip().split(',')
            movies.append([title, int(year), category, status])
    return movies


def save_movies(movies, filename):
    """Save movies to a CSV file."""
    with open(filename, 'w') as file:
        for movie in movies:
            file.write(f"{movie[0]},{movie[1]},{movie[2]},{movie[3]}\n")


def display_movies(movies):
    """Display the list of movies, sorted by year and then by title."""
    movies.sort(key=lambda x: (x[1], x[0]))
    watched_count = sum(1 for movie in movies if movie[3] == WATCHED)
    unwatched_count = len(movies) - watched_count

    print("Unwatched movies:")
    for i, movie in enumerate(movies, start=1):
        status_marker = "*" if movie[3] == UNWATCHED else " "
        print(f"{i}. {status_marker} {movie[0]} - {movie[1]} ({movie[2]})")

    print(f"{watched_count} movies watched. {unwatched_count} movies still to watch.")


def add_movie(movies):
    """Add a new movie to the list."""
    title = input("Title: ").strip()
    while not title:
        print("Input can not be blank")
        title = input("Title: ").strip()

    year = input("Year: ").strip()
    while not year.isdigit() or int(year) < 1:
        print("Invalid input; enter a valid number")
        year = input("Year: ").strip()
    year = int(year)

    categories = ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]
    print("Categories available:", ", ".join(categories))
    category = input("Category: ").strip()
    while not category:
        print("Input can not be blank")
        category = input("Category: ").strip()
    category = category if category in categories else "Other"

    movies.append([title, year, category, UNWATCHED])
    print(f"{title} ({category} from {year}) added to movie list")


def watch_movie(movies):
    """Mark a movie as watched."""
    unwatched_movies = [i for i, movie in enumerate(movies) if movie[3] == UNWATCHED]
    if not unwatched_movies:
        print("No more movies to watch!")
        return

    print("Enter the movie number to mark watched.")
    choice = input(">>> ").strip()
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(movies):
        print("Invalid movie number.")
        choice = input(">>> ").strip()
    choice = int(choice) - 1

    if movies[choice][3] == WATCHED:
        print(f"You have already watched {movies[choice][0]}.")
    else:
        movies[choice][3] = WATCHED
        print(f"{movies[choice][0]} ({movies[choice][1]}) watched.")


if __name__ == '__main__':
    main()
