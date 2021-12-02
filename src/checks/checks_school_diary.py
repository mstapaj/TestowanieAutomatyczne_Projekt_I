def check_firstname(firstname):
    if isinstance(firstname, str):
        return True
    else:
        raise Exception('Błedny typ danych w imieniu')


def check_lastname(lastname):
    if isinstance(lastname, str):
        return True
    else:
        raise Exception('Błedny typ danych w nazwisku')


def check_age(age):
    if isinstance(age, int) and str(age) != 'True' and str(age) != 'False':
        if 0 < age:
            return True
        else:
            raise Exception('Wiek jest poniżej 0')
    else:
        raise Exception('Błedny typ danych w wieku')


def check_id(id, object):
    if isinstance(id, int) and str(id) != 'True' and str(id) != 'False':
        if 0 < id < len(object.students) + 1:
            return True
        else:
            raise Exception('Brak ucznia o takim Id')
    else:
        raise Exception('Id ucznia nie jest typu int')


def check_subject_id(id, subject_id, object):
    if isinstance(subject_id, int) and str(subject_id) != 'True' and str(subject_id) != 'False':
        number_of_subjects = len(object.students[id - 1].get_subjects())
        if 0 < subject_id < number_of_subjects + 1:
            return True
        else:
            raise Exception('Brak przedmiotu o takim Id')
    else:
        raise Exception('Id przedmiotu nie jest typu int')


def check_grade_id(id, subject_id, grade_id, object):
    if isinstance(grade_id, int) and str(grade_id) != 'True' and str(grade_id) != 'False':
        number_of_grades = len(object.students[id - 1].get_grades(subject_id))
        if 0 < grade_id < number_of_grades + 1:
            return True
        else:
            raise Exception('Brak oceny o takim Id')
    else:
        raise Exception('Id oceny nie jest typu int')


def check_remark_id(id, remark_id, object):
    if isinstance(remark_id, int) and str(remark_id) != 'True' and str(remark_id) != 'False':
        number_of_remarks = len(object.students[id - 1].get_remarks())
        if 0 < remark_id < number_of_remarks + 1:
            return True
        else:
            raise Exception('Brak uwagi o takim Id')
    else:
        raise Exception('Id uwagi nie jest typu int')
