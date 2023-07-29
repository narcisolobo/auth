"""
This module contains the Flask app factory.
"""

from os import environ

from dotenv import load_dotenv
from flask import Flask, redirect, url_for

from .blueprints.auth import auth
from .blueprints.auth.model import User
from .extensions import bcrypt, db, login_manager, migrate

# Environment variables
load_dotenv()
SECRET_KEY = environ.get("SECRET_KEY")


def create_app():
    """Flask app factory."""

    app = Flask(__name__)

    # Configurations
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

    # Extensions
    db.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Blueprints
    app.register_blueprint(auth)

    # Routes
    @app.get("/")
    def redirect_to_login():
        """Redirects user from / to /auth/login."""

        return redirect(url_for("auth.login"))

    # Flask-Login settings
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
