import unittest
from hamcrest import *
from src.student import Student

class test_Student(unittest.TestCase):
    def setUp(self):
        self.temp = Student('Jan', 'Kowalski', 12)

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