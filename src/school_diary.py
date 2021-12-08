from src.student import Student
from src.checks.checks_school_diary import check_firstname, check_lastname, check_age, check_student_id, \
    check_subject_id, check_remark_id, check_grade_id
from src.checks.checks_school_subject import check_grade, check_subject_name
from src.student import check_remark_text
import csv


class SchoolDiary:

    def __init__(self, students=None):
        if students is None:
            students = []
        self.students = []
        for i in students:
            if 'subjects' in i and 'remarks' in i:
                self.students.append(Student(i['firstname'], i['lastname'], i['age'], i['subjects'], i['remarks']))
            elif 'subjects' in i:
                self.students.append(Student(i['firstname'], i['lastname'], i['age'], i['subjects']))
            elif 'remarks' in i:
                self.students.append(Student(i['firstname'], i['lastname'], i['age'], None, i['remarks']))
            else:
                self.students.append(Student(i['firstname'], i['lastname'], i['age']))

    def add_student(self, firstname, lastname, age):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c=None
        """
        if check_firstname(firstname) and check_lastname(lastname) and check_age(age):
            student = Student(firstname, lastname, age)
            self.students.append(student)
            result = []
            for i in self.students:
                result.append(i.get_details())
            return result

    def show_students(self):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.show_students()
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c=None
        """
        result = []
        for i in self.students:
            result.append(i.get_details())
        return result

    def edit_student(self, student_id, firstname=None, lastname=None, age=None):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.edit_student(2,'Paweł','Pawłowski',10)
        {'firstname': 'Paweł', 'lastname': 'Pawłowski', 'age': 10}
        >>> c.edit_student(1,age=17)
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 17}
        >>> c.edit_student(1,firstname='Kamil')
        {'firstname': 'Kamil', 'lastname': 'Kowalski', 'age': 17}
        >>> c=None
        """
        if check_student_id(student_id, self):
            temp = {
                'firstname': None,
                'lastname': None,
                'age': None
            }
            if isinstance(firstname, str):
                temp['firstname'] = firstname
            elif firstname is not None:
                raise TypeError('Błedny typ danych w imieniu')
            if isinstance(lastname, str):
                temp['lastname'] = lastname
            elif lastname is not None:
                raise TypeError('Błedny typ danych w nazwisku')
            if isinstance(age, int) and str(age) != 'True' and str(age) != 'False' and 0 < age:
                temp['age'] = age
            elif age is not None:
                raise TypeError('Błedny typ danych w wieku')
            return self.students[student_id - 1].edit_student(temp['firstname'], temp['lastname'], temp['age'])

    def delete_student(self, student_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.delete_student(2)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.delete_student(1)
        []
        >>> c=None
        """
        if check_student_id(student_id, self):
            self.students.pop(student_id - 1)
            result = []
            for i in self.students:
                result.append(i.get_details())
            return result

    def add_subject_to_student(self, student_id, name):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c=None
        """
        if check_student_id(student_id, self) and check_subject_name(name):
            return self.students[student_id - 1].add_subject(name)

    def get_subjects_from_student(self, student_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.get_subjects_from_student(1)
        ['Matematyka', 'Fizyka']
        >>> c.get_subjects_from_student(2)
        []
        >>> c=None
        """
        if check_student_id(student_id, self):
            return self.students[student_id - 1].get_subjects()

    def edit_subject_in_student(self, student_id, subject_id, name):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.edit_subject_in_student(1,1,'Angielski')
        ['Angielski', 'Fizyka']
        >>> c.edit_subject_in_student(1,2,'Chemia')
        ['Angielski', 'Chemia']
        >>> c=None
        """
        if check_student_id(student_id, self) and check_subject_id(student_id, subject_id, self) and check_subject_name(
                name):
            return self.students[student_id - 1].edit_subject(subject_id, name)

    def delete_subject_in_student(self, student_id, subject_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.delete_subject_in_student(1,1)
        ['Fizyka']
        >>> c.delete_subject_in_student(1,1)
        []
        >>> c=None
        """
        if check_student_id(student_id, self) and check_subject_id(student_id, subject_id, self):
            return self.students[student_id - 1].delete_subject(subject_id)

    def add_grade_in_student_in_subject(self, student_id, subject_id, grade):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.add_grade_in_student_in_subject(1,1,3)
        {'Matematyka': [3], 'Fizyka': []}
        >>> c.add_grade_in_student_in_subject(1,1,6)
        {'Matematyka': [3, 6], 'Fizyka': []}
        >>> c=None
        """
        if check_student_id(student_id, self) and check_subject_id(student_id, subject_id, self) and check_grade(grade):
            return self.students[student_id - 1].add_grade(subject_id, grade)

    def get_grades_in_student_from_subject(self, student_id, subject_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.add_grade_in_student_in_subject(1,1,3)
        {'Matematyka': [3], 'Fizyka': []}
        >>> c.add_grade_in_student_in_subject(1,1,6)
        {'Matematyka': [3, 6], 'Fizyka': []}
        >>> c.get_grades_in_student_from_subject(1,1)
        [3, 6]
        >>> c.get_grades_in_student_from_subject(1,2)
        []
        >>> c=None
        """
        if check_student_id(student_id, self) and check_subject_id(student_id, subject_id, self):
            return self.students[student_id - 1].get_grades(subject_id)

    def edit_grade_in_student_in_subject(self, student_id, subject_id, grade_id, grade):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.add_grade_in_student_in_subject(1,1,3)
        {'Matematyka': [3], 'Fizyka': []}
        >>> c.add_grade_in_student_in_subject(1,1,6)
        {'Matematyka': [3, 6], 'Fizyka': []}
        >>> c.edit_grade_in_student_in_subject(1,1,1,1)
        [1, 6]
        >>> c.edit_grade_in_student_in_subject(1,1,2,4)
        [1, 4]
        >>> c=None
        """
        if check_student_id(student_id, self) and check_grade_id(student_id, subject_id, grade_id,
                                                                 self) and check_grade(grade):
            return self.students[student_id - 1].edit_grade(subject_id, grade_id, grade)

    def delete_grade_in_student_in_subject(self, student_id, subject_id, grade_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.add_grade_in_student_in_subject(1,1,3)
        {'Matematyka': [3], 'Fizyka': []}
        >>> c.add_grade_in_student_in_subject(1,1,6)
        {'Matematyka': [3, 6], 'Fizyka': []}
        >>> c.delete_grade_in_student_in_subject(1,1,2)
        [3]
        >>> c.delete_grade_in_student_in_subject(1,1,1)
        []
        >>> c=None
        """
        if check_student_id(student_id, self) and check_subject_id(student_id, subject_id, self) and check_grade_id(
                student_id, subject_id, grade_id, self):
            return self.students[student_id - 1].delete_grade(subject_id, grade_id)

    def average_of_subject_in_student(self, student_id, subject_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.add_grade_in_student_in_subject(1,1,3)
        {'Matematyka': [3], 'Fizyka': []}
        >>> c.add_grade_in_student_in_subject(1,1,6)
        {'Matematyka': [3, 6], 'Fizyka': []}
        >>> c.average_of_subject_in_student(1,1)
        4.5
        >>> c.average_of_subject_in_student(1,2)
        0
        >>> c=None
        """
        if check_student_id(student_id, self) and check_subject_id(student_id, subject_id, self):
            return self.students[student_id - 1].average_of_subject(subject_id)

    def average_of_student(self, student_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_subject_to_student(1,'Matematyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka']}
        >>> c.add_subject_to_student(1,'Fizyka')
        {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12, 'subjects': ['Matematyka', 'Fizyka']}
        >>> c.add_grade_in_student_in_subject(1,1,3)
        {'Matematyka': [3], 'Fizyka': []}
        >>> c.add_grade_in_student_in_subject(1,1,6)
        {'Matematyka': [3, 6], 'Fizyka': []}
        >>> c.add_grade_in_student_in_subject(1,2,5)
        {'Matematyka': [3, 6], 'Fizyka': [5]}
        >>> c.average_of_student(1)
        4.5
        >>> c=None
        """
        if check_student_id(student_id, self):
            return self.students[student_id - 1].average_of_student()

    def add_remark_to_student(self, student_id, text):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_remark_to_student(1,'Uwaga 1')
        ['Uwaga 1']
        >>> c.add_remark_to_student(1,'Uwaga 2')
        ['Uwaga 1', 'Uwaga 2']
        >>> c=None
        """
        if check_student_id(student_id, self) and check_remark_text(text):
            return self.students[student_id - 1].add_remark(text)

    def get_remarks_from_student(self, student_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_remark_to_student(1,'Uwaga 1')
        ['Uwaga 1']
        >>> c.add_remark_to_student(1,'Uwaga 2')
        ['Uwaga 1', 'Uwaga 2']
        >>> c.get_remarks_from_student(1)
        ['Uwaga 1', 'Uwaga 2']
        >>> c.get_remarks_from_student(2)
        []
        >>> c=None
        """
        if check_student_id(student_id, self):
            return self.students[student_id - 1].get_remarks()

    def edit_remark_in_student(self, student_id, remark_id, text):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_remark_to_student(1,'Uwaga 1')
        ['Uwaga 1']
        >>> c.add_remark_to_student(1,'Uwaga 2')
        ['Uwaga 1', 'Uwaga 2']
        >>> c.edit_remark_in_student(1,1,'Uwaga 1 po edycji')
        ['Uwaga 1 po edycji', 'Uwaga 2']
        >>> c=None
        """
        if check_student_id(student_id, self) and check_remark_id(student_id, remark_id, self) and check_remark_text(
                text):
            return self.students[student_id - 1].edit_remark(remark_id, text)

    def delete_remark_in_student(self, student_id, remark_id):
        """
        >>> c=SchoolDiary()
        >>> c.add_student('Jan','Kowalski',12)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}]
        >>> c.add_student('Ola','Kot',8)
        [{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}, {'firstname': 'Ola', 'lastname': 'Kot', 'age': 8}]
        >>> c.add_remark_to_student(1,'Uwaga 1')
        ['Uwaga 1']
        >>> c.add_remark_to_student(1,'Uwaga 2')
        ['Uwaga 1', 'Uwaga 2']
        >>> c.delete_remark_in_student(1,2)
        ['Uwaga 1']
        >>> c.delete_remark_in_student(1,1)
        []
        >>> c=None
        """
        if check_student_id(student_id, self) and check_remark_id(student_id, remark_id, self):
            return self.students[student_id - 1].delete_remark(remark_id)

    def export_data_to_csv(self):
        data = []
        for i in range(len(self.show_students())):
            data.append({
                'Imie': self.show_students()[i]['firstname'],
                'Nazwisko': self.show_students()[i]['lastname'],
                'Wiek': self.show_students()[i]['age']
            })
            subjects_with_grades = []
            subjects = self.get_subjects_from_student(i + 1)
            for j in range(len(subjects)):
                grades = self.get_grades_in_student_from_subject(i + 1, j + 1)
                subjects_with_grades.append({
                    'Przedmiot': subjects[j],
                    'Oceny': grades
                })
            data[i]['Przedmioty z ocenami'] = subjects_with_grades
            data[i]['Średnia ucznia'] = self.average_of_student(i + 1)
            data[i]['Uwagi'] = self.get_remarks_from_student(i + 1)
        with open('poExporcie.csv', mode='w') as file:
            fieldnames = ['Imie', 'Nazwisko', 'Wiek', 'Przedmioty z ocenami', 'Średnia ucznia', 'Uwagi']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in data:
                writer.writerow(i)
        return 'Wyeksportowano dane'

    def import_data_from_csv(self):
        a_csv_file = open("poExporcie.csv", "r")
        dict_reader = csv.DictReader(a_csv_file)
        dict_from_csv = []
        for i in list(dict_reader):
            dict_from_csv.append(dict(i))
        for i in range(len(dict_from_csv)):
            self.add_student(dict_from_csv[i]['Imie'], dict_from_csv[i]['Nazwisko'], int(dict_from_csv[i]['Wiek']))
            for j in range(len(eval(dict_from_csv[i]['Przedmioty z ocenami']))):
                self.add_subject_to_student(i + 1, eval(dict_from_csv[i]['Przedmioty z ocenami'])[j]['Przedmiot'])
                for k in range(len(eval(dict_from_csv[i]['Przedmioty z ocenami'])[j]['Oceny'])):
                    self.add_grade_in_student_in_subject(i + 1, j + 1,
                                                         eval(dict_from_csv[i]['Przedmioty z ocenami'])[j]['Oceny'][k])
            for m in range(len(eval(dict_from_csv[i]['Uwagi']))):
                self.add_remark_to_student(i + 1, eval(dict_from_csv[i]['Uwagi'])[m])
        return 'Zaimportowano dane'


if __name__ == "__main__":
    import doctest

    # doctest.testmod()
    doctest.testmod(extraglobs={'c': SchoolDiary()})

# Testy eksportowania danych
# dziennik = SchoolDiary()
# dziennik.add_student('Jan', 'Kowalski', 12)
# dziennik.add_subject_to_student(1, 'Matematyka')
# dziennik.add_subject_to_student(1, 'Polski')
# dziennik.add_grade_in_student_in_subject(1, 1, 1)
# dziennik.add_grade_in_student_in_subject(1, 1, 3)
# dziennik.add_grade_in_student_in_subject(1, 1, 5)
# dziennik.add_grade_in_student_in_subject(1, 2, 4)
# dziennik.add_grade_in_student_in_subject(1, 2, 2)
# dziennik.add_remark_to_student(1, 'Uwaga 1')
# dziennik.add_remark_to_student(1, 'Uwaga 2')
# dziennik.add_student('Ola', 'Kot', 8)
# dziennik.add_subject_to_student(2, 'Matematyka')
# dziennik.add_grade_in_student_in_subject(2, 1, 2)
# dziennik.add_grade_in_student_in_subject(2, 1, 2)
# dziennik.add_remark_to_student(2, 'Uwaga 1')
# print(dziennik.export_data_to_csv())

# Testy importowania danych
# dziennik = SchoolDiary()
# print(dziennik.import_data_from_csv())
# print(dziennik.show_students())
# print(dziennik.get_subjects_from_student(1))
# print(dziennik.get_remarks_from_student(1))
# print(dziennik.get_grades_in_student_from_subject(2, 1))
