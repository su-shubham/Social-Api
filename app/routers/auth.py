from fastapi import FastAPI,status,HTTPException,Response,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. database import get_db
from ..utils import hash_password,verify_password
from .. import  schemas
from .. import models
from . import oauth

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login',response_model=schemas.Token)
# def login_user(user_auth :schemas.loginUser,db:Session = Depends(get_db)):
def login_user(user_auth :OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user_info = db.query(models.User).filter(models.User.email==user_auth.username).first()
    
    if not user_info:
        raise HTTPException(status_code=403,detail='Invalid Credentails')
    
    if not  verify_password(user_auth.password,user_info.password):
        raise HTTPException(status_code=403,detail='Invalid Credentails')
    
    access_token = oauth.create_access_token(data={"user_id":user_info.id})
    return {"token":access_token,"token_type":"bearer"}
    