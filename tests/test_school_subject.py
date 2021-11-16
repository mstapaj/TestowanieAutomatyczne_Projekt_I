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