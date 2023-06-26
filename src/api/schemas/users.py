from datetime import datetime
from pydantic import BaseModel, constr

class UserBaseSchema(BaseModel):
    username: str
    full_name: str
    class Config:
        orm_mode = True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str

class LoginUserSchema(BaseModel):
    username: str
    password: constr(min_length=8)

class UserResponse(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime


