from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class UserForm(FlaskForm):
    name = StringField(
        label="Name",
        validators=[DataRequired(),Length(min=3, max=40)]
    )
    username = StringField(
        label="Username",
        validators=[DataRequired(),Length(min=3, max=50)]
    )
    email = StringField(
        label="Email",
        validators=[DataRequired(),Length(max=50)]
    )