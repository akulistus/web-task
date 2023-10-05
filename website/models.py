from flask_login import UserMixin
from . import db
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Appointment(db.Model):
    __tablename__ = 'appointments'
    doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey('doctors.id'), primary_key=True)
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey('patients.id'), primary_key=True)
    info: Mapped[str] = mapped_column(String, nullable=True)
    doctor: Mapped["Doctor"] = db.relationship(back_populates="patients")
    patient: Mapped["Patient"] = db.relationship(back_populates="doctors")

class Hospital(db.Model):
    __tablename__ = 'hospitals'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)

class Passport(db.Model):
    __tablename__ = 'passports'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ind_code: Mapped[str] = mapped_column(String, nullable=False)
    patient = db.relationship('Patient', backref='passport')

class Doctor(db.Model, UserMixin):
    __tablename__ = 'doctors'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    speciality: Mapped[int] = mapped_column(String, nullable=False)
    hospital_id: Mapped[int] = mapped_column(Integer, ForeignKey(Hospital.id))
    patients: Mapped[list["Appointment"]] = db.relationship(back_populates='doctor')

class Patient(db.Model, UserMixin):
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    passport_id: Mapped[int] = mapped_column(Integer, ForeignKey(Passport.id))
    doctors: Mapped[list["Appointment"]] = db.relationship(back_populates='patient')

