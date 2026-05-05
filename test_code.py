import pytest
from src import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5
    assert subtract(-2, -3) == 1


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == pytest.approx(5.0)
    assert divide(7, 2) == pytest.approx(3.5)
    assert divide(-9, 3) == pytest.approx(-3.0)


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
