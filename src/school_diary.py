from src.student import Student
from src.checks.checks_school_diary import check_firstname, check_lastname, check_age, check_id, check_grade_id, \
    check_subject_id, check_remark_id
from src.checks.checks_school_subject import check_grade, check_subject_name
from src.student import check_remark_text


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

    def edit_subject_in_student(self, id, subject_id, name):
        if check_id(id, self):
            if check_subject_id(id, subject_id, self):
                if check_subject_name(name):
                    return self.students[id - 1].edit_subject(subject_id, name)

    def delete_subject_in_student(self, id, subject_id):
        if check_id(id, self):
            if check_subject_id(id, subject_id, self):
                return self.students[id - 1].delete_subject(subject_id)

    def add_grade_in_student_in_subject(self, id, subject_id, grade):
        if check_id(id, self):
            if check_subject_id(id, subject_id, self):
                if check_grade(grade):
                    return self.students[id - 1].add_grade(subject_id, grade)

    def get_grades_in_student_from_subject(self, id, subject_id):
        if check_id(id, self):
            if check_subject_id(id, subject_id, self):
                return self.students[id - 1].get_grades(subject_id)

    def edit_grade_in_student_in_subject(self, id, subject_id, grade_id, grade):
        if check_id(id, self):
            if check_subject_id(id, subject_id, self):
                if check_grade_id(id, subject_id, grade_id, self):
                    if check_grade(grade):
                        return self.students[id - 1].edit_grade(subject_id, grade_id, grade)

    def delete_grade_in_student_in_subject(self, id, subject_id, grade_id):
        if check_id(id, self):
            if check_subject_id(id, subject_id, self):
                if check_grade_id(id, subject_id, grade_id, self):
                    return self.students[id - 1].delete_grade(subject_id, grade_id)

    def average_of_subject_in_student(self, id, subject_id):
        if check_id(id, self):
            if check_subject_id(id, subject_id, self):
                return self.students[id - 1].average_of_subject(subject_id)

    def average_of_student(self, id):
        if check_id(id, self):
            return self.students[id - 1].average_of_student()

    def add_remark_to_student(self, id, text):
        if check_id(id, self):
            if check_remark_text(text):
                return self.students[id - 1].add_remark(text)

    def get_remarks_from_student(self, id):
        if check_id(id, self):
            return self.students[id - 1].get_remarks()

    def edit_remark_in_student(self, id, remark_id, text):
        if check_id(id, self):
            if check_remark_id(id, remark_id, self):
                if check_remark_text(text):
                    return self.students[id - 1].edit_remark(remark_id, text)

    def delete_remark_in_student(self, id, remark_id):
        if check_id(id, self):
            if check_remark_id(id, remark_id, self):
                return self.students[id - 1].delete_remark(remark_id)