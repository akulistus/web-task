from werkzeug.security import check_password_hash
from .forms import SignUpForm, LoginForm, DoctorForm, AppointmentForm
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .services import loginUser, signUpUser, signUpNewDoctor, newAppointment, getHospitalchoices, getDoctorchoices, getPatientchoices

auth = Blueprint("auth", __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        patient, password = loginUser(form)
        if patient:
            if check_password_hash(patient.password, password):
                flash('Logged in successefully', category='alert-success')
                login_user(patient, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Inocrrect password', category='alert-danger')
        else:
            flash('No such patient!', category='alert-danger')

    return render_template("login.html", form = form, user = current_user)

@auth.route('/sign-up', methods = ['POST', 'GET'])
def sign_up():

    form = SignUpForm()
    if form.validate_on_submit():
        new_patient = signUpUser(form)
        login_user(new_patient, remember=True)
        flash('Account created!', category="alert-success")
        return redirect(url_for('views.home'))

    return render_template("sign-up.html", form = form, user = current_user)

@auth.route('/logout', methods = ['POST', 'GET'])
@login_required
def logout():
    logout_user()
    
    return redirect(url_for('auth.login'))

@auth.route('/new-doctor', methods = ['POST', 'GET'])
def new_doctor():

    form = DoctorForm()
    form.hospital.choices = getHospitalchoices()
    if form.validate_on_submit():
        signUpNewDoctor(form)
        flash('Doctor successfully added!', category="alert-success")

    return render_template("registerDoctor.html", form = form, user = current_user)

@auth.route('/new-appointment', methods = ['POST', 'GET'])
def new_appointment():

    form = AppointmentForm()
    form.doctor.choices = getDoctorchoices()
    form.patient.choices = getPatientchoices()
    if form.validate_on_submit():
        newAppointment(form)
        flash('Appointment successfully crated!', category="alert-success")

    return render_template("createAppointment.html", form = form, user = current_user)