from flask_login import UserMixin
from . import db
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Hospital(db.Model):
    __tablename__ = 'hospitals'
    hospital_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)

class Passport(db.Model):
    __tablename__ = 'passports'
    passprt_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ind_code: Mapped[str] = mapped_column(String, nullable=False)

class Doctor(db.Model, UserMixin):
    __tablename__ = 'doctors'
    doctor_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[int] = mapped_column(Integer, nullable=False)
    hospital_id: Mapped[int] = mapped_column(Integer, ForeignKey(Hospital.hospital_id))

class Patient(db.Model, UserMixin):
    __tablename__ = 'patients'
    patient_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    surname: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[int] = mapped_column(Integer, nullable=False)
    passport_id: Mapped[int] = mapped_column(Integer, ForeignKey(Passport.passprt_id))

appointments = db.Table(
    'appointments',
    Column('doctor_id', ForeignKey(Doctor.doctor_id), primary_key=True),
    Column('patient_id', ForeignKey(Patient.patient_id), primary_key=True)
)
