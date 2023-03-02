from pydantic import BaseModel, EmailStr, SecretStr, Field

class UserCreate(BaseModel):
    name:str=Field(max_length=1024)
    email:EmailStr
    password:SecretStr