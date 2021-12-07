import unittest
from src.school_diary import SchoolDiary


class SchoolDiaryParamterizedFile(unittest.TestCase):

    def test_SchoolDiary_from_file(self):
        # Przu odpalaniu testów za pomocą nose2 ścieżka do pliku powinna być taka "data/data_test_SchoolDiary"
        # Przu odpalaniu testów za pomocą pycharm ścieżka do pliku powinna być taka "../data/data_test_SchoolDiary"
        filetest = open("data/data_test_SchoolDiary")
        temp = SchoolDiary()
        temp.add_student('Jan', 'Kowalski', 12)
        temp.add_student('Ola', 'Kot', 8)
        temp.add_remark_to_student(1, 'Uwaga1')
        temp.add_remark_to_student(1, 'Uwaga2')
        for line in filetest:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                if data[0] == 'add':
                    student_id, text, result = int(data[1]), data[2], eval(data[3])
                    self.assertEqual(temp.add_remark_to_student(student_id, text), result)
                elif data[0] == 'get':
                    student_id, result = int(data[1]), eval(data[2])
                    self.assertEqual(temp.get_remarks_from_student(student_id), result)
                elif data[0] == 'edit':
                    student_id, remark_id, text, result = int(data[1]), int(data[2]), data[3], eval(data[4])
                    self.assertEqual(temp.edit_remark_in_student(student_id, remark_id, text), result)
                elif data[0] == 'del':
                    student_id, remark_id, result = int(data[1]), int(data[2]), eval(data[3])
                    self.assertEqual(temp.delete_remark_in_student(student_id, remark_id), result)
        filetest.close()


if __name__ == '__main__':
    unittest.main()
