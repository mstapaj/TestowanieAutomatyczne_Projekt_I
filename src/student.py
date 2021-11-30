from src.checks.checks_student import check_subject_id, check_grade_id
from src.checks.checks_school_subject import check_grade,check_subject_name
from src.school_subject import SchoolSubject


class Student:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.subjects = []

    def get_details(self):
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'age': self.age
        }

    def edit_student(self, firstname=None, lastname=None, age=None):
        if isinstance(firstname, str):
            self.firstname = firstname
        elif firstname != None:
            raise Exception('Błedny typ danych w imieniu')
        if isinstance(lastname, str):
            self.lastname = lastname
        elif lastname != None:
            raise Exception('Błedny typ danych w nazwisku')
        if isinstance(age, int) and str(age) != 'True' and str(age) != 'False' and 0 < age:
            self.age = age
        elif age != None:
            raise Exception('Błedny typ danych w wieku')
        return {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'age': self.age
        }

    def add_subject(self, subject):
        if check_subject_name(subject):
            temp = SchoolSubject(subject)
            self.subjects.append(temp)
            result = []
            for i in self.subjects:
                result.append(i.get_details()['name'])
            return {
                'firstname': self.firstname,
                'lastname': self.lastname,
                'age': self.age,
                'subjects': result
            }

    def get_subjects(self):
        result = []
        for i in self.subjects:
            result.append(i.get_details()['name'])
        return result

    def edit_subject(self, subject_id, name):
        if check_subject_id(subject_id, self):
            if check_subject_name(name):
                self.subjects[subject_id - 1].edit_subject(name)
                result = []
                for i in self.subjects:
                    result.append(i.get_details()['name'])
                return result

    def delete_subject(self, subject_id):
        if check_subject_id(subject_id, self):
            self.subjects.pop(subject_id - 1)
            result = []
            for i in self.subjects:
                result.append(i.get_details()['name'])
            return result

    def add_grade(self, subject_id, grade):
        if check_subject_id(subject_id, self):
            if check_grade(grade):
                self.subjects[subject_id - 1].add_grade(grade)
                result = {}
                for i in self.subjects:
                    temp = i.get_details()
                    result[temp['name']] = temp['grades']
                return result

    def get_grades(self, subject_id):
        if check_subject_id(subject_id, self):
            return self.subjects[subject_id - 1].get_details()['grades']

    def edit_grade(self, subject_id, grade_id, grade):
        if check_subject_id(subject_id, self):
            if check_grade_id(subject_id, grade_id, self):
                if check_grade(grade):
                    return self.subjects[subject_id - 1].edit_grade(grade_id, grade)['grades']

    def delete_grade(self, subject_id, grade_id):
        if check_subject_id(subject_id, self):
            if check_grade_id(subject_id, grade_id, self):
                return self.subjects[subject_id - 1].delete_grade(grade_id)['grades']

    def average_of_subject(self, subject_id):
        if check_subject_id(subject_id, self):
            return self.subjects[subject_id - 1].average_of_subject()

    def average_of_student(self):
        summary = 0
        for i in self.subjects:
            avg = i.average_of_subject()
            if 0 <= avg < 1.51:
                summary += 1
            elif 1.51 <= avg < 2.51:
                summary += 2
            elif 2.51 <= avg < 3.51:
                summary += 3
            elif 3.51 <= avg < 4.51:
                summary += 4
            elif 4.51 <= avg < 5.51:
                summary += 5
            elif 5.51 <= avg <= 6:
                summary += 6
            else:
                raise Exception('Średnia nie jest z przedziału 0-6')
        return round(summary / len(self.subjects), 2)
