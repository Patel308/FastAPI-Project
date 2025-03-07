from sqlalchemy import Column, Integer,String,ForeignKey
from . database import Base 
from . database import engine 
from sqlalchemy.orm import relationship 

class blog(Base):

    __tablename__  = 'blogs'
    
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer , ForeignKey('users.id'))
    creater = relationship('user', back_populates= 'blogs')
    



class user(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key = True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('blog', back_populates= 'creater')

