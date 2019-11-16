from fastapi import APIRouter

from .endpoints.topogen import router as topogen_router

router = APIRouter()
router.include_router(topogen_router)