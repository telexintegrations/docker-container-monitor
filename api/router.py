from fastapi import APIRouter

from api.routes import integrations

api_router = APIRouter()
api_router.include_router(integrations.router, tags=["integration.json"])
