from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session 
from .. import schemas,database,models
from typing import List

gets_db = database.gets_db

router  = APIRouter(
    prefix='/blog',
    tags=['blogs']
)

@router.get("/",response_model=List[schemas.showblog])
def all(db:Session= Depends(gets_db)):
    blogs = db.query(models.blog).all()
    return blogs 


@router.post('/',status_code = status.HTTP_201_CREATED)
def create(request:schemas.blog,db:Session = Depends(gets_db)):
    new_blog = models.blog(title = request.title, body=request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog  


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session= Depends(gets_db)):
     db.query(models.blog).filter(models.blog.id == id).delete(synchronize_session=False)
     db.commit()
     return "done"


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.blog,db:Session = Depends(gets_db)):
    db.query(models.blog).filter(models.blog.id == id).update(request.model_dump())
    db.commit()
    return 'updated'


@router.get('/{id}',status_code=200,response_model= schemas.showblog,tags=['blogs'])
def show(id,  db:Session= Depends(gets_db)) :
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"blog with the {id} is not aavailable")
    
    return blog          
