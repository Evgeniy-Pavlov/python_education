import datetime
from .database import db
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING, Type



class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(40), unique=False, nullable=False)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    date_create = Column(DateTime, default=datetime.datetime.now())
    posts = relationship('Post', back_populates='user')

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model

    Product: Type[Model]