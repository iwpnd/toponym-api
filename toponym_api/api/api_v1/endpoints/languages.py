from fastapi import APIRouter
from toponym import settings

router = APIRouter()


@router.get("/languages", tags=["supported languages"])
def topodic_supported_languages():
    """
    Show supported languages.

    This will show the user which languages are currently supported.

    And this path operation will:
    * return a dictionary of supported languages along with their ISO2 language codes

    """
    return settings.LANGUAGE_DICT
