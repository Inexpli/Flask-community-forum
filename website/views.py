from flask import Blueprint, render_template
from flask_login import login_required, login_user, logout_user


views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/home')
@login_required
def home():
    return render_template('home.html')