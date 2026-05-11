from flask import Blueprint, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from models import User
from extensions import db

auth = Blueprint('auth', __name__)

# HOME = LOGIN PAGE
@auth.route('/')
def home():
    return render_template('index.html')


# LOGIN (FIXED: GET + POST)
@auth.route('/login', methods=['GET', 'POST'])
def login():

    # SHOW LOGIN PAGE
    if request.method == 'GET':
        return render_template('index.html')

    # PROCESS LOGIN
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session['user'] = user.fullname
        return redirect('/dashboard')

    return redirect('/')


# REGISTER (FIXED WITH ERROR HANDLING)
@auth.route('/register', methods=['GET', 'POST'])
def register():

    error = None

    if request.method == 'POST':
        fullname = request.form['fullname']
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        role = request.form['role']

        new_user = User(
            fullname=fullname,
            username=username,
            password=password,
            role=role
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')

        except IntegrityError:
            db.session.rollback()
            error = "You already have an account"

    return render_template('register.html', error=error)


# DASHBOARD
@auth.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    return render_template('dashboard.html')


# LOGOUT
@auth.route('/logout')
def logout():
    session.clear()
    return redirect('/')