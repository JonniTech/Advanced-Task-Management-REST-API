from pydantic import BaseModel
from typing import Optional,List

class TaskCreate(BaseModel):
    title:str
    description:Optional[str] = None


class TaskUpdate(BaseModel):
    title:Optional[str] =  None
    description:Optional[str] =  None
    completed:Optional[bool] = None
    assigned_to:Optional[List[int]] = None


class TaskOut(BaseModel):
    id:str
    title:str
    description:Optional[str]
    completed:bool
    project_id:int
    assigned_to:List[str] = [] # list of assigned users

    class Config:
        orm_mode = True
