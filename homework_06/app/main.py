import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template, flash
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from models import db



config_name = os.getenv("CONFIG_NAME", "DevelopmentConfig")

app = Flask(__name__)
app.config.from_object(f"config.{config_name}")
db.init_app(app)

with app.app_context():
    db.create_all()

@app.get('/')
def index_view():
    return render_template('index.html')


@app.get('/users')
def users_view():
    return render_template('users.html')


@app.get('/posts')
def posts_view():
    return render_template('posts.html')


if __name__ == '__main__':
    app.run()

