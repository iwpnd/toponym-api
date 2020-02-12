from fastapi import APIRouter

from .endpoints.languages import router as languages_router
from .endpoints.recipes import router as recipes_router
from .endpoints.topogen import router as topogen_router

router = APIRouter()
router.include_router(topogen_router)
router.include_router(recipes_router)
router.include_router(languages_router)
