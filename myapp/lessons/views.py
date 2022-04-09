from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Lesson
from myapp.lessons.forms import LessonForm
from myapp.models import User

lessons = Blueprint('lessons', __name__)

@lessons.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = LessonForm()
    if form.validate_on_submit():
        lesson = Lesson(date_of_lesson=form.date_of_lesson.data, title=form.title.data, subject=form.subject.data, content=form.content.data, user_id=current_user.id)
        db.session.add(lesson)
        db.session.commit()
        flash('Blog Post Created')
        print('Blog post was created')
        return redirect(url_for('core.index'))
    return render_template('create_lesson.html', form=form)