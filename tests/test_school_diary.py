import unittest
from hamcrest import *

from src.school_diary import SchoolDiary


class test_school_diary(unittest.TestCase):

    def setUp(self):
        self.temp = SchoolDiary()
        self.temp_with_students = SchoolDiary()
        self.temp_with_students.add_student('Jan', 'Kowalski', 12)
        self.temp_with_students.add_student('Ola', 'Kot', 17)
        self.temp_with_student_with_subject = SchoolDiary()
        self.temp_with_student_with_subject.add_student('Paweł', 'Pawłowski', 15)
        self.temp_with_student_with_subject.add_subject_to_student(1, 'Matematyka')
        self.temp_with_student_with_subject.add_subject_to_student(1, 'Polski')

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

    # Testy add_subject
    def test_add_subject_to_student(self):
        assert_that(self.temp_with_students.add_subject_to_student(1, 'Polski'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12,
            'subjects': ['Polski']
        }))

    def test_add_subject_to_student_2(self):
        assert_that(self.temp_with_students.add_subject_to_student(1, 'Matematyka'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12,
            'subjects': ['Matematyka']
        }))
        assert_that(self.temp_with_students.add_subject_to_student(1, 'Polski'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12,
            'subjects': ['Matematyka', 'Polski']
        }))

    def test_add_subject_to_student_none_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(None, 'Fizyka'),
                    raises(Exception))

    def test_add_subject_to_student_none_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, None), raises(Exception))

    def test_add_subject_to_student_none(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(None, None), raises(Exception))

    def test_add_subject_to_student_object_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args({}, 'Fizyka'), raises(Exception))

    def test_add_subject_to_student_object_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, {}), raises(Exception))

    def test_add_subject_to_student_object(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args({}, {}), raises(Exception))

    def test_add_subject_to_student_array_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args([], 'Fizyka'), raises(Exception))

    def test_add_subject_to_student_array_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, []), raises(Exception))

    def test_add_subject_to_student_array(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args([], []), raises(Exception))

    def test_add_subject_to_student_true_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(True, 'Fizyka'),
                    raises(Exception))

    def test_add_subject_to_student_true_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, True), raises(Exception))

    def test_add_subject_to_student_true(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(True, True), raises(Exception))

    def test_add_subject_to_student_false_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(False, 'Fizyka'),
                    raises(Exception))

    def test_add_subject_to_student_false_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, False), raises(Exception))

    def test_add_subject_to_student_false(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(False, False), raises(Exception))

    def test_add_subject_to_student_string_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args('abc', 'Fizyka'),
                    raises(Exception))

    def test_add_subject_to_student_string_number_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args('3', 'Fizyka'), raises(Exception))

    def test_add_subject_to_student_int_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, 2), raises(Exception))

    def test_add_subject_to_student_string_subject_id_int_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args('32a', 5), raises(Exception))

    def test_add_subject_to_student_float_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(2.15, 'Fizyka'),
                    raises(Exception))

    def test_add_subject_to_student_float_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, 3.87), raises(Exception))

    def test_add_subject_to_student_float(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1.32, 4.12), raises(Exception))

    def test_add_subject_to_student_negative_int_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(-3, 'Fizyka'), raises(Exception))

    def test_add_subject_to_student_negative_int_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, -1), raises(Exception))

    def test_add_subject_to_student_negative_int(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(-2, -9), raises(Exception))

    def test_add_subject_to_student_negative_float_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(-3.12, 'Fizyka'),
                    raises(Exception))

    def test_add_subject_to_student_negative_float_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, -1.55), raises(Exception))

    def test_add_subject_to_student_negative_float(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(-2.12, -9.65), raises(Exception))

    def test_add_subject_to_student_id_out_of_range(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(0, 'Fizyka'), raises(Exception))

    def test_add_subject_to_student_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(5, 'Fizyka'), raises(Exception))

    # Testy get_subjects_from_student
    def test_get_subjects_from_student(self):
        assert_that(self.temp_with_student_with_subject.get_subjects_from_student(1),
                    equal_to(['Matematyka', 'Polski']))

    def test_get_subjects_from_student_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(0),
                    raises(Exception))

    def test_get_subjects_from_student_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(3),
                    raises(Exception))

    def test_get_subjects_from_student_none(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(None),
                    raises(Exception))

    def test_get_subjects_from_student_object(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args({}),
                    raises(Exception))

    def test_get_subjects_from_student_array(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args([]),
                    raises(Exception))

    def test_get_subjects_from_student_true(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(True),
                    raises(Exception))

    def test_get_subjects_from_student_false(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(False),
                    raises(Exception))

    def test_get_subjects_from_student_string(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args('abc'),
                    raises(Exception))

    def test_get_subjects_from_student_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args('2'),
                    raises(Exception))

    def test_get_subjects_from_student_float(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(2.15),
                    raises(Exception))

    def test_get_subjects_from_student_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(-3),
                    raises(Exception))

    def test_get_subjects_from_student_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(-3.45),
                    raises(Exception))

    # Testy edit_subject_in_student
    def test_edit_subject_in_student(self):
        assert_that(self.temp_with_student_with_subject.edit_subject_in_student(1, 1, 'Fizyka'),
                    equal_to(['Fizyka', 'Polski']))

    def test_edit_subject_in_student_2(self):
        assert_that(self.temp_with_student_with_subject.edit_subject_in_student(1, 2, 'Biologia'),
                    equal_to(['Matematyka', 'Biologia']))

    def test_edit_subject_in_student_id_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(0, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(4, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 0, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 6, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_none(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(None, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_object(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args({}, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_array(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args([], 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_true(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(True, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_false(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(False, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_string(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args('abc', 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args('2', 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(2.14, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(-3, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_id_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(-2.51, 1, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_none(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, None, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_object(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, {}, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_array(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, [], 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_true(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, True, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_false(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, False, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_string(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 'abc', 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, '3', 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 2.14, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, -3, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_subject_id_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, -2.51, 'Fizyka'),
                    raises(Exception))

    def test_edit_subject_in_student_name_none(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, None),
                    raises(Exception))

    def test_edit_subject_in_student_name_object(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, {}),
                    raises(Exception))

    def test_edit_subject_in_student_name_array(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, []),
                    raises(Exception))

    def test_edit_subject_in_student_name_true(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, True),
                    raises(Exception))

    def test_edit_subject_in_student_name_false(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, False),
                    raises(Exception))

    def test_edit_subject_in_student_name_int(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, 3),
                    raises(Exception))

    def test_edit_subject_in_student_name_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, 3.14),
                    raises(Exception))

    def test_edit_subject_in_student_name_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, -4),
                    raises(Exception))

    def test_edit_subject_in_student_name_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, -4.11),
                    raises(Exception))
