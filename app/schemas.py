from pydantic import BaseModel

class Task(BaseModel):
    title: str
    done: bool

class TaskOut(Task):
    id: int
    class Config:
        orm_mode = True 
        
class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True