import sqlite3

DB_NAME = "exam_results.db"

def get_db_connection():
    """
    Returns a SQLite3 database connection.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Result ko dictionary jaisa access karne ke liye
    return conn
