from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


#defining database
db = SQLAlchemy()
dbName = 'database.db'



def createApp():
	app = Flask(__name__)

	#this is going to encrypt or secure the cookies and session data related to the website
	app.config['SECRET_KEY'] = 'b5f48h78f2ryh8dg83457t9'

	app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbName}"

	db.init_app(app)

	#importing the views URLs from the blueprints
	from .views import views
	from .auth import auth

	from .models import User, Note

	app.register_blueprint(views, url_prefix = '/')
	app.register_blueprint(auth, url_prefix = '/')

	createDatabase(app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))
	
	return app


def createDatabase(app):
	if not path.exists('website/' +  dbName):
		db.create_all(app=app)
		print('Created database')
