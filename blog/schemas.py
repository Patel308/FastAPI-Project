from pydantic import BaseModel

class blog(BaseModel):
    title: str
    body: str
    
class showblog(BaseModel):
    title:str
    body:str
    class config():
        orm_mode = True

class user(BaseModel):
    name:str
    email:str
    password:str