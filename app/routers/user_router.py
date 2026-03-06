from fastapi import APIRouter, HTTPException
from app.crud.crud import get_users, get_user, create_user
from app.schemas.schemas import UserCreate

router = APIRouter()

@router.get("/users")
def read_users():
    return get_users()

@router.get("/users/{user_id}")
def read_user(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users")
def add_user(user: UserCreate):
    return create_user(user)