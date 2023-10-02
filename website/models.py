from flask_login import UserMixin
from . import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nickname: Mapped[str] = mapped_column(String, unique = True, nullable=False)
    password: Mapped[str] = mapped_column(String)
    # info = db.relationship('Info')

    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

# class Info(db.Model):
#     __tablename__ = 'ratings'
#     rating = db.Column(db.Integer)
#     tries = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key = True)