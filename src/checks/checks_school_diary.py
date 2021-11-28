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


def check_subject_name(name):
    if isinstance(name, str):
        return True
    else:
        raise Exception('Nazwa przedmiotu nie jest typu string')
