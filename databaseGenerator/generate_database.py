import sqlite3


def init_database():
    with sqlite3.connect("password_manager.db") as db:
        cursor = db.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS master(
            id INTEGER PRIMARY KEY,
            password TEXT NOT NULL);
            """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS storage(
            id INTEGER PRIMARY KEY,
            userid TEXT NOT NULL,
            password TEXT NOT NULL);
            """)
    return db, cursor
