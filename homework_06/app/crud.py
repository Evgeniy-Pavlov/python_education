from models import User, Post, db
from jsonplaceholder import fetch_posts_data, fetch_users_data, USERS_DATA_URL, POSTS_DATA_URL


def create_user_from_jsonplaceholder():
    users_data = fetch_users_data(USERS_DATA_URL)
    username_in_database = [user.username for user in User.query.order_by(User.id).all()]
    users_list: list[dict] = [User(name=i.get('name'), username=i.get('username'), email=i.get('email'))
                               for i in users_data if i.get('username') not in username_in_database]
    db.session.add_all(users_list)
    db.session.commit()
    return users_list


def create_post_from_jsonplaceholder():
    posts_data = fetch_posts_data(POSTS_DATA_URL)
    userid_in_database = [user.id for user in User.query.order_by(User.id).all()]
    posts_list: list[dict] = [Post(user_id=i.get('userId'), title=i.get('title'), body=i.get('body'))
                               for i in posts_data if i.get('userId') not in userid_in_database]
    db.session.add_all(posts_list)
    db.session.commit()
    return posts_list    


def create_user(user):
    db.session.add(user)
    db.session.commit()
    return user
        


def create_post(post):
    db.session.add(post)
    db.session.commit()
    return post
        


def read_all_posts_with_authors():
    result_posts = Post.query.join(User, User.id == Post.user_id).add_columns(User.name, Post.title, Post.body).order_by(Post.title).all()
    return result_posts


def read_all_users():
    result_users = User.query.order_by(User.id).all()
    return result_users


if __name__== '__main__':
    create_user_from_jsonplaceholder()
    create_post_from_jsonplaceholder()