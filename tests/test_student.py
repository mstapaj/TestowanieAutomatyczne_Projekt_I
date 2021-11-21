import unittest
from hamcrest import *
from src.student import Student

class test_Student(unittest.TestCase):
    def setUp(self):
        self.temp = Student('Jan', 'Kowalski', 12)
        self.temp_with_subjects = Student('Paweł', 'Pawłowski', 15)
        self.temp_with_subjects.add_subject('Matematyka')
        self.temp_with_subjects.add_subject('Polski')

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
