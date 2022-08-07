from sqlalchemy import Boolean, Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.types import TIMESTAMP


class Posts(Base):
    __tablename__="posts"
    id= Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    is_published=Column(Boolean,server_default='True')
    is_created=Column(TIMESTAMP(timezone=True),nullable=False,server_default="now()")
    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")
    
class User(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    is_created=Column(TIMESTAMP(timezone=True),nullable=False,server_default="now()")
    
class Votes(Base):
    __tablename__="votes"
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)