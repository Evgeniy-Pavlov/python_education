"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def users_data_get(users_data_url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(users_data_url) as response:
            data_users: list[dict] = await response.json()
            return data_users


async def posts_data_get(posts_data_url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(posts_data_url) as response:
            data_posts: list[dict] = await response.json()
            return data_posts


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(users_data_get(USERS_DATA_URL))
    asyncio.get_event_loop().run_until_complete(posts_data_get(POSTS_DATA_URL))
