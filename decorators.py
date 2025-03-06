import functools
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_query(func):
    """Декоратор для логирования запросов."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        query_text = args[0] if args else 'No query'
        logging.info(f"Запрос: {query_text}")  # Логируем запрос
        return func(self, *args, **kwargs)
    return wrapper

def validate_params(func):
    """Декоратор для проверки параметров запроса."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        genre = kwargs.get('genre')
        year = kwargs.get('year')

        if genre and genre not in self.get_all_genres():
            raise ValueError(f"Жанр '{genre}' не существует.")
        if year and (year < 1990 or year > 2025):
            raise ValueError(f"Год '{year}' неверен.")

        return func(self, *args, **kwargs)
    return wrapper

def handle_errors(func):
    """Декоратор для обработки ошибок."""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
    return wrapper