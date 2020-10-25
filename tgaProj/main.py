from flask import Flask
from flask import request
from flask import jsonify
from .TeamsByStudents import get_teams_by_students
from .Models.Student import Student
from typing import List

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def stam():
    print('roy')
    return 'Hello, World'

@app.route('/teams', methods=['GET','POST'])
def teams_by_students_route():
    request_body = request.json
    students: List[Student] = []
    number_of_teams: int = request_body["team_length"]
    for student in students_sended["students"]:
        students.append(Student(student["id"], student["grade"], student["eval_grade"]))
    print(students)

    return "Thank you"
