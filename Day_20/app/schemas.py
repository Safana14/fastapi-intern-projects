from pydantic import BaseModel, Field, EmailStr


class EntryCreate(BaseModel):
    text: str = Field(
        min_length=3,
        max_length=1000
    )


class EntryUpdate(BaseModel):
    text: str = Field(
        min_length=3,
        max_length=1000
    )


class EntryResponse(BaseModel):
    id: int
    text: str
    sentiment: str
    score: float

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str = Field(
        min_length=3,
        max_length=50
    )
    email: EmailStr
    password: str = Field(
        min_length=6
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str