# app/routers/auth_router.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.auth import create_access_token

router = APIRouter()

# Schema pour login
class LoginRequest(BaseModel):
    username: str
    password: str


# Route LOGIN
@router.post("/login")
def login(data: LoginRequest):

    # simulation d'utilisateur (plus tard DB)
    if data.username != "alice" or data.password != "1234":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }