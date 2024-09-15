from fastapi import HTTPException, status
from ..hashing import Hash
from .. import models, schemas
from sqlalchemy.orm import Session


def create(request: schemas.User, db: Session):
    hashed_password = Hash.bcrypt(request.user_password)
    new_user = models.User(user_name=request.user_name, user_email=request.user_email, user_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    if not new_user:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail='not able to create user')

    return new_user


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with id {id} is not available')
    
    return user