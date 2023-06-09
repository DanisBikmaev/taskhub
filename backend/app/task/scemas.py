from pydantic import BaseModel

class TaskBase(BaseModel):
    head: str
    body: str

class TaskCreate(TaskBase):
    pass 

class TaskRead(TaskBase):
    id: int
    created_at: str
    
    class Config:
        orm_mode = True