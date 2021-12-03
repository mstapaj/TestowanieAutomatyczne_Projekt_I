import pytest
from src.checks.checks_school_diary import check_firstname, check_lastname, check_age
from src.checks.checks_student import check_remark_text
from src.checks.checks_school_subject import check_subject_name, check_grade


# Testy check_firstname
def test_check_firstname():
    assert check_firstname('Jan') == True


def test_check_firstname_2():
    assert check_firstname('Ola') == True


def test_check_firstname_3():
    assert check_firstname('abcdefghijklmnopqrsteuwyxz') == True


def test_check_firstname_none():
    with pytest.raises(TypeError):
        check_firstname(None)


def test_check_firstname_object():
    with pytest.raises(TypeError):
        check_firstname([])


def test_check_firstname_array():
    with pytest.raises(TypeError):
        check_firstname({})


def test_check_firstname_true():
    with pytest.raises(TypeError):
        check_firstname(True)


def test_check_firstname_false():
    with pytest.raises(TypeError):
        check_firstname(False)


def test_check_firstname_int():
    with pytest.raises(TypeError):
        check_firstname(12)


def test_check_firstname_float():
    with pytest.raises(TypeError):
        check_firstname(4.12)


def test_check_firstname_negative_int():
    with pytest.raises(TypeError):
        check_firstname(-3)


def test_check_firstname_negative_float():
    with pytest.raises(TypeError):
        check_firstname(-7.12)


# Testy check_lastname
def test_check_lastname():
    assert check_lastname('Kowalski') == True


def test_check_lastname_2():
    assert check_lastname('Nowak') == True


def test_check_lastname_3():
    assert check_lastname('abcdefghijklmnopqrsteuwyxz') == True


def test_check_lastname_none():
    with pytest.raises(TypeError):
        check_lastname(None)


def test_check_lastname_object():
    with pytest.raises(TypeError):
        check_lastname([])


def test_check_lastname_array():
    with pytest.raises(TypeError):
        check_lastname({})


def test_check_lastname_true():
    with pytest.raises(TypeError):
        check_lastname(True)


def test_check_lastname_false():
    with pytest.raises(TypeError):
        check_lastname(False)


def test_check_lastname_int():
    with pytest.raises(TypeError):
        check_lastname(12)


def test_check_lastname_float():
    with pytest.raises(TypeError):
        check_lastname(4.12)


def test_check_lastname_negative_int():
    with pytest.raises(TypeError):
        check_lastname(-3)


def test_check_lastname_negative_float():
    with pytest.raises(TypeError):
        check_lastname(-7.12)
