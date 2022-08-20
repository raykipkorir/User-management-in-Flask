from flask_wtf import FlaskForm
from wtforms.fields import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from authentication.models import User


class RegisterForm(FlaskForm):
    username = StringField(
        label="Username:", validators=[DataRequired(), Length(min=2, max=30)]
    )
    email = EmailField(label="Email Address:", validators=[DataRequired()])
    password1 = PasswordField(
        label="Password:", validators=[DataRequired(), Length(min=6)]
    )
    password2 = PasswordField(
        label="Confirm Password:", validators=[DataRequired(), EqualTo("password1")]
    )
    submit = SubmitField(label="Get started")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exists")


class LoginForm(FlaskForm):
    username = StringField(label="Username: ", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Log In")
