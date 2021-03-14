from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():

    return render_template('login.html')

@auth.route('/logout')
def logout():

    pass

@auth.route('/signup', methods=['GET','POST'])
def singup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if len(username) < 3 or len(username)>20:
            flash("Username must be greater than 3 characters and lower than 20.", category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')
        elif password != confirm_password:
            flash("Passwords don\'t match.", category='error')
        else:
            flash("Account has been created!", category='success')
    return render_template('signup.html')