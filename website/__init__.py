from flask import Flask

def createApp():
	app = Flask(__name__)

	#this is going to encrypt or secure the cookies and session data related to the website
	app.config['SECRET_KEY'] = '35aa0a5e582bf7fdd64254e054170813'

	#importing the views URLs from the blueprints
	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix = '/')
	app.register_blueprint(auth, url_prefix = '/')
	
	return app
