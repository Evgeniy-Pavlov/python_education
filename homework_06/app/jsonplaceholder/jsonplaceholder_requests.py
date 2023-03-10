import asyncio
import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users_data(users_data_url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(users_data_url) as response:
            data_users: list[dict] = await response.json()
            return data_users


async def fetch_posts_data(posts_data_url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        async with session.get(posts_data_url) as response:
            data_posts: list[dict] = await response.json()
            return data_posts


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch_posts_data(USERS_DATA_URL))
    asyncio.get_event_loop().run_until_complete(fetch_posts_data(POSTS_DATA_URL))
