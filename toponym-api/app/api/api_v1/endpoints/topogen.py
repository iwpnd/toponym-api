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
from app.core.models.output import OutputToponym
from app.core.models.input import InputWord


router = APIRouter()


@router.post("/toponym/", response_model=OutputToponym, tags=["toponym"])
def topogen_language(inputword: InputWord):
    try:
        td = topodict.Topodict(language=inputword.language.lower())
        td.load()
        tn = toponym.Toponym(inputword.word, td)
        tn.build()
        toponyms = tn.topo

        return {"word": inputword.word, "toponyms": toponyms}
    except KeyError as e:
        raise HTTPException(
            status_code=404, detail=f"Language: {inputword.language} not found."
        )
