from flask import Blueprint

from factory.extensions import login_manager

from .model import User

auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)

from factory.blueprints.auth import routes

# Flask-Login settings
login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    """User loader for Flask-Login."""

    return User.query.get(int(user_id))
