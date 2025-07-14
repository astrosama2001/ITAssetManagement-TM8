
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartasset.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    from .views import main
    from .auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
