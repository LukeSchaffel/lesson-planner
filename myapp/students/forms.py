from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Post')