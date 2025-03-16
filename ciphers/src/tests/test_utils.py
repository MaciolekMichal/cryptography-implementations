import pytest
from ..utils import shift_letter


@pytest.mark.parametrize("letter, offset, expected", [
    ('a', 1, 'b'),
    ('g', 5, 'l'),
    ('m', 3, 'p')
])
def test_shift_letter_unwrapped(letter, offset, expected):
    assert shift_letter(letter, offset) == expected


@pytest.mark.parametrize("letter, offset, expected", [
    ('x', 3, 'a'),
    ('z', 2, 'b'),
    ('w', 6, 'c')
])
def test_shift_letter_wrapped(letter, offset, expected):
    assert shift_letter(letter, offset) == expected


@pytest.mark.parametrize("letter, offset, expected", [
    ('A', 1, 'B'),
    ('X', 3, 'A'),
    ('Z', 4, 'D')
])
def test_shift_letter_uppercase(letter, offset, expected):
    assert shift_letter(letter, offset) == expected


@pytest.mark.parametrize("letter, offset, expected", [
    ('b', -1, 'a'),
    ('a', -2, 'y'),
    ('A', -2, 'Y')
])
def test_shift_letter_negative_shift(letter, offset, expected):
    assert shift_letter(letter, offset) == expected


@pytest.mark.parametrize("letter, offset, expected", [
    ('a', 29, 'd'),
    ('a', 53, 'b'),
    ('z', -27, 'y')
])
def test_shift_letter_large_offets(letter, offset, expected):
    assert shift_letter(letter, offset) == expected


def test_shift_letter_non_alphabetic():
    with pytest.raises(ValueError):
        shift_letter('1', 3)
    
    with pytest.raises(ValueError):
        shift_letter('*', 5)
