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