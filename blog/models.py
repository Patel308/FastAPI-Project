from sqlalchemy import Column, Integer,String
from . database import Base 
from . database import engine 

class blog(Base):

    __tablename__  = 'blogs'
    
    id = Column(Integer,primary_key = True, index=True)
    title = Column(String)
    body = Column(String)


class user(Base):
    __tablename__ = "users"

    id =  id = Column(Integer,primary_key = True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

