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
    form = StudentForm()
    if form.validate():
        student = model.student(id= form.id.data, name = form.name.data, course_code = form.course_code.data,  year  =form.year.data, gender = form.gender.data)
        student.add()
        return redirect('/')
    return render_template('add-student.html', form = form)

@routes.route('/students/edit-student', methods=['GET', 'POST'])
def stud_edit():
    return render_template('edit-student.html')

@routes.route('/students/student-details', methods=['GET', 'POST'])
def stud_open():
    return render_template('student-details.html')

#Courses
@routes.route('/courses', methods=['GET', 'POST'])
def course_list():
    courses = model.course.all()
    return render_template('course.html' , data = courses)

@routes.route('/courses/add-course', methods=['GET', 'POST'])
def course_add():
    form = CourseForm()
    if form.validate():
        course = model.course(course_code= form.course_code.data, course_name = form.course_name.data, college_code = form.college_code.data)
        course.add()
        return redirect('/')
    return render_template('add-course.html', form = form)

@routes.route('/courses/edit-course', methods=['GET', 'POST'])
def course_edit():
    return render_template('edit-course.html')

@routes.route('/courses/course-details', methods=['GET', 'POST'])
def course_open():
    return render_template('course-details.html')


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
        return redirect('/')
    return render_template('add-college.html', form = form)
    
@routes.route('/colleges/edit-college', methods=['GET', 'POST'])
def college_edit():
    return render_template('edit-college.html')

@routes.route('/colleges/college-details', methods=['GET', 'POST'])
def college_open():
    return render_template('college-details.html')
