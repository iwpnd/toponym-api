from fastapi import APIRouter, Body, Depends, Path, Query
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse
from starlette.status import (
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)
from pydantic import BaseModel, StrictStr, Schema
from toponym import toponym, topodict
from app.core.models.output import Outputtoponym
from app.core.models.input import Inputword


router = APIRouter()


@router.post(
    "/toponym/russian", response_model=Outputtoponym, tags=["toponym", "russian"]
)
def topogen_russian(word: Inputword):
    td = topodict.Topodict(language="russian")
    td.load()

    tn = toponym.Toponym(word.word, td)
    tn.build()
    toponyms = tn.topo

    return {"word": word.word, "toponyms": toponyms}


@router.post(
    "/toponym/croatian", response_model=Outputtoponym, tags=["toponym", "croatian"]
)
def topogen_croatian(word: Inputword):
    td = topodict.Topodict(language="croatian")
    td.load()

    tn = toponym.Toponym(word.word, td)
    tn.build()
    toponyms = tn.topo

    return {"word": word.word, "toponyms": toponyms}
