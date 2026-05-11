from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(20))


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    contact = db.Column(db.String(20))
    address = db.Column(db.Text)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer)
    appointment_date = db.Column(db.String(20))
    doctor = db.Column(db.String(100))
    status = db.Column(db.String(50))


class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer)
    diagnosis = db.Column(db.Text)
    treatment = db.Column(db.Text)
    record_date = db.Column(db.String(20))


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    position = db.Column(db.String(100))
    contact = db.Column(db.String(20))
    email = db.Column(db.String(100))