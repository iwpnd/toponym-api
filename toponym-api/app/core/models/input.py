from pydantic import BaseModel, StrictStr, Schema


class Inputword(BaseModel):
    word: StrictStr = Schema(..., title="Word to create grammatical cases for")
