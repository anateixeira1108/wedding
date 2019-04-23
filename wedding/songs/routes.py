from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import login_required
from wedding import db
from wedding.models import Song
from wedding.songs.forms import SongForm

songs = Blueprint('songs', __name__)

@songs.route("/song-request")
def song_request():
    page = request.args.get('page', 1, type=int)
    song_list = Song.query.paginate(page=page, per_page=7)
    return render_template('song_request.html', song_list=song_list)

@songs.route("/song/new", methods=['GET', 'POST'])
def new_song():
    form = SongForm()
    if form.validate_on_submit():
        song = Song(name=form.name.data, artist=form.artist.data)
        db.session.add(song)
        db.session.commit()
        flash('You added a new song', 'success')
        return redirect(url_for('songs.song_request'))
    return render_template('add_song.html', form=form, legend='Add Song')


@songs.route("/song/<int:song_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    db.session.delete(song)
    db.session.commit()
    flash('Your song has been deleted!', 'success')
    return redirect(url_for('songs.song_request'))