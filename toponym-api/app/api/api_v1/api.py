from fastapi import APIRouter

from .endpoints.topogen import router as topogen_router
from .endpoints.topodic import router as topodic_router

router = APIRouter()
router.include_router(topogen_router)
router.include_router(topodic_router)
