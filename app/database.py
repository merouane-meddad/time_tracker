import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()

DB_PATH=os.getenv("DB_PATH")

def create_database():
    connection = sqlite3.connect(DB_PATH)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            window_title TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            duration_seconds INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    print("database created successfully")

def save_session(window_title,start_time,end_time,duration_seconds):
    connection = sqlite3.connect(DB_PATH)

    connection.execute(
        """
        INSERT INTO sessions (
            window_title,
            start_time,
            end_time,
            duration_seconds
        )
        VALUES (?,?,?,?)

        """,
        (
            window_title,
            start_time,
            end_time,
            duration_seconds
        )
    )

    connection.commit()
    connection.close()
    print(
    f"Saved: {window_title} "
    f"({duration_seconds}s)"
    )