from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, InputRequired, Length, Regexp

class SignUpForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50), Regexp("^[a-zA-Z]+$", message="Must contain only letters")])
    surname = StringField("Surname", validators=[DataRequired(), Length(min=2, max=50), Regexp("^[a-zA-Z]+$", message="Must contain only letters")])
    passport_code = StringField("Passport Code", validators=[DataRequired(), Length(min=10, max=10), Regexp("^\\d+$", message="Must contain only numbers")])
    password1 = PasswordField("Password",validators=[InputRequired(), EqualTo("password2", message="Passwords don't match"), Length(min=5, max=50)])
    password2 = PasswordField("Password (Confirm)", validators=[DataRequired(), Length(min=5, max=50)])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50), Regexp("^[a-zA-Z]+$", message="Must contain only letters")])
    password = PasswordField("Password",validators=[InputRequired(), Length(min=5, max=50)])
    submit = SubmitField("Submit")

class DoctorForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50), Regexp("^[a-zA-Z]+$", message="Must contain only letters")])
    surname = StringField("Surname", validators=[DataRequired(), Length(min=2, max=50), Regexp("^[a-zA-Z]+$", message="Must contain only letters")])
    speciality = StringField("Speciality", validators=[DataRequired(), Length(min=2, max=50), Regexp("^[a-zA-Z]+$", message="Must contain only letters")])
    hospital = SelectField("Hospital" , choices=[])
    submit = SubmitField("Submit")
    
class AppointmentForm(FlaskForm):
    doctor = SelectField("Doctor" , choices=[])
    patient = SelectField("Patient" , choices=[])
    info = TextAreaField("Info")
    submit = SubmitField("Submit")