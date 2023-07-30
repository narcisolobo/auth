"""
This module contains the Flask app factory.
"""

from os import environ

from dotenv import load_dotenv
from flask import Flask

from .blueprints.auth import auth
from .blueprints.main import main
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
    login_manager.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
