from fastapi import APIRouter
from toponym import settings

router = APIRouter()


@router.get("/languages", tags=["topodict", "supported languages"])
def topodic_supported_languages():

    return settings.LANGUAGE_DICT
