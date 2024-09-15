from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models, database, token
from ..hashing import Hash
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
 
router = APIRouter(
    tags=['authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.user_email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='invalid credentials')
    
    if not Hash.verify(user.user_password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='incorrect password')

    access_token = token.create_access_token(
        data={"sub": user.user_email}
    )
    return schemas.Token(access_token=access_token, token_type="bearer")