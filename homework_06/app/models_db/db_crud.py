import asyncio
from models import User, Post, Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


async def create_user(session: AsyncSession, data_users: list[dict]) -> list[User]:
    users = [User(name=i.get('name'), username=i.get('username'), email=i.get('email')) for i in data_users]
    session.add_all(users)
    await session.commit()
    return users


async def create_post(session: AsyncSession, data_posts: list[dict]) -> list[Post]:
    posts = [Post(user_id=i.get('userId'), title=i.get('title'), body=i.get('body')) for i in data_posts]
    session.add_all(posts)
    await session.commit()
    return posts


async def read_post(session: AsyncSession) -> list[Post]:
    stmnt = select(Post)
    result = await session.execute(stmnt)
    all_posts = result.scalars().all()
    return all_posts


async def read_user(session: AsyncSession) -> list[User]:
    stmnt = select(User)
    result = await session.execute(stmnt)
    all_users = result.scalars().all()
    return all_users


# async def async_main():
#     await create_tables()
#     result_users, result_posts = await asyncio.gather(fetch_users_data(USERS_DATA_URL),
#                                                       fetch_posts_data(POSTS_DATA_URL))
#     async with Session() as session:
#         await create_user(session, result_users)
#     async with Session() as session:
#         await create_post(session, result_posts)

async def async_main():
    async with Session() as session:
        result = await read_user(session)
    
    for i in result:
        print(i.username, i.date_create, i.email)


def main():
   result = asyncio.get_event_loop().run_until_complete(async_main())


if __name__ == "__main__":
    main()
