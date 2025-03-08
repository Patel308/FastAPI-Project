from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session 
from .. import schemas,database,models
from typing import List
from .. import models,hashing
from .. repositery import users 


gets_db = database.gets_db

router  = APIRouter(
    prefix='/user',
    tags=['users']
)


@router.get("/{id}",response_model=schemas.showuser)
def get_user(id:int,db:Session = Depends(gets_db)):
   return users.get_user(id, db)


@router.post("/",response_model=schemas.showuser)
def create_user(request:schemas.user,db:Session = Depends(gets_db)) : 
   return users.create_user(request, db) 
  