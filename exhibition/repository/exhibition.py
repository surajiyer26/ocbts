from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    exhibitions = db.query(models.Exhibition).all()
    return exhibitions


def create(request: schemas.ShowExhibition, db: Session):
    new_exhibition = models.Exhibition(exhibition_title=request.exhibition_title, exhibition_date=request.exhibition_date, exhibition_time=request.exhibition_time, exhibition_duration=request.exhibition_duration, exhibition_capacity=request.exhibition_capacity)
    db.add(new_exhibition)
    db.commit()
    db.refresh(new_exhibition)
    return f'exhibiton {new_exhibition.exhibition_title} is created with {new_exhibition.exhibition_capacity} capacity'


def delete(id: int, db: Session):
    exhibition = db.query(models.Exhibition).filter(models.Exhibition.id == id)

    if not exhibition.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Exhibition with id {id} is not available')
    
    exhibition.delete(synchronize_session=False)

    db.commit()

    return f'exhibition with id {id} has been deleted'


def update(request: schemas.ShowExhibition, id: int, db: Session):
    exhibition = db.query(models.Exhibition).filter(models.Exhibition.id == id)
    
    if not exhibition.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Exhibition with id {id} is not available')
    
    # Convert Pydantic model to dictionary if necessary

    exhibition_data = request.dict(exclude_unset=True)  # exclude_unset avoids overwriting with None values
    
    exhibition.update(exhibition_data)
    
    db.commit()

    return {"message": f'Exhibition with id {id} has been updated'}


def get(id: int, db: Session):
    exhibition = db.query(models.Exhibition).filter(models.Exhibition.id == id).first()

    # if not exhibition:  
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {'details': f'exhibition with id {id} is not available'}

    if not exhibition:
        raise HTTPException(status_code=404, detail=f'exhibition with id {id} is not available')
    
    return exhibition