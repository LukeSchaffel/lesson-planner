from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from myapp.models import Lesson, Student



class LessonForm(FlaskForm):
    # student = SelectField('Student', choices = [Student])
    student = StringField("Student")
    title = StringField('Title', validators=[DataRequired()])
    lessonDate = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    subject = TextAreaField('Subject', validators=[DataRequired()])
    submit = SubmitField('Post')