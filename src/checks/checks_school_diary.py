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