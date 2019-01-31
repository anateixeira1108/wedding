from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from wedding.models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already in our database')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

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