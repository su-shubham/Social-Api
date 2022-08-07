from fastapi import FastAPI,status,HTTPException,Response,Depends,APIRouter
from sqlalchemy.orm import Session
from .. database import get_db
from ..utils import hash_password
from .. import  schemas
from .. import models

router = APIRouter(
    prefix="/user",
    tags=['User']
)

@router.post('/',response_model=schemas.UserResponse)
def user_create(user:schemas.userCreate,db:Session = Depends(get_db)):
    secure_password=hash_password(user.password)
    user.password= secure_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}',response_model=schemas.UserResponse)
def get_specific_user(id:int,db:Session = Depends(get_db)):
    get_user=db.query(models.User).filter(models.User.id == id).first()
    if not get_user:
        raise HTTPException(status_code=404)
    return get_user

    
    
    