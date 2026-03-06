from app.core.logger import logger
from fastapi import APIRouter, HTTPException, Query
from app.crud.crud import get_users, get_user, create_user, update_user, delete_user
from app.schemas.schemas import UserCreate, UserUpdate

router = APIRouter()

@router.get("/users")
def read_users(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100)):

    logger.info(f"Fetching users page={page} limit={limit}")

    return get_users(page, limit)

@router.get("/users/{user_id}")
def read_user(user_id: int):
    user = get_user(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.post("/users")
def add_user(user: UserCreate):
    return create_user(user)