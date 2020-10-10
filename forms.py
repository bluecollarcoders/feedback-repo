from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Optional


class RegistrationForm(FlaskForm):
    """Form for adding a User"""

    username = StringField(
        "Username",
        validators=[InputRequired()]
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired()]
    )
    email = StringField(
        "Email",
        validators=[InputRequired()]
    )
    first_name = StringField(
        "First Name",
        validators=[InputRequired()]
    )
    last_name = StringField(
        "Last Name",
        validators=[InputRequired()]
    )


class LoginForm(FlaskForm):
    """Form for Login a User"""

    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class FeedbackForm(FlaskForm):
    """Add feedback form."""

    title = StringField(
        "Title",
        validators=[InputRequired()],
    )
    content = StringField(
        "Content",
        validators=[InputRequired()],
    )


class DeleteForm(FlaskForm):
    """Delete Form"""
