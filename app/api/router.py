from fastapi import APIRouter
from app.api.routes import fish_routes, measurement_routes, user_routes, tank_routes

api_router= APIRouter()

api_router.include_router(user_routes.router)
api_router.include_router(fish_routes.router)
api_router.include_router(measurement_routes.router)
api_router.include_router(tank_routes.router)