from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Lesson, Student, User
from myapp.students.forms import StudentForm

students = Blueprint('students', __name__)

@students.route('/students/create', methods=['GET', 'POST'])
@login_required
def create_lesson():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(name=form.name.data, user_id=current_user.id)
        db.session.add(student)
        db.session.commit()
        flash('Student CREATED')
        print('Student CREATED')
        return redirect(url_for('core.index'))
    return render_template('create_student.html', form=form)