from app import mysql

class student(object):

    def __init__(self, id = None, firstname = None, lastname = None, course_code = None, year = None, gender =None, prof_url = None ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.course_code = course_code
        self.year = year
        self.gender = gender
        self.prof_url = prof_url

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO student(id, firstname, lastname, course_code, year, gender, prof_url) \
                VALUES('{self.id}','{self.firstname}','{self.lastname}','{self.course_code}', '{self.year}', '{self.gender}', '{self.prof_url}')" 
        cursor.execute(sql)
        mysql.connection.commit()

    def edit(self, id):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE student SET firstname='{self.firstname}', lastname = '{self.lastname}', course_code ='{self.course_code}', year = '{self.year}' , gender ='{self.gender}', prof_url = '{self.prof_url}' WHERE id='{id}' " 
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def open(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from student where id = '{id}' "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT student.id, student.firstname, student.lastname, courses.course_name, student.year, student.gender, student.prof_url FROM student INNER JOIN courses ON student.course_code = courses.course_code"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls,id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from student where id= '{id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False

class college(object):
    
    def __init__(self, college_code= None, college_name = None):
        self.college_code = college_code
        self.college_name = college_name

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO colleges(college_code, college_name) \
                VALUES('{self.college_code}','{self.college_name}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    def edit(self, id):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE colleges SET college_name='{self.college_name}' WHERE college_code='{id}'" 
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def open(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from colleges where college_code = '{id}' "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from colleges where college_code != 'None'"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls,id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from colleges where college_code= '{id}'"
            cursor.execute(sql)
            sql = f"Update courses set college_code = 'None' where college_code = '{id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            
            return True
        except:
            return False

class course(object):

    def __init__(self, course_code = None, course_name = None, college_code = None):
        self.course_code = course_code
        self.course_name = course_name
        self.college_code = college_code

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO courses(course_code, course_name, college_code) \
                VALUES('{self.course_code}','{self.course_name}','{self.college_code}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    def edit(self, id):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE courses SET course_name='{self.course_name}', college_code = '{self.college_code}' WHERE course_code='{id}'"
        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def open(cls, id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * from courses where course_code = '{id}' "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT courses.course_code, courses.course_name, colleges.college_name FROM courses INNER JOIN colleges on courses.college_code = colleges.college_code where course_code != 'None' "
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
        

    @classmethod
    def delete(cls,id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from courses where course_code= '{id}' "
            cursor.execute(sql)
            sql = f"Update student set course_code = 'None' where course_code = '{id}'"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False