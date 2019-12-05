from functools import partial
from ipynb.fs.defs.aoc.day_04 import _digits, adjacent_pt1, increase, adjacent_pt2


def test_digits():
    digits = partial(_digits, 6)
    assert not digits(1000)
    assert not digits(10000)
    assert digits(100000)
    assert digits(999999)
    assert not digits(1000000)


def test_adjacent_pt1():
    assert adjacent_pt1(122345)
    assert adjacent_pt1(123444)
    assert not adjacent_pt1(123789)
    assert adjacent_pt1(111111)


def test_increase():
    assert increase(111123)
    assert increase(135679)
    assert not increase(223450)


def test_adjacent_pt2():
    assert adjacent_pt2(112233)
    assert not adjacent_pt2(123444)
    assert adjacent_pt2(111122)
