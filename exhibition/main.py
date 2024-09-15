from fastapi import FastAPI
from . import models
from .database import engine
from .routers import exhibition, user, authentication


app = FastAPI()


models.Base.metadata.create_all(engine)


app.include_router(exhibition.router)
app.include_router(user.router)
app.include_router(authentication.router)