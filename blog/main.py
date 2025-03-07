from fastapi import FastAPI,Depends,status,HTTPException
from . import schemas
from . import models
from . database import engine ,SessionLocal
from sqlalchemy.orm import Session 
from typing import List


app  = FastAPI()

models.Base.metadata.create_all(engine) #if we find any models lets create on the database 


def gets_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


@app.get("/blog",response_model=List[schemas.showblog])
def all(db:Session= Depends(gets_db)):
    blogs = db.query(models.blog).all()
    return   blogs             



@app.post('/blog',status_code =status.HTTP_201_CREATED)
def create(request:schemas.blog,db:Session = Depends(gets_db)):
    new_blog = models.blog(title = request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session= Depends(gets_db)):
     db.query(models.blog).filter(models.blog.id == id).delete(synchronize_session=False)
     db.commit()
     return "done"

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.blog,db:Session = Depends(gets_db)):
    db.query(models.blog).filter(models.blog.id == id).update(request.model_dump())
    db.commit()
    return 'updated'



@app.get('/blog/{id}',status_code=200,response_model= schemas.showblog)
def show(id,  db:Session= Depends(gets_db)) :
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"blog with the {id} is not aavailable")
    
    return blog


@app.post('/user')
def create_user(request:schemas.user,db:Session = Depends(gets_db)):
    new_user = models.user(name = request.name, email = request.email,password = request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user