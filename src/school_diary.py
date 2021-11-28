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

    def show_students(self):
        result = []
        for i in self.students:
            result.append(i.get_details())
        return result

    def edit_student(self, id, firstname=None, lastname=None, age=None):
        if check_id(id, self):
            temp = {
                'firstname': None,
                'lastname': None,
                'age': None
            }
            if isinstance(firstname, str):
                temp['firstname'] = firstname
            elif firstname != None:
                raise Exception('Błedny typ danych w imieniu')
            if isinstance(lastname, str):
                temp['lastname'] = lastname
            elif lastname != None:
                raise Exception('Błedny typ danych w nazwisku')
            if isinstance(age, int) and str(age) != 'True' and str(age) != 'False' and 0 < age:
                temp['age'] = age
            elif age != None:
                raise Exception('Błedny typ danych w wieku')
            return self.students[id - 1].edit_student(temp['firstname'], temp['lastname'], temp['age'])

    def delete_student(self, id):
        if check_id(id, self):
            self.students.pop(id - 1)
            result = []
            for i in self.students:
                result.append(i.get_details())
            return result

    def add_subject_to_student(self, id, name):
        if check_id(id, self):
            if check_subject_name(name):
                return self.students[id - 1].add_subject(name)

    def get_subjects_from_student(self, id):
        if check_id(id, self):
            return self.students[id - 1].get_subjects()
