from pydantic import BaseModel
from typing import List ,Optional

class blogbase(BaseModel):
    title: str
    body: str
    #user_id :int |None=None 
    
class blog(blogbase):
    class Config:
        orm_mode = True    
    

class user(BaseModel):
    name:str
    email:str
    password:str

class showuser(BaseModel):
    name:str
    email:str 
    blogs: List[blog] =[]
    class config():
        orm_mode = True  

class showblog(BaseModel):
    title:str
    body:str
    creater: showuser
    class config():
        orm_mode = True


class Login(BaseModel):
    username :str
    password : str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email: Optional[str] = None        