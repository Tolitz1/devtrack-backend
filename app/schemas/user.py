# """
# Pydantic schemas for user validation.

# Defines request and response structures
# separately from database models.
# """

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    # """
    # Schema for creating a new user.
    # """
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    # """
    # Schema returned to client.
    # """
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"