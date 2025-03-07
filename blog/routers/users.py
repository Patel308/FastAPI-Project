from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session 
from .. import schemas,database,models
from typing import List
from .. import models,hashing

gets_db = database.gets_db

router  = APIRouter(
    prefix='/user',
    tags=['users']
)






@router.get("/{id}",response_model=schemas.showuser)
def get_user(id:int,db:Session = Depends(gets_db)):
    user = db.query(models.user).filter(models.user.id ==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with the {id} is not available ")
    
    return user 

@router.post("/",response_model=schemas.showuser)
def create_user(request:schemas.user,db:Session = Depends(gets_db)) :  
    new_user = models.user(name = request.name, email = request.email,password = hashing.hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user