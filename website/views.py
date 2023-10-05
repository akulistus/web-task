from flask import Blueprint, render_template, request, flash
from . import db
from .models import Doctor, Hospital, Appointment
from flask_login import login_required, current_user

views = Blueprint("views", __name__)

@views.route('/')
@login_required
def home(id = None):
    if id:
        chosen_hospital = Hospital.query.get(id).name
    else:
        chosen_hospital = "Choose Hospital"

    hdata = Hospital.query.order_by(Hospital.name).all()
    existing_appointments = [x.doctor_id for x in current_user.doctors]
    ddata_all = Doctor.query.filter_by(hospital_id = id)
    ddata = list(filter(lambda x: x.id not in existing_appointments, ddata_all))

    return render_template("home.html", hospital_list=hdata, doctor_list=ddata, hospital_name = chosen_hospital, user = current_user)

@views.route('/appointments')
@login_required
def appointments():
    ddata = current_user.doctors

    return render_template("appointments.html", doctor_list=ddata, user = current_user)
    
@views.route('/get-doctors/')
@login_required
def get_doctors():
    id = request.args.get('id')
    
    return home(id)

@views.route('/create-appointment/', methods = ['POST', 'GET'])
@login_required
def create_appointment():
    id = request.args.get('id')
    doctor = Doctor.query.get(id)
    appointment = Appointment()
    appointment.patient = current_user
    appointment.doctor = doctor
    doctor.patients.append(appointment)
    db.session.commit()
    flash('Appointment created', category='succsess')

    return home()

@views.route('/delete-appointment/', methods = ['POST', 'GET'])
@login_required
def delete_appointment():
    doc_id = request.args.get('doc_id')
    pat_id = request.args.get('pat_id') 
    appointmen = Appointment.query.get({"doctor_id": doc_id, "patient_id": pat_id})
    db.session.delete(appointmen)
    db.session.commit()
    flash('Appointment deleted', category='succsess')

    return appointments()

@views.route('/edit-appointment/', methods = ['GET', 'POST'])
@login_required
def edit_appointment():
    doc_id = request.args.get('doc_id')
    pat_id = request.args.get('pat_id') 
    appointmen = Appointment.query.get({"doctor_id": doc_id, "patient_id": pat_id})
    info = request.form.get('info')
    appointmen.info = info
    db.session.commit()
    flash('Appointment edited', category='succsess')

    return appointments()