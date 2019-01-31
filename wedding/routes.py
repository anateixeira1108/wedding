from flask import Flask, render_template, url_for, flash, redirect, request
from wedding import app, db, bcrypt
from wedding.forms import RegistrationForm, LoginForm
from wedding.models import User, Invitation
from flask_login import login_user, current_user, logout_user, login_required

invitations = [
    {
        'id': 0,
        'name': 'Jose Teixeira',
        'people': 3,
        'confirmated': 0
    },
    {
        'id': 1,
        'name': 'Kevin May Sr',
        'people': 4,
        'confirmated': 0
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/schedule")
def schedule():
    return render_template('schedule.html')


@app.route("/wedding-party")
def weddingparty():
    return render_template('wedding-party.html')


@app.route("/registry")
def registry():
    return render_template('registry.html')


@app.route("/rsvp")
def rsvp():
    return render_template('rsvp.html')

@app.route("/registernewuser", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/guestlist")
@login_required
def guestlist():
    return render_template('guestlist.html', invitations=invitations)