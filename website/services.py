from . import db
from werkzeug.security import generate_password_hash
from .models import Appointment, Patient, Passport, Doctor, Hospital

def deleteAppointment(doc_id:int, pat_id:int):
    appointmen = Appointment.query.get({"doctor_id": doc_id, "patient_id": pat_id})
    db.session.delete(appointmen)
    db.session.commit()

def editAppointment(doc_id:int, pat_id:int, info:str):
    appointmen = Appointment.query.get({"doctor_id": doc_id, "patient_id": pat_id})
    appointmen.info = info
    db.session.commit()

def createAppointment(id:int, current_user):
    doctor = Doctor.query.get(id)
    appointment = Appointment()
    appointment.patient = current_user
    appointment.doctor = doctor
    db.session.add(appointment)
    db.session.commit()

def getAppointments(current_user):
    appointments = Appointment.query.filter_by(patient_id = current_user.id)
    return appointments

def createHomePage(current_user, id = None):
    if id:
        chosen_hospital = Hospital.query.get(id).name
    else:
        chosen_hospital = "Choose Hospital"

    hdata = Hospital.query.order_by(Hospital.name).all()
    existing_appointments = [x.id for x in current_user.doctors]
    ddata_all = Doctor.query.filter_by(hospital_id = id)
    ddata = list(filter(lambda x: x.id not in existing_appointments, ddata_all))
    return hdata, ddata, chosen_hospital

def loginUser(form):
    name = form.name.data
    password = form.password.data
    patient = Patient.query.filter_by(name = name).first()
    return patient, password

def signUpUser(form):
    name = form.name.data
    surname = form.surname.data
    passport_code = form.passport_code.data
    password1 = form.password1.data
    new_passport = Passport(ind_code = passport_code)
    new_patient = Patient(name = name, surname = surname, password = generate_password_hash(password1), passport = new_passport)
    db.session.add(new_passport)
    db.session.add(new_patient)
    db.session.commit()

    return new_patient

def signUpNewDoctor(form):
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

def newAppointment(form):
    doctor_id = form.doctor.data[0]
    patient_id = form.patient.data[0]
    info = form.info.data
    appointment = Appointment(doctor_id = doctor_id, patient_id = patient_id, info = info)
    db.session.add(appointment)
    db.session.commit()

def getHospitalchoices():
    return [(hospital.id, hospital.name) for hospital in Hospital.query.order_by(Hospital.name).all()]

def getDoctorchoices():
    return [(doctor.id, doctor.name) for doctor in Doctor.query.order_by(Doctor.name).all()]

def getPatientchoices():
    return [(patient.id, patient.name) for patient in Patient.query.order_by(Patient.name).all()]