from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__ )

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                print('Logged in successfully!')
                # flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                # flash('Incorrect password, try again.', category='error')
                print('Invalid details, try again')
        else:
            # flash('Email does not exist.', category='error')
            print('User does not exist.')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register() :
    if request.method == "POST" :
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        cpassword = request.form.get('confirm_password')
        
        if len(email) < 4:
            # flash('Email must be greater than 3 characters.', category='error')
            print('Email must be greater than 3 characters')
        elif len(username) < 2:
            # flash('Username must be greater than 1 character.', category='error')
            print('Username must be greater than 1 character')
        elif password != cpassword:
            # flash('Passwords don\'t match.', category='error')
            print('Passwords don\'t match.')
        elif len(password) < 7:
            # flash('Password must be at least 7 characters.', category='error')
            print('Password must be at least 7 characters.')
        else:
            # flash('Account created successfully!', category='success')
            new_user = User(email=email, username=username, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            print('Account created successfully!')
            return redirect(url_for('auth.login'))
    return render_template('register.html', user=current_user)