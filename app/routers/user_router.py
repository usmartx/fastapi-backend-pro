# app/routers/user_router.py
from fastapi import APIRouter, HTTPException, Query, Depends
from app.crud.crud import get_users, get_user, create_user
from app.schemas.schemas import UserCreate
from app.core.dependencies import get_current_user

router = APIRouter()

# Route publique pour récupérer tous les utilisateurs avec pagination
@router.get("/users")
def read_users(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=100)):
    """
    Retourne les utilisateurs avec pagination
    - page: numéro de page (par défaut 1)
    - limit: nombre d'utilisateurs par page (par défaut 10, max 100)
    """
    return get_users(page, limit)

# Route publique pour récupérer un utilisateur par ID
@router.get("/users/{user_id}")
def read_user(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Route publique pour ajouter un utilisateur
@router.post("/users")
def add_user(user: UserCreate):
    return create_user(user)

# Route sécurisée pour tester le JWT
@router.get("/secure-users")
def read_secure_users(current_user: dict = Depends(get_current_user)):
    """
    Route sécurisée protégée par JWT.
    Renvoie un message personnalisé à l'utilisateur connecté.
    """
    username = current_user.get("sub", "Utilisateur")
    return {"message": f"Bonjour {username}, ceci est votre donnée sécurisée !"}