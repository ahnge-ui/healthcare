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
        patient_id=request.form['patient_id'],
        diagnosis=request.form['diagnosis'],
        treatment=request.form['treatment'],
        record_date=request.form['record_date']
    )

    db.session.add(new_record)
    db.session.commit()

    return redirect('/medical_records')