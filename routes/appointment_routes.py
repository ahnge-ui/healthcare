from flask import Blueprint, render_template, request, redirect
from extensions import db
from models import Appointment, Patient

appointments = Blueprint('appointments', __name__)

# LIST APPOINTMENTS
@appointments.route('/appointments')
def appointment_list():
    data = Appointment.query.all()
    patients = Patient.query.all()
    return render_template('appointments.html', appointments=data, patients=patients)


# ADD APPOINTMENT
@appointments.route('/add_appointment', methods=['POST'])
def add_appointment():
    patient_id = request.form.get('patient_id')
    patient = Patient.query.get(patient_id)
    
    new_appointment = Appointment(
        patient_name=patient.fullname if patient else '',
        appointment_date=request.form['appointment_date'],
        doctor=request.form['doctor'],
        status=request.form['status']
    )

    db.session.add(new_appointment)
    db.session.commit()

    return redirect('/appointments')


# DELETE APPOINTMENT
@appointments.route('/delete_appointment/<int:id>')
def delete_appointment(id):

    appointment = Appointment.query.get(id)

    if appointment:
        db.session.delete(appointment)
        db.session.commit()

    return redirect('/appointments')


# SEARCH APPOINTMENTS
@appointments.route('/search_appointments', methods=['GET'])
def search_appointments():
    query = request.args.get('query', '')
    if query:
        data = Appointment.query.filter(Appointment.patient_name.ilike(f'%{query}%')).all()
    else:
        data = Appointment.query.all()
    patients = Patient.query.all()
    return render_template('appointments.html', appointments=data, patients=patients, search_query=query)