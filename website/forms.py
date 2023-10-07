from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, InputRequired

class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surname")
    passport_code = StringField("Passport Code")
    password1 = PasswordField("Password",validators=[InputRequired(), EqualTo("password2", message="Passwords must match")])
    password2 = PasswordField("Password (Confirm)")
    submit = SubmitField("Submit")
