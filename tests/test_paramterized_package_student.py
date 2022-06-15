import unittest
from src.student import Student
from parameterized import parameterized, parameterized_class
from assertpy import assert_that


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.temp = Student('Jan', 'Kowalski', 12,
                            [{'name': 'Polski', 'grades': [5]}, {'name': 'Biologia', 'grades': [2, 4]}])

    @parameterized.expand([
        ('N', 1, 5),
        ('N', 2, 3),
        ('E', None, TypeError),
        ('E', True, TypeError),
        ('E', False, TypeError),
        ('E', [], TypeError),
        ('E', {}, TypeError),
        ('E', 'abc', TypeError),
        ('E', '23', TypeError),
        ('E', -2, ValueError),
        ('E', 8, ValueError),
        ('E', 2.78, TypeError),
        ('E', -4.12, TypeError)
    ])
    def test_average_of_subject(self, type_of_test, subject_id, output):
        if type_of_test == 'N':
            self.assertEqual(self.temp.average_of_subject(subject_id), output)
        elif type_of_test == 'E':
            self.assertRaises(output, self.temp.average_of_subject, subject_id)


@parameterized_class(('type_of_test', 'output'), [
    ('N1', 4),
    ('N2', 5.5)
])
class TestAverageOfStudent(unittest.TestCase):

    def setUp(self):
        self.temp = Student('Ola', 'Kot', 8,
                            [{'name': 'Fizyka', 'grades': [2]}, {'name': 'Matematyka', 'grades': [6, 6]}])
        self.temp2 = Student('Paweł', 'Pawłowski', 7, [{'name': 'Fizyka', 'grades': [6]}, {'name': 'Matematyka',
                                                                                           'grades': [4, 6]}])

    def test_average_of_student_Parameterized(self):
        if self.type_of_test == 'N1':
            self.assertEqual(self.temp.average_of_student(), self.output)
        elif self.type_of_test == 'N2':
            self.assertEqual(self.temp2.average_of_student(), self.output)


# Test odpala sie tylko przy pomocy nose2
@parameterized([
    (1, 2),
    (2, 3),
    (3, 1.33)
])
def test_average_of_subject(subject_id, output):
    temp = Student('Ola', 'Kot', 8, [{'name': 'Fizyka', 'grades': [1, 3]}, {'name': 'Matematyka', 'grades': [3]},
                                     {'name': 'Polski', 'grades': [1, 1, 2]}])
    assert_that(temp.average_of_subject(subject_id)).is_equal_to(output)


if __name__ == '__main__':
    unittest.main()
