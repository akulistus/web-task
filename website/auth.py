from flask import Blueprint, request, render_template, flash

auth = Blueprint("auth", __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form
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
            flash('Account created!', category="success")

    return render_template("sign-up.html")

@auth.route('logout', methods = ['POST', 'GET'])
def logout():
    return render_template("home.html")