from typing import List, Optional
from fastapi import FastAPI,status,HTTPException,Response,Depends,APIRouter
from sqlalchemy.orm import Session
from .. database import get_db
from sqlalchemy import func
from .. import  schemas
from .. import models
from  . import oauth

router = APIRouter(
    prefix="/post",
    tags=['Posts']
)

@router.get('/',response_model=List[schemas.PostResponse])
# @router.get("/", response_model=List[schemas.PostOut])
def get_post(db:Session = Depends(get_db),limit:int=3,skip=0,search:Optional[str]=""):
    read_user = db.query(models.Posts).filter(models.Posts.title.contains(search)).limit(limit).offset(skip).all()
    return read_user
    # posts = db.query(models.Posts, func.count(models.Votes.post_id).label("votes")).join(
    #     models.Votes, models.Votes.post_id == models.Posts.id, isouter=True).group_by(models.Posts.id).filter(models.Posts.title.contains(search)).limit(limit).offset(skip).all()
    # return posts

@router.get('/{id}',response_model=schemas.PostResponse)
def get_specific_post(id:int,db:Session = Depends(get_db)):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with {id} was not found")
    return post


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate,db:Session = Depends(get_db),current_user:int = Depends(oauth.get_current_user)):
    new_post = models.Posts(owner_id=current_user.id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

    
@router.delete('/{id}',response_model=schemas.PostResponse)
def delete_post(id:int,db:Session = Depends(get_db),current_user:int = Depends(oauth.get_current_user)):
    post_query = db.query(models.Posts).filter(models.Posts.id == id)
    post = post_query.first()
    
    if post == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Posts with {id} doesn't exists")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403,detail="User doesn't have valid credentials")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}',response_model=schemas.PostResponse)  
def update_post(id:int,updated_post:schemas.PostCreate,db:Session = Depends(get_db),current_user:int = Depends(oauth.get_current_user)):
    post_query= db.query(models.Posts).filter(models.Posts.id==id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Posts with {id} doesn't exists")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403,detail="User doesn't have valid credentials")
    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()