import mysql.connector

class Database:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None

    def get_connection(self):
        """Подключение к базе данных."""
        if self.connection is None or not self.connection.is_connected():
            self.connection = mysql.connector.connect(**self.db_config)
        return self.connection

    def execute_query(self, query, params=None):
        """Выполнение SQL-запроса."""
        connection = self.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        connection.commit()
        cursor.close()

    def fetch_all(self, query, params=None):
        """Получение всех результатов запроса."""
        connection = self.get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        result = cursor.fetchall()
        cursor.close()
        return result