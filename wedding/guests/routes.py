from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from wedding import db
from wedding.models import Invitation
from wedding.guests.forms import InvitationForm, GuestSearchForm, RSVPForm
from sqlalchemy import func


guests = Blueprint('guests', __name__)

@guests.route("/rsvp", methods=['GET', 'POST'])
def rsvp():
    form = GuestSearchForm()
    if form.validate_on_submit():
        search_name = "%" + form.search.data + "%"
        invitations = Invitation.query.filter(Invitation.name.like(search_name)).all()
        if invitations:
            return render_template('rsvp.html', form=form, invitations=invitations)
        else:
            flash('Unsuccessful. Please reach out to the couple to see exactly how they entered your details.', 'danger')
    return render_template('rsvp.html', form=form)



@guests.route("/rsvp/<int:invitation_id>/update", methods=['GET', 'POST'])
def update_attendance(invitation_id):
    invitation = Invitation.query.get_or_404(invitation_id)
    form = RSVPForm()
    if form.validate_on_submit():
        invitation.party_size = form.party_size.data
        invitation.attending_to_ceremony = form.attending_to_ceremony.data
        invitation.attending_to_reception = form.attending_to_reception.data
        db.session.commit()
        flash('Thank you!', 'success')
        return redirect(url_for('main.home')) 
    elif request.method == 'GET':
        name = invitation.name
        form.party_size.data = invitation.party_size
        form.attending_to_ceremony.data = invitation.attending_to_ceremony
        form.attending_to_reception.data = invitation.attending_to_reception
    return render_template('update_attendance.html', form=form, name=name)


@guests.route("/guest-list")
@login_required
def guest_list():
    total_c = db.session.query(func.sum(Invitation.party_size)).filter(Invitation.attending_to_ceremony==True).one()[0]
    total_r = db.session.query(func.sum(Invitation.party_size)).filter(Invitation.attending_to_reception==True).one()[0]
    page = request.args.get('page', 1, type=int)
    invitations = Invitation.query.paginate(page=page, per_page=7)
    return render_template('guest_list.html', invitations=invitations, total_r=total_r, total_c=total_c)


@guests.route("/guest/new", methods=['GET', 'POST'])
@login_required
def new_invitation():
    form = InvitationForm()
    if form.validate_on_submit():
        invitation = Invitation(name=form.name.data)
        db.session.add(invitation)
        db.session.commit()
        flash('You added a new guest', 'success')
        return redirect(url_for('guests.guest_list'))
    return render_template('create_invitation.html', form=form, legend='Add Guest')


@guests.route("/guest/<int:invitation_id>/update", methods=['GET', 'POST'])
@login_required
def update_invitation(invitation_id):
    invitation = Invitation.query.get_or_404(invitation_id)
    form = InvitationForm()
    if form.validate_on_submit():
        invitation.name = form.name.data
        db.session.commit()
        flash('Your invitation has been updated!', 'success')
        return redirect(url_for('guests.guest_list'))
    elif request.method == 'GET':
        form.name.data = invitation.name
    return render_template('create_invitation.html', form=form, legend='Update Guest')


@guests.route("/guest/<int:invitation_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_invitation(invitation_id):
    invitation = Invitation.query.get_or_404(invitation_id)
    db.session.delete(invitation)
    db.session.commit()
    flash('Your invitation has been deleted!', 'success')
    return redirect(url_for('guests.guest_list'))

