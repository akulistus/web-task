from flask_login import login_required, current_user
from flask import Blueprint, render_template, request, flash
from .services import deleteAppointment, editAppointment, createAppointment, getAppointments, createHomePage
# from .message import send_appointment_created_message ,send_appointment_deleted_message

views = Blueprint("views", __name__)

@views.route('/')
@login_required
def home(id = None):
    
    hdata, ddata, chosen_hospital = createHomePage(current_user, id)
    return render_template("home.html", hospital_list=hdata, doctor_list=ddata, hospital_name = chosen_hospital, user = current_user)

@views.route('/appointments')
@login_required
def appointments():
    appointments = getAppointments(current_user)

    return render_template("appointments.html", doctor_list=appointments, user = current_user)
    
@views.route('/get-doctors/')
@login_required
def get_doctors():
    id = request.args.get('id')
    
    return home(id)

@views.route('/create-appointment', methods = ['POST'])
@login_required
def create_appointment():
    id = request.json.get('id')
    createAppointment(id, current_user)
    # send_appointment_created_message()

    return get_doctors()

@views.route('/delete-appointment', methods = ['POST'])
@login_required
def delete_appointment():
    doc_id = request.json.get('did')
    pat_id = request.json.get('pid') 
    deleteAppointment(doc_id, pat_id)
    # send_appointment_deleted_message()

    return appointments()

@views.route('/edit-appointment', methods = ['POST'])
@login_required
def edit_appointment():
    doc_id = request.form.get('doc_id')
    pat_id = request.form.get('pat_id') 
    info = request.form.get('info')
    editAppointment(doc_id, pat_id, info)

    return appointments()