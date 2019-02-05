from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from wedding.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)

	from wedding.users.routes import users
	from wedding.guests.routes import guests
	from wedding.main.routes import main
	from wedding.errors.handlers import errors
	app.register_blueprint(users)
	app.register_blueprint(guests)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app
