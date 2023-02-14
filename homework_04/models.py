"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, declared_attr
from sqlalchemy import Column, Integer

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost:5432/postgres"

async_engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=True)


class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User -> blog_users
        Author -> blog_authors
        """
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
Session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
