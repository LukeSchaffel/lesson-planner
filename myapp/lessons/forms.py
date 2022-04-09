from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired

class LessonForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    date_of_lesson = StringField('Date', validators=[DataRequired()])
    subject = TextAreaField('Subject', validators=[DataRequired()])
    submit = SubmitField('Post')