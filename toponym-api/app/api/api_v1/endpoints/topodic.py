from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException
from pydantic import BaseModel, StrictStr, Schema
from toponym import toponym, topodict, settings
from app.core.models.output import Outputtopodict

router = APIRouter()


@router.get("/topodict/{language}", response_model=Outputtopodict, tags=["topodict"])
def topodic_language(language: StrictStr):
    try:
        td = topodict.Topodict(language=language.lower())
        td.load()

        topodic = td._dict

        return {"language": language, "topodictionary": topodic}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Language: {language} not found.")


@router.get("/topodict/{language}/{ending}", tags=["topodict"])
def topodic_ending(language: StrictStr, ending: StrictStr):
    td = topodict.Topodict(language=language.lower())
    td.load()

    if language.lower() not in settings.LANGUAGE_DICT:
        raise HTTPException(status_code=404, detail="Language not found")

    if ending not in td._dict.keys():
        raise HTTPException(status_code=404, detail="Ending not found")

    return {"language": language, ending: td._dict[ending]}
