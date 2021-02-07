from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


#defining database
db = SQLAlchemy()
dbName = 'database.db'



def createApp():
	app = Flask(__name__)

	#this is going to encrypt or secure the cookies and session data related to the website
	app.config['SECRET_KEY'] = '35aa0a5e582bf7fdd64254e054170813'

	app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbName}"

	db.init_app(app)

	#importing the views URLs from the blueprints
	from .views import views
	from .auth import auth

	from .models import User, Note

	app.register_blueprint(views, url_prefix = '/')
	app.register_blueprint(auth, url_prefix = '/')

	createDatabase(app)
	
	return app


def createDatabase(app):
	if not path.exists('website/' +  dbName):
		db.create_all(app=app)
		print('Created database')
