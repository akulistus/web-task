# from flask_mail import Message
# from . import mail

def send_appointment_created_message():
    msg = Message("Appointment Update", recipients=["wayigo5919@estudys.com"])
    msg.html = "<h1> Your appintment has been created! </h1>"
    mail.send(msg)

def send_appointment_deleted_message():
    msg = Message("Appointment Update", recipients=["wayigo5919@estudys.com"])
    msg.html = "<h1> Your appintment has been deleted! </h1>"
    mail.send(msg)