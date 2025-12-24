import sqlite3
from database import get_db_connection

def init_db():
    # Get DB connection
    conn = get_db_connection()
    cursor = conn.cursor()

    # Open schema.sql and execute
    with open("database/schema.sql", "r") as f:
        sql_script = f.read()
    
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()
