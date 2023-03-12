import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, flash
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from models import db, User, Post
from flask_sqlalchemy.query import Query
from sqlalchemy.orm import joinedload
from crud import create_post_from_jsonplaceholder, create_user_from_jsonplaceholder, read_all_posts_with_authors, read_all_users


config_name = os.getenv("CONFIG_NAME", "DevelopmentConfig")

app = Flask(__name__)
app.config.from_object(f"config.{config_name}")
db.init_app(app)
migrate = Migrate(app=app, db=db)


@app.cli.command('create-all')
def table_create_all():
    with app.app_context():
        db.create_all()

@app.get('/')
def index_view():
    return render_template('index.html')


@app.get('/users')
def users_view():
    users = read_all_users()
    return render_template('users.html', users=users)


@app.get('/posts')
def posts_view():
    posts = read_all_posts_with_authors()
    return render_template('posts.html', posts=posts)


if __name__ == '__main__':
    app.run()
    
    

