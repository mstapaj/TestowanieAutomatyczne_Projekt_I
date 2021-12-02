def check_subject_id(subject_id, object):
    if isinstance(subject_id, int) and str(subject_id) != "True" and str(subject_id) != "False":
        if 0 < subject_id < len(object.subjects) + 1:
            return True
        else:
            raise Exception('Brak przedmiotu o takim Id')
    else:
        raise Exception('Id przedmiotu nie jest typu int')


def check_grade_id(subject_id, grade_id, object):
    if isinstance(grade_id, int) and str(grade_id) != 'True' and str(grade_id) != 'False':
        number_of_grades = len(object.subjects[subject_id - 1].get_details()['grades'])
        if 0 < grade_id < number_of_grades + 1:
            return True
        else:
            raise Exception('Brak oceny o takim Id')
    else:
        raise Exception('Id oceny nie jest typu int')


def check_remark_text(text):
    if isinstance(text, str):
        return True
    else:
        raise Exception('Treść uwagi nie jest typu string')


def check_remark_id(remark_id, object):
    if isinstance(remark_id, int) and str(remark_id) != "True" and str(remark_id) != "False":
        if 0 < remark_id < len(object.remarks) + 1:
            return True
        else:
            raise Exception('Brak uwagi o takim Id')
    else:
        raise Exception('Id uwagi nie jest typu int')
