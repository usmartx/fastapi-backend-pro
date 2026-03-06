from fastapi import FastAPI, HTTPException
from app.crud.crud import get_users, get_user, create_user, update_user, delete_user
from app.schemas.schemas import UserCreate, UserUpdate
from app.database.database import init_db, populate_users

app = FastAPI(title="Backend Pro API")

# création table
init_db()

# remplir base avec 1000 users
populate_users(1000)

@app.get("/users")
def read_users():
    return get_users()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users")
def add_user(user: UserCreate):
    return create_user(user)