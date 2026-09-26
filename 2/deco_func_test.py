import pytest

from deco_func import retry_deco


@retry_deco(3)
def add(a, b):
    return a + b


@retry_deco(3)
def check_str(value=None):
    if value is None:
        raise ValueError()

    return isinstance(value, str)


@retry_deco(2, [ValueError])
def check_int(value=None):
    if value is None:
        raise ValueError()

    return isinstance(value, int)


def test_add_positional_args():
    assert add(4, 2) == 6


def test_add_keyword_args():
    assert add(4, b=3) == 7


def test_check_str_true():
    assert check_str(value="123") is True


def test_check_str_false():
    assert check_str(value=1) is False


def test_check_str_exception():
    with pytest.raises(ValueError):
        check_str(value=None)


def test_check_int_true():
    assert check_int(value=1) is True


def test_check_int_expected_exception():
    with pytest.raises(ValueError):
        check_int(value=None)
