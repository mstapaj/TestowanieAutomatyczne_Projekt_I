import unittest
from hamcrest import *

from src.school_diary import SchoolDiary


class test_school_diary(unittest.TestCase):

    def setUp(self):
        self.temp = SchoolDiary()
        self.temp_with_students = SchoolDiary()
        self.temp_with_students.add_student('Jan', 'Kowalski', 12)
        self.temp_with_students.add_student('Ola', 'Kot', 17)

    # Testy add_student
    def test_add_student(self):
        assert_that(self.temp.add_student('Jan', 'Kowalski', 12), equal_to([
            {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}
        ]))

    def test_add_student_2(self):
        assert_that(self.temp.add_student('Ola', 'Kot', 17), equal_to([
            {'firstname': 'Ola', 'lastname': 'Kot', 'age': 17}
        ]))

    def test_add_student_3(self):
        assert_that(self.temp.add_student('Ola', 'Kot', 17), equal_to([
            {'firstname': 'Ola', 'lastname': 'Kot', 'age': 17}
        ]))
        assert_that(self.temp.add_student('Jan', 'Kowalski', 12), equal_to([
            {'firstname': 'Ola', 'lastname': 'Kot', 'age': 17},
            {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}
        ]))

    def test_add_student_firstname_object(self):
        assert_that(calling(self.temp.add_student).with_args({}, 'Nowak', 10), raises(Exception))

    def test_add_student_firstname_array(self):
        assert_that(calling(self.temp.add_student).with_args([], 'Nowak', 10), raises(Exception))

    def test_add_student_firstname_true(self):
        assert_that(calling(self.temp.add_student).with_args(True, 'Nowak', 10), raises(Exception))

    def test_add_student_firstname_false(self):
        assert_that(calling(self.temp.add_student).with_args(False, 'Nowak', 10), raises(Exception))

    def test_add_student_firstname_int(self):
        assert_that(calling(self.temp.add_student).with_args(12, 'Nowak', 10), raises(Exception))

    def test_add_student_firstname_float(self):
        assert_that(calling(self.temp.add_student).with_args(3.14, 'Nowak', 10), raises(Exception))

    def test_add_student_firstname_int_negative(self):
        assert_that(calling(self.temp.add_student).with_args(-12, 'Nowak', 10), raises(Exception))

    def test_add_student_firstname_float_negative(self):
        assert_that(calling(self.temp.add_student).with_args(-2.56, 'Nowak', 10), raises(Exception))

    def test_add_student_lastname_object(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', {}, 10), raises(Exception))

    def test_add_student_lastname_array(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', [], 10), raises(Exception))

    def test_add_student_lastname_true(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', True, 10), raises(Exception))

    def test_add_student_lastname_false(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', False, 10), raises(Exception))

    def test_add_student_lastname_int(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 31, 10), raises(Exception))

    def test_add_student_lastname_float(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 2.13, 10), raises(Exception))

    def test_add_student_lastname_int_negative(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', -12, 10), raises(Exception))

    def test_add_student_lastname_float_negative(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', -2.45, 10), raises(Exception))

    def test_add_student_age_object(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', {}), raises(Exception))

    def test_add_student_age_array(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', []), raises(Exception))

    def test_add_student_age_true(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', True), raises(Exception))

    def test_add_student_age_false(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', False), raises(Exception))

    def test_add_student_age_string(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', 'abc'), raises(Exception))

    def test_add_student_age_string_number(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', '23'), raises(Exception))

    def test_add_student_age_int_negative(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', -2), raises(Exception))

    def test_add_student_age_float_negative(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', -1.0), raises(Exception))

    def test_add_student_age_zero(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', 0), raises(Exception))

    # Testy show_students
    def test_show_students(self):
        assert_that(self.temp_with_students.show_students(), equal_to([
            {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12},
            {'firstname': 'Ola', 'lastname': 'Kot', 'age': 17}
        ]))

    def test_show_students_2(self):
        assert_that(self.temp.show_students(), equal_to([]))

    # Testy edit_student
    def test_edit_student(self):
        assert_that(self.temp_with_students.edit_student(1, firstname='Marcin', lastname='Nowak', age=10), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Nowak',
            'age': 10
        }))

    def test_edit_student_without_age(self):
        assert_that(self.temp_with_students.edit_student(1, firstname='Marcin', lastname='Nowak'), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Nowak',
            'age': 12
        }))

    def test_edit_student_without_lastname(self):
        assert_that(self.temp_with_students.edit_student(1, firstname='Marcin', age=10), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Kowalski',
            'age': 10
        }))

    def test_edit_student_without_firstname(self):
        assert_that(self.temp_with_students.edit_student(1, lastname='Nowak', age=10), equal_to({
            'firstname': 'Jan',
            'lastname': 'Nowak',
            'age': 10
        }))

    def test_edit_student_without_firstname_lastname(self):
        assert_that(self.temp_with_students.edit_student(1, age=10), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 10
        }))

    def test_edit_student_without_firstname_age(self):
        assert_that(self.temp_with_students.edit_student(1, lastname='Nowak'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Nowak',
            'age': 12
        }))

    def test_edit_student_without_lastname_age(self):
        assert_that(self.temp_with_students.edit_student(1, firstname='Marcin'), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Kowalski',
            'age': 12
        }))

    def test_edit_student_firstname_object(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, {}, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_array(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, [], 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_true(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, True, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_false(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, False, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_int(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 12, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_float(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 3.14, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_int_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, -12, 'Nowak', 10), raises(Exception))

    def test_edit_student_firstname_float_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, -2.56, 'Nowak', 10), raises(Exception))

    def test_edit_student_lastname_object(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', {}, 10), raises(Exception))

    def test_edit_student_lastname_array(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', [], 10), raises(Exception))

    def test_edit_student_lastname_true(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', True, 10), raises(Exception))

    def test_edit_student_lastname_false(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', False, 10), raises(Exception))

    def test_edit_student_lastname_int(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 31, 10), raises(Exception))

    def test_edit_student_lastname_float(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 2.13, 10), raises(Exception))

    def test_edit_student_lastname_int_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', -12, 10), raises(Exception))

    def test_edit_student_lastname_float_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', -2.45, 10), raises(Exception))

    def test_edit_student_age_object(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', {}),
                    raises(Exception))

    def test_edit_student_age_array(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', []),
                    raises(Exception))

    def test_edit_student_age_true(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', True),
                    raises(Exception))

    def test_edit_student_age_false(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', False),
                    raises(Exception))

    def test_edit_student_age_string(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', 'abc'),
                    raises(Exception))

    def test_edit_student_age_string_number(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', '23'),
                    raises(Exception))

    def test_edit_student_age_int_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', -2),
                    raises(Exception))

    def test_edit_student_age_float_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', -1.0),
                    raises(Exception))

    def test_edit_student_age_zero(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', 0), raises(Exception))

    # Testy delete_student
    def test_delete_student(self):
        assert_that(self.temp_with_students.delete_student(1), equal_to([
            {'firstname': 'Ola', 'lastname': 'Kot', 'age': 17}
        ]))

    def test_delete_student_2(self):
        assert_that(self.temp_with_students.delete_student(2), equal_to([
            {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}
        ]))

    def test_delete_student_3(self):
        assert_that(self.temp_with_students.delete_student(2), equal_to([
            {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}
        ]))
        assert_that(self.temp_with_students.delete_student(1), equal_to([]))

    def test_delete_student_out_of_range(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(0), raises(Exception))

    def test_delete_student_out_of_range_2(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(3), raises(Exception))

    def test_delete_student_none(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(None), raises(Exception))

    def test_delete_student_object(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args({}), raises(Exception))

    def test_delete_student_array(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args([]), raises(Exception))

    def test_delete_student_true(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(True), raises(Exception))

    def test_delete_student_false(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(False), raises(Exception))

    def test_delete_student_string(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args('abc'), raises(Exception))

    def test_delete_student_string_number(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args('2'), raises(Exception))

    def test_delete_student_float(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(2.15), raises(Exception))

    def test_delete_student_negative_int(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(-3), raises(Exception))

    def test_delete_student_negative_float(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(-3.45), raises(Exception))