import sqlite3
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_file="daily_work_log.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        # Create a table if it doesn't exist
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS daily_work_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    work_description TEXT
                )
            ''')

    def save_daily_work_log(self, work_description):
        # Function to save daily work log to the database
        current_date = datetime.now().strftime("%Y-%m-%d")
        log_entry = (current_date, work_description)

        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO daily_work_logs (date, work_description) VALUES (?, ?)
            ''', log_entry)

    def fetch_all_logs(self):
        # Retrieve all logs from the database
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT * FROM daily_work_logs
            ''')
            return cursor.fetchall()