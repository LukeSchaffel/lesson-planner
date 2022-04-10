from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class LessonForm(FlaskForm):
    student = TextAreaField('Student', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    lessonDate = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    subject = TextAreaField('Subject', validators=[DataRequired()])
    submit = SubmitField('Post')