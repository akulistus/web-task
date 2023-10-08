from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import Patient, Passport, Hospital, Doctor, Appointment
from .forms import SignUpForm, LoginForm, DoctorForm, AppointmentForm
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():

    form = LoginForm()
    if form.validate_on_submit():

        name = form.name.data
        password = form.password.data

        patient = Patient.query.filter_by(name = name).first()
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
        name = form.name.data
        surname = form.surname.data
        passport_code = form.passport_code.data
        password1 = form.password1.data
        new_passport = Passport(ind_code = passport_code)
        new_patient = Patient(name = name, surname = surname, password = generate_password_hash(password1), passport = new_passport)
        db.session.add(new_passport)
        db.session.add(new_patient)
        db.session.commit()
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
    form.hospital.choices = [(hospital.id, hospital.name) for hospital in Hospital.query.order_by(Hospital.name).all()]
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        speciality = form.speciality.data
        hospital_id = form.hospital.data[0]

        new_doctor = Doctor(
            name = name,
            surname = surname,
            speciality = speciality,
            hospital_id = hospital_id)
        db.session.add(new_doctor)
        db.session.commit()
        flash('Doctor successfully added!', category="alert-success")

    return render_template("registerDoctor.html", form = form, user = current_user)

@auth.route('/new-appointment', methods = ['POST', 'GET'])
def new_appointment():

    form = AppointmentForm()
    form.doctor.choices = [(doctor.id, doctor.name) for doctor in Doctor.query.order_by(Doctor.name).all()]
    form.patient.choices = [(patient.id, patient.name) for patient in Patient.query.order_by(Patient.name).all()]
    if form.validate_on_submit():
        doctor_id = form.doctor.data[0]
        patient_id = form.patient.data[0]
        info = form.info.data
        appointment = Appointment(doctor_id = doctor_id, patient_id = patient_id, info = info)
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment successfully crated!', category="alert-success")

    return render_template("createAppointment.html", form = form, user = current_user)