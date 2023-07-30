from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from factory.blueprints.auth import auth
from factory.extensions import bcrypt, db

from .forms import LoginForm, RegisterForm
from .model import User


@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    GET: Displays the register form template.
    POST: Process the register form.
    """

    form = RegisterForm()
    if form.validate_on_submit():
        # Get valid user input
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user's email already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email exists. Please log in.")
            return redirect(url_for("auth.login"))

        pw_hash = bcrypt.generate_password_hash(password)

        new_user = User(username=username, email=email, password=pw_hash)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful. Please log in.")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    GET: Displays the login form template.
    POST: Process the login form.
    """

    form = LoginForm()
    if form.validate_on_submit():
        # Get valid user input
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        # Check if user's email exists and password is correct
        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            flash("Invalid credentials.")
            return redirect(url_for("auth.login"))

        # Log in the user
        login_user(user, remember=remember)
        return redirect(url_for("main.dashboard"))

    return render_template("login.html", form=form)


@auth.get("/logout")
@login_required
def logout():
    """Logs out the current user."""

    logout_user()
    return redirect(url_for("auth.login"))
