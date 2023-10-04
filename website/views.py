from flask import Blueprint, render_template, jsonify
from . import db
from .models import Doctor, Hospital
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route('/')
@login_required
def home(id = None):
    hdata = Hospital.query.order_by(Hospital.name).all()
    ddata = Doctor.query.filter_by(hospital_id = id)
    return render_template("home.html", hospital_list=hdata, doctor_list=ddata)

@views.route('/appointments')
@login_required
def appointments():
    ddata = current_user.doctors
    return render_template("appointments.html", doctor_list=ddata)
    
@views.route('/get-doctors/<id>')
@login_required
def get_doctors(id):
    return home(id)

@views.route('/create-appointment/<id>')
@login_required
def create_appointment(id):
    doctor = Doctor.query.get(id)
    user = current_user
    doctor.patients.append(user)
    db.session.commit()
    return jsonify({})
