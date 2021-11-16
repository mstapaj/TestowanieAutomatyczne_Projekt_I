import unittest
from assertpy import *
from src.school_subject import SchoolSubject


class test_SchoolSubject(unittest.TestCase):
    def setUp(self):
        self.temp = SchoolSubject('Polski')

    # Testy get_details
    def test_get_details(self):
        assert_that(self.temp.get_details()).is_equal_to({
            'name': 'Polski',
            'grades': []
        })

    # Testy edit_subject
    def test_edit_subject_Matematyka(self):
        assert_that(self.temp.edit_subject('Matematyka')).is_equal_to({
            'name': 'Matematyka',
            'grades': []
        })

    def test_edit_subject_int(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with(25)

    def test_edit_subject_float(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with(2.5)

    def test_edit_subject_negative_int(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with(-10)

    def test_edit_subject_negative_float(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with(-3.2)

    def test_edit_subject_object(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with({})

    def test_edit_subject_array(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with([])

    def test_edit_subject_none(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with(None)

    def test_edit_subject_true(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with(True)

    def test_edit_subject_false(self):
        assert_that(self.temp.edit_subject).raises(Exception).when_called_with(False)

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
        assert_that(self.temp.add_grade(5)).is_equal_to({
            'name': 'Polski',
            'grades': [5]
        })
        assert_that(self.temp.add_grade(3)).is_equal_to({
            'name': 'Polski',
            'grades': [5, 3]
        })

    def test_add_grade_1(self):
        assert_that(self.temp.add_grade(1)).is_equal_to({
            'name': 'Polski',
            'grades': [1]
        })

    def test_add_grade_7(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with(7)

    def test_add_grade_0(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with(0)

    def test_add_grade_negative_int(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with(-2)

    def test_add_grade_negative_float(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with(-3.1)

    def test_add_grade_float(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with(2.45)

    def test_add_grade_object(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with({})

    def test_add_grade_array(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with([])

    def test_add_grade_none(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with(None)

    def test_add_grade_true(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with(True)

    def test_add_grade_false(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with(False)

    def test_add_grade_string(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with('abc')

    def test_add_grade_string_number(self):
        assert_that(self.temp.add_grade).raises(Exception).when_called_with('5')