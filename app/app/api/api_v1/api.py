from fastapi import APIRouter

from app.api.api_v1.shorturl.endpoints import app as shorturl

api_router = APIRouter()

api_router.include_router(shorturl)
