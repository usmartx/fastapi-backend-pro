# app/populate_db.py
from faker import Faker
import sqlite3
from app.database.database import DB_FILE

fake = Faker()

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Générer 100 utilisateurs fictifs
for _ in range(100):
    name = fake.name()
    age = fake.random_int(min=18, max=70)
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

conn.commit()
conn.close()
print("Database populated with 100 fake users ✅")