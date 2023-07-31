import os

from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from factory.blueprints.auth import auth
from factory.extensions import bcrypt, db
from factory.utils import allowed_file, safe_unique_name

from .forms import AccountForm, AvatarForm, LoginForm, RegisterForm
from .model import User


@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    GET: Displays the register form template.
    POST: Processes the register form.
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

    return render_template("/auth/register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    GET: Displays the login form template.
    POST: Processes the login form.
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

    return render_template("/auth/login.html", form=form)


@auth.get("/account")
@login_required
def account():
    """Displays the current user's account info."""

    user = current_user
    return render_template("/auth/account.html", user=user)


@auth.route("/account/edit", methods=["GET", "POST"])
@login_required
def edit_account():
    """
    GET: Displays the edit account form template.
    POST: Processes the edit account form.
    """

    user: User = current_user
    form = AccountForm()
    context = {"user": user, "form": form}

    if form.validate_on_submit():
        print("form valid".center(50, "*"))
        # Get valid user input
        location = request.form.get("location")
        blurb = request.form.get("blurb")

        user.location = location
        user.blurb = blurb
        db.session.commit()
        return redirect(url_for("auth.account"))

    if not form.validate_on_submit():
        print("form not valid".center(50, "*"))
        print(form.errors.items())

    return render_template("/auth/edit_account.html", **context)


@auth.route("/avatar", methods=["GET", "POST"])
@login_required
def avatar():
    """
    GET: Displays the edit account form template.
    POST: Processes the edit account form.
    """

    user: User = current_user
    form = AvatarForm()
    context = {"user": user, "form": form}

    if form.validate_on_submit():
        file = form.avatar.data
        if allowed_file(file.filename):
            safe_name = safe_unique_name(file.filename)
            file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], safe_name))
            user.avatar = safe_name
            db.session.commit()
            return redirect(url_for("auth.account"))

    return render_template("/auth/avatar.html", **context)


@auth.get("/logout")
@login_required
def logout():
    """Logs out the current user."""

    logout_user()
    return redirect(url_for("auth.login"))
