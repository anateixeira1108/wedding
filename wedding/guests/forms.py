from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class InvitationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Save')
 
class GuestSearchForm(FlaskForm):
    search = StringField('Enter the name on your invitation', validators=[DataRequired()])
    submit = SubmitField('Continue')

class RSVPForm(FlaskForm):
    party_size = IntegerField('Number of people in your party', validators=[DataRequired()])
    attending_to_ceremony = BooleanField('Attending?')
    attending_to_reception = BooleanField('Attending?')
    submit = SubmitField('Submit RSVP')