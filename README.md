# Student-Information-System-Web-Application--Flask-python-mysql

Please run create_db.py before running Flask. Thank you (づ ◕‿◕ )づ

Project requirements:
Web version of Simple Student Information System

Tables:
(1) student
  - id  format: YYYY-NNNN
  - firstname
  - lastname
  - course => refers to course table
  - year
  - gender
  
(2) course
  - code  e.g. BSCS
  - name e.g. Bachelor of Science in Computer Science
  -college => refers to college table

(3) college
  - code e.g. CCS
  - name e.g. College of Computer Studies

CRUDL for student, course, college
use MySQL

Search by fields
