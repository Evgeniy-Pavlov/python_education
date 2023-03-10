from flask import Flask, request, render_template, flash
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from jsonplaceholder.jsonplaceholder_requests import fetch_posts_data, fetch_users_data

app = Flask(__name__)


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
    app.run(debug=True)

