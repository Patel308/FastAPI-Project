from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException 
from .. import models 
from .. import schemas
from .. import models,hashing

def get_user(id:int, db:Session):
    user = db.query(models.user).filter(models.user.id ==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with the {id} is not available ")
    
    return user 

def create_user(request:schemas.user, db:Session):
    new_user = models.user(name = request.name, email = request.email,password = hashing.hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user