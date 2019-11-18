from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException
from pydantic import BaseModel, StrictStr, Schema
from toponym import toponym, topodict

router = APIRouter()

@router.get("/topodict/{language}", tags=["toponym"])
def topodic(language: StrictStr):
    td = topodict.Topodict(language=language.lower())
    td.load()

    return td._dict


@router.get("/topodict/{language}/{ending}", tags=["toponym"])
def topodic_ending(language: StrictStr, ending: StrictStr):
    td = topodict.Topodict(language=language.lower())
    td.load()

    if ending not in td._dict.keys():
        raise HTTPException(status_code=404, detail="Ending not found")

    return {
        "language": language,
        ending: td._dict[ending]
    }