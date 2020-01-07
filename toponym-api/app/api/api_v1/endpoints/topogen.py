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


class Input(BaseModel):
    word: StrictStr = Schema(..., title="Word to create grammatical cases for")


class Output(BaseModel):
    word: StrictStr = Schema(..., title="Input word")
    toponyms: dict = Schema(..., title="Grammatical cases for input word")


router = APIRouter()


@router.post("/toponym/russian", response_model=Output, tags=["toponym", "russian"])
def topogen_russian(word: Input):
    td = topodict.Topodict(language="russian")
    td.load()

    tn = toponym.Toponym(word.word, td)
    tn.build()
    toponyms = tn.topo

    return {"word": word.word, "toponyms": toponyms}


@router.post("/toponym/croatian", response_model=Output, tags=["toponym", "croatian"])
def topogen_croatian(word: Input):
    td = topodict.Topodict(language="croatian")
    td.load()

    tn = toponym.Toponym(word.word, td)
    tn.build()
    toponyms = tn.topo

    return {"word": word.word, "toponyms": toponyms}
