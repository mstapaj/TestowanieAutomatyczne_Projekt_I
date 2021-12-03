def check_subject_name(name):
    if isinstance(name, str):
        return True
    else:
        raise TypeError('Nazwa przedmiotu nie jest typu string')


def check_grade(grade):
    if isinstance(grade, int) and str(grade) != 'True' and str(grade) != 'False':
        if 0 < grade < 7:
            return True
        else:
            raise ValueError('Ocena nie jest z przedziału 1-6')
    else:
        raise TypeError('Ocena nie jest typu int')


def check_grade_id(grade_id, subject):
    if isinstance(grade_id, int) and str(grade_id) != "True" and str(grade_id) != "False":
        if 0 < grade_id < len(subject.grades) + 1:
            return True
        else:
            raise ValueError('Brak oceny o takim Id')
    else:
        raise TypeError('Id oceny nie jest typu int')
