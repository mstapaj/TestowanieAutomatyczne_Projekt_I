def check_subject_id(subject_id, student):
    if isinstance(subject_id, int) and str(subject_id) != "True" and str(subject_id) != "False":
        if 0 < subject_id < len(student.subjects) + 1:
            return True
        else:
            raise ValueError('Brak przedmiotu o takim Id')
    else:
        raise TypeError('Id przedmiotu nie jest typu int')


def check_grade_id(subject_id, grade_id, student):
    if isinstance(grade_id, int) and str(grade_id) != 'True' and str(grade_id) != 'False':
        number_of_grades = len(student.subjects[subject_id - 1].get_details()['grades'])
        if 0 < grade_id < number_of_grades + 1:
            return True
        else:
            raise ValueError('Brak oceny o takim Id')
    else:
        raise TypeError('Id oceny nie jest typu int')


def check_remark_text(text):
    if isinstance(text, str):
        return True
    else:
        raise TypeError('Treść uwagi nie jest typu string')


def check_remark_id(remark_id, student):
    if isinstance(remark_id, int) and str(remark_id) != "True" and str(remark_id) != "False":
        if 0 < remark_id < len(student.remarks) + 1:
            return True
        else:
            raise ValueError('Brak uwagi o takim Id')
    else:
        raise TypeError('Id uwagi nie jest typu int')
