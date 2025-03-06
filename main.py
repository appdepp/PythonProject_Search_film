from config import FILM_DB_CONFIG, LOG_DB_CONFIG
from film_search import FilmSearch
from logger import Logger

def main():
    film_search = FilmSearch(FILM_DB_CONFIG)
    logger = Logger(LOG_DB_CONFIG)

    while True:
        print("\nВыберите вариант поиска:")
        print("1. Поиск по названию фильма.")
        print("2. Поиск по жанру и году выпуска.")
        print("3. Показать ТОП-10 запросов.")
        print("4. Выход из программы.")

        choice = input("\nВведите номер варианта (1-4): ")

        if choice == "1":
            title = input("Введите ключевое слово: ")
            results = film_search.search_by_title(title)
            if results:
                print("\nРезультаты поиска:")
                for row in results:
                    print(row['title'])
            else:
                print("\nНичего не найдено.")
            logger.log_query(f"Поиск по названию: {title}")

        elif choice == "2":
            genres = film_search.get_all_genres()
            years = film_search.get_all_years()

            print("\nДоступные жанры:", ", ".join(genres))
            genre = input("\nВведите жанр: ").strip().title()

            print("\nДоступные года:", ", ".join(map(str, years)))
            while True:
                year = input("\nВведите год выпуска: ")
                if year.isdigit():
                    year = int(year)
                    if 1990 <= year <= 2025:
                        break
                print("Ошибка: введите корректный год от 1990 до 2025!")

            if genre not in genres:
                print("Ошибка: указанного жанра нет в базе!")
                continue
            results = film_search.search_by_genre_and_year(genre, year)
            if results:
                print("\nРезультаты поиска:")
                for row in results:
                    print(row['title'])
            else:
                print("\nНичего не найдено.")
            logger.log_query(f"Поиск по жанру: {genre}, год: {year}")

        elif choice == "3":
            top_queries = logger.get_top_queries()
            print("\nТОП-10 запросов:")
            for query in top_queries:
                print(f"{query['query_text']} — {query['count_query']} раз(а)")

        elif choice == "4":
            print("Выход из программы.")
            break


if __name__ == "__main__":
    main()