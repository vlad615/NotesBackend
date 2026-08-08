from fastapi import APIRouter
from .todolists import todolists_router
from .tasks import tasks_router

router = APIRouter(prefix="/v1")
router.include_router(todolists_router)
router.include_router(tasks_router)
