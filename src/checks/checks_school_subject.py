def check_subject_name(name):
    if isinstance(name, str):
        return True
    else:
        raise Exception('Nazwa przedmiotu nie jest typu string')


def check_grade(grade):
    if isinstance(grade, int) and str(grade) != 'True' and str(grade) != 'False':
        if 0 < grade < 7:
            return True
        else:
            raise Exception('Ocena nie jest z przedziału 1-6')
    else:
        raise Exception('Ocena nie jest typu int')
