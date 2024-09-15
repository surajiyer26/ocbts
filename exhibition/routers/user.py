from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, database
from ..hashing import Hash
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['users']
)


get_db = database.get_db


@router.post('/')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)