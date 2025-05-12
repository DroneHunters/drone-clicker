import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self._init_db()

    def _init_db(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            drones INTEGER DEFAULT 1,
            parts INTEGER DEFAULT 0,
            referrals INTEGER DEFAULT 0
        )
        """)
        self.connection.commit()

    def user_exists(self, user_id):
        self.cursor.execute("SELECT 1 FROM users WHERE user_id = ?", (user_id,))
        return bool(self.cursor.fetchone())

    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
        self.connection.commit()