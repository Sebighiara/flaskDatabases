from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
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
		if len(firstName) == 0 and len(lastName) == 0 and len(email) == 0 and len(password) == 0:
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
			flash('Account created!', category = 'succes')
			#add user to database
	return render_template("signUp.html")