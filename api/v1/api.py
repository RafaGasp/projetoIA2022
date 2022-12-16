from fastapi import APIRouter

from api.v1.endpoints import knn

api_router = APIRouter()
api_router.include_router(knn.router, prefix="/knn")
