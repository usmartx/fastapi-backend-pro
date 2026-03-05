import sqlite3
from faker import Faker

DB_FILE = "users.db"
fake = Faker()

# créer la table
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


# remplir la base avec des faux utilisateurs
def populate_users(n=1000):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    if count < n:
        for _ in range(n - count):
            cursor.execute(
                "INSERT INTO users (name, age) VALUES (?, ?)",
                (fake.name(), fake.random_int(min=18, max=70))
            )

    conn.commit()
    conn.close()