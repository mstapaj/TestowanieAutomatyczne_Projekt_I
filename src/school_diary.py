from src.student import Student
from src.checks.checks_school_diary import *


class SchoolDiary:

    def __init__(self):
        self.students = []

    def add_student(self, firstname, lastname, age):
        if check_firstname(firstname):
            if check_lastname(lastname):
                if check_age(age):
                    student = Student(firstname, lastname, age)
                    self.students.append(student)
                    result = []
                    for i in self.students:
                        result.append(i.get_details())
                    return result
