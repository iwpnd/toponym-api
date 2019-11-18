from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException
from pydantic import BaseModel, StrictStr, Schema
from toponym import toponym, topodict, settings

router = APIRouter()

@router.get("/topodict/{language}", tags=["topodict"])
def topodic(language: StrictStr):
    td = topodict.Topodict(language=language.lower())
    td.load()

    if language.lower() not in settings.LANGUAGE_DICT:
        raise HTTPException(status_code=404, detail="Language not found")

    return td._dict


@router.get("/topodict/{language}/{ending}", tags=["topodict"])
def topodic_ending(language: StrictStr, ending: StrictStr):
    td = topodict.Topodict(language=language.lower())
    td.load()

    if language.lower() not in settings.LANGUAGE_DICT:
        raise HTTPException(status_code=404, detail="Language not found")

    if ending not in td._dict.keys():
        raise HTTPException(status_code=404, detail="Ending not found")

    return {
        "language": language,
        ending: td._dict[ending]
    }

@router.get("/supported_languages", tags=["topodict", "supported languages"])
def topodic_supported_languages():

    return settings.LANGUAGE_DICT