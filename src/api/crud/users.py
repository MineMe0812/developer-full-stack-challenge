from fastapi import HTTPException
from passlib.context import CryptContext

from database.models import User

from sqlalchemy.orm import Session
from database.config import get_db
from fastapi import status, Depends, HTTPException
import utils.helper as helper

async def create_user(payload, db):
    # Check if user already exist
    user_query = db.query(User).filter(
        User.username == payload.username.lower())
    user = user_query.first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Account already exist')
    # Compare password and passwordConfirm
    if payload.password != payload.passwordConfirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Passwords do not match')
    #  Hash the password
    payload.password = helper.hash_password(payload.password)
    del payload.passwordConfirm

    payload.username = payload.username.lower()
    new_user = User(**payload.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {'status': 'success', 'message': 'Verification token successfully sent to your email'}

