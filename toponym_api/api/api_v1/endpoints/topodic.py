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
    """
    Show topodictionary for language.

    This will show the topodictionary for the input language to the user.
    A topodictionary is a collection of recipe on how to construct
    grammatical cases for an input word.

    And this path operation will:
    * return the entire collection of recipes in a topodictionary

    """
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
    """
    Show the recipe for a word-ending.

    Given an input language and an ending, present the user with
    the recipe that will be used to build grammatical cases
    for that specific ending.

    e.g.
        "д": {
        "nominative": [
            [""],0
            ],
        "genitive": [
            ["да","дя"],1
        ],
        "dative": [
            ["дю","ду"],1
        ],
        "accusative": [
            ["да","дя"],
            1
        ],
        "instrumental": [
            ["дем","дом"],1
        ],
        "prepositional": [
            ["де"],1
        ]
    }

    And this path operation will:
    * returns a single recipe for the ending specific in the path

    """
    try:
        td = topodict.Topodict(language=language.lower())
        td.load()

        if ending not in td._dict.keys():
            raise HTTPException(status_code=404, detail="Ending not found")

        return {"language": language, "ending": ending, "recipe": td._dict[ending]}

    except KeyError:
        raise HTTPException(status_code=404, detail=f"Language: {language} not found.")


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
            "recipe": td._dict["_default"]
            if not tn._get_longest_word_ending(inputword.word)
            else td._dict[tn._get_longest_word_ending(inputword.word)],
        }

    except KeyError:
        raise HTTPException(
            status_code=404, detail=f"Language: {inputword.language} not found"
        )
