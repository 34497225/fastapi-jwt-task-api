from pydantic import BaseModel,Field

class Task(BaseModel):
    title: str
    done: bool

class TaskOut(Task):
    id: int
    class Config:
        orm_mode = True 
        
class UserCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1, max_length=72)

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True