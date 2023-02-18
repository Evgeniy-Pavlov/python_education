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
from sqlalchemy import Column, Integer, String, DateTime, Text
import datetime
import asyncio

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or \
              "postgresql+asyncpg://username:passwd!@localhost:5432/postgres"

async_engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=True)


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}"

    id = Column(Integer, primary_key=True)


Base_declarative = declarative_base(cls=Base)
Session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


class User(Base_declarative):
    name = Column(String(40), unique=False, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    date_create = Column(DateTime, default=datetime.datetime.now())


class Post(Base_declarative):
    user_id = Column(Integer, unique=True, nullable=False)
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, unique=False, nullable=False)


async def create_tables():
    async with async_engine.begin() as connect:
        await connect.run_sync(Base_declarative.metadata.create_all)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(create_tables())
    print(Base_declarative.metadata.tables)
