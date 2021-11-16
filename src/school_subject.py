from src.checks.checks_school_subject import *


class SchoolSubject:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def get_details(self):
        return {
            'name': self.name,
            'grades': self.grades
        }

    def edit_subject(self, name):
        if check_subject_name(name):
            self.name = name
            return {
                'name': self.name,
                'grades': self.grades
            }

    def add_grade(self, grade):
        if check_grade(grade):
            self.grades.append(grade)
            return {
                'name': self.name,
                'grades': self.grades
            }

    def edit_grade(self, grade_id, grade):
        if check_grade_id(grade_id, self):
            if check_grade(grade):
                self.grades[grade_id - 1] = grade
                return {
                    'name': self.name,
                    'grades': self.grades
                }

    def delete_grade(self, grade_id):
        if check_grade_id(grade_id, self):
            self.grades.pop(grade_id - 1)
            return {
                'name': self.name,
                'grades': self.grades
            }

    def average_of_subject(self):
        summary = 0
        for i in self.grades:
            summary += i
        if len(self.grades) <= 0:
            return 0
        else:
            return round(summary / len(self.grades), 2)
