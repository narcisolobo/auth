from re import compile

from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, PasswordField, StringField
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    InputRequired,
    Length,
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
