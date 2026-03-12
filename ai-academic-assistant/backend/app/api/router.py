from fastapi import APIRouter
from app.api.v1 import auth_routes, chat_routes, upload_routes, health_routes

api_router = APIRouter()

api_router.include_router(
    auth_routes.router,
    prefix="/auth",
    tags=["Authentication"]
)

api_router.include_router(
    chat_routes.router,
    prefix="/chat",
    tags=["Chat"]
)

api_router.include_router(
    upload_routes.router,
    prefix="/upload",
    tags=["Upload"]
)

api_router.include_router(
    health_routes.router,
    prefix="/health",
    tags=["Health"]
)