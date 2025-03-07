from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {"data":{"name":"deepesh"}}


@app.get('/about/{n}')
def about(n):
    return {'data':n}

@app.get('/blog')
def index(limit =10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return { 'data': f'{limit} blogs from the db'}


@app.get('/blog/{id}')
def message(id:int):
    return {'message':id}


@app.get('/blog/{id}/comments')
def comments(id):
    return { 'data':{'1','2'}}

#request body 
class blog(BaseModel):
    title:str
    body:str
    published: Optional[bool]



@app.post("/blog")
def create_blog(blog:blog):
    return { 'data': f"Blog is Created with title as {blog.title}"}

'''if __name__ =="__main__":
    uvicorn.run(app,host="127.0.0.1", port=9000)'''
