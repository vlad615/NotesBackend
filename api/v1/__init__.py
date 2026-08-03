from fastapi import APIRouter
from .todolists import todolists_router

router = APIRouter(prefix="/v1")
router.include_router(todolists_router)
