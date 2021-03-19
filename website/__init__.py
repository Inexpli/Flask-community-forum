from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from .models import User

db = SQLAlchemy()

DB_NAME = 'database.db'

def create_app():
    
    #Config
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    #Routes
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    #Database
    create_database(app)
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Database has been created!')