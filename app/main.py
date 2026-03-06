# app/main.py
from fastapi import FastAPI
from app.routers import user_router

app = FastAPI(title="Backend Pro API")

# Inclure le router
app.include_router(user_router.router)