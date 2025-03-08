from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session 
from .. import schemas,database,models
from typing import List
from .. repositery import blog 

gets_db = database.gets_db

router  = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.get("/",response_model=List[schemas.showblog])
def all(db:Session= Depends(gets_db)):
   return blog.get_all(db) 


@router.post('/',status_code = status.HTTP_201_CREATED)
def create(request:schemas.blog,db:Session = Depends(gets_db)):
    return blog.create(request,db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session= Depends(gets_db)):
     return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.blog,db:Session = Depends(gets_db)):
    return blog.update(id, request,db)



@router.get('/{id}',status_code=200,response_model= schemas.showblog,tags=['blogs'])
def show(id:int,  db:Session= Depends(gets_db)) :
  return blog.show(id, db)      
