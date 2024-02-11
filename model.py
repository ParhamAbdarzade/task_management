from pydantic import BaseModel


class TaskModel(BaseModel):
    title: str
    description: str
    completed: bool = False

