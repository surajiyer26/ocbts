from datetime import date, time, timedelta
from typing import List
from pydantic import BaseModel


class Exhibition(BaseModel):
    id: int = None
    exhibition_title: str = None
    exhibition_date: date = None
    exhibition_time: time = None
    exhibition_duration: int = None
    exhibition_capacity: int = None
    users: List['User'] = []


class ShowExhibition(BaseModel):
    exhibition_title: str = None
    exhibition_date: date = None
    exhibition_time: time = None
    exhibition_duration: int = None
    exhibition_capacity: int = None
    class Config():
        orm_mode=True


class User(BaseModel):
    user_name: str = None
    user_email: str = None
    user_password: str = None
    exhibitions: List[Exhibition]


class ShowUser(BaseModel):
    user_name: str = None
    user_email: str = None
    exhibitions: List[Exhibition]
    class Config():
        orm_mode=True


class Login(BaseModel):
    user_name: str = None
    user_password: str = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_name: str | None = None