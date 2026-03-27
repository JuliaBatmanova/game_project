import sqlite3


class DatabaseManager:

    def __init__(self, db_name="game_scores.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score INTEGER,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        self.connection.execute(query)
        self.connection.commit()

    def add_score(self, name, score):

        query = "INSERT INTO players (name, score) VALUES (?, ?)"
        self.connection.execute(query, (name, score))
        self.connection.commit()

    def get_top_players(self, limit=5):

        query = """
        SELECT name, score
        FROM players
        ORDER BY score DESC
        LIMIT ?
        """

        cursor = self.connection.execute(query, (limit,))
        return cursor.fetchall()

    def close(self):
        self.connection.close()
