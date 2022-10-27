from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, SelectField, RadioField    


class StudentForm(FlaskForm):
    id = StringField ('ID Number', [validators.DataRequired(), validators.Length(min=9, max=9)])
    name = StringField('Name', [validators.DataRequired(), validators.Length(min=3)])
#change course options later
    course_code = SelectField('Course', [validators.DataRequired()])
    year = SelectField('Year', [validators.DataRequired()], choices = ['1','2','3','4','5','Irregular'])
    gender = RadioField('Gender', [validators.DataRequired()], choices = ['Female', 'Male'])
    submit = SubmitField("Submit")


class CourseForm(FlaskForm):
    course_code = StringField ('Course Code', [validators.DataRequired()])
    course_name = StringField('Course Name', [validators.DataRequired()])
#change course options later
    college_code = SelectField('College Code', [validators.DataRequired()])
    submit = SubmitField("Submit")

class CollegeForm(FlaskForm):
    college_code = StringField ('College Code', [validators.DataRequired()])
    college_name = StringField('College Name', [validators.DataRequired()])
    submit = SubmitField("Submit")