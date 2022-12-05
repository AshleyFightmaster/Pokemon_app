from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TeamCreationform(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired()])
    submit_btn = SubmitField()