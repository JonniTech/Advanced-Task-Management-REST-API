from pydantic import BaseModel,EmailStr

class RegisterSchema(BaseModel):
    username:str
    email:EmailStr
    password:str

class LoginScheme(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    username:str
    email:EmailStr
    role:str

    class Config:
        orm_mode = True

class TokenSchema(BaseModel):
    access_token:str
    refresh_token:str
    token_type:str = "bearer"

    class Config:
        orm_mode = True

    