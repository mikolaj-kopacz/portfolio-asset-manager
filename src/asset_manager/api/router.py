from fastapi import APIRouter
from src.asset_manager.api.v1.endpoints import users
from src.asset_manager.api.v1.endpoints import auth

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users",tags=["users"])

api_router.include_router(auth.router, prefix="",tags=["auth"])