"""
This module contains the Flask app factory.
"""

from os import environ
from os.path import dirname, join, realpath

from dotenv import load_dotenv
from flask import Flask

from .blueprints.auth import auth
from .blueprints.main import main
from .extensions import bcrypt, db, login_manager, migrate

# Environment variables and constants
load_dotenv()
SECRET_KEY = environ.get("SECRET_KEY")
BASE_DIR = join(dirname(realpath(__file__)))
UPLOAD_PATH = ["static", "images", "avatars"]
UPLOAD_FOLDER = join(BASE_DIR, *UPLOAD_PATH)


def create_app():
    """Flask app factory."""

    app = Flask(__name__)

    # Configurations
    app.secret_key = SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    # Extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    # Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(main)

    return app
