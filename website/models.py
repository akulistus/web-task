from flask_login import UserMixin
from . import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.associationproxy import association_proxy

class Appointment(db.Model):
    __tablename__ = 'appointments'
    doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey('doctors.id'), primary_key=True)
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey('patients.id'), primary_key=True)
    info: Mapped[str] = mapped_column(String(512), nullable=True)
    doctor: Mapped["Doctor"] = db.relationship('Doctor', back_populates="patients_assosiation")
    patient: Mapped["Patient"] = db.relationship('Patient', back_populates="doctors_assosiation")

class Hospital(db.Model):
    __tablename__ = 'hospitals'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    address: Mapped[str] = mapped_column(String(256))

class Passport(db.Model):
    __tablename__ = 'passports'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ind_code: Mapped[str] = mapped_column(String, nullable=False)
    patient = db.relationship('Patient', backref='passport')

class Doctor(db.Model, UserMixin):
    __tablename__ = 'doctors'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    surname: Mapped[str] = mapped_column(String(256), nullable=False)
    speciality: Mapped[int] = mapped_column(String(256), nullable=False)
    hospital_id: Mapped[int] = mapped_column(Integer, ForeignKey(Hospital.id))
    patients_assosiation = db.relationship('Appointment', back_populates='doctor')
    patients = association_proxy('patients_assosiation', 'patient')

class Patient(db.Model, UserMixin):
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    surname: Mapped[str] = mapped_column(String(256), nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    passport_id: Mapped[int] = mapped_column(Integer, ForeignKey(Passport.id))
    doctors_assosiation = db.relationship('Appointment', back_populates='patient')
    doctors = association_proxy('doctors_assosiation', 'doctor')

