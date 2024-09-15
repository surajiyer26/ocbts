from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Time
from .database import Base
from sqlalchemy.orm import relationship


ticket = Table(
    'ticket',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('exhibition_id', Integer, ForeignKey('exhibitions.id'), primary_key=True)
)


class Exhibition(Base):
    __tablename__ = 'exhibitions'

    id = Column(Integer, primary_key=True, index=True)
    exhibition_title = Column(String)
    exhibition_date = Column(Date)
    exhibition_time = Column(Time)
    exhibition_duration = Column(Integer)
    exhibition_capacity = Column(Integer)

    users = relationship("User", secondary=ticket, back_populates="exhibitions")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True) 
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)

    exhibitions = relationship("Exhibition", secondary=ticket, back_populates="users")