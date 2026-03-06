# app/main.py
from fastapi import FastAPI
from app.database.database import init_db, populate_users
from app.routers import user_router  # <-- import du router

app = FastAPI(title="Backend Pro API")

# Création de la table et remplissage
init_db()
populate_users(1000)

# Inclure le router pour toutes les routes /users
app.include_router(user_router.router)

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.get("/")
def root():
    return {"message": "Backend Pro API is running"}