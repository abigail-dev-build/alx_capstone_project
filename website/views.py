from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Post, Comment
from . import db

views = Blueprint("views", __name__ )

@views.route('/')
@login_required
def home() :
    return render_template("home.html", user=current_user)

@views.route('/post', methods=['GET', 'POST'])
@login_required
def create_post() :
    if request.method == 'POST': 
        content = request.form.get('article')
        title = request.form.get('title')
        category = request.form.get('category')
        author = request.form.get('author')

        if len(content) < 1:
            flash('Post cannot be empty!', category='error') 
        elif len(title) < 1:
            flash('Title cannot be empty!', category='error')
        elif len(category) < 1:
            flash('Category cannot be empty!', category='error')
        elif len(author) < 1:
            flash('Author cannot be empty!', category='error')
        else:
            new_post = Post(content=content, title=title, category=category, author=author, user_id=current_user.id) 
            db.session.add(new_post)
            db.session.commit()
            flash('Post added!', category='success')
            return redirect(url_for('views.home'))

    return render_template("blog-create.html", user=current_user)

@views.route('/post/<int:id>')
def hello(id):
    return render_template('single-post.html', id=id, user=current_user)
