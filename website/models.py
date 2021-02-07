from . import db
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	data = db.Column(db.String(10000))
	date = db.Column(db.DateTime(timezone = True), default = func.now())
	userId = db.Column(db.Integer, db.ForeignKey('user.id'))



class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(50), unique = True)
	password = db.Column(db.String(50))
	firstName = db.Column(db.String(50))
	notes = db.relationship('Note')