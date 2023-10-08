from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy.extension import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager

db = SQLAlchemy()
# mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "asdasasdasdasda"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:admin@localhost/test"
    # app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
    # app.config['MAIL_PORT'] = 587
    # app.config['MAIL_USE_TLS'] = True
    # app.config['MAIL_USERNAME'] = 'sendtestmessages@rambler.ru'
    # app.config['MAIL_DEFAULT_SENDER'] = 'sendtestmessages@rambler.ru'
    # app.config['MAIL_PASSWORD'] = 'AHVaIDX67J3WRN4k'
    # mail.init_app(app)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import Passport, Hospital, Doctor, Patient, Appointment

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Patient.query.get(int(id))

    return app

def create_database(_app: Flask):
    with _app.app_context():
        db.create_all()