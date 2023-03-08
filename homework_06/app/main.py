from flask import Flask, request, render_template, flash
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

app = Flask(__name__)

@app.get('/')
def index_view():
    return render_template('index.html')