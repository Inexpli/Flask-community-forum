from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():

    return render_template('login.html')

@auth.route('/logout')
def logout():

    pass

@auth.route('/signup', methods=['GET','POST'])
def singup():

    return render_template('signup.html')