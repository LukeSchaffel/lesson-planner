from cgi import print_arguments
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
        return redirect(url_for('users.lessons', username=current_user.username))
    return render_template('create_lesson.html', form=form)

@lessons.route('/<int:lesson_id>/delete',methods=['GET','POST'])
@login_required
def delete_lesson(lesson_id):

    lesson = Lesson.query.get_or_404(lesson_id)
    if lesson.author != current_user:
        abort(403)

    db.session.delete(lesson)
    db.session.commit()
    flash('Lesson Deleted')
    return redirect(url_for('users.lessons', username=current_user.username))    

@lessons.route('/<int:lesson_id>')
def lesson(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id) 
    return render_template('lesson.html', title=lesson.title, student=lesson.student, lessonDate=lesson.lessonDate, content=lesson.content, subject=lesson.subject, date=lesson.date, lesson=lesson)    

@lessons.route('/<int:lesson_id>/update',methods=['GET','POST'])
@login_required
def update(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)

    if lesson.author != current_user:
        abort(403)

    form = LessonForm()

    if form.validate_on_submit():
        lesson.lessonDate = form.lessonDate.data
        lesson.title = form.title.data
        lesson.subject = form.subject.data
        lesson.content = form.content.data
        lesson.student = form.student.data
        db.session.commit()
        flash('Lesson Updated')
        return redirect(url_for('lessons.lesson',lesson_id=lesson.id))

    elif request.method == 'GET':
        form.lessonDate.data = lesson.lessonDate
        form.title.data = lesson.title
        form.subject.data = lesson.subject
        form.content.data = lesson.content
        form.content.data = lesson.content
        form.student.data = lesson.student
        

    return render_template('create_lesson.html',title='Updating',form=form)

@lessons.route('/')
def lessons(student):
  page = request.args.get('page', 1, type=int)
  lessons = Lesson.query.filter_by(student=student).order_by(Lesson.lessonDate.desc()).paginate(page=page, per_page=5) 
  return render_template('student.html', lessons=lessons)