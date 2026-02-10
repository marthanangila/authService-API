from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


# Format users should adhere to when registering
class UserRegister(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=8)


# Format for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Format of what we send back after registration
class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: str | None = None

