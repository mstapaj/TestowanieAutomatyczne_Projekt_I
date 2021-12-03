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


# Testy check_age
def test_check_age():
    assert check_age(12) == True


def test_check_age_2():
    assert check_age(8) == True


def test_check_age_3():
    assert check_age(75) == True


def test_check_age_below_zero():
    with pytest.raises(ValueError):
        check_age(-2)


def test_check_age_none():
    with pytest.raises(TypeError):
        check_age(None)


def test_check_age_object():
    with pytest.raises(TypeError):
        check_age([])


def test_check_age_array():
    with pytest.raises(TypeError):
        check_age({})


def test_check_age_true():
    with pytest.raises(TypeError):
        check_age(True)


def test_check_age_false():
    with pytest.raises(TypeError):
        check_age(False)


def test_check_age_string():
    with pytest.raises(TypeError):
        check_age('abc')


def test_check_age_string_number():
    with pytest.raises(TypeError):
        check_age('12')


def test_check_age_float():
    with pytest.raises(TypeError):
        check_age(4.12)


def test_check_age_negative_int():
    with pytest.raises(ValueError):
        check_age(-3)


def test_check_age_negative_float():
    with pytest.raises(TypeError):
        check_age(-7.12)


# Testy check_remark_text
def test_check_remark_text():
    assert check_remark_text('Uwaga1') == True


def test_check_remark_text_2():
    assert check_remark_text('Uwaga z większą ilością tekstu') == True


def test_check_remark_text_3():
    assert check_remark_text('Bardzo długa uwaga '
                             'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb') \
           == True


def test_check_remark_text_none():
    with pytest.raises(TypeError):
        check_remark_text(None)


def test_check_remark_text_object():
    with pytest.raises(TypeError):
        check_remark_text([])


def test_check_remark_text_array():
    with pytest.raises(TypeError):
        check_remark_text({})


def test_check_remark_text_true():
    with pytest.raises(TypeError):
        check_remark_text(True)


def test_check_remark_text_false():
    with pytest.raises(TypeError):
        check_remark_text(False)


def test_check_remark_text_int():
    with pytest.raises(TypeError):
        check_remark_text(12)


def test_check_remark_text_float():
    with pytest.raises(TypeError):
        check_remark_text(4.12)


def test_check_remark_text_negative_int():
    with pytest.raises(TypeError):
        check_remark_text(-3)


def test_check_remark_text_negative_float():
    with pytest.raises(TypeError):
        check_remark_text(-7.12)
