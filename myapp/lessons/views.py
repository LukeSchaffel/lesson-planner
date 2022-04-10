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
        lesson = Lesson(lessonDate=form.lessonDate.data, title=form.title.data, subject=form.subject.data, content=form.content.data, user_id=current_user.id, student=form.student.data)
        db.session.add(lesson)
        db.session.commit()
        flash('Lesson CREATED')
        print('LESSON CREATED')
        return redirect(url_for('core.index'))
    return render_template('create_lesson.html', form=form)

@lessons.route('/<int:lesson_id>/delete',methods=['GET','POST'])
@login_required
def delete_lesson(lesson_id):

    lesson = Lesson.query.get_or_404(lesson_id)
    if lesson.author != current_user:
        abort(403)

    db.session.delete(lesson)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))    