from flask import Blueprint, render_template, request, redirect
from extensions import db
from models import Staff

staff = Blueprint('staff', __name__)

# LIST STAFF
@staff.route('/staff')
def staff_list():
    data = Staff.query.all()
    return render_template('staff.html', staff=data)


# ADD STAFF
@staff.route('/add_staff', methods=['POST'])
def add_staff():

    new_staff = Staff(
        fullname=request.form['fullname'],
        position=request.form['position'],
        contact=request.form['contact'],
        email=request.form['email']
    )

    db.session.add(new_staff)
    db.session.commit()

    return redirect('/staff')