from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SongForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    artist = StringField('Artist')
    submit = SubmitField('Save')
 