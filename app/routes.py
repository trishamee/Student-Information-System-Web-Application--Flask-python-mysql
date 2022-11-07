
from flask import Blueprint,render_template, redirect, request, flash, jsonify
from app.forms import StudentForm, CourseForm, CollegeForm
import app.model as model


routes = Blueprint('routes', __name__)

#Dashboard
@routes.route('/', methods=['GET', 'POST'])
def dashboard():
    students = model.student.all()
    student_num = len(students)
    courses = model.course.all()    
    course_num = len(courses)
    colleges = model.college.all()    
    college_num = len(colleges)
    return render_template("index.html", title = 'Dashboard' , stud_num = student_num, course_num = course_num, college_num = college_num )

#Student
@routes.route('/students', methods=[ 'GET', 'POST'])
def stud_list():
    students = model.student.all()
    return render_template('students.html', data = students, title = 'Students')

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
        flash('Student info has been added!')
        return redirect('/students')
    return render_template('add-student.html', form = form, title = 'Add Student')

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
        return render_template('edit-student.html', form = form ,title = 'Edit Student')
    elif request.method == 'POST' and form.validate():
        student = model.student( name = form.name.data, course_code = form.course_code.data,  year  =form.year.data, gender = form.gender.data)
        student.edit(id)
        flash('Student info has been updated!')
        return redirect('/students')

@routes.route('/students/student-details/<id>', methods=['GET', 'POST'])
def stud_open(id):
    details = model.student.open(id)
    return render_template('student-details.html', data = details, title = 'Student Details')

@routes.route('/students/delete/ <id>', methods=['GET','POST'])
def stud_delete(id):
    model.student.delete(id)
    flash('Student has been deleted!')
    return redirect('/students')
   
#Courses
@routes.route('/courses', methods=['GET', 'POST'])
def course_list():
    courses = model.course.all()
    return render_template('course.html' , data = courses, title = 'Courses')

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
        flash('Course has been added!')
        return redirect('/courses')
    return render_template('add-course.html', form = form, title = 'Add Course')

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
        return render_template('edit-course.html', form = form, title = 'Edit Course')
    elif request.method == 'POST' and form.validate():
        course = model.course( course_name = form.course_name.data, college_code = form.college_code.data)
        course.edit(id)
        flash('Course has been updated!')
        return redirect('/courses')

@routes.route('/courses/course-details/<id>', methods=['GET', 'POST'])
def course_open(id):
    details = model.course.open(id)
    return render_template('course-details.html', data = details, title = 'Course Details')

@routes.route('/courses/delete/ <id>', methods=['GET','POST'])
def course_delete(id):
    model.course.delete(id)
    flash('Course has been deleted!')
    return redirect('/courses')


#Colleges
@routes.route('/colleges', methods=['GET', 'POST'])
def college_list():
    colleges = model.college.all()
    return render_template('college.html' , data = colleges, title = 'Colleges')

@routes.route('/colleges/add-college', methods=['GET', 'POST'])
def college_add():
    form = CollegeForm()
    if form.validate():
        college = model.college(college_code= form.college_code.data, college_name= form.college_name.data)
        college.add()
        flash('College has been added!')
        return redirect('/colleges')
    return render_template('add-college.html', form = form, title = 'Add College')

@routes.route('/colleges/edit-college/<id>', methods=['GET', 'POST'])
def college_edit(id):
    form = CollegeForm()
    details = model.college.open(id)
    if request.method == 'GET':
        form.college_code.data = details[0][0]
        form.college_name.data = details[0][1]
        return render_template('edit-college.html', form = form, title = 'Edit College')
    elif request.method == 'POST' and form.validate():
        college = model.college( college_name = form.college_name.data)
        college.edit(id)
        flash('College has been updated!')
        return redirect('/colleges')

@routes.route('/colleges/college-details/<id>', methods=['GET', 'POST'])
def college_open(id):
    details = model.college.open(id)
    return render_template('college-details.html', data = details, title = 'College details')

@routes.route('/colleges/delete/ <id>', methods=['GET','POST'])
def college_delete(id):
    model.college.delete(id)
    flash('College has been deleted!')
    return redirect('/colleges')