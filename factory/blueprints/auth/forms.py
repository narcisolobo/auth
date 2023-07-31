from re import compile

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import BooleanField, EmailField, PasswordField, StringField, TextAreaField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    InputRequired,
    Length,
    Optional,
    Regexp,
)

EMAIL_REGEX = compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")
PASSWORD_REGEX = compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$")


class RegisterForm(FlaskForm):
    username = StringField(
        "Username:",
        validators=[
            DataRequired("Please enter your username."),
            Length(1, 20, "Username must be between 1 and 20 characters long."),
        ],
    )
    email = EmailField(
        "Email:",
        validators=[
            DataRequired("Please enter your email address."),
            Email("Invalid email."),
        ],
    )
    password = PasswordField(
        "Password:",
        validators=[
            DataRequired("Please enter your password."),
            Regexp(
                PASSWORD_REGEX,
                message="At least 8 characters, 1 upper, 1 lower, 1 number.",
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password:",
        [
            DataRequired("Please retype your password."),
            EqualTo("password", "Passwords must match."),
        ],
    )


class LoginForm(FlaskForm):
    email = EmailField(
        "Email:",
        validators=[
            InputRequired("Please enter your email address."),
            Email("Invalid email."),
        ],
    )
    password = PasswordField(
        "Password:",
        validators=[
            DataRequired("Please enter your password."),
            Regexp(
                PASSWORD_REGEX,
                message="At least 8 characters, 1 upper, 1 lower, 1 number.",
            ),
        ],
    )
    remember = BooleanField("Remember me")


class AccountForm(FlaskForm):
    location = StringField(
        "Edit Location:",
        validators=[
            Optional(),
            Length(1, 60, "Location must be between 1 and 60 characters long."),
        ],
    )
    blurb = TextAreaField(
        "Edit Blurb:",
        validators=[
            Optional(),
            Length(1, 280, "Blurb must be between 1 and 280 characters long."),
        ],
    )


class AvatarForm(FlaskForm):
    avatar = FileField(validators=[FileRequired("Please choose an image.")])
