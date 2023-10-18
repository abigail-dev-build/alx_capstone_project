from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Post
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
            # flash('Note is too short!', category='error') 
            print('Post cannot be empty!')
        elif len(title) < 1:
            print('Title cannot be empty!')
        elif len(category) < 1:
            print('Category cannot be empty!')
        elif len(author) < 1:
            print('Author cannot be empty!')
        else:
            new_post = Post(content=content, title=title, category=category, author=author, user_id=current_user.id) 
            db.session.add(new_post)
            db.session.commit()
            # flash('Note added!', category='success')
            print('Post added!')
            return redirect(url_for('views.home'))

    return render_template("blog-create.html", user=current_user)
