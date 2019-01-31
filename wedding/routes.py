from flask import Flask, render_template, url_for, flash, redirect, request
from wedding import app, db, bcrypt
from wedding.forms import RegistrationForm, LoginForm, InvitationForm
from wedding.models import User, Invitation
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/schedule")
def schedule():
    return render_template('schedule.html')


@app.route("/wedding-party")
def weddingparty():
    return render_template('wedding_party.html')


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
    invitations = Invitation.query.all()
    return render_template('guestlist.html', invitations=invitations)


@app.route("/guest/new", methods=['GET', 'POST'])
@login_required
def new_guest():
    form = InvitationForm()
    if form.validate_on_submit():
        invitation = Invitation(name=form.name.data, max_party_size=form.max_party_size.data, people=form.people.data)
        db.session.add(invitation)
        db.session.commit()
        flash('You added a new guest', 'success')
        return redirect(url_for('guestlist'))
    return render_template('create_invitation.html', form=form)


@app.route("/guest/<int:invitation_id>/update", methods=['GET', 'POST'])
@login_required
def update_invitation(invitation_id):
    invitation = Invitation.query.get_or_404(invitation_id)
    form = InvitationForm()
    if form.validate_on_submit():
        invitation.name = form.name.data
        invitation.max_party_size = form.max_party_size.data
        invitation.people = form.people.data
        db.session.commit()
        flash('Your invitation has been updated!', 'success')
        return redirect(url_for('guestlist', invitation_id=invitation.id))
    elif request.method == 'GET':
        form.name.data = invitation.name
        form.max_party_size.data = invitation.max_party_size
        form.people.data = invitation.people
    return render_template('create_invitation.html', form=form)


@app.route("/invitation/<int:invitation_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_invitation(invitation_id):
    invitation = Invitation.query.get_or_404(invitation_id)
    db.session.delete(invitation)
    db.session.commit()
    flash('Your invitation has been deleted!', 'success')
    return redirect(url_for('guestlist'))