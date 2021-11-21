def check_subject_name(name):
    if isinstance(name, str):
        return True
    else:
        raise Exception('Nazwa przedmiotu nie jest typu string')

def check_subject_id(subject_id, object):
    if isinstance(subject_id, int) and str(subject_id) != "True" and str(subject_id) != "False":
        if 0 < subject_id < len(object.subjects) + 1:
            return True
        else:
            raise Exception('Brak przedmiotu o takim Id')
    else:
        raise Exception('Id przedmiotu nie jest typu int')