from pydantic import BaseModel, StrictStr, Schema


class InputWord(BaseModel):
    word: StrictStr = Schema(..., title="input word to create grammatical cases for")
    language: StrictStr = Schema(..., title="language of the input word")
