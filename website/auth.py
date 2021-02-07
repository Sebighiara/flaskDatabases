from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

		user = User.query.filter_by(email = email).first()

		if user:
			if check_password_hash(user.password, password):
				flash('Logged In successfully', category = 'success')
				return redirect(url_for('views.home'))
			else:
				flash('Incorrect password, try again', category = 'error')
		else:
			flash('Email doesn\'t exist.', category = 'error')
	return render_template("login.html", text = "testing")


@auth.route('/logout')
def logout():
	return "<h1>Logout</h1>"


@auth.route('/sign-up', methods = ['GET', 'POST'])
def signUp():
	if request.method == 'POST':
		firstName = request.form.get('firstName')
		lastName = request.form.get('lastName')
		email = request.form.get('email')
		password = request.form.get('password')
		confirmPassword = request.form.get('confirmPassword')
		

		#user validation
		user = User.query.filter_by(email = email).first()

		if user:
			flash('this email already exists', category = 'error') 
		elif len(firstName) == 0 and len(lastName) == 0 and len(email) == 0 and len(password) == 0:
			flash('fill the form', category = 'error')
		elif len(firstName) < 2 and len(lastName) < 2:
			flash('Your first or last name is too short', category = 'error')
		elif len(email) < 4:
			flash('Your email must be greater than 4 characters', category = 'error')
		elif len(password) < 7:
			flash('Your password is too short', category = 'error')
		elif password != confirmPassword:
			flash('Passwords don\'t match.', category = 'error')
		else:
			#add user to database
			newUser = User(email = email, firstName = firstName, password = generate_password_hash(password, method = 'sha256'))
			db.session.add(newUser)
			db.session.commit()
			flash('Account created!', category = 'succes')
			return redirect(url_for('views.home'))

	return render_template("signUp.html")