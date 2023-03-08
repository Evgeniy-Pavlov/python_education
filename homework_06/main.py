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
from models import create_tables, User, Post, Session
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data, USERS_DATA_URL, POSTS_DATA_URL
from sqlalchemy.ext.asyncio import AsyncSession


async def create_user(session: AsyncSession, data_users) -> list[User]:
    users = [User(name=i.get('name'), username=i.get('username'), email=i.get('email')) for i in data_users]
    session.add_all(users)
    await session.commit()
    return users


async def create_post(session: AsyncSession, data_posts):
    posts = [Post(user_id=i.get('userId'), title=i.get('title'), body=i.get('body')) for i in data_posts]
    session.add_all(posts)
    await session.commit()
    return posts


async def async_main():
    await create_tables()
    result_users, result_posts = await asyncio.gather(fetch_users_data(USERS_DATA_URL),
                                                      fetch_posts_data(POSTS_DATA_URL))
    async with Session() as session:
        await create_user(session, result_users)
    async with Session() as session:
        await create_post(session, result_posts)


def main():
    asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
