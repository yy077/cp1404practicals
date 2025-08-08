"""
Name: Yang Ruishen
Date Started: 2025/08/04
Brief Project Description: A Kivy app for managing movies
GitHub URL:https://github.com/yy077/cp1404practicals/tree/main/assignment%202
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.button import Button
from movie import Movie
from moviecollection import MovieCollection


class MoviesApp(App):
    """Main Kivy app for managing movies."""

    status_text = StringProperty()
    current_sort = StringProperty("Title")

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies("movies.json")

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Movies To Watch 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_movies()
        return self.root

    def sort_movies(self, key="title"):
        """Sort movies and update display."""
        self.current_sort = key
        self.movie_collection.sort(key.lower())
        self.create_movie_buttons()

    def create_movie_buttons(self):
        """Create buttons for each movie."""
        movie_box = self.root.ids.movies_box
        movie_box.clear_widgets()

        for movie in self.movie_collection.movies:
            color = (0.2, 0.8, 0.2, 1) if movie.is_watched else (0.8, 0.2, 0.2, 1)
            button = Button(
                text=f"{movie.title} ({movie.year})",
                background_color=color,
                color=(1, 1, 1, 1)
            )
            button.bind(on_release=self.toggle_watched)
            button.movie = movie
            movie_box.add_widget(button)

        self.update_status()

    def toggle_watched(self, instance):
        """Toggle watched status of a movie."""
        movie = instance.movie
        if movie.is_watched:
            movie.mark_unwatched()
            self.status_text = f"You need to watch {movie.title}"
        else:
            movie.mark_watched()
            self.status_text = f"You have watched {movie.title}"
        self.sort_movies(self.current_sort)

    def add_movie(self):
        """Add a new movie from input fields."""
        title = self.root.ids.title_input.text.strip()
        year = self.root.ids.year_input.text.strip()
        category = self.root.ids.category_input.text.strip()

        if not all([title, year, category]):
            self.status_text = "All fields must be completed"
            return

        try:
            year = int(year)
            if year < 0:
                self.status_text = "Please enter a valid number"
                return
        except ValueError:
            self.status_text = "Please enter a valid number"
            return

        valid_categories = ["Action", "Comedy", "Documentary", "Drama", "Fantasy", "Thriller"]
        if category not in valid_categories:
            self.status_text = "Please enter a valid category"
            return

        self.movie_collection.add_movie(Movie(title, year, category))
        self.root.ids.title_input.text = ""
        self.root.ids.year_input.text = ""
        self.root.ids.category_input.text = ""
        self.status_text = f"{title} added"
        self.sort_movies(self.current_sort)

    def clear_fields(self):
        """Clear all input fields."""
        self.root.ids.title_input.text = ""
        self.root.ids.year_input.text = ""
        self.root.ids.category_input.text = ""
        self.status_text = ""

    def update_status(self):
        """Update the status label with movie counts."""
        unwatched = self.movie_collection.get_number_unwatched()
        watched = self.movie_collection.get_number_watched()
        self.root.ids.status_label.text = f"To watch: {unwatched}. Watched: {watched}"

    def on_stop(self):
        """Save movies when app stops."""
        self.movie_collection.save_movies("movies.json")


if __name__ == '__main__':
    MoviesApp().run()
