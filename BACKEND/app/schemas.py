from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# format users should adhere to
class UserRegister(BaseModel):
    email: EmailStr
    username: str= Field(..., min_length=3, max_length=20)
    password: str= Field(..., min_length=8)

class UserLogin(BaseModel):
    username: str
    password: str

#format of what we send back
class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    created_at: datetime

class Token(BaseModel):
    access_token: str
    token_type: str= "bearer"

class TokenData(BaseModel):
    username: Optional[str]= None

