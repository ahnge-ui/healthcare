from flask import Blueprint, render_template, request, redirect
from extensions import db
from models import Appointment

appointments = Blueprint('appointments', __name__)

# LIST APPOINTMENTS
@appointments.route('/appointments')
def appointment_list():
    data = Appointment.query.all()
    return render_template('appointments.html', appointments=data)


# ADD APPOINTMENT
@appointments.route('/add_appointment', methods=['POST'])
def add_appointment():

    new_appointment = Appointment(
        patient_id=request.form['patient_id'],
        appointment_date=request.form['appointment_date'],
        doctor=request.form['doctor'],
        status=request.form['status']
    )

    db.session.add(new_appointment)
    db.session.commit()

    return redirect('/appointments')