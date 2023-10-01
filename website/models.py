from flask_login import UserMixin
from . import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(150))
    info = db.relationship('Info')

class Info(db.Model):
    __tablename__ = 'ratings'
    rating = db.Column(db.Integer)
    tries = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)