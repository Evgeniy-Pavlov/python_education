import requests

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_users_data(users_data_url: str) -> list[dict]:
    result = requests.get(users_data_url)
    return result.json()

def fetch_posts_data(posts_data_url: str) -> list[dict]:
    result = requests.get(posts_data_url)
    return result.json()

if __name__ == '__main__':
    fetch_posts_data(POSTS_DATA_URL)
    fetch_users_data(USERS_DATA_URL)
