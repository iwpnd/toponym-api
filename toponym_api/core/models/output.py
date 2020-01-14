from pydantic import BaseModel, StrictStr, Schema


class OutputToponym(BaseModel):
    word: StrictStr = Schema(..., title="input word")
    toponyms: dict = Schema(..., title="grammatical cases for input word")


class OutputTopodict(BaseModel):
    language: StrictStr = Schema(..., title="input language")
    topodictionary: dict = Schema(
        ..., title="topodictionary recipe for selected language"
    )


class OutputTopodictRecipe(BaseModel):
    language: StrictStr = Schema(..., title="input language")
    ending: StrictStr = Schema(..., title="ending for input word")
    recipe: dict = Schema(..., title=f"topodictionary recipe for {ending}")


class OutputTopodictLongestEnding(BaseModel):
    language: StrictStr = Schema(..., title="input language")
    word: StrictStr = Schema(..., title="input word")
    longest_ending: StrictStr = Schema(
        ..., title="longest available ending for input word"
    )
    recipe: dict = Schema(..., title=f"recipe for {longest_ending}")