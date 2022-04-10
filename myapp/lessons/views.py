from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Lesson, Student
from myapp.lessons.forms import LessonForm
from myapp.models import User

lessons = Blueprint('lessons', __name__)

@lessons.route('/lessons/create', methods=['GET', 'POST'])
@login_required
def create_lesson():
    form = LessonForm()
    if form.validate_on_submit():
        lesson = Lesson(lessonDate=form.lessonDate.data, title=form.title.data, subject=form.subject.data, content=form.content.data, student=form.student.data, user_id=current_user.id)
        db.session.add(lesson)
        db.session.commit()
        flash('Lesson CREATED')
        print('LESSON CREATED')
        return redirect(url_for('core.index'))
    return render_template('create_lesson.html', form=form)