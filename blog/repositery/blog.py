from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException 
from .. import models 
from .. import schemas

def get_all(db:Session): 
   blogs = db.query(models.blog).all()
   return blogs


def create(request:schemas.blog, db:Session):
    new_blog = models.blog(title = request.title, body=request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog  


def destroy(id : int, db:Session):
    db.query(models.blog).filter(models.blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"

def update(id:int, request:schemas.blog,db:Session):
    blog = db.query(models.blog).filter(models.blog.id == id).update(request.model_dump())

    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,details= f"blod with {id } not found ")
    
    blog.update(request)
    db.commit()
    return 'updated'

def show(id:int, db:Session):
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"blog with the {id} is not aavailable")
    
    return blog    