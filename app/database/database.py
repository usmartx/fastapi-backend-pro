import sqlite3
from faker import Faker

DB_FILE = "users.db"

def init_db():
    """Créer la table users si elle n'existe pas"""
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


def check_if_users_empty() -> bool:
    """Retourne True si la table users est vide, sinon False"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    conn.close()
    return count == 0


def populate_users(n: int):
    """Peuple la table users avec n utilisateurs fictifs"""
    fake = Faker()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    for _ in range(n):
        cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (fake.name(), fake.random_int(min=18, max=65))
        )
    conn.commit()
    conn.close()