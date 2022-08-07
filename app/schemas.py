from typing import Optional
from app.models import User
from pydantic.types import conint
from pydantic import BaseModel,EmailStr

# <----------------------------------------PYDANTIC MODEL--------------------------------------------------->

# Pydantic Model

# For Request

class PostBase(BaseModel):
    title:str
    content:str
    is_published:bool =True
    
class PostCreate(PostBase):
    pass

class userCreate(BaseModel):
    email: EmailStr
    password:str
    
class loginUser(BaseModel):
    email:EmailStr
    password:str
    
class Token(BaseModel):
    token: str
    token_type: str
    
class tokenData(BaseModel):
    id:Optional[str]=None
    
class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)

# For response
class UserResponse(BaseModel):
    id:int
    email:EmailStr
    class Config:
        orm_mode = True
        
class PostResponse(PostBase):
    id:int
    owner_id:int
    owner:UserResponse
    class Config:
        orm_mode = True
        
# class PostOut(BaseModel):
#     post: PostResponse
#     votes: int

#     class Config:
#         orm_mode = True


