from flask import Blueprint, request, render_template, flash, redirect, url_for
# from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    # if request.method == 'POST':
    #     nickname = request.form.get('nickname')
    #     password = request.form.get('password')

    #     user = User.query.filter_by(nickname = nickname).first()
    #     if user:
    #         if check_password_hash(user.password, password):
    #             flash('Logged in successefully', category='succsess')
    #             login_user(user, remember=True)
    #             return redirect(url_for('views.home'))
    #         else:
    #             flash('Inocrrect password', category='error')
    #     else:
    #         flash('No such user!', category='error')
    return render_template("login.html")

@auth.route('/sign-up', methods = ['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(nickname) < 2:
            print("here")
            flash('Nickname must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category="error")
        else:
            # new_user = User(nickname, generate_password_hash(password1))
            # db.session.add(new_user)
            # db.session.commit()
            # login_user(new_user, remember=True)
            # flash('Account created!', category="success")
            return redirect(url_for('views.home'))

    return render_template("sign-up.html")

@auth.route('/logout', methods = ['POST', 'GET'])
# @login_required
def logout():
    # logout_user()
    return redirect(url_for('auth.login'))