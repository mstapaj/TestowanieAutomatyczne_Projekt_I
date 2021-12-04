import unittest
from assertpy import *
from src.school_subject import SchoolSubject


def is_length_of_grades_above_or_equal_2(self):
    if len(self.val['grades']) < 2:
        return self.error('Ilość ocen nie jest równe lub powyżej 2!')
    return self


add_extension(is_length_of_grades_above_or_equal_2)


class test_SchoolSubject(unittest.TestCase):
    def setUp(self):
        self.temp = SchoolSubject('Polski')
        self.temp_with_grades = SchoolSubject('Matematyka')
        self.temp_with_grades.add_grade(3)
        self.temp_with_grades.add_grade(6)
        self.temp_with_grades_2 = SchoolSubject('Angielski')
        self.temp_with_grades_2.add_grade(1)
        self.temp_with_grades_2.add_grade(4)
        self.temp_with_grades_2.add_grade(6)

    # Testy get_details
    def test_get_details(self):
        assert_that(self.temp.get_details()).is_equal_to({
            'name': 'Polski',
            'grades': []
        })

    def test_get_details_2(self):
        assert_that(self.temp_with_grades.get_details()).is_equal_to({
            'name': 'Matematyka',
            'grades': [3, 6]
        })

    def test_get_details_is_not_none(self):
        assert_that(self.temp_with_grades.get_details()).is_not_none()

    def test_get_details_contains_key_grades(self):
        assert_that(self.temp_with_grades.get_details()).contains_key('grades')

    def test_get_details_contains_key_name(self):
        assert_that(self.temp_with_grades.get_details()).contains_key('name')

    def test_get_details_custom_matcher(self):
        assert_that(self.temp_with_grades.get_details()).is_length_of_grades_above_or_equal_2()

    # Testy edit_subject
    def test_edit_subject_Matematyka(self):
        assert_that(self.temp.edit_subject('Matematyka')).is_equal_to({
            'name': 'Matematyka',
            'grades': []
        })

    def test_edit_subject_Angielski_is_type_of(self):
        assert_that(self.temp_with_grades.edit_subject('Angielski')).contains_value('Angielski')

    def test_edit_subject_Fizyka_is_not_none(self):
        assert_that(self.temp.edit_subject('Fizyka')).is_not_none()

    def test_edit_subject_contains_key_grades(self):
        assert_that(self.temp_with_grades.edit_subject('Chemia')).contains_key('grades')

    def test_edit_subject_contains_key_name(self):
        assert_that(self.temp_with_grades.edit_subject('Biologia')).contains_key('name')

    # Test nie przechodzi zgodnie z założeniami matchera
    # def test_edit_subject_custom_matcher_failed(self):
    #     assert_that(self.temp.edit_subject('Fizyka')).is_length_of_grades_above_or_equal_2()

    def test_edit_subject_int(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with(25)

    def test_edit_subject_float(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with(2.5)

    def test_edit_subject_negative_int(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with(-10)

    def test_edit_subject_negative_float(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with(-3.2)

    def test_edit_subject_object(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with({})

    def test_edit_subject_array(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with([])

    def test_edit_subject_none(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with(None)

    def test_edit_subject_true(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with(True)

    def test_edit_subject_false(self):
        assert_that(self.temp.edit_subject).raises(TypeError).when_called_with(False)

    # Testy add_grade
    def test_add_grade_2(self):
        assert_that(self.temp.add_grade(2)).is_equal_to({
            'name': 'Polski',
            'grades': [2]
        })

    def test_add_grade_5(self):
        assert_that(self.temp.add_grade(5)).is_equal_to({
            'name': 'Polski',
            'grades': [5]
        })

    def test_add_grade_5_3(self):
        self.temp.add_grade(5)
        assert_that(self.temp.add_grade(3)).is_equal_to({
            'name': 'Polski',
            'grades': [5, 3]
        })

    def test_add_grade_2_4_3(self):
        self.temp.add_grade(2)
        self.temp.add_grade(4)
        assert_that(self.temp.add_grade(3)).is_length_of_grades_above_or_equal_2()

    def test_add_grade_1(self):
        assert_that(self.temp.add_grade(1)).is_equal_to({
            'name': 'Polski',
            'grades': [1]
        })

    def test_add_grade_6_is_type_of(self):
        assert_that(self.temp.add_grade(6)).contains_value([6])

    def test_add_grade_7(self):
        assert_that(self.temp.add_grade).raises(ValueError).when_called_with(7)

    def test_add_grade_0(self):
        assert_that(self.temp.add_grade).raises(ValueError).when_called_with(0)

    def test_add_grade_negative_int(self):
        assert_that(self.temp.add_grade).raises(ValueError).when_called_with(-2)

    def test_add_grade_negative_float(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with(-3.1)

    def test_add_grade_float(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with(2.45)

    def test_add_grade_object(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with({})

    def test_add_grade_array(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with([])

    def test_add_grade_none(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with(None)

    def test_add_grade_true(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with(True)

    def test_add_grade_false(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with(False)

    def test_add_grade_string(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with('abc')

    def test_add_grade_string_number(self):
        assert_that(self.temp.add_grade).raises(TypeError).when_called_with('5')

    # Testy edit_grade
    def test_edit_grade_3_to_1(self):
        assert_that(self.temp_with_grades.edit_grade(1, 1)).is_equal_to({
            'name': 'Matematyka',
            'grades': [1, 6]
        })

    def test_edit_grade_6_to_4(self):
        assert_that(self.temp_with_grades.edit_grade(2, 4)).is_equal_to({
            'name': 'Matematyka',
            'grades': [3, 4]
        })

    def test_edit_grade_3_to_2_custom_matcher(self):
        assert_that(self.temp_with_grades.edit_grade(1, 2)).is_length_of_grades_above_or_equal_2()

    def test_edit_grade_3_to_2_is_type_of(self):
        assert_that(self.temp_with_grades.edit_grade(1, 2)).contains_value([2,6])

    def test_edit_grade_id_out_of_range(self):
        assert_that(self.temp_with_grades.edit_grade).raises(ValueError).when_called_with(4, 4)

    def test_edit_grade_id_out_of_range_2(self):
        assert_that(self.temp_with_grades.edit_grade).raises(ValueError).when_called_with(-3, 4)

    def test_edit_grade_grade_out_of_range(self):
        assert_that(self.temp_with_grades.edit_grade).raises(ValueError).when_called_with(1, 7)

    def test_edit_grade_grade_out_of_range_2(self):
        assert_that(self.temp_with_grades.edit_grade).raises(ValueError).when_called_with(1, -5)

    def test_edit_grade_string_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with('Polski', 4)

    def test_edit_grade_string_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(1, 'abc')

    def test_edit_grade_string(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with('Polski', 'abc')

    def test_edit_grade_float_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(3.14, 4)

    def test_edit_grade_float_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(1, 3.14)

    def test_edit_grade_float(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(3.14, 2.56)

    def test_edit_grade_negative_float_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(-3.14, 4)

    def test_edit_grade_negative_float_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(1, -3.14)

    def test_edit_grade_negative_float(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(-3.14, -2.56)

    def test_edit_grade_negative_int_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(ValueError).when_called_with(-3, 4)

    def test_edit_grade_negative_int_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(ValueError).when_called_with(1, -3)

    def test_edit_grade_negative_int(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(-3.14, -2)

    def test_edit_grade_none_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(None, 4)

    def test_edit_grade_none_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(1, None)

    def test_edit_grade_none(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(None, None)

    def test_edit_grade_object_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with({}, 4)

    def test_edit_grade_object_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(1, {})

    def test_edit_grade_object(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with({}, {})

    def test_edit_grade_array_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with([], 4)

    def test_edit_grade_array_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(1, [])

    def test_edit_grade_array(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with([], [])

    def test_edit_grade_true_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(True, 4)

    def test_edit_grade_true_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(1, True)

    def test_edit_grade_true(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(True, True)

    def test_edit_grade_false_id(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(False, 4)

    def test_edit_grade_false_grade(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(1, False)

    def test_edit_grade_false(self):
        assert_that(self.temp_with_grades.edit_grade).raises(TypeError).when_called_with(False, False)

    # Testy delete_grade
    def test_delete_grade(self):
        assert_that(self.temp_with_grades.delete_grade(1)).is_equal_to({
            'name': 'Matematyka',
            'grades': [6]
        })

    def test_delete_grade_2(self):
        assert_that(self.temp_with_grades.delete_grade(2)).is_equal_to({
            'name': 'Matematyka',
            'grades': [3]
        })

    def test_delete_grade_3(self):
        self.temp_with_grades.delete_grade(2)
        assert_that(self.temp_with_grades.delete_grade(1)).is_equal_to({
            'name': 'Matematyka',
            'grades': []
        })

    def test_delete_grade_is_not_none(self):
        self.temp_with_grades.delete_grade(2)
        assert_that(self.temp_with_grades.delete_grade(1)).is_not_none()

    def test_delete_grade_contains_key_grades(self):
        assert_that(self.temp_with_grades.delete_grade(1)).contains_key('grades')

    def test_delete_grade_contains_key_name(self):
        assert_that(self.temp_with_grades.delete_grade(2)).contains_key('name')

    def test_delete_grade_out_of_range(self):
        assert_that(self.temp.delete_grade).raises(ValueError).when_called_with(0)

    def test_delete_grade_out_of_range_2(self):
        assert_that(self.temp.delete_grade).raises(ValueError).when_called_with(3)

    def test_delete_grade_out_of_range_8(self):
        assert_that(self.temp.delete_grade).raises(ValueError).when_called_with(8)

    def test_delete_grade_negative_int(self):
        assert_that(self.temp.delete_grade).raises(ValueError).when_called_with(-2)

    def test_delete_grade_negative_float(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with(-3.1)

    def test_delete_grade_float(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with(2.45)

    def test_delete_grade_object(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with({})

    def test_delete_grade_array(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with([])

    def test_delete_grade_none(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with(None)

    def test_delete_grade_true(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with(True)

    def test_delete_grade_false(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with(False)

    def test_delete_grade_string(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with('abc')

    def test_delete_grade_string_number(self):
        assert_that(self.temp.delete_grade).raises(TypeError).when_called_with('5')

    # Testy average_of_subject
    def test_average_of_subject(self):
        assert_that(self.temp_with_grades.average_of_subject()).is_equal_to(4.5)

    def test_average_of_subject_2(self):
        assert_that(self.temp_with_grades_2.average_of_subject()).is_equal_to(3.67)

    def test_average_of_subject_is_not_zero(self):
        assert_that(self.temp_with_grades.average_of_subject()).is_not_zero()

    def test_average_of_subject_is_not_zero_2(self):
        assert_that(self.temp_with_grades_2.average_of_subject()).is_not_zero()

    def tearDown(self):
        self.temp = None
        self.temp_with_grades = None
        self.temp_with_grades_2 = None
