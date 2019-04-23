from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import login_required
from wedding import db
from wedding.models import Post
from wedding.posts.forms import PostForm


posts = Blueprint('posts', __name__)

@posts.route("/guest-book")
def guest_book():
    page = request.args.get('page', 1, type=int)
    book = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=6)
    return render_template('guest_book.html', book=book)


@posts.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(content=form.content.data, author=form.author.data)
        db.session.add(post)
        db.session.commit()
        flash('You added a new post', 'success')
        return redirect(url_for('posts.guest_book'))
    return render_template('create_post.html', form=form, legend='Add Post')


@posts.route("/post/<int:post_id>/delete", methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('posts.guest_book'))
