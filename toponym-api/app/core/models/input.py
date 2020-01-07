from pydantic import BaseModel, StrictStr, Schema


class InputWord(BaseModel):
    word: StrictStr = Schema(..., title="Word to create grammatical cases for")
