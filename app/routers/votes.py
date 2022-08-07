from app import schemas
from app.database import get_db
from fastapi import FastAPI,status,HTTPException,Response,Depends,APIRouter
from sqlalchemy.orm import Session
from . import oauth
from .. import models

router = APIRouter(
    prefix="/votes",
    tags=['Votes']
)

@router.post('/',status_code=201)
def add_vote(vote: schemas.Vote,db:Session = Depends(get_db),current_user:int = Depends(oauth.get_current_user)):
    vote_query = db.query(models.Votes).filter(models.Votes.post_id==vote.post_id,models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()
    if (vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=409,detail=f"User had already voted on post with id is {current_user.id}")
        new_vote = models.Votes(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Vote successfully"}
    else:
        if not found_vote:
            raise HTTPException(status_code = 404,detail=f"Vote doesn't exists")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message":"Vote deleted Successfully"}
        
    