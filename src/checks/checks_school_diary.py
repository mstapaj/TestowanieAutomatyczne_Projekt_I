def check_firstname(firstname):
    if isinstance(firstname, str):
        return True
    else:
        raise TypeError('Błedny typ danych w imieniu')


def check_lastname(lastname):
    if isinstance(lastname, str):
        return True
    else:
        raise TypeError('Błedny typ danych w nazwisku')


def check_age(age):
    if isinstance(age, int) and str(age) != 'True' and str(age) != 'False':
        if 0 < age:
            return True
        else:
            raise ValueError('Wiek jest poniżej 0')
    else:
        raise TypeError('Błedny typ danych w wieku')


def check_student_id(student_id, diary):
    if isinstance(student_id, int) and str(student_id) != 'True' and str(student_id) != 'False':
        if 0 < student_id < len(diary.students) + 1:
            return True
        else:
            raise ValueError('Brak ucznia o takim Id')
    else:
        raise TypeError('Id ucznia nie jest typu int')


def check_subject_id(student_id, subject_id, diary):
    if isinstance(subject_id, int) and str(subject_id) != 'True' and str(subject_id) != 'False':
        number_of_subjects = len(diary.students[student_id - 1].get_subjects())
        if 0 < subject_id < number_of_subjects + 1:
            return True
        else:
            raise ValueError('Brak przedmiotu o takim Id')
    else:
        raise TypeError('Id przedmiotu nie jest typu int')


def check_grade_id(student_id, subject_id, grade_id, diary):
    if isinstance(grade_id, int) and str(grade_id) != 'True' and str(grade_id) != 'False':
        number_of_grades = len(diary.students[student_id - 1].get_grades(subject_id))
        if 0 < grade_id < number_of_grades + 1:
            return True
        else:
            raise ValueError('Brak oceny o takim Id')
    else:
        raise TypeError('Id oceny nie jest typu int')


def check_remark_id(student_id, remark_id, diary):
    if isinstance(remark_id, int) and str(remark_id) != 'True' and str(remark_id) != 'False':
        number_of_remarks = len(diary.students[student_id - 1].get_remarks())
        if 0 < remark_id < number_of_remarks + 1:
            return True
        else:
            raise ValueError('Brak uwagi o takim Id')
    else:
        raise TypeError('Id uwagi nie jest typu int')
