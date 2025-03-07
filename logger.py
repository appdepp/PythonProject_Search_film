from database import Database
from decorators import log_query, handle_errors

class Logger:
    def __init__(self, db_config):
        self.db = Database(db_config)

    @log_query
    def log_query(self, query_text):
        query = """
        INSERT INTO alex_search_logs (query_text, count_query) 
        VALUES (%s, 1)
        ON DUPLICATE KEY UPDATE count_query = count_query + 1
        """
        self.db.execute_query(query, (query_text,))

    @handle_errors
    def get_top_queries(self):
        query = """
        SELECT query_text, count_query 
        FROM alex_search_logs 
        ORDER BY count_query DESC 
        LIMIT 10
        """
        return self.db.fetch_all(query)