from flask import Flask
from flask import request
from flask import jsonify
from TeamsByStudents import get_teams_by_students

app = Flask(__name__)


@app.route('/teams/')
def teams_by_students_route():
    students = request.json
    return jsonify(get_teams_by_students(students))
