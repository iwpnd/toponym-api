from fastapi import APIRouter
from starlette.exceptions import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from toponym.recipes import Recipes
from toponym.toponym import get_longest_word_ending
from toponym.toponym import Toponym
from toponym.utils import LanguageNotFoundError

from toponym_api.core.models.input import InputWord
from toponym_api.core.models.output import OutputToponym


router = APIRouter()


@router.post("/toponym/", response_model=OutputToponym)
def topogen_language(inputword: InputWord):
    """
    Create toponyms for input word and language.

    This will create the toponyms for the input word and the input language.

    And this path operation will:
    * return toponyms
    """
    try:
        recipes = Recipes(language=inputword.language.lower())
        recipes.load()
        t = Toponym(input_word=inputword.word, recipes=recipes)
        t.build()
        toponyms = t.toponyms

        return {
            "word": inputword.word,
            "language": inputword.language,
            "longest_ending": get_longest_word_ending(
                input_word=inputword.word, recipes=recipes
            ),
            "toponyms": toponyms,
        }
    except LanguageNotFoundError:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"Language: {inputword.language} not found.",
        )
