from fastapi import FastAPI
from app.database.database import init_db, populate_users
from app.routers import user_router

app = FastAPI(title="Backend Pro API")

init_db()
populate_users(1000)

app.include_router(user_router.router)