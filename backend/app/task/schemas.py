from pydantic import BaseModel
from datetime import datetime


class TaskRead(BaseModel):
    id: int
    head: str
    body: str
    created_at: datetime

    class Config:
        orm_mode = True

class TaskCreate(BaseModel):
    head: str
    body: str

    class Config:
        orm_mode = True
