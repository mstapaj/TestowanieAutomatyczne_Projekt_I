import unittest
from hamcrest import *
from src.student import Student


class test_Student(unittest.TestCase):
    def setUp(self):
        self.temp = Student('Jan', 'Kowalski', 12)
        self.temp_with_subjects = Student('Paweł', 'Pawłowski', 15)
        self.temp_with_subjects.add_subject('Matematyka')
        self.temp_with_subjects.add_subject('Polski')
        self.temp_with_grades = Student('Paweł', 'Pawłowski', 15)
        self.temp_with_grades.add_subject('Matematyka')
        self.temp_with_grades.add_subject('Polski')
        self.temp_with_grades.add_grade(1, 2)
        self.temp_with_grades.add_grade(1, 5)
        self.temp_with_grades.add_grade(2, 2)
        self.temp_with_remarks = Student('Paweł', 'Pawłowski', 15)
        self.temp_with_remarks.add_remark('Uwaga 1')
        self.temp_with_remarks.add_remark('Uwaga 2')

    # Testy get_details
    def test_get_details(self):
        assert_that(self.temp.get_details(), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12
        }))

    # Testy edit_student
    def test_edit_student(self):
        assert_that(self.temp.edit_student('Marcin', 'Nowak', 10), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Nowak',
            'age': 10
        }))

    def test_edit_student_without_age(self):
        assert_that(self.temp.edit_student('Marcin', 'Nowak'), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Nowak',
            'age': 12
        }))

    def test_edit_student_without_lastname(self):
        assert_that(self.temp.edit_student('Marcin', age=10), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Kowalski',
            'age': 10
        }))

    def test_edit_student_without_firstname(self):
        assert_that(self.temp.edit_student(lastname='Nowak', age=10), equal_to({
            'firstname': 'Jan',
            'lastname': 'Nowak',
            'age': 10
        }))

    def test_edit_student_without_firstname_lastname(self):
        assert_that(self.temp.edit_student(age=10), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 10
        }))

    def test_edit_student_without_firstname_age(self):
        assert_that(self.temp.edit_student(lastname='Nowak'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Nowak',
            'age': 12
        }))

    def test_edit_student_without_lastname_age(self):
        assert_that(self.temp.edit_student(firstname='Marcin'), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Kowalski',
            'age': 12
        }))

    def test_edit_student_firstname_object(self):
        assert_that(calling(self.temp.edit_student).with_args({}, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_array(self):
        assert_that(calling(self.temp.edit_student).with_args([], 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_true(self):
        assert_that(calling(self.temp.edit_student).with_args(True, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_false(self):
        assert_that(calling(self.temp.edit_student).with_args(False, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_int(self):
        assert_that(calling(self.temp.edit_student).with_args(12, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_float(self):
        assert_that(calling(self.temp.edit_student).with_args(3.14, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_int_negative(self):
        assert_that(calling(self.temp.edit_student).with_args(-12, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_float_negative(self):
        assert_that(calling(self.temp.edit_student).with_args(-2.56, 'Nowak', 10), raises(Exception))

    def test_edit_student_lastname_object(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', {}, 10), raises(Exception))

    def test_edit_student_lastname_array(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', [], 10), raises(Exception))

    def test_edit_student_lastname_true(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', True, 10), raises(Exception))

    def test_edit_student_lastname_false(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', False, 10), raises(Exception))

    def test_edit_student_lastname_int(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 31, 10), raises(Exception))

    def test_edit_student_lastname_float(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 2.13, 10), raises(Exception))

    def test_edit_student_lastname_int_negative(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', -12, 10), raises(Exception))

    def test_edit_student_lastname_float_negative(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', -2.45, 10), raises(Exception))

    def test_edit_student_age_object(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', {}), raises(Exception))

    def test_edit_student_age_array(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', []), raises(Exception))

    def test_edit_student_age_true(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', True), raises(Exception))

    def test_edit_student_age_false(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', False), raises(Exception))

    def test_edit_student_age_string(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', 'abc'), raises(Exception))

    def test_edit_student_age_string_number(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', '23'), raises(Exception))

    def test_edit_student_age_int_negative(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', -2), raises(Exception))

    def test_edit_student_age_float_negative(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', -1.0), raises(Exception))

    def test_edit_student_age_zero(self):
        assert_that(calling(self.temp.edit_student).with_args('Marcin', 'Nowak', 0), raises(Exception))

    # Testy add_subject
    def test_add_subject(self):
        assert_that(self.temp.add_subject('Polski'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12,
            'subjects': ['Polski']
        }))

    def test_add_subject_2(self):
        assert_that(self.temp.add_subject('Matematyka'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12,
            'subjects': ['Matematyka']
        }))
        assert_that(self.temp.add_subject('Polski'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12,
            'subjects': ['Matematyka', 'Polski']
        }))

    def test_add_subject_none(self):
        assert_that(calling(self.temp.add_subject).with_args(None), raises(Exception))

    def test_add_subject_object(self):
        assert_that(calling(self.temp.add_subject).with_args({}), raises(Exception))

    def test_add_subject_array(self):
        assert_that(calling(self.temp.add_subject).with_args([]), raises(Exception))

    def test_add_subject_true(self):
        assert_that(calling(self.temp.add_subject).with_args(True), raises(Exception))

    def test_add_subject_false(self):
        assert_that(calling(self.temp.add_subject).with_args(False), raises(Exception))

    def test_add_subject_int(self):
        assert_that(calling(self.temp.add_subject).with_args(12), raises(Exception))

    def test_add_subject_float(self):
        assert_that(calling(self.temp.add_subject).with_args(3.12), raises(Exception))

    def test_add_subject_negative_int(self):
        assert_that(calling(self.temp.add_subject).with_args(-8), raises(Exception))

    def test_add_subject_negative_float(self):
        assert_that(calling(self.temp.add_subject).with_args(-1.23), raises(Exception))

    # Testy get_subjects
    def test_get_subjects(self):
        assert_that(self.temp_with_subjects.get_subjects(), equal_to(['Matematyka', 'Polski']))

    # Testy edit_subject
    def test_edit_subject(self):
        assert_that(self.temp_with_subjects.edit_subject(1, 'Angielski'), equal_to(['Angielski', 'Polski']))

    def test_edit_subject_2(self):
        assert_that(self.temp_with_subjects.edit_subject(2, 'Fizyka'), equal_to(['Matematyka', 'Fizyka']))

    def test_edit_subject_none_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(None, 'Fizyka'), raises(Exception))

    def test_edit_subject_none_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, None), raises(Exception))

    def test_edit_subject_none(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(None, None), raises(Exception))

    def test_edit_subject_object_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args({}, 'Fizyka'), raises(Exception))

    def test_edit_subject_object_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, {}), raises(Exception))

    def test_edit_subject_object(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args({}, {}), raises(Exception))

    def test_edit_subject_array_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args([], 'Fizyka'), raises(Exception))

    def test_edit_subject_array_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, []), raises(Exception))

    def test_edit_subject_array(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args([], []), raises(Exception))

    def test_edit_subject_true_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(True, 'Fizyka'), raises(Exception))

    def test_edit_subject_true_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, True), raises(Exception))

    def test_edit_subject_true(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(True, True), raises(Exception))

    def test_edit_subject_false_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(False, 'Fizyka'), raises(Exception))

    def test_edit_subject_false_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, False), raises(Exception))

    def test_edit_subject_false(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(False, False), raises(Exception))

    def test_edit_subject_string_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args('abc', 'Fizyka'), raises(Exception))

    def test_edit_subject_string_number_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args('3', 'Fizyka'), raises(Exception))

    def test_edit_subject_int_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, 2), raises(Exception))

    def test_edit_subject_string_subject_id_int_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args('32a', 5), raises(Exception))

    def test_edit_subject_float_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(2.15, 'Fizyka'), raises(Exception))

    def test_edit_subject_float_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, 3.87), raises(Exception))

    def test_edit_subject_float(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1.32, 4.12), raises(Exception))

    def test_edit_subject_negative_int_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(-3, 'Fizyka'), raises(Exception))

    def test_edit_subject_negative_int_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, -1), raises(Exception))

    def test_edit_subject_negative_int(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(-2, -9), raises(Exception))

    def test_edit_subject_negative_float_subject_id(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(-3.12, 'Fizyka'), raises(Exception))

    def test_edit_subject_negative_float_name(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(1, -1.55), raises(Exception))

    def test_edit_subject_negative_float(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(-2.12, -9.65), raises(Exception))

    def test_edit_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(0, 'Fizyka'), raises(Exception))

    def test_edit_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.edit_subject).with_args(5, 'Fizyka'), raises(Exception))

    # Testy delete_subject
    def test_delete_subject(self):
        assert_that(self.temp_with_subjects.delete_subject(1), equal_to(['Polski']))

    def test_delete_subject_2(self):
        assert_that(self.temp_with_subjects.delete_subject(2), equal_to(['Matematyka']))

    def test_delete_subject_3(self):
        assert_that(self.temp_with_subjects.delete_subject(2), equal_to(['Matematyka']))
        assert_that(self.temp_with_subjects.delete_subject(1), equal_to([]))

    def test_delete_subject_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args(0), raises(Exception))

    def test_delete_subject_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args(3), raises(Exception))

    def test_delete_subject_none(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args(None), raises(Exception))

    def test_delete_subject_object(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args({}), raises(Exception))

    def test_delete_subject_array(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args([]), raises(Exception))

    def test_delete_subject_true(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args(True), raises(Exception))

    def test_delete_subject_false(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args(False), raises(Exception))

    def test_delete_subject_string(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args('abc'), raises(Exception))

    def test_delete_subject_string_number(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args('2'), raises(Exception))

    def test_delete_subject_float(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args(2.15), raises(Exception))

    def test_delete_subject_negative_int(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args(-3), raises(Exception))

    def test_delete_subject_negative_float(self):
        assert_that(calling(self.temp_with_subjects.delete_subject).with_args(-3.45), raises(Exception))

    # Testy add_grade

    def test_add_grade(self):
        assert_that(self.temp_with_subjects.add_grade(1, 4), equal_to({
            'Matematyka': [4],
            'Polski': []
        }))

    def test_add_grade_2(self):
        assert_that(self.temp_with_subjects.add_grade(2, 3), equal_to({
            'Matematyka': [],
            'Polski': [3]
        }))

    def test_add_grade_3(self):
        assert_that(self.temp_with_subjects.add_grade(2, 3), equal_to({
            'Matematyka': [],
            'Polski': [3]
        }))
        assert_that(self.temp_with_subjects.add_grade(1, 5), equal_to({
            'Matematyka': [5],
            'Polski': [3]
        }))

    def test_add_grade_4(self):
        assert_that(self.temp_with_subjects.add_grade(2, 3), equal_to({
            'Matematyka': [],
            'Polski': [3]
        }))
        assert_that(self.temp_with_subjects.add_grade(2, 5), equal_to({
            'Matematyka': [],
            'Polski': [3, 5]
        }))

    def test_add_grade_id_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(0, 4), raises(Exception))

    def test_add_grade_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(6, 4), raises(Exception))

    def test_add_grade_grade_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, -2), raises(Exception))

    def test_add_grade_grade_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, 8), raises(Exception))

    def test_add_grade_none_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(None, 3), raises(Exception))

    def test_add_grade_none_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, None), raises(Exception))

    def test_add_grade_none(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(None, None), raises(Exception))

    def test_add_grade_object_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args({}, 3), raises(Exception))

    def test_add_grade_object_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, {}), raises(Exception))

    def test_add_grade_object(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args({}, {}), raises(Exception))

    def test_add_grade_true_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(True, 3), raises(Exception))

    def test_add_grade_true_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, True), raises(Exception))

    def test_add_grade_true(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(True, True), raises(Exception))

    def test_add_grade_false_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(False, 3), raises(Exception))

    def test_add_grade_false_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, False), raises(Exception))

    def test_add_grade_false(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(False, False), raises(Exception))

    def test_add_grade_string_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args('abc', 3), raises(Exception))

    def test_add_grade_string_number_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args('2', 3), raises(Exception))

    def test_add_grade_string_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(2, 'abc'), raises(Exception))

    def test_add_grade_string_number_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(2, '3'), raises(Exception))

    def test_add_grade_string(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args('b2', '3a'), raises(Exception))

    def test_add_grade_float_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(2.31, 3), raises(Exception))

    def test_add_grade_float_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, 1.67), raises(Exception))

    def test_add_grade_float(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(3.12, 4.33), raises(Exception))

    def test_add_grade_negative_int_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(-3, 3), raises(Exception))

    def test_add_grade_negative_int_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, -8), raises(Exception))

    def test_add_grade_negative_int(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(-2, -5), raises(Exception))

    def test_add_grade_negative_float_id(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(-2.31, 3), raises(Exception))

    def test_add_grade_negative_float_grade(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(1, -1.67), raises(Exception))

    def test_add_grade_negative_float(self):
        assert_that(calling(self.temp_with_subjects.add_grade).with_args(-3.12, -4.33), raises(Exception))

    # Testy get_grades
    def test_get_grades(self):
        assert_that(self.temp_with_grades.get_grades(1), equal_to([2, 5]))

    def test_get_grades_2(self):
        assert_that(self.temp_with_grades.get_grades(2), equal_to([2]))

    def test_get_grades_id_out_of_range(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args(-1), raises(Exception))

    def test_get_grades_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args(4), raises(Exception))

    def test_get_grades_none(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args(None), raises(Exception))

    def test_get_grades_object(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args({}), raises(Exception))

    def test_get_grades_array(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args([]), raises(Exception))

    def test_get_grades_true(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args(True), raises(Exception))

    def test_get_grades_false(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args(False), raises(Exception))

    def test_get_grades_string(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args('abc'), raises(Exception))

    def test_get_grades_string_number(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args('12'), raises(Exception))

    def test_get_grades_float(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args(2.12), raises(Exception))

    def test_get_grades_negative_int(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args(-4), raises(Exception))

    def test_get_grades_negative_float(self):
        assert_that(calling(self.temp_with_grades.get_grades).with_args(-4.22), raises(Exception))

    # Testy edit_grade
    def test_edit_grade(self):
        assert_that(self.temp_with_grades.edit_grade(1, 1, 6), equal_to([6, 5]))

    def test_edit_grade_2(self):
        assert_that(self.temp_with_grades.edit_grade(2, 1, 1), equal_to([1]))

    def test_edit_grade_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(0, 1, 4), raises(Exception))

    def test_edit_grade_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(6, 1, 4), raises(Exception))

    def test_edit_grade_id_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 0, 4), raises(Exception))

    def test_edit_grade_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 4, 4), raises(Exception))

    def test_edit_grade_grade_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, -2), raises(Exception))

    def test_edit_grade_grade_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, 8), raises(Exception))

    def test_edit_grade_subject_id_none(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(None, 1, 4), raises(Exception))

    def test_edit_grade_subject_id_object(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args({}, 1, 4), raises(Exception))

    def test_edit_grade_subject_id_array(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args([], 1, 4), raises(Exception))

    def test_edit_grade_subject_id_true(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(True, 1, 4), raises(Exception))

    def test_edit_grade_subject_id_false(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(False, 1, 4), raises(Exception))

    def test_edit_grade_subject_id_string(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args('abc', 1, 4), raises(Exception))

    def test_edit_grade_subject_id_string_number(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args('3', 1, 4), raises(Exception))

    def test_edit_grade_subject_id_float(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(2.31, 1, 4), raises(Exception))

    def test_edit_grade_subject_id_negative_int(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(-3, 1, 4), raises(Exception))

    def test_edit_grade_subject_id_negative_float(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(-2.16, 1, 4), raises(Exception))

    def test_edit_grade_grade_id_none(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, None, 4), raises(Exception))

    def test_edit_grade_grade_id_object(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, {}, 4), raises(Exception))

    def test_edit_grade_grade_id_array(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, [], 4), raises(Exception))

    def test_edit_grade_grade_id_true(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, True, 4), raises(Exception))

    def test_edit_grade_grade_id_false(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, False, 4), raises(Exception))

    def test_edit_grade_grade_id_string(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 'abc', 4), raises(Exception))

    def test_edit_grade_grade_id_string_number(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, '3', 4), raises(Exception))

    def test_edit_grade_grade_id_float(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 2.31, 4), raises(Exception))

    def test_edit_grade_grade_id_negative_int(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, -1, 4), raises(Exception))

    def test_edit_grade_grade_id_negative_float(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, -2.16, 4), raises(Exception))

    def test_edit_grade_grade_none(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, None), raises(Exception))

    def test_edit_grade_grade_object(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, {}), raises(Exception))

    def test_edit_grade_grade_array(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, []), raises(Exception))

    def test_edit_grade_grade_true(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, True), raises(Exception))

    def test_edit_grade_grade_false(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, False), raises(Exception))

    def test_edit_grade_grade_string(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, 'abc'), raises(Exception))

    def test_edit_grade_grade_string_number(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, '3'), raises(Exception))

    def test_edit_grade_grade_float(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, 2.31), raises(Exception))

    def test_edit_grade_grade_negative_int(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, -1), raises(Exception))

    def test_edit_grade_grade_negative_float(self):
        assert_that(calling(self.temp_with_subjects.edit_grade).with_args(1, 1, -2.16), raises(Exception))

    # Testy delete_grade
    def test_delete_grade(self):
        assert_that(self.temp_with_grades.delete_grade(1, 1), equal_to([5]))

    def test_delete_grade_2(self):
        assert_that(self.temp_with_grades.delete_grade(2, 1), equal_to([]))

    def test_delete_grade_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(0, 1), raises(Exception))

    def test_delete_grade_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(6, 1), raises(Exception))

    def test_delete_grade_id_out_of_range(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, 0), raises(Exception))

    def test_delete_grade_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, 4), raises(Exception))

    def test_delete_grade_none_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(None, 1), raises(Exception))

    def test_delete_grade_none_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, None), raises(Exception))

    def test_delete_grade_none(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(None, None), raises(Exception))

    def test_delete_grade_object_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args({}, 1), raises(Exception))

    def test_delete_grade_object_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, {}), raises(Exception))

    def test_delete_grade_object(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args({}, {}), raises(Exception))

    def test_delete_grade_true_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(True, 1), raises(Exception))

    def test_delete_grade_true_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, True), raises(Exception))

    def test_delete_grade_true(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(True, True), raises(Exception))

    def test_delete_grade_false_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(False, 1), raises(Exception))

    def test_delete_grade_false_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, False), raises(Exception))

    def test_delete_grade_false(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(False, False), raises(Exception))

    def test_delete_grade_string_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args('abc', 1), raises(Exception))

    def test_delete_grade_string_number_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args('2', 1), raises(Exception))

    def test_delete_grade_string_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(2, 'abc'), raises(Exception))

    def test_delete_grade_string_number_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(2, '3'), raises(Exception))

    def test_delete_grade_string(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args('b2', '3a'), raises(Exception))

    def test_delete_grade_float_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(2.31, 1), raises(Exception))

    def test_delete_grade_float_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, 1.67), raises(Exception))

    def test_delete_grade_float(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(3.12, 4.33), raises(Exception))

    def test_delete_grade_negative_int_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(-3, 1), raises(Exception))

    def test_delete_grade_negative_int_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, -8), raises(Exception))

    def test_delete_grade_negative_int(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(-2, -5), raises(Exception))

    def test_delete_grade_negative_float_subject_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(-2.31, 1), raises(Exception))

    def test_delete_grade_negative_float_grade_id(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(1, -1.67), raises(Exception))

    def test_delete_grade_negative_float(self):
        assert_that(calling(self.temp_with_subjects.delete_grade).with_args(-3.12, -4.33), raises(Exception))

    # Testy average_of_subject
    def test_average_of_subject(self):
        assert_that(self.temp_with_grades.average_of_subject(1), equal_to(3.5))

    def test_average_of_subject_2(self):
        assert_that(self.temp_with_grades.average_of_subject(2), equal_to(2))

    def test_average_of_subject_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args(-1), raises(Exception))

    def test_average_of_subject_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args(4), raises(Exception))

    def test_average_of_subject_none(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args(None), raises(Exception))

    def test_average_of_subject_object(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args({}), raises(Exception))

    def test_average_of_subject_array(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args([]), raises(Exception))

    def test_average_of_subject_true(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args(True), raises(Exception))

    def test_average_of_subject_false(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args(False), raises(Exception))

    def test_average_of_subject_string(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args('abc'), raises(Exception))

    def test_average_of_subject_string_number(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args('12'), raises(Exception))

    def test_average_of_subject_float(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args(2.12), raises(Exception))

    def test_average_of_subject_negative_int(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args(-4), raises(Exception))

    def test_average_of_subject_negative_float(self):
        assert_that(calling(self.temp_with_grades.average_of_subject).with_args(-4.22), raises(Exception))

    # Testy average_of_student
    def test_average_of_student(self):
        assert_that(self.temp_with_grades.average_of_student(), equal_to(2.5))

    def test_average_of_student_2(self):
        assert_that(self.temp_with_subjects.average_of_student(), equal_to(1.0))

    # Testy add_remark
    def test_add_remark(self):
        assert_that(self.temp.add_remark('Uwaga'), equal_to(['Uwaga']))

    def test_add_remark_2(self):
        self.temp.add_remark('Uwaga 1')
        assert_that(self.temp.add_remark('Uwaga 2'), equal_to(['Uwaga 1', 'Uwaga 2']))

    def test_add_remark_none(self):
        assert_that(calling(self.temp.add_remark).with_args(None), raises(Exception))

    def test_add_remark_object(self):
        assert_that(calling(self.temp.add_remark).with_args({}), raises(Exception))

    def test_add_remark_array(self):
        assert_that(calling(self.temp.add_remark).with_args([]), raises(Exception))

    def test_add_remark_true(self):
        assert_that(calling(self.temp.add_remark).with_args(True), raises(Exception))

    def test_add_remark_false(self):
        assert_that(calling(self.temp.add_remark).with_args(False), raises(Exception))

    def test_add_remark_int(self):
        assert_that(calling(self.temp.add_remark).with_args(12), raises(Exception))

    def test_add_remark_float(self):
        assert_that(calling(self.temp.add_remark).with_args(2.98), raises(Exception))

    def test_add_remark_negative_int(self):
        assert_that(calling(self.temp.add_remark).with_args(-9), raises(Exception))

    def test_add_remark_negative_float(self):
        assert_that(calling(self.temp.add_remark).with_args(-8.123), raises(Exception))

    # Testy get_remarks
    def test_get_remarks(self):
        assert_that(self.temp_with_remarks.get_remarks(), equal_to(['Uwaga 1', 'Uwaga 2']))

    def tearDown(self):
        self.temp = None
        self.temp_with_subjects = None
        self.temp_with_grades = None
        self.temp_with_remarks = None
