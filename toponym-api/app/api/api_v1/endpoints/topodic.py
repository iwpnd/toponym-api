from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException
from pydantic import BaseModel, StrictStr, Schema
from toponym import toponym, topodict, settings
from app.core.models.output import (
    OutputTopodict,
    OutputTopodictRecipe,
    OutputTopodictLongestEnding,
)
from app.core.models.input import InputWord

router = APIRouter()


@router.get("/topodict/{language}", response_model=OutputTopodict, tags=["topodict"])
def topodic_language(language: StrictStr):
    try:
        td = topodict.Topodict(language=language.lower())
        td.load()

        topodic = td._dict

        return {"language": language, "topodictionary": topodic}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Language: {language} not found.")


@router.get(
    "/topodict/{language}/{ending}",
    response_model=OutputTopodictRecipe,
    tags=["topodict", "recipe", "ending"],
)
def topodic_ending(language: StrictStr, ending: StrictStr):
    td = topodict.Topodict(language=language.lower())
    td.load()

    if language.lower() not in settings.LANGUAGE_DICT:
        raise HTTPException(status_code=404, detail="Language not found")

    if ending not in td._dict.keys():
        raise HTTPException(status_code=404, detail="Ending not found")

    return {"language": language, "ending": ending, "recipe": td._dict[ending]}


@router.post(
    "/topodict/{language}/recipe",
    response_model=OutputTopodictLongestEnding,
    tags=["topodictionary", "recipe", "longest ending"],
)
def topodict_recipe_for_input(word: InputWord, language: StrictStr):
    try:
        td = topodict.Topodict(language=language.lower())
        td.load()

        tn = toponym.Toponym(word.word, td)

        return {
            "language": language,
            "word": word.word,
            "longest_ending": tn._get_longest_word_ending(word.word),
            "recipe": td._dict[tn._get_longest_word_ending(word.word)],
        }

    except KeyError:
        raise HTTPException(status_code=404, detail="Language not found")
