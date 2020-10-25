from random import shuffle
from typing import List
from Team import Team

class ProjectFormation:
    def __init__(self):
        self.teams_list: List[Team] = []

    def generate_random(self, students_list, team_length):
        teams_amount = len(students_list) / team_length
        shuffled_students = shuffle(students_list)
        student_index = 0
        for team_index in range(teams_amount):
            curr_team = Team()
            for team_mate_index in range(teams_amount):
                curr_team.add_student(shuffled_students[student_index])
                student_index += 1
            self.teams_list.append(curr_team)

        remaining_students_amount = len(students_list) % team_length
        if remaining_students_amount != 0:
            if remaining_students_amount < team_length / 2:
                team_index = 0
                for remaining_index in range(remaining_students_amount):
                    self.teams_list[team_index].add_student(students_list[remaining_index])
                    team_index += 1
            else:
                curr_team = Team()
                for remaining_index in range(remaining_students_amount):
                    curr_team.add_student(students_list[remaining_index])
                for team_to_remove_from_index in range(team_length - remaining_students_amount):
                    curr_team.add_student(self.teams_list[team_to_remove_from_index].remove_student())
                self.teams_list.append(curr_team)

    def fitness(self) -> int:
        
        for team in self.teams_list:
            team.get_average_grades
