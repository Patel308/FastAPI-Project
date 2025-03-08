from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session 
from .. import schemas,database,models,token
from typing import List
from .. import hashing
from ..hashing import hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.gets_db)):
    user = db.query(models.user).filter(models.user.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid authentication ")
    if not hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"incorrect password ")
    
    #access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    access_token = token.create_access_token(data = {'sub':user.email})
    return {"access_token": access_token,"token_type":"bearer"}