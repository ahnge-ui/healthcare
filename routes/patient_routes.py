from flask import Blueprint, render_template, request, redirect
from extensions import db
from models import Patient

patients = Blueprint('patients', __name__)

@patients.route('/patients')
def patient_list():
    data = Patient.query.all()
    return render_template('patients.html', patients=data)


@patients.route('/add_patient', methods=['POST'])
def add_patient():

    new_patient = Patient(
        fullname=request.form['fullname'],
        age=request.form['age'],
        gender=request.form['gender'],
        contact=request.form['contact'],
        address=request.form['address']
    )

    db.session.add(new_patient)
    db.session.commit()

    return redirect('/patients')


@patients.route('/delete_patient/<int:id>')
def delete_patient(id):

    patient = Patient.query.get(id)

    if patient:
        db.session.delete(patient)
        db.session.commit()

    return redirect('/patients')


# SEARCH PATIENTS
@patients.route('/search_patients', methods=['GET'])
def search_patients():
    query = request.args.get('query', '')
    if query:
        data = Patient.query.filter(Patient.fullname.ilike(f'%{query}%')).all()
    else:
        data = Patient.query.all()
    return render_template('patients.html', patients=data, search_query=query)