from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

import crud.users as crud
from database.models import User
import schemas.users as schema
from sqlalchemy.orm import Session
from database.config import get_db

import utils.helper as helper

from auth.jwthandler import (
    create_access_token,
    get_current_user,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

router = APIRouter()

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def create_user(payload: schema.CreateUserSchema, db: Session = Depends(get_db)):
    return await crud.create_user(payload, db)



@router.post('/login')
def login(payload: schema.LoginUserSchema, db: Session = Depends(get_db)):
    # Check if the user exist
    user = db.query(User).filter(
        User.username == payload.username.lower()).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Incorrect Username')

    # Check if the password is valid
    if not helper.verify_password(payload.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Incorrect Password')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "You've successfully logged in. Welcome back!"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False,
    )

    return response

