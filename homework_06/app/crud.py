from models import User, Post, db
from jsonplaceholder import fetch_posts_data, fetch_users_data, USERS_DATA_URL, POSTS_DATA_URL


def create_user_from_jsonplaceholder():
    users_data = fetch_users_data(USERS_DATA_URL)
    users_list: list[dict] = [User(name=i.get('name'), username=i.get('username'), email=i.get('email')) for i in users_data]
    db.session.add_all(users_list)
    db.session.commit()
    return users_list


def create_post_from_jsonplaceholder():
    posts_data = fetch_posts_data(POSTS_DATA_URL)
    posts_list: list[dict] = [Post(user_id=i.get('userId'), title=i.get('title'), body=i.get('body')) for i in posts_data]
    db.session.add_all(posts_list)
    db.session.commit()
    return posts_list    


if __name__== '__main__':
    create_user_from_jsonplaceholder()
    create_post_from_jsonplaceholder()