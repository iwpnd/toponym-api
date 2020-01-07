from fastapi import APIRouter
from starlette.exceptions import HTTPException
from pydantic import BaseModel, StrictStr, Schema
from toponym import toponym, topodict, settings

router = APIRouter()


@router.get("/languages", tags=["topodict", "supported languages"])
def topodic_supported_languages():

    return settings.LANGUAGE_DICT
