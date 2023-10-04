from flask import Blueprint, request, render_template, flash, redirect, url_for
from .models import Patient, Passport
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        patient = Patient.query.filter_by(name = name).first()
        if patient:
            if check_password_hash(patient.password, password):
                flash('Logged in successefully', category='succsess')
                login_user(patient, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Inocrrect password', category='error')
        else:
            flash('No such patient!', category='error')
    return render_template("login.html")

@auth.route('/sign-up', methods = ['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        passport_code = request.form.get('passport_code')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(name) < 2:
            print("here")
            flash('Name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category="error")
        else:
            new_passport = Passport(ind_code = passport_code)
            new_patient = Patient(name = name, surname = surname, password = generate_password_hash(password1), passport = new_passport)
            db.session.add(new_passport)
            db.session.add(new_patient)
            db.session.commit()
            login_user(new_patient, remember=True)
            flash('Account created!', category="success")
            return redirect(url_for('views.home'))

    return render_template("sign-up.html")

@auth.route('/logout', methods = ['POST', 'GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))