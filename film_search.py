from decorators import validate_params, handle_errors
from database import Database

class FilmSearch:
    def __init__(self, db_config):
        self.db = Database(db_config)

    @handle_errors  # Добавлен декоратор для обработки ошибок
    def search_by_title(self, title):
        query = "SELECT title FROM film WHERE title LIKE %s"
        return self.db.fetch_all(query, (f"%{title}%",))

    @handle_errors  # Добавлен декоратор для обработки ошибок
    @validate_params  # Добавлен декоратор для проверки параметров
    def search_by_genre_and_year(self, genre, year):
        query = """
        SELECT title FROM film
        JOIN film_category fc ON film.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE c.name = %s AND film.release_year = %s
        """
        return self.db.fetch_all(query, (genre, year))

    @handle_errors  # Добавлен декоратор для обработки ошибок
    def get_all_genres(self):
        query = "SELECT DISTINCT name FROM category"
        return [row["name"] for row in self.db.fetch_all(query)]

    @handle_errors  # Добавлен декоратор для обработки ошибок
    def get_all_years(self):
        query = "SELECT DISTINCT release_year FROM film ORDER BY release_year DESC"
        return [row["release_year"] for row in self.db.fetch_all(query)]