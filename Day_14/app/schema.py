from pydantic import BaseModel, EmailStr


# User Schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }


# Task Schemas
class TaskCreate(BaseModel):
    title: str
    description: str


class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    completed: bool
    user_id: int

    model_config = {
        "from_attributes": True
    }