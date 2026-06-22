from pydantic import BaseModel

class EntryCreate(BaseModel):
    text: str


class EntryResponse(BaseModel):
    id: int
    text: str
    sentiment: str
    score: float

    class Config:
        from_attributes = True