from flask import redirect, render_template, url_for
from flask_login import current_user, login_required

from factory.blueprints.main import main


@main.get("/")
def redirect_to_login():
    """Redirects user from / to /auth/login."""

    return redirect(url_for("auth.login"))


@main.get("/dashboard")
@login_required
def dashboard():
    """Displays the dashboard template."""

    user = current_user
    return render_template("/main/dashboard.html", user=user)
