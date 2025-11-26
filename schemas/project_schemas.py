from pydantic import BaseModel
from typing import Optional

class ProjectCreate(BaseModel):
    name:str
    description:Optional[str] = None

class ProjectUpdate(BaseModel):
    name:Optional[str] = None
    description:Optional[str] =  None

class ProjectOut(BaseModel):
    id:int
    name:str
    description:Optional[str]
    owner_id:int

    class Config:
        orm_mode = True