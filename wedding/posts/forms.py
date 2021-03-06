from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    author = StringField('By:', validators=[DataRequired()])
    submit = SubmitField('Save')