from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    username = StringField(
        label="Username",
        validators=[Length(min=3, max=50)]
    )
    title = StringField(
        label="Title",
        validators=[Length(max=200)]
    )
    body = StringField(
        label="Body",
        validators=[Length(max=1000)]
    )