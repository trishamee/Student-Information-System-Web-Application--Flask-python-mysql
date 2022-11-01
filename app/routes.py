# from flask import Blueprint, render_template, request, flash, jsonify
# from flask_login import login_required, current_user
# from .models import Note
# from . import db
# import json

#gikan sa flask demo:
from flask import Blueprint,render_template, redirect, request, jsonify
from app.forms import StudentForm, CourseForm, CollegeForm
import app.model as model

#from . import user_bp
# import app.models as models
# from app.user.forms import UserForm

routes = Blueprint('routes', __name__)
@routes.route('/', methods=['GET', 'POST'])
def dashboard():
    return render_template("index.html")


# @login_required
# def home():
#     if request.method == 'POST':
#         note = request.form.get('note')

#         if len(note) < 1:
#             flash('Note is too short!', category='error')
#         else:
#             new_note = Note(data=note, user_id=current_user.id)
#             db.session.add(new_note)
#             db.session.commit()
#             flash('Note added!', category='success')

#     return render_template("home.html", user=current_user)


#Student
@routes.route('/students', methods=[ 'GET', 'POST'])
def stud_list():
    students = model.student.all()
    return render_template('students.html', data = students)

@routes.route('/students/add-student', methods=['GET', 'POST'])
def stud_add():
    available_courses = []
    for element in model.course.all():
        available_courses.append(element[0])
    form = StudentForm()
    form.course_code.choices = available_courses
    if form.validate():
        student = model.student(id= form.id.data, name = form.name.data, course_code = form.course_code.data,  year  =form.year.data, gender = form.gender.data)
        student.add()
        return redirect('/students')
    return render_template('add-student.html', form = form)

@routes.route('/students/edit-student/<id>', methods=['GET', 'POST'])
def stud_edit(id):
    form = StudentForm()
    details = model.student.open(id)
    available_courses = []
    for element in model.course.all():
        available_courses.append(element[0])
    form.course_code.choices = available_courses
    if request.method == 'GET':
        form.id.data = details[0][0]
        form.name.data = details[0][1]
        form.course_code.data = details[0][2]
        form.year.data = details[0][3]
        form.gender.data = details[0][4]
        return render_template('edit-student.html', form = form)
    elif request.method == 'POST' and form.validate():
        student = model.student( name = form.name.data, course_code = form.course_code.data,  year  =form.year.data, gender = form.gender.data)
        student.edit(id)
        return redirect('/students')

@routes.route('/students/student-details/<id>', methods=['GET', 'POST'])
def stud_open(id):
    details = model.student.open(id)
    return render_template('student-details.html', data = details)

#Courses
@routes.route('/courses', methods=['GET', 'POST'])
def course_list():
    courses = model.course.all()
    return render_template('course.html' , data = courses)

@routes.route('/courses/add-course', methods=['GET', 'POST'])
def course_add():
    available_colleges = []
    for element in model.college.all():
        available_colleges.append(element[0])
    form = CourseForm()
    form.college_code.choices = available_colleges
    if form.validate():
        course = model.course(course_code= form.course_code.data, course_name = form.course_name.data, college_code = form.college_code.data)
        course.add()
        return redirect('/courses')
    return render_template('add-course.html', form = form)

@routes.route('/courses/edit-course/<id>', methods=['GET', 'POST'])
def course_edit(id):
    form = CourseForm()
    details = model.course.open(id)
    available_colleges = []
    for element in model.college.all():
        available_colleges.append(element[0])
    form.college_code.choices = available_colleges
    if request.method == 'GET':
        form.course_code.data = details[0][0]
        form.course_name.data = details[0][1]
        form.college_code.data = details[0][2]
        return render_template('edit-course.html', form = form)
    elif request.method == 'POST' and form.validate():
        course = model.course( course_name = form.course_name.data, college_code = form.college_code.data)
        course.edit(id)
        return redirect('/courses')

@routes.route('/courses/course-details/<id>', methods=['GET', 'POST'])
def course_open(id):
    details = model.course.open(id)
    return render_template('course-details.html', data = details)

#Colleges
@routes.route('/colleges', methods=['GET', 'POST'])
def college_list():
    colleges = model.college.all()
    return render_template('college.html' , data = colleges)

@routes.route('/colleges/add-college', methods=['GET', 'POST'])
def college_add():
    form = CollegeForm()
    if form.validate():
        college = model.college(college_code= form.college_code.data, college_name= form.college_name.data)
        college.add()
        return redirect('/colleges')
    return render_template('add-college.html', form = form)

@routes.route('/colleges/edit-college/<id>', methods=['GET', 'POST'])
def college_edit(id):
    form = CollegeForm()
    details = model.college.open(id)
    if request.method == 'GET':
        form.college_code.data = details[0][0]
        form.college_name.data = details[0][1]
        return render_template('edit-college.html', form = form)
    elif request.method == 'POST' and form.validate():
        college = model.college( college_name = form.college_name.data)
        college.edit(id)
        return redirect('/colleges')

@routes.route('/colleges/college-details/<id>', methods=['GET', 'POST'])
def college_open(id):
    details = model.college.open(id)
    return render_template('college-details.html', data = details)
