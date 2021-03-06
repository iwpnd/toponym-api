from pydantic import BaseModel
from pydantic import Schema
from pydantic import StrictStr


class OutputToponym(BaseModel):
    word: StrictStr = Schema(..., title="input word")
    language: StrictStr = Schema(..., title="input language")
    longest_ending: StrictStr = Schema(
        ..., title="longest available ending for input word"
    )
    toponyms: dict = Schema(..., title="grammatical cases for input word")


class OutputRecipes(BaseModel):
    language: StrictStr = Schema(..., title="input language")
    recipes: dict = Schema(..., title="Recipes for selected language")


class OutputRecipe(BaseModel):
    language: StrictStr = Schema(..., title="input language")
    ending: StrictStr = Schema(..., title="ending for input word")
    recipe: dict = Schema(..., title=f"recipe for {ending}")


class OutputRecipeLongestEnding(BaseModel):
    language: StrictStr = Schema(..., title="input language")
    word: StrictStr = Schema(..., title="input word")
    longest_ending: StrictStr = Schema(
        ..., title="longest available ending for input word"
    )
    recipe: dict = Schema(..., title=f"recipe for {longest_ending}")
