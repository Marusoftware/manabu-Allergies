from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from ..db.auth import TokenType

class Token(BaseModel):
    access_token: str
    token_type: TokenType
    user_id:UUID
    expired_in:datetime

class User(BaseModel):
    id:UUID
    name:str
    email:EmailStr