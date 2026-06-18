from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: int


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