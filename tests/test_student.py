import unittest
from hamcrest import *
from src.student import Student

class test_Student(unittest.TestCase):
    def setUp(self):
        self.temp = Student('Jan', 'Kowalski', 12)

    def test_get_details(self):
        assert_that(self.temp.get_details(), equal_to({
            'firstname': 'Jan',
            'lastname': 'Kowalski',
            'age': 12
        }))