import mysql.connector 


#Create Database if it does not exist
mysqldb = mysql.connector.connect(host="localhost",user="root",password="Beleta000", port = '3306')
mycursor = mysqldb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS student_information")
mysqldb.close()

#Create table for courses
mysqldb = mysql.connector.connect(host="localhost",user="root",password="Beleta000", database = "student_information")
mycursor = mysqldb.cursor()
mycursor.execute("SHOW TABLES LIKE 'courses'")
result = mycursor.fetchone()
if result:
    # there is a table 
    pass
else:
     # there are no tables 
    mycursor.execute("CREATE TABLE courses(course_code VARCHAR(100) NOT NULL,course_name VARCHAR(100), college_code VARCHAR(100), PRIMARY KEY (course_code))")
    mycursor.execute("INSERT INTO courses(course_code, course_name, college_code) VALUES ('None', 'None', 'None')")
    mysqldb.commit()
    lastid = mycursor.lastrowid
mysqldb.close()

#Create table for students
mysqldb = mysql.connector.connect(host="localhost",user="root",password="Beleta000", database = "student_information")
mycursor = mysqldb.cursor()
mycursor.execute("SHOW TABLES LIKE 'student'")
result = mycursor.fetchone()
if result:
    # there is a table 
    pass
else:
     # there are no tables
    mycursor.execute("CREATE TABLE student(id CHAR(10) NOT NULL,name VARCHAR(100) NOT NULL, course_code VARCHAR(100) NOT NULL, year VARCHAR(10) NOT NULL, gender VARCHAR(10) NOT NULL , PRIMARY KEY (id))")
mysqldb.close()

#Create table for college
mysqldb = mysql.connector.connect(host="localhost",user="root",password="Beleta000", database = "student_information")
mycursor = mysqldb.cursor()
mycursor.execute("SHOW TABLES LIKE 'colleges'")
result = mycursor.fetchone()
if result:
    # there is a table 
    pass
else:
     # there are no tables 
    mycursor.execute("CREATE TABLE colleges(college_code VARCHAR(100) NOT NULL,college_name VARCHAR(100), PRIMARY KEY (college_code))")
    mycursor.execute("INSERT INTO colleges(college_code, college_name) VALUES ('None', 'None')")
    mysqldb.commit()
    lastid = mycursor.lastrowid
mysqldb.close()