import functools
import logging
import os

# Путь к файлу логов
log_file = "film_bot.log"

# Создание файла логов
if not os.path.exists(log_file):
    with open(log_file, 'w'): pass

# Настройка логирования
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# Для вывода в консоль
# console_handler = logging.StreamHandler()
# console_handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
# logging.getLogger().addHandler(console_handler)


def log_query(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        query_text = args[0] if args else 'No query'
        logging.info(f"Запрос: {query_text}")  # Логируем запрос
        return func(self, *args, **kwargs)
    return wrapper

def validate_params(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if func.__name__ == "search_by_genre_and_year":
            genre, year = args

            if genre not in self.get_all_genres():
                raise ValueError(f"Жанр '{genre}' не существует.")
            if not (1990 <= year <= 2025):
                raise ValueError(f"Год '{year}' неверен.")

        return func(self, *args, **kwargs)
    return wrapper

def handle_errors(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
    return wrapper