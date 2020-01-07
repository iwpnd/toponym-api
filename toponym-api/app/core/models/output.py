from pydantic import BaseModel, StrictStr, Schema


class OutputToponym(BaseModel):
    word: StrictStr = Schema(..., title="Input word")
    toponyms: dict = Schema(..., title="Grammatical cases for input word")


class OutputTopodict(BaseModel):
    language: StrictStr = Schema(..., title="Input language")
    topodictionary: dict = Schema(..., title="Topodict recipe for selected language")


class OutputTopodictRecipe(BaseModel):
    language: StrictStr = Schema(..., title="Input language")
    ending: StrictStr = Schema(..., title="Ending for input word")
    recipe: dict = Schema(..., title=f"Recipe for {ending}")
