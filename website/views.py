from flask import Blueprint, render_template, request
from . import db
from .models import Doctor, Hospital, Appointment
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
    appointment = Appointment()
    appointment.patient = current_user
    appointment.doctor = doctor
    doctor.patients.append(appointment)
    db.session.commit()
    return home()

@views.route('/delete-appointment/<did>,<pid>')
@login_required
def delete_appointment(did,pid):
    appointmen = Appointment.query.get({"doctor_id": did, "patient_id": pid})
    db.session.delete(appointmen)
    db.session.commit()
    return appointments()

@views.route('/edit-appointment/<did>,<pid>', methods = ['GET', 'POST'])
@login_required
def edit_appointment(did, pid):
    if request.method == 'POST':
        appointmen = Appointment.query.get({"doctor_id": did, "patient_id": pid})
        info = request.form.get('info')
        appointmen.info = info
        db.session.commit()

    return appointments()