import bisect


class Team:
    def __init__(self):
        self.students_list = []

    def __eq__(self, other):
        return other.students_list == self.students_list

    def add_student(self, new_student):
        bisect.insort(self.students_list, new_student)

    def remove_student(self, student_to_remove):
        self.students_list.remove(student_to_remove)

    def remove_student(self):
        return self.students_list.pop()

    def get_average_grades(self):
        grades_list = [student.grade for student in self.students_list]
        return sum(grades_list) / len(self.students_list)

    def get_average_eval_grades(self):
        grades_list = [student.eval_grade for student in self.students_list]
        return sum(grades_list) / len(self.students_list)

    def crossover(self, another_team):
        # TODO
        return None

    def distance_from_average(self, average):
        # TODO
        return None
