import mysql.connector 

mysqldb = mysql.connector.connect(host="localhost",user="root",password="Beleta000", database = "student_information")
mycursor = mysqldb.cursor()

# 7 Colleges
mycursor.execute("INSERT INTO colleges (college_code, college_name) VALUES ('COET' , 'College of Engineering Technology'), ('CSM', 'College of Science and Mathematics'), ('CCS', 'College of Computer Studies'), ('CED', 'College of Education'), ('CASS', 'College of Arts and Social Sciences'), ('CBAA', 'College of Business Administration and Accountancy'), ('CON', 'College of Nursing')")
mysqldb.commit()

#  15 Courses
mycursor.execute("INSERT INTO courses (course_code, course_name, college_code) VALUES ('BSChE', 'Bachelor of Science in Chemical Engineering', 'COET'), ('BSEnE', 'Bachelor of Science in Environmental Engineering','COET'), ('BSBio', 'Bachelor of Science in Biology', 'CSM'), ('BSMCB', 'Bachelor of Science in Microbiology', 'CSM'), ('BSCS', 'Bachelor of Science in Computer Science', 'CCS'), ('BSIS','Bachelor of Science in Information Science','CCS'), ('BSIT', 'Bachelor of Science in Information Technology', 'CCS'), ('BESM','Bachelor of Elementary Education Science and Mathematics','CED'), ('BSEP','Bachelor of Secondary Education Physics','CED'), ('BAELS', 'Bachelor of Arts in English Language Studies','CASS'), ('BAF','Bachelor of Arts in Filipino','CASS'), ('BSA','Bachelor of Science in Accountancy','CBAA'), ('BSHM','Bachelor of Science in Hospitality Management', 'CBAA'), ('BSN','Bachelor of Science in Nursing','CON'),('BSCA','Bachelor of Science in Computer Applications','CCS') ")
mysqldb.commit()

# 30 students
mycursor.execute("INSERT INTO student (id, firstname, lastname, course_code, year, gender, prof_url) VALUES ('2020-0000','Neveah','Herman','BSChe','3','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2021-0001', 'Bryanna', 'Vance','BSChe', '2','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2015-8755', 'Kaia', 'Whitney', 'BSEnE', 'Irregular', 'Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2019-7777', 'Salvador', 'Padilla', 'BSEnE', '4', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2018-5588','Branden','Hartman', 'BSBio', '5', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2022-1211','Gunnar','Hays', 'BSBio', '1','Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-1114', 'Dillon', 'Beltran', 'BSMCB', '3', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2021-3666', 'Cullen', 'Patel', 'BSMCB', '2','Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2019-6664', 'Genessis','Williamson','BSCS', '4','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-9877', 'Grant','Hopkins', 'BSCS', '4', 'Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2019-8777', 'Adrienne', 'Shea', 'BSIS', '4', 'Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-0081','Chase', 'Caldwell', 'BSIS', '3','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2019-3131', 'Pheonix','Atkins','BSIT','4','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2018-8455','Mariela', 'Fowler','BSIT', '5', 'Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-9112', 'Jovany','Martinez', 'BESM', '3', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-9633', 'Connor', 'Knox', 'BESM', '3', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2022-8002', 'Kira','Griffin','BSEP','1','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'),('2020-0123','Landen', 'Huff', 'BSEP', '3', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2015-0303', 'Reynaldo', 'Lin', 'BAELS', 'Irregular', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-1455', 'Carlee', 'Jenkins', 'BAELS', '3', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2019-3122', 'Whitney',' Ware', 'BAF', '4', 'Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-1411', 'Duncan', 'Landry', 'BAF', '3', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-7411', 'Isabela', 'Hart', 'BSA', '3','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2019-1032','Nola','Obrien','BSA', '4', 'Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-8711','Nayeli', 'Pratt', 'BSHM', '3','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'),('2022-2344', 'Jay',' Velasquez', 'BSHM', '1', 'Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-0122','Connie', 'Boone','BSN', '3', 'Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2019-3221','Emilio','Beck','BSN','4','Male', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2020-4003', 'Tyrese', 'Barrera', 'BSCA', '3', 'Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png'), ('2019-3322', 'Sofia', 'Waters', 'BSCA', '4','Female', 'https://res.cloudinary.com/dcmskf8xh/image/upload/v1668866976/SIS/no_profile_k2cffs.png')")
mysqldb.commit()

mysqldb.close()