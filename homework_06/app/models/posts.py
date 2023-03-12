from .database import db
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .users import User
from typing import TYPE_CHECKING, Type

class Post(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, unique=False, nullable=False)
    user = relationship('User', back_populates='posts')

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model

    Product: Type[Model]