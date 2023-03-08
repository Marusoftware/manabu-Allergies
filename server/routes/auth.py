from typing import List
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import APIRouter, Depends, HTTPException, Request

from ..models.response.user import User, Token
from ..models.request.auth import UserCreate
from ..models.db.user import User as UserDB
from ..models.db.auth import Token as TokenDB, TokenType
import secrets
from datetime import datetime, timedelta
from passlib.context import CryptContext

from tortoise.expressions import Q

router=APIRouter(tags=["Auth"])
oauth=OAuth2PasswordBearer(tokenUrl="/api/v1/auth/signin")
crypt=CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signin", response_model=Token)
async def signin(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    user=await UserDB.get_or_none(Q(name=form_data.username) | Q(email=form_data.username))
    if user is None:
        raise HTTPException(status_code=400, detail="Password or Username is wrong.")
    if user.password is not None:
        if not crypt.verify(form_data.password,user.password):
            raise HTTPException(status_code=400, detail="Password or Username is wrong.")
        #if user.otp_key is not None:
        #    token=await TokenDB.create(token=secrets.token_hex(32), token_type=TokenType.pre, user=user, expired_in=datetime.now()+timedelta(=2))
        #    return Token(access_token=token.token, token_type=token.token_type, user_id=user.id, expired_in=token.expired_in)
        #else:
        token=await TokenDB.create(token=secrets.token_hex(32), token_type=TokenType.bearer, user=user, expired_in=datetime.now()+timedelta(hours=2))
        if "users" not in request.session:
            request.session["users"]=[]
        request.session["users"].append({"name":user.name, "id":str(user.id), "token":token.token, "expired_in":token.expired_in.isoformat()})
        return Token(access_token=token.token, token_type=TokenType.bearer, user_id=user.id, expired_in=token.expired_in)

@router.post("/signup", response_model=User)
async def signup(user:UserCreate):
    if await UserDB.exists(name=user.name) or await UserDB.exists(email=user.email):
        raise HTTPException(status_code=400, detail="Password or Username is wrong.")
    return await UserDB.create(name=user.name, email=user.email, password=crypt.hash(user.password.get_secret_value()))

@router.post("/signout")
async def signout(request:Request, token:str =Depends(oauth)):
    if "users" in request.session:
        request.session["users"]=[user for user in request.session["users"] if user["token"]!=token]
    await TokenDB.filter(token=token).delete()

@router.get("/session", response_model=List[Token])
async def session(request:Request):
    if not "users" in request.session:
        return []
    return [Token(access_token=user["token"], token_type="bearer", user_id=user["id"], expired_in=user["expired_in"]) for user in request.session["users"] if await TokenDB.exists(token=user["token"], token_type=TokenType.bearer)]