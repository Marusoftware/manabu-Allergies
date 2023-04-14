from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name:str
    fullname:str
    email:EmailStr
    password:str

class UserUpdate(BaseModel):
    name:str=None
    fullname:str=None
    email:EmailStr=None
    oldPassword:str=None
    newPassword:str=None