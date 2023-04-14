from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from .auth import get_user
from ..models.response.user import User
from ..models.request.user import UserUpdate
from ..models.db import User as UserDB
from .auth import crypt

router=APIRouter(tags=["user"])

@router.get("/me", response_model=User)
async def me(user:UserDB=Depends(get_user)):
    return user

@router.get("/{id}", response_model=User)
async def get(id:UUID):
    return await UserDB.get(id=id)

@router.delete("/me")
async def delete_me(user:UserDB=Depends(get_user), password:str=None):
    if user.password is not None and password is None:
        raise HTTPException(status_code=400, detail="Password is wrong")
    if user.password is not None:
        if not crypt.verify(password, user.password):
            raise HTTPException(status_code=400, detail="Password is wrong")
    await user.delete()

@router.patch("/me", response_model=User)
async def update_me(user:UserUpdate, user_db:UserDB=Depends(get_user)):
    update_dict=user.dict()
    if user.oldPassword is not None and user.newPassword is not None:
        if crypt.verify(user.oldPassword, user_db.password):
            update_dict["password"]=crypt.hash(user.newPassword)
    def checkUpdate(item):
        key, value=item
        if key in ["oldPassword", "newPassword"]:
            return False
        elif value is None:
            return False
        else:
            return True
    update_dict=dict(filter(checkUpdate, update_dict.items()))
    user_db.update_from_dict(update_dict)
    await user_db.save()
    return user_db