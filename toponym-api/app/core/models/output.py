from pydantic import BaseModel, StrictStr, Schema


class Outputtoponym(BaseModel):
    word: StrictStr = Schema(..., title="Input word")
    toponyms: dict = Schema(..., title="Grammatical cases for input word")