from Typing import List
from ..Models.Student import Student

def calculate_average_grades(students: List[Student]) -> float:
    return sum(students, key = lambda studnet: studnet.grade) / len(students)