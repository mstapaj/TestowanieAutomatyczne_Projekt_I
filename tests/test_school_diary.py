import unittest
from hamcrest import assert_that, equal_to, has_length, calling, raises, close_to

from src.school_diary import SchoolDiary


class TestSchoolDiary(unittest.TestCase):

    def setUp(self):
        self.temp = SchoolDiary([])
        self.temp_with_students = SchoolDiary([{'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12},
                                               {'firstname': 'Ola', 'lastname': 'Kot', 'age': 17}])
        self.temp_with_student_with_subject = SchoolDiary([{'firstname': 'Paweł', 'lastname': 'Pawłowski', 'age': 15,
                                                            'subjects': [{'name': 'Matematyka'}, {'name': 'Polski'}]}])
        self.temp_with_student_with_subject_with_grades = SchoolDiary([{'firstname': 'Paweł', 'lastname': 'Pawłowski',
                                                                        'age': 15,
                                                                        'subjects': [
                                                                            {'name': 'Matematyka', 'grades': [2, 5]}
                                                                            , {'name': 'Polski', 'grades': [2]}]}])
        self.temp_with_students_with_remarks = SchoolDiary(
            [{'firstname': 'Paweł', 'lastname': 'Pawłowski', 'age': 15, 'remarks': ['Uwaga 1', 'Uwaga 2']}])

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
        self.temp.add_student('Ola', 'Kot', 17)
        assert_that(self.temp.add_student('Jan', 'Kowalski', 12), equal_to([
            {'firstname': 'Ola', 'lastname': 'Kot', 'age': 17},
            {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12}
        ]))

    def test_add_student_has_length(self):
        self.temp.add_student('Ola', 'Kot', 17)
        assert_that(self.temp.add_student('Jan', 'Kowalski', 12), has_length(2))

    def test_add_student_firstname_object(self):
        assert_that(calling(self.temp.add_student).with_args({}, 'Nowak', 10), raises(TypeError))

    def test_add_student_firstname_array(self):
        assert_that(calling(self.temp.add_student).with_args([], 'Nowak', 10), raises(TypeError))

    def test_add_student_firstname_true(self):
        assert_that(calling(self.temp.add_student).with_args(True, 'Nowak', 10), raises(TypeError))

    def test_add_student_firstname_false(self):
        assert_that(calling(self.temp.add_student).with_args(False, 'Nowak', 10), raises(TypeError))

    def test_add_student_firstname_int(self):
        assert_that(calling(self.temp.add_student).with_args(12, 'Nowak', 10), raises(TypeError))

    def test_add_student_firstname_float(self):
        assert_that(calling(self.temp.add_student).with_args(3.14, 'Nowak', 10), raises(TypeError))

    def test_add_student_firstname_int_negative(self):
        assert_that(calling(self.temp.add_student).with_args(-12, 'Nowak', 10), raises(TypeError))

    def test_add_student_firstname_float_negative(self):
        assert_that(calling(self.temp.add_student).with_args(-2.56, 'Nowak', 10), raises(TypeError))

    def test_add_student_lastname_object(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', {}, 10), raises(TypeError))

    def test_add_student_lastname_array(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', [], 10), raises(TypeError))

    def test_add_student_lastname_true(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', True, 10), raises(TypeError))

    def test_add_student_lastname_false(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', False, 10), raises(TypeError))

    def test_add_student_lastname_int(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 31, 10), raises(TypeError))

    def test_add_student_lastname_float(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 2.13, 10), raises(TypeError))

    def test_add_student_lastname_int_negative(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', -12, 10), raises(TypeError))

    def test_add_student_lastname_float_negative(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', -2.45, 10), raises(TypeError))

    def test_add_student_age_object(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', {}), raises(TypeError))

    def test_add_student_age_array(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', []), raises(TypeError))

    def test_add_student_age_true(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', True), raises(TypeError))

    def test_add_student_age_false(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', False), raises(TypeError))

    def test_add_student_age_string(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', 'abc'), raises(TypeError))

    def test_add_student_age_string_number(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', '23'), raises(TypeError))

    def test_add_student_age_int_negative(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', -2), raises(ValueError))

    def test_add_student_age_float_negative(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', -1.0), raises(TypeError))

    def test_add_student_age_zero(self):
        assert_that(calling(self.temp.add_student).with_args('Marcin', 'Nowak', 0), raises(ValueError))

    # Testy show_students
    def test_show_students(self):
        assert_that(self.temp_with_students.show_students(), equal_to([
            {'firstname': 'Jan', 'lastname': 'Kowalski', 'age': 12},
            {'firstname': 'Ola', 'lastname': 'Kot', 'age': 17}
        ]))

    def test_show_students_has_length(self):
        assert_that(self.temp_with_students.show_students(), has_length(2))

    def test_show_students_2(self):
        assert_that(self.temp.show_students(), equal_to([]))

    # Testy edit_student
    def test_edit_student(self):
        assert_that(self.temp_with_students.edit_student(1, firstname='Marcin', lastname='Nowak', age=10), equal_to({
            'firstname': 'Marcin',
            'lastname': 'Nowak',
            'age': 10
        }))

    def test_edit_student_has_length(self):
        assert_that(self.temp_with_students.edit_student(1, firstname='Marcin', lastname='Nowak', age=10),
                    has_length(3))

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
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, {}, 'Nowak', 10), raises(TypeError))

    def test_edit_student_firstname_array(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, [], 'Nowak', 10), raises(TypeError))

    def test_edit_student_firstname_true(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, True, 'Nowak', 10), raises(TypeError))

    def test_edit_student_firstname_false(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, False, 'Nowak', 10), raises(TypeError))

    def test_edit_student_firstname_int(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 12, 'Nowak', 10), raises(TypeError))

    def test_edit_student_firstname_float(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 3.14, 'Nowak', 10), raises(TypeError))

    def test_edit_student_firstname_int_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, -12, 'Nowak', 10), raises(TypeError))

    def test_edit_student_firstname_float_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, -2.56, 'Nowak', 10), raises(TypeError))

    def test_edit_student_lastname_object(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', {}, 10), raises(TypeError))

    def test_edit_student_lastname_array(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', [], 10), raises(TypeError))

    def test_edit_student_lastname_true(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', True, 10), raises(TypeError))

    def test_edit_student_lastname_false(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', False, 10), raises(TypeError))

    def test_edit_student_lastname_int(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 31, 10), raises(TypeError))

    def test_edit_student_lastname_float(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 2.13, 10), raises(TypeError))

    def test_edit_student_lastname_int_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', -12, 10), raises(TypeError))

    def test_edit_student_lastname_float_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', -2.45, 10), raises(TypeError))

    def test_edit_student_age_object(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', {}),
                    raises(TypeError))

    def test_edit_student_age_array(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', []),
                    raises(TypeError))

    def test_edit_student_age_true(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', True),
                    raises(TypeError))

    def test_edit_student_age_false(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', False),
                    raises(TypeError))

    def test_edit_student_age_string(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', 'abc'),
                    raises(TypeError))

    def test_edit_student_age_string_number(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', '23'),
                    raises(TypeError))

    def test_edit_student_age_int_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', -2),
                    raises(TypeError))

    def test_edit_student_age_float_negative(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', -1.0),
                    raises(TypeError))

    def test_edit_student_age_zero(self):
        assert_that(calling(self.temp_with_students.edit_student).with_args(1, 'Marcin', 'Nowak', 0), raises(TypeError))

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
        self.temp_with_students.delete_student(2)
        assert_that(self.temp_with_students.delete_student(1), equal_to([]))

    def test_delete_student_has_length(self):
        self.temp_with_students.delete_student(2)
        assert_that(self.temp_with_students.delete_student(1), has_length(0))

    def test_delete_student_out_of_range(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(0), raises(ValueError))

    def test_delete_student_out_of_range_2(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(3), raises(ValueError))

    def test_delete_student_none(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(None), raises(TypeError))

    def test_delete_student_object(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args({}), raises(TypeError))

    def test_delete_student_array(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args([]), raises(TypeError))

    def test_delete_student_true(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(True), raises(TypeError))

    def test_delete_student_false(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(False), raises(TypeError))

    def test_delete_student_string(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args('abc'), raises(TypeError))

    def test_delete_student_string_number(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args('2'), raises(TypeError))

    def test_delete_student_float(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(2.15), raises(TypeError))

    def test_delete_student_negative_int(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(-3), raises(ValueError))

    def test_delete_student_negative_float(self):
        assert_that(calling(self.temp_with_students.delete_student).with_args(-3.45), raises(TypeError))

    # Testy add_subject
    def test_add_subject_to_student(self):
        assert_that(self.temp_with_students.add_subject_to_student(1, 'Polski'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12,
            'subjects': ['Polski']
        }))

    def test_add_subject_to_student_2(self):
        self.temp_with_students.add_subject_to_student(1, 'Matematyka')
        assert_that(self.temp_with_students.add_subject_to_student(1, 'Polski'), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12,
            'subjects': ['Matematyka', 'Polski']
        }))

    def test_add_subject_to_student_none_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(None, 'Fizyka'),
                    raises(TypeError))

    def test_add_subject_to_student_none_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, None), raises(TypeError))

    def test_add_subject_to_student_none(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(None, None), raises(TypeError))

    def test_add_subject_to_student_object_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args({}, 'Fizyka'), raises(TypeError))

    def test_add_subject_to_student_object_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, {}), raises(TypeError))

    def test_add_subject_to_student_object(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args({}, {}), raises(TypeError))

    def test_add_subject_to_student_array_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args([], 'Fizyka'), raises(TypeError))

    def test_add_subject_to_student_array_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, []), raises(TypeError))

    def test_add_subject_to_student_array(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args([], []), raises(TypeError))

    def test_add_subject_to_student_true_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(True, 'Fizyka'),
                    raises(TypeError))

    def test_add_subject_to_student_true_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, True), raises(TypeError))

    def test_add_subject_to_student_true(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(True, True), raises(TypeError))

    def test_add_subject_to_student_false_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(False, 'Fizyka'),
                    raises(TypeError))

    def test_add_subject_to_student_false_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, False), raises(TypeError))

    def test_add_subject_to_student_false(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(False, False), raises(TypeError))

    def test_add_subject_to_student_string_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args('abc', 'Fizyka'),
                    raises(TypeError))

    def test_add_subject_to_student_string_number_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args('3', 'Fizyka'), raises(TypeError))

    def test_add_subject_to_student_int_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, 2), raises(TypeError))

    def test_add_subject_to_student_string_subject_id_int_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args('32a', 5), raises(TypeError))

    def test_add_subject_to_student_float_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(2.15, 'Fizyka'),
                    raises(TypeError))

    def test_add_subject_to_student_float_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, 3.87), raises(TypeError))

    def test_add_subject_to_student_float(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1.32, 4.12), raises(TypeError))

    def test_add_subject_to_student_negative_int_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(-3, 'Fizyka'), raises(ValueError))

    def test_add_subject_to_student_negative_int_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, -1), raises(TypeError))

    def test_add_subject_to_student_negative_int(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(-2, -9), raises(ValueError))

    def test_add_subject_to_student_negative_float_subject_id(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(-3.12, 'Fizyka'),
                    raises(TypeError))

    def test_add_subject_to_student_negative_float_name(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(1, -1.55), raises(TypeError))

    def test_add_subject_to_student_negative_float(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(-2.12, -9.65), raises(TypeError))

    def test_add_subject_to_student_id_out_of_range(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(0, 'Fizyka'), raises(ValueError))

    def test_add_subject_to_student_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_students.add_subject_to_student).with_args(5, 'Fizyka'), raises(ValueError))

    # Testy get_subjects_from_student
    def test_get_subjects_from_student(self):
        assert_that(self.temp_with_student_with_subject.get_subjects_from_student(1),
                    equal_to(['Matematyka', 'Polski']))

    def test_get_subjects_from_student_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(0),
                    raises(ValueError))

    def test_get_subjects_from_student_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(3),
                    raises(ValueError))

    def test_get_subjects_from_student_none(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(None),
                    raises(TypeError))

    def test_get_subjects_from_student_object(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args({}),
                    raises(TypeError))

    def test_get_subjects_from_student_array(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args([]),
                    raises(TypeError))

    def test_get_subjects_from_student_true(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(True),
                    raises(TypeError))

    def test_get_subjects_from_student_false(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(False),
                    raises(TypeError))

    def test_get_subjects_from_student_string(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args('abc'),
                    raises(TypeError))

    def test_get_subjects_from_student_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args('2'),
                    raises(TypeError))

    def test_get_subjects_from_student_float(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(2.15),
                    raises(TypeError))

    def test_get_subjects_from_student_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(-3),
                    raises(ValueError))

    def test_get_subjects_from_student_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.get_subjects_from_student).with_args(-3.45),
                    raises(TypeError))

    # Testy edit_subject_in_student
    def test_edit_subject_in_student(self):
        assert_that(self.temp_with_student_with_subject.edit_subject_in_student(1, 1, 'Fizyka'),
                    equal_to(['Fizyka', 'Polski']))

    def test_edit_subject_in_student_2(self):
        assert_that(self.temp_with_student_with_subject.edit_subject_in_student(1, 2, 'Biologia'),
                    equal_to(['Matematyka', 'Biologia']))

    def test_edit_subject_in_student_id_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(0, 1, 'Fizyka'),
                    raises(ValueError))

    def test_edit_subject_in_student_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(4, 1, 'Fizyka'),
                    raises(ValueError))

    def test_edit_subject_in_student_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 0, 'Fizyka'),
                    raises(ValueError))

    def test_edit_subject_in_student_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 6, 'Fizyka'),
                    raises(ValueError))

    def test_edit_subject_in_student_id_none(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(None, 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_id_object(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args({}, 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_id_array(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args([], 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_id_true(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(True, 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_id_false(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(False, 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_id_string(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args('abc', 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_id_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args('2', 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_id_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(2.14, 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_id_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(-3, 1, 'Fizyka'),
                    raises(ValueError))

    def test_edit_subject_in_student_id_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(-2.51, 1, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_none(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, None, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_object(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, {}, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_array(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, [], 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_true(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, True, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_false(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, False, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_string(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 'abc', 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, '3', 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 2.14, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_subject_id_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, -3, 'Fizyka'),
                    raises(ValueError))

    def test_edit_subject_in_student_subject_id_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, -2.51, 'Fizyka'),
                    raises(TypeError))

    def test_edit_subject_in_student_name_none(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, None),
                    raises(TypeError))

    def test_edit_subject_in_student_name_object(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, {}),
                    raises(TypeError))

    def test_edit_subject_in_student_name_array(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, []),
                    raises(TypeError))

    def test_edit_subject_in_student_name_true(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, True),
                    raises(TypeError))

    def test_edit_subject_in_student_name_false(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, False),
                    raises(TypeError))

    def test_edit_subject_in_student_name_int(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, 3),
                    raises(TypeError))

    def test_edit_subject_in_student_name_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, 3.14),
                    raises(TypeError))

    def test_edit_subject_in_student_name_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, -4),
                    raises(TypeError))

    def test_edit_subject_in_student_name_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.edit_subject_in_student).with_args(1, 1, -4.11),
                    raises(TypeError))

    # Testy delete_subject
    def test_delete_subject_in_student(self):
        assert_that(self.temp_with_student_with_subject.delete_subject_in_student(1, 1), equal_to(['Polski']))

    def test_delete_subject_in_student_2(self):
        assert_that(self.temp_with_student_with_subject.delete_subject_in_student(1, 2), equal_to(['Matematyka']))

    def test_delete_subject_in_student_3(self):
        self.temp_with_student_with_subject.delete_subject_in_student(1, 2)
        assert_that(self.temp_with_student_with_subject.delete_subject_in_student(1, 1), equal_to([]))

    def test_delete_subject_in_student_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(0, 1),
                    raises(ValueError))

    def test_delete_subject_in_student_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(6, 1),
                    raises(ValueError))

    def test_delete_subject_in_student_id_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, 0),
                    raises(ValueError))

    def test_delete_subject_in_student_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, 4),
                    raises(ValueError))

    def test_delete_subject_in_student_none_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(None, 1),
                    raises(TypeError))

    def test_delete_subject_in_student_none_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, None),
                    raises(TypeError))

    def test_delete_subject_in_student_none(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(None, None),
                    raises(TypeError))

    def test_delete_subject_in_student_object_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args({}, 1),
                    raises(TypeError))

    def test_delete_subject_in_student_object_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, {}),
                    raises(TypeError))

    def test_delete_subject_in_student_object(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args({}, {}),
                    raises(TypeError))

    def test_delete_subject_in_student_true_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(True, 1),
                    raises(TypeError))

    def test_delete_subject_in_student_true_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, True),
                    raises(TypeError))

    def test_delete_subject_in_student_true(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(True, True),
                    raises(TypeError))

    def test_delete_subject_in_student_false_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(False, 1),
                    raises(TypeError))

    def test_delete_subject_in_student_false_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, False),
                    raises(TypeError))

    def test_delete_subject_in_student_false(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(False, False),
                    raises(TypeError))

    def test_delete_subject_in_student_string_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args('abc', 1),
                    raises(TypeError))

    def test_delete_subject_in_student_string_number_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args('2', 1),
                    raises(TypeError))

    def test_delete_subject_in_student_string_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(2, 'abc'),
                    raises(ValueError))

    def test_delete_subject_in_student_string_number_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(2, '3'),
                    raises(ValueError))

    def test_delete_subject_in_student_string(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args('b2', '3a'),
                    raises(TypeError))

    def test_delete_subject_in_student_float_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(2.31, 1),
                    raises(TypeError))

    def test_delete_subject_in_student_float_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, 1.67),
                    raises(TypeError))

    def test_delete_subject_in_student_float(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(3.12, 4.33),
                    raises(TypeError))

    def test_delete_subject_in_student_negative_int_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(-3, 1),
                    raises(ValueError))

    def test_delete_subject_in_student_negative_int_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, -8),
                    raises(ValueError))

    def test_delete_subject_in_student_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(-2, -5),
                    raises(ValueError))

    def test_delete_subject_in_student_negative_float_subject_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(-2.31, 1),
                    raises(TypeError))

    def test_delete_subject_in_student_negative_float_grade_id(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(1, -1.67),
                    raises(TypeError))

    def test_delete_subject_in_student_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.delete_subject_in_student).with_args(-3.12, -4.33),
                    raises(TypeError))

    # Testy add_grade_in_student_in_subject
    def test_add_grade_in_student_in_subject(self):
        assert_that(self.temp_with_student_with_subject.add_grade_in_student_in_subject(1, 1, 4), equal_to({
            'Matematyka': [4],
            'Polski': []
        }))

    def test_add_grade_in_student_in_subject_2(self):
        assert_that(self.temp_with_student_with_subject.add_grade_in_student_in_subject(1, 2, 1), equal_to({
            'Matematyka': [],
            'Polski': [1]
        }))

    def test_add_grade_in_student_in_subject_3(self):
        self.temp_with_student_with_subject.add_grade_in_student_in_subject(1, 2, 1)
        self.temp_with_student_with_subject.add_grade_in_student_in_subject(1, 2, 4)
        assert_that(self.temp_with_student_with_subject.add_grade_in_student_in_subject(1, 1, 6), equal_to({
            'Matematyka': [6],
            'Polski': [1, 4]
        }))

    def test_add_grade_in_student_in_subject_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(0, 1, 4),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(6, 1, 4),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_id_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 0, 4),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 4, 4),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_grade_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, -2),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_grade_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, 8),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_subject_id_none(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(None, 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_subject_id_object(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args({}, 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_subject_id_array(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args([], 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_subject_id_true(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(True, 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_subject_id_false(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(False, 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_subject_id_string(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args('abc', 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_subject_id_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args('3', 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_subject_id_float(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(2.31, 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_subject_id_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(-3, 1, 4),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_subject_id_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(-2.16, 1, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_none(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, None, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_object(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, {}, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_array(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, [], 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_true(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, True, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_false(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, False, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_string(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 'abc', 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, '3', 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_float(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 2.31, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_id_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, -1, 4),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_grade_id_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, -2.16, 4),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_none(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, None),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_object(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, {}),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_array(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, []),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_true(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, True),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_false(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, False),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_string(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, 'abc'),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, '3'),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_float(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, 2.31),
                    raises(TypeError))

    def test_add_grade_in_student_in_subject_grade_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, -1),
                    raises(ValueError))

    def test_add_grade_in_student_in_subject_grade_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject.add_grade_in_student_in_subject).with_args(1, 1, -2.16),
                    raises(TypeError))

    # Testy get_grades_in_student_from_subject
    def test_get_grades_in_student_from_subject(self):
        assert_that(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject(1, 1),
                    equal_to([2, 5]))

    def test_get_grades_in_student_from_subject_2(self):
        assert_that(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject(1, 2),
                    equal_to([2]))

    def test_get_grades_in_student_from_subject_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(0, 1),
            raises(ValueError))

    def test_get_grades_in_student_from_subject_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(4, 1),
            raises(ValueError))

    def test_get_grades_in_student_from_subject_none_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(None,
                                                                                                                  1),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_none_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(1,
                                                                                                                  None),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(None,
                                                                                                                  None),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_object_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args({},
                                                                                                                  1),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_object_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(1,
                                                                                                                  {}),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args({},
                                                                                                                  {}),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_true_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(True,
                                                                                                                  1),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_true_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(1,
                                                                                                                  True),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(True,
                                                                                                                  True),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_false_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(False,
                                                                                                                  1),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_false_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(1,
                                                                                                                  False),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(False,
                                                                                                                  False),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_string_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args('abc',
                                                                                                                  1),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_string_number_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args('2',
                                                                                                                  1),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_string_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(2,
                                                                                                                  'abc'),
            raises(ValueError))

    def test_get_grades_in_student_from_subject_string_number_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(2,
                                                                                                                  '3'),
            raises(ValueError))

    def test_get_grades_in_student_from_subject_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args('b2',
                                                                                                                  '3a'),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_float_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(2.31,
                                                                                                                  1),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_float_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(1,
                                                                                                                  1.67),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(3.12,
                                                                                                                  4.33),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_negative_int_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(-3,
                                                                                                                  1),
            raises(ValueError))

    def test_get_grades_in_student_from_subject_negative_int_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(1,
                                                                                                                  -8),
            raises(ValueError))

    def test_get_grades_in_student_from_subject_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(-2,
                                                                                                                  -5),
            raises(ValueError))

    def test_get_grades_in_student_from_subject_negative_float_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(-2.31,
                                                                                                                  1),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_negative_float_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(1,
                                                                                                                  -1.67),
            raises(TypeError))

    def test_get_grades_in_student_from_subject_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.get_grades_in_student_from_subject).with_args(-3.12,
                                                                                                                  -4.33),
            raises(TypeError))

    # Testy edit_grade_in_student_in_subject
    def test_edit_grade_in_student_in_subject(self):
        assert_that(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject(1, 1, 1, 6),
                    equal_to([6, 5]))

    def test_edit_grade_in_student_in_subject_2(self):
        assert_that(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject(1, 2, 1, 1),
                    equal_to([1]))

    def test_edit_grade_in_student_in_subject_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(0, 1, 1,
                                                                                                                3),
            raises(ValueError))

    def test_edit_grade_in_student_in_subject_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(4, 1, 1,
                                                                                                                3),
            raises(ValueError))

    def test_edit_grade_in_student_in_subject_subject_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 0, 1,
                                                                                                                3),
            raises(ValueError))

    def test_edit_grade_in_student_in_subject_subject_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 7, 1,
                                                                                                                3),
            raises(ValueError))

    def test_edit_grade_subject_grade_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 0,
                                                                                                                3),
            raises(ValueError))

    def test_edit_grade_subject_grade_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 4,
                                                                                                                3),
            raises(ValueError))

    def test_edit_grade_subject_grade_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                0),
            raises(ValueError))

    def test_edit_grade_subject_grade_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                8),
            raises(ValueError))

    def test_edit_grade_subject_id_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(None, 1,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_id_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args({}, 1,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_id_array(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args([], 1,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_id_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(True, 1,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_id_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(False,
                                                                                                                1, 1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_id_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args('abc',
                                                                                                                1, 1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_id_string_number(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args('3', 1,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_id_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(2.14, 1,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_id_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(-3, 1,
                                                                                                                1,
                                                                                                                1),
            raises(ValueError))

    def test_edit_grade_subject_id_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(-2.81,
                                                                                                                1, 1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, None,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, {},
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_array(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, [],
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, True,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1,
                                                                                                                False,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1,
                                                                                                                'abc',
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_string_number(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, '3',
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 2.14,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_subject_id_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, -3,
                                                                                                                1,
                                                                                                                1),
            raises(ValueError))

    def test_edit_grade_subject_subject_id_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1,
                                                                                                                -2.81,
                                                                                                                1,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                None,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                {},
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_array(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                [],
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                True,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                False,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                'abc',
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_string_number(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                '3',
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                2.14,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_id_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                -3,
                                                                                                                1),
            raises(ValueError))

    def test_edit_grade_subject_grade_id_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                -3.76,
                                                                                                                1),
            raises(TypeError))

    def test_edit_grade_subject_grade_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                None),
            raises(TypeError))

    def test_edit_grade_subject_grade_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                {}),
            raises(TypeError))

    def test_edit_grade_subject_grade_array(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                []),
            raises(TypeError))

    def test_edit_grade_subject_grade_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                True),
            raises(TypeError))

    def test_edit_grade_subject_grade_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                False),
            raises(TypeError))

    def test_edit_grade_subject_grade_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                'abc'),
            raises(TypeError))

    def test_edit_grade_subject_grade_string_number(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                '2'),
            raises(TypeError))

    def test_edit_grade_subject_grade_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                1.67),
            raises(TypeError))

    def test_edit_grade_subject_grade_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                -5),
            raises(ValueError))

    def test_edit_grade_subject_grade_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.edit_grade_in_student_in_subject).with_args(1, 1, 1,
                                                                                                                -3.76),
            raises(TypeError))

    # Testy delete_grade_in_student_in_subject
    def test_delete_grade_in_student_in_subject(self):
        assert_that(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject(1, 1, 1),
                    equal_to([5]))

    def test_delete_grade_in_student_in_subject_2(self):
        assert_that(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject(1, 2, 1),
                    equal_to([]))

    def test_delete_grade_in_student_in_subject_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(0, 1,
                                                                                                                  1),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(4, 1,
                                                                                                                  1),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_subject_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 0,
                                                                                                                  1),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_subject_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 6,
                                                                                                                  1),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_grade_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  0),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_grade_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  9),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_id_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(None,
                                                                                                                  1, 4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_id_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args({}, 1,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_id_array(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args([], 1,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_id_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(True,
                                                                                                                  1, 4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_id_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(False,
                                                                                                                  1,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_id_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args('abc',
                                                                                                                  1,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_id_string_number(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args('3',
                                                                                                                  1, 4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_id_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(2.31,
                                                                                                                  1, 4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_id_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(-3, 1,
                                                                                                                  4),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_id_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(-2.16,
                                                                                                                  1,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1,
                                                                                                                  None,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, {},
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_array(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, [],
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1,
                                                                                                                  True,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1,
                                                                                                                  False,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1,
                                                                                                                  'abc',
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_string_number(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1,
                                                                                                                  '3',
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1,
                                                                                                                  2.31,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_subject_id_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, -1,
                                                                                                                  4),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_subject_id_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1,
                                                                                                                  -2.16,
                                                                                                                  4),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  None),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  {}),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_array(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  []),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  True),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  False),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  'abc'),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_string_number(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  '3'),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  2.31),
            raises(TypeError))

    def test_delete_grade_in_student_in_subject_grade_id_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  -1),
            raises(ValueError))

    def test_delete_grade_in_student_in_subject_grade_id_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.delete_grade_in_student_in_subject).with_args(1, 1,
                                                                                                                  -2.16),
            raises(TypeError))

    # Testy average_of_subject_in_student
    def test_average_of_subject_in_student(self):
        assert_that(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student(1, 1), equal_to(3.5))

    def test_average_of_subject_in_student_2(self):
        assert_that(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student(1, 2), equal_to(2))

    def test_average_of_subject_in_student_close_to(self):
        assert_that(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student(1, 2),
                    close_to(1.8, 0.25))

    def test_average_of_subject_in_student_close_to_2(self):
        assert_that(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student(1, 1),
                    close_to(3, 0.6))

    def test_average_of_subject_in_student_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(0, 1),
            raises(ValueError))

    def test_average_of_subject_in_student_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(4, 1),
            raises(ValueError))

    def test_average_of_subject_in_student_none_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(None, 1),
            raises(TypeError))

    def test_average_of_subject_in_student_none_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(1, None),
            raises(TypeError))

    def test_average_of_subject_in_student_none(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(None,
                                                                                                             None),
            raises(TypeError))

    def test_average_of_subject_in_student_object_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args({}, 1),
            raises(TypeError))

    def test_average_of_subject_in_student_object_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(1, {}),
            raises(TypeError))

    def test_average_of_subject_in_student_object(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args({}, {}),
            raises(TypeError))

    def test_average_of_subject_in_student_true_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(True, 1),
            raises(TypeError))

    def test_average_of_subject_in_student_true_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(1, True),
            raises(TypeError))

    def test_average_of_subject_in_student_true(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(True,
                                                                                                             True),
            raises(TypeError))

    def test_average_of_subject_in_student_false_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(False, 1),
            raises(TypeError))

    def test_average_of_subject_in_student_false_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(1, False),
            raises(TypeError))

    def test_average_of_subject_in_student_false(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(False,
                                                                                                             False),
            raises(TypeError))

    def test_average_of_subject_in_student_string_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args('abc', 1),
            raises(TypeError))

    def test_average_of_subject_in_student_string_number_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args('2', 1),
            raises(TypeError))

    def test_average_of_subject_in_student_string_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(2, 'abc'),
            raises(ValueError))

    def test_average_of_subject_in_student_string_number_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(2, '3'),
            raises(ValueError))

    def test_average_of_subject_in_student_string(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args('b2',
                                                                                                             '3a'),
            raises(TypeError))

    def test_average_of_subject_in_student_float_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(2.31, 1),
            raises(TypeError))

    def test_average_of_subject_in_student_float_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(1, 1.67),
            raises(TypeError))

    def test_average_of_subject_in_student_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(3.12,
                                                                                                             4.33),
            raises(TypeError))

    def test_average_of_subject_in_student_negative_int_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(-3, 1),
            raises(ValueError))

    def test_average_of_subject_in_student_negative_int_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(1, -8),
            raises(ValueError))

    def test_average_of_subject_in_student_negative_int(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(-2, -5),
            raises(ValueError))

    def test_average_of_subject_in_student_negative_float_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(-2.31, 1),
            raises(TypeError))

    def test_average_of_subject_in_student_negative_float_subject_id(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(1, -1.67),
            raises(TypeError))

    def test_average_of_subject_in_student_negative_float(self):
        assert_that(
            calling(self.temp_with_student_with_subject_with_grades.average_of_subject_in_student).with_args(-3.12,
                                                                                                             -4.33),
            raises(TypeError))

    # Testy average_of_student
    def test_average_of_student(self):
        assert_that(self.temp_with_student_with_subject_with_grades.average_of_student(1), equal_to(2.5))

    def test_average_of_student_2(self):
        assert_that(self.temp_with_student_with_subject.average_of_student(1), equal_to(1.0))

    def test_average_of_student_close_to(self):
        assert_that(self.temp_with_student_with_subject_with_grades.average_of_student(1), close_to(2, 0.55))

    def test_average_of_student_close_to_2(self):
        assert_that(self.temp_with_student_with_subject.average_of_student(1), close_to(0.9, 0.15))

    def test_average_of_student_out_of_range(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args(0),
                    raises(ValueError))

    def test_average_of_student_out_of_range_2(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args(4),
                    raises(ValueError))

    def test_average_of_student_none(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args(None),
                    raises(TypeError))

    def test_average_of_student_object(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args({}),
                    raises(TypeError))

    def test_average_of_student_array(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args([]),
                    raises(TypeError))

    def test_average_of_student_true(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args(True),
                    raises(TypeError))

    def test_average_of_student_false(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args(False),
                    raises(TypeError))

    def test_average_of_student_string(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args('abc'),
                    raises(TypeError))

    def test_average_of_student_string_number(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args('2'),
                    raises(TypeError))

    def test_average_of_student_float(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args(2.15),
                    raises(TypeError))

    def test_average_of_student_negative_int(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args(-3),
                    raises(ValueError))

    def test_average_of_student_negative_float(self):
        assert_that(calling(self.temp_with_student_with_subject_with_grades.average_of_student).with_args(-3.45),
                    raises(TypeError))

    # Testy add_remark_to_student
    def test_add_remark_to_student(self):
        assert_that(self.temp_with_students.add_remark_to_student(1, 'Uwaga 1'), equal_to(['Uwaga 1']))

    def test_add_remark_to_student_2(self):
        self.temp_with_students.add_remark_to_student(2, 'Uwaga 1')
        assert_that(self.temp_with_students.add_remark_to_student(2, 'Uwaga 2'), equal_to(['Uwaga 1', 'Uwaga 2']))

    def test_add_remark_to_student_none_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(None, 'Uwaga'),
                    raises(TypeError))

    def test_add_remark_to_student_none_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, None), raises(TypeError))

    def test_add_remark_to_student_none(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(None, None), raises(TypeError))

    def test_add_remark_to_student_object_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args({}, 'Uwaga'), raises(TypeError))

    def test_add_remark_to_student_object_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, {}), raises(TypeError))

    def test_add_remark_to_student_object(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args({}, {}), raises(TypeError))

    def test_add_remark_to_student_array_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args([], 'Uwaga'), raises(TypeError))

    def test_add_remark_to_student_array_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, []), raises(TypeError))

    def test_add_remark_to_student_array(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args([], []), raises(TypeError))

    def test_add_remark_to_student_true_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(True, 'Uwaga'),
                    raises(TypeError))

    def test_add_remark_to_student_true_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, True), raises(TypeError))

    def test_add_remark_to_student_true(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(True, True), raises(TypeError))

    def test_add_remark_to_student_false_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(False, 'Uwaga'),
                    raises(TypeError))

    def test_add_remark_to_student_false_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, False), raises(TypeError))

    def test_add_remark_to_student_false(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(False, False), raises(TypeError))

    def test_add_remark_to_student_string_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args('abc', 'Uwaga'),
                    raises(TypeError))

    def test_add_remark_to_student_string_number_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args('3', 'Uwaga'), raises(TypeError))

    def test_add_remark_to_student_int_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, 2), raises(TypeError))

    def test_add_remark_to_student_string_student_id_int_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args('32a', 5), raises(TypeError))

    def test_add_remark_to_student_float_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(2.15, 'Uwaga'),
                    raises(TypeError))

    def test_add_remark_to_student_float_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, 3.87), raises(TypeError))

    def test_add_remark_to_student_float(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1.32, 4.12), raises(TypeError))

    def test_add_remark_to_student_negative_int_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(-3, 'Uwaga'), raises(ValueError))

    def test_add_remark_to_student_negative_int_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, -1), raises(TypeError))

    def test_add_remark_to_student_negative_int(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(-2, -9), raises(ValueError))

    def test_add_remark_to_student_negative_float_student_id(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(-3.12, 'Uwaga'),
                    raises(TypeError))

    def test_add_remark_to_student_negative_float_text(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(1, -1.55), raises(TypeError))

    def test_add_remark_to_student_negative_float(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(-2.12, -9.65), raises(TypeError))

    def test_add_remark_to_student_id_out_of_range(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(0, 'Uwaga'), raises(ValueError))

    def test_add_remark_to_student_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_students.add_remark_to_student).with_args(5, 'Uwaga'), raises(ValueError))

    # Testy get_remarks_from_student
    def test_get_remarks_from_student(self):
        assert_that(self.temp_with_students_with_remarks.get_remarks_from_student(1), equal_to(['Uwaga 1', 'Uwaga 2']))

    def test_get_remarks_from_student_out_of_range(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args(0),
                    raises(ValueError))

    def test_get_remarks_from_student_out_of_range_2(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args(3),
                    raises(ValueError))

    def test_get_remarks_from_student_none(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args(None),
                    raises(TypeError))

    def test_get_remarks_from_student_object(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args({}),
                    raises(TypeError))

    def test_get_remarks_from_student_array(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args([]),
                    raises(TypeError))

    def test_get_remarks_from_student_true(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args(True),
                    raises(TypeError))

    def test_get_remarks_from_student_false(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args(False),
                    raises(TypeError))

    def test_get_remarks_from_student_string(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args('abc'),
                    raises(TypeError))

    def test_get_remarks_from_student_string_number(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args('2'),
                    raises(TypeError))

    def test_get_remarks_from_student_float(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args(2.15),
                    raises(TypeError))

    def test_get_remarks_from_student_negative_int(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args(-3),
                    raises(ValueError))

    def test_get_remarks_from_student_negative_float(self):
        assert_that(calling(self.temp_with_students_with_remarks.get_remarks_from_student).with_args(-3.45),
                    raises(TypeError))

    # Testy edit_remark_in_student
    def test_edit_remark_in_student(self):
        assert_that(self.temp_with_students_with_remarks.edit_remark_in_student(1, 1, 'Uwaga 1 po edycji'),
                    equal_to(['Uwaga 1 po edycji', 'Uwaga 2']))

    def test_edit_remark_in_student_2(self):
        assert_that(self.temp_with_students_with_remarks.edit_remark_in_student(1, 2, 'Uwaga 2 po edycji'),
                    equal_to(['Uwaga 1', 'Uwaga 2 po edycji']))

    def test_edit_remark_in_student_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(0, 1, 'Uwaga po edycji'),
            raises(ValueError))

    def test_edit_remark_in_student_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(4, 1, 'Uwaga po edycji'),
            raises(ValueError))

    def test_edit_remark_in_student_remark_id_out_of_range(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 0, 'Uwaga po edycji'),
            raises(ValueError))

    def test_edit_remark_in_student_remark_id_out_of_range_2(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 6, 'Uwaga po edycji'),
            raises(ValueError))

    def test_edit_remark_in_student_id_none(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(None, 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_id_object(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args({}, 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_id_array(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args([], 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_id_true(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(True, 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_id_false(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(False, 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_id_string(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args('abc', 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_id_string_number(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args('2', 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_id_float(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(2.14, 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_id_negative_int(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(-3, 1, 'Uwaga po edycji'),
            raises(ValueError))

    def test_edit_remark_in_student_id_negative_float(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(-2.51, 1, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_none(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, None, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_object(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, {}, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_array(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, [], 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_true(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, True, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_false(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, False, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_string(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 'abc', 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_string_number(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, '3', 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_float(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 2.14, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_remark_id_negative_int(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, -3, 'Uwaga po edycji'),
            raises(ValueError))

    def test_edit_remark_in_student_remark_id_negative_float(self):
        assert_that(
            calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, -2.51, 'Uwaga po edycji'),
            raises(TypeError))

    def test_edit_remark_in_student_text_none(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, None),
                    raises(TypeError))

    def test_edit_remark_in_student_text_object(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, {}),
                    raises(TypeError))

    def test_edit_remark_in_student_text_array(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, []),
                    raises(TypeError))

    def test_edit_remark_in_student_text_true(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, True),
                    raises(TypeError))

    def test_edit_remark_in_student_text_false(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, False),
                    raises(TypeError))

    def test_edit_remark_in_student_text_int(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, 3),
                    raises(TypeError))

    def test_edit_remark_in_student_text_float(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, 3.14),
                    raises(TypeError))

    def test_edit_remark_in_student_text_negative_int(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, -4),
                    raises(TypeError))

    def test_edit_remark_in_student_text_negative_float(self):
        assert_that(calling(self.temp_with_students_with_remarks.edit_remark_in_student).with_args(1, 1, -4.11),
                    raises(TypeError))

    # Testy delete_remark_in_student
    def test_delete_remark_in_student(self):
        assert_that(self.temp_with_students_with_remarks.delete_remark_in_student(1, 1), equal_to(['Uwaga 2']))

    def test_delete_remark_in_student_2(self):
        self.temp_with_students_with_remarks.delete_remark_in_student(1, 2)
        assert_that(self.temp_with_students_with_remarks.delete_remark_in_student(1, 1), equal_to([]))

    def test_delete_remark_in_student_remark_id_out_of_range(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(0, 1),
                    raises(ValueError))

    def test_delete_remark_in_student_remark_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(6, 1),
                    raises(ValueError))

    def test_delete_remark_in_student_id_out_of_range(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, 0),
                    raises(ValueError))

    def test_delete_remark_in_student_id_out_of_range_2(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, 4),
                    raises(ValueError))

    def test_delete_remark_in_student_none_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(None, 1),
                    raises(TypeError))

    def test_delete_remark_in_student_none_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, None),
                    raises(TypeError))

    def test_delete_remark_in_student_none(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(None, None),
                    raises(TypeError))

    def test_delete_remark_in_student_object_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args({}, 1),
                    raises(TypeError))

    def test_delete_remark_in_student_object_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, {}),
                    raises(TypeError))

    def test_delete_remark_in_student_object(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args({}, {}),
                    raises(TypeError))

    def test_delete_remark_in_student_true_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(True, 1),
                    raises(TypeError))

    def test_delete_remark_in_student_true_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, True),
                    raises(TypeError))

    def test_delete_remark_in_student_true(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(True, True),
                    raises(TypeError))

    def test_delete_remark_in_student_false_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(False, 1),
                    raises(TypeError))

    def test_delete_remark_in_student_false_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, False),
                    raises(TypeError))

    def test_delete_remark_in_student_false(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(False, False),
                    raises(TypeError))

    def test_delete_remark_in_student_string_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args('abc', 1),
                    raises(TypeError))

    def test_delete_remark_in_student_string_number_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args('2', 1),
                    raises(TypeError))

    def test_delete_remark_in_student_string_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(2, 'abc'),
                    raises(ValueError))

    def test_delete_remark_in_student_string_number_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(2, '3'),
                    raises(ValueError))

    def test_delete_remark_in_student_string(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args('b2', '3a'),
                    raises(TypeError))

    def test_delete_remark_in_student_float_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(2.31, 1),
                    raises(TypeError))

    def test_delete_remark_in_student_float_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, 1.67),
                    raises(TypeError))

    def test_delete_remark_in_student_float(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(3.12, 4.33),
                    raises(TypeError))

    def test_delete_remark_in_student_negative_int_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(-3, 1),
                    raises(ValueError))

    def test_delete_remark_in_student_negative_int_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, -8),
                    raises(ValueError))

    def test_delete_remark_in_student_negative_int(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(-2, -5),
                    raises(ValueError))

    def test_delete_remark_in_student_negative_float_remark_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(-2.31, 1),
                    raises(TypeError))

    def test_delete_remark_in_student_negative_float_grade_id(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(1, -1.67),
                    raises(TypeError))

    def test_delete_remark_in_student_negative_float(self):
        assert_that(calling(self.temp_with_students_with_remarks.delete_remark_in_student).with_args(-3.12, -4.33),
                    raises(TypeError))

    def test_export_data_to_csv(self):
        assert_that(self.temp_with_student_with_subject_with_grades.export_data_to_csv(),
                    equal_to('Wyeksportowano dane'))

    def test_import_data_from_csv(self):
        assert_that(self.temp_with_student_with_subject_with_grades.import_data_from_csv(),
                    equal_to('Zaimportowano dane'))

    def tearDown(self):
        self.temp = None
        self.temp_with_students = None
        self.temp_with_student_with_subject = None
        self.temp_with_student_with_subject_with_grades = None
        self.temp_with_students_with_remarks = None
