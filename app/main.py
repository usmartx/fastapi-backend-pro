# app/main.py

from fastapi import FastAPI
from app.routers import user_router
from app.routers import auth_router

app = FastAPI()

app.include_router(user_router.router, tags=["Users"])
app.include_router(auth_router.router, tags=["Authentication"])