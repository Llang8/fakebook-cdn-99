from . import bp as app
from app.blueprints.main.models import User
from app import db
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    # Otherwise, attempt to login the user
    email = request.form['inputEmail']
    password = request.form['inputPassword']

    user = User.query.filter_by(email=email).first()

    # There was not a user with the input email
    # There was a user, but the password was incorrect
    # There was a user, and the password was correct

    if user is None:
        print('There was not a user with that email.')
    elif user.password != password:
        print('The password was incorrect.')
    else:
        print('Logged in successfully')
        login_user(user)
        return redirect(url_for('main.home'))

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    email = request.form['inputEmail']
    username = request.form['inputUsername']
    first_name = request.form['inputFirstName']
    last_name = request.form['inputLastName']
    password = request.form['inputPassword']
    confirm_password = request.form['inputPasswordConfirm']

    # A user with this email already exists
    # A user with this email does not exist, but the passwords do not match
    # A user with this email does not exist, and the passwords match - REGISTER THE USER
    check_user = User.query.filter_by(email=email).first()

    if check_user is not None:
        print('A user with this email already exists.')

    elif password != confirm_password:
        print('The passwords do not match')

    else:
        # REGISTER USER
        new_user = User(email=email, username=username, first_name=first_name, last_name=last_name, password=password)
        db.session.add(new_user)
        db.session.commit()
        print('User registered successfully')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))