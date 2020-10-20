class Student:
    def __init__(self, student_id, grade, eval_grade):
        self.student_id = student_id
        self.grade = grade
        self.eval_grade = eval_grade

    def __eq__(self, other):
        return other.student_id == self.student_id
