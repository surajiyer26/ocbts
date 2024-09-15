from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
from typing import List
from ..repository import exhibition


router = APIRouter(
    prefix='/exhibition',
    tags=['exhibitions']
)


get_db = database.get_db


@router.get('/', status_code=200, response_model=List[schemas.Exhibition])
def show_exhibitions(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return exhibition.get_all(db)


@router.post('/')
def create_exhibition(request: schemas.ShowExhibition, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return exhibition.create(request, db)


@router.delete('/{id}', status_code=200)
def delete_exhibition(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return exhibition.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_exhibition(request: schemas.ShowExhibition, id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    exhibition.update(request, id, db)


@router.get('/{id}', status_code=200, response_model=schemas.Exhibition)
def show_exhibition(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return exhibition.get(id, db)