from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException
from pydantic import BaseModel, StrictStr, Schema
from toponym import toponym, topodict, settings
from toponym_api.core.models.output import (
    OutputTopodict,
    OutputTopodictRecipe,
    OutputTopodictLongestEnding,
)
from toponym_api.core.models.input import InputWord

router = APIRouter()


@router.get(
    "/topodict/{language}", response_model=OutputTopodict, tags=["topodictionary"]
)
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
    tags=["topodictionary"],
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
    "/topodict/recipe",
    response_model=OutputTopodictLongestEnding,
    tags=["topodictionary"],
)
def topodict_recipe_for_input(inputword: InputWord):
    try:
        td = topodict.Topodict(language=inputword.language.lower())
        td.load()

        tn = toponym.Toponym(inputword.word, td)

        return {
            "language": inputword.language,
            "word": inputword.word,
            "longest_ending": tn._get_longest_word_ending(inputword.word),
            "recipe": td._dict[tn._get_longest_word_ending(inputword.word)],
        }

    except KeyError:
        raise HTTPException(status_code=404, detail="Language not found")
