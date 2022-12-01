from flask_wtf import FlaskForm
from wtforms import Stringfield, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class UserCreation(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit_btn = SubmitField() 
