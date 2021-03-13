from flask import Flask

def create_app():
    #Config
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'
    
    #Routes
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    return app