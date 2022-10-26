from app import mysql

class student(object):

    def __init__(self, id = None, name = None, course_code = None, year = None, gender =None ):
        self.id = id
        self.name = name
        self.course_code = course_code
        self.year = year
        self.gender = gender

    def add(self):
        cursor = mysql.connection.cursor()
        sql = f"INSERT INTO student(id, name, course_code, year, gender) \
                VALUES('{self.id}','{self.name}','{self.course_code}', '{self.year}', '{self.gender}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    def edit(self, id):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE student SET name=%s, course_code = %s, year = %s , gender = %s WHERE id=%s \
                VALUES('{self.name}','{self.course_code}', '{self.year}', '{self.gender}', {self.id}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls,id):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from student where id= {id}"
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
                VALUES('{self.collge_code}','{self.college_name}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    def edit(self, college_code):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE colleges SET college_name=%s WHERE college_code=%s \
                VALUES('{self.college_name}','{self.college_code}')" 

        cursor.execute(sql)
        mysql.connection.commit()

    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()

        sql = "SELECT * from colleges"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls,college_code):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from colleges where college_code= {college_code}"
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

    def edit(self, course_code):
        cursor = mysql.connection.cursor()
        sql = f"UPDATE courses SET course_name=%s, college_code = %s WHERE id=%s \
                VALUES('{self.course_name}','{self.college_code}', {self.course_code}')" 

        cursor.execute(sql)
        mysql.connection.commit()
    
    @classmethod
    def all(cls):
        cursor = mysql.connection.cursor()
        sql = "SELECT * from courses"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    @classmethod
    def delete(cls,course_code):
        try:
            cursor = mysql.connection.cursor()
            sql = f"DELETE from courses where course_code= {course_code}"
            cursor.execute(sql)
            mysql.connection.commit()
            return True
        except:
            return False