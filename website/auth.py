from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_required, login_user, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_username = User.query.filter_by(username=username).first()

        if user_username:
            if check_password_hash(user_username.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user_username, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('User does not exist.', category='error')

    return render_template("login.html", user = current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        user_username = User.query.filter_by(username=username).first()
        user_email = User.query.filter_by(email=email).first()
        if user_username:
            flash("Username already exist", category='error')
        elif user_email:
            flash("Email already in use", category='error')
        elif len(username) < 3 or len(username)>20:
            flash("Username must be greater than 3 characters and lower than 20.", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif password != confirm_password:
            flash("Passwords don\'t match.", category='error')
        else:
            new_user = User(username=username, email=email, password=generate_password_hash(
                password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user = current_user)