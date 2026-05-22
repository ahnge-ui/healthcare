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


# DELETE STAFF
@staff.route('/delete_staff/<int:id>')
def delete_staff(id):

    staff_member = Staff.query.get(id)

    if staff_member:
        db.session.delete(staff_member)
        db.session.commit()

    return redirect('/staff')


# SEARCH STAFF
@staff.route('/search_staff', methods=['GET'])
def search_staff():
    query = request.args.get('query', '')
    if query:
        data = Staff.query.filter(Staff.fullname.ilike(f'%{query}%')).all()
    else:
        data = Staff.query.all()
    return render_template('staff.html', staff=data, search_query=query)