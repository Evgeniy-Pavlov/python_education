import os
from flask import Flask, request, render_template, flash, redirect, url_for
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from models import db, User, Post
from flask_sqlalchemy.query import Query
from crud import create_post_from_jsonplaceholder, create_user_from_jsonplaceholder, \
    read_all_posts_with_authors, read_all_users, create_post, create_user
from forms import UserForm, PostForm
from http import HTTPStatus

config_name = os.getenv("CONFIG_NAME", "DevelopmentConfig")

app = Flask(__name__)
app.config.from_object(f"config.{config_name}")
db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)


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
    flash(f'You read all users', category='warning')
    return render_template('users.html', users=users)


@app.get('/posts')
def posts_view():
    posts = read_all_posts_with_authors()
    return render_template('posts.html', posts=posts)


@app.route('/CreateUser', methods=["GET", "POST"])
def user_create_form():
    form = UserForm()
    if request.method == "GET":
        return render_template('create_user.html', form=form)
    if not form.validate_on_submit():
        return (
            render_template("create_user.html", form=form),
            HTTPStatus.BAD_REQUEST,
        )
    
    username_in_database = User.query.filter(User.username.ilike(form.data['username'])).all()
    if not username_in_database:
        create_user(User(name=form.data['name'], username=form.data['username'], email=form.data['email']))
        flash(f"User was created!", category="success")
        return redirect(url_for("index_view"))
    else:
        flash(f"User already exists!", category="warning")
        return redirect(url_for("users_view"))


@app.route('/CreatePost', methods=["GET", "POST"])
def post_create_form():
    form = PostForm()
    if request.method == "GET":
        return render_template('create_post.html', form=form)
    if not form.validate_on_submit():
        return (
            render_template("create_user.html", form=form),
            HTTPStatus.BAD_REQUEST,
        )
    userid_in_database = User.query.filter(User.username.ilike(form.data['username'])).all()
    if userid_in_database:
        post = Post(title=form.data['title'], body=form.data['body'], user_id=userid_in_database[0].id)
        create_post(post)
        flash(f"Post was created!", category="success")
        return redirect(url_for("posts_view"))    


@app.get('/getRecordsUsers')
def get_records_users():
    create_user_from_jsonplaceholder()
    flash(f"User records retrieved!", category="success")
    return redirect(url_for("users_view"))


@app.get('/getRecordsPosts')
def get_records_posts():
    create_post_from_jsonplaceholder()
    flash(f"Post records retrieved!", category="success")
    return redirect(url_for("posts_view"))


if __name__ == '__main__':
    app.run()
