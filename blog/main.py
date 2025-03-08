from fastapi import FastAPI
from . import models
from . database import engine 
from . routers import blog,users,authentication



app  = FastAPI()

models.Base.metadata.create_all(engine) #if we find any models lets create on the database 

app.include_router(blog.router)
app.include_router(users.router)
app.include_router(authentication.router)


