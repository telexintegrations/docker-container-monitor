from fastapi import APIRouter

from api.routes import integrations, telex

api_router = APIRouter()
api_router.include_router(integrations.router, tags=["integration.json"])
api_router.include_router(telex.router, tags=["telex"])
