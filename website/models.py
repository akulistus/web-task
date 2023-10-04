from flask_login import UserMixin
from . import db
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

appointments = db.Table(
    'appointments',
    Column('doctor_id', ForeignKey('doctors.id'), primary_key=True),
    Column('patient_id', ForeignKey('patients.id'), primary_key=True),
    Column('Info')
)

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
    password: Mapped[int] = mapped_column(Integer, nullable=False)
    hospital_id: Mapped[int] = mapped_column(Integer, ForeignKey(Hospital.id))
    patients = db.relationship('Patient', secondary = appointments, backref = 'doctors')

class Patient(db.Model, UserMixin):
    __tablename__ = 'patients'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    passport_id: Mapped[int] = mapped_column(Integer, ForeignKey(Passport.id))

