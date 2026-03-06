import sqlite3
from app.schemas.schemas import UserCreate

DB_FILE = "users.db"


def get_connection():
    return sqlite3.connect(DB_FILE)


def create_user(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, age) VALUES (?, ?)",
        (user.name, user.age)
    )

    conn.commit()
    conn.close()

    return {"message": f"Utilisateur {user.name} ajouté avec succès"}


def get_users(page: int = 1, limit: int = 10):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    offset = (page - 1) * limit
    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (limit, offset))
    users = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    conn.close()

    return {
        "page": page,
        "limit": limit,
        "total_users": total_users,
        "data": [{"id": u[0], "name": u[1], "age": u[2]} for u in users]
    }

def get_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, age FROM users WHERE id=?",
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return {
            "id": user[0],
            "name": user[1],
            "age": user[2]
        }

    return None


def update_user(user_id: int, user):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name=?, age=? WHERE id=?",
        (user.name, user.age, user_id)
    )

    conn.commit()
    conn.close()

    return {"message": "Utilisateur modifié avec succès"}


def delete_user(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (user_id,)
    )

    conn.commit()
    conn.close()

    return {"message": "Utilisateur supprimé avec succès"}