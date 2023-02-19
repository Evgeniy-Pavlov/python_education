"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from models import create_tables, User, Post, PG_CONN_URI
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data, USERS_DATA_URL, POSTS_DATA_URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine
from sqlalchemy.orm import sessionmaker

async_engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=True)
Session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


async def create_user(session: AsyncSession, name: str, username: str, email: str) -> User:
    user = User(name=name, username=username, email=email)
    session.add(user)
    await session.commit()
    return User


async def create_post(session: AsyncSession, user_id: int, title: str, body: str) -> Post:
    post = Post(user_id=user_id, title=title, body=body)
    session.add(post)
    await session.commit()
    return Post


async def async_main():
    await create_tables()
    result_users, result_posts = await asyncio.gather(fetch_users_data(USERS_DATA_URL),
                                                      fetch_posts_data(POSTS_DATA_URL))
    for user in result_users:
        async with Session() as session:
            await create_user(session=session, name=user.get('name'),
                              username=user.get('username'), email=user.get('email'))
    for post_item in result_posts:
        async with Session() as session:
            await create_post(session=session, user_id=int(post_item.get('userId')), title=post_item.get('title'),
                              body=post_item.get('body'))


def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
