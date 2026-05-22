from flask import Blueprint, render_template, request, redirect
from extensions import db
from models import MedicalRecord

medical = Blueprint('medical', __name__)

# LIST RECORDS
@medical.route('/medical_records')
def medical_records():
    data = MedicalRecord.query.all()
    return render_template('medical_records.html', records=data)


# ADD RECORD
@medical.route('/add_record', methods=['POST'])
def add_record():

    new_record = MedicalRecord(
        patient_name=request.form['patient_name'],
        diagnosis=request.form['diagnosis'],
        treatment=request.form['treatment'],
        record_date=request.form['record_date']
    )

    db.session.add(new_record)
    db.session.commit()

    return redirect('/medical_records')


# DELETE RECORD
@medical.route('/delete_record/<int:id>')
def delete_record(id):

    record = MedicalRecord.query.get(id)

    if record:
        db.session.delete(record)
        db.session.commit()

    return redirect('/medical_records')


# SEARCH RECORDS
@medical.route('/search_records', methods=['GET'])
def search_records():
    query = request.args.get('query', '')
    if query:
        data = MedicalRecord.query.filter(MedicalRecord.patient_name.ilike(f'%{query}%')).all()
    else:
        data = MedicalRecord.query.all()
    return render_template('medical_records.html', records=data, search_query=query)