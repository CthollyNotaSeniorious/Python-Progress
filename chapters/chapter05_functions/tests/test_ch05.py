from ..exercises.exercise_30 import increment_value_by
from ..exercises.exercise_31 import is_palindrome
from ..exercises.exercise_32 import factorial
from ..exercises.exercise_33 import fibonacci
from ..exercises.exercise_34 import apply_vouchers
from ..exercises.exercise_35 import find_max
from ..exercises.exercise_36 import sum_digits
from ..exercises.exercise_37 import multiply
from ..exercises.exercise_38 import count_vowels
from ..exercises.exercise_39 import count_char_freq


def test_e30():
    assert increment_value_by(5, 5) == 10
    assert increment_value_by(10, 2) == 12
    assert increment_value_by(10) == 11


def test_e31():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("mom") is True


def test_e32():
    assert factorial(5) == 120
    assert factorial(4) == 24
    assert factorial(3) == 6


def test_e33():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765


def test_e34():
    def ten_percent(x: int):
        return x - (x * 0.10)

    def fifteen_percent(x: int):
        return x - (x * 0.15)

    def five_dollar(x: int):
        return x - 5

    assert apply_vouchers([ten_percent], total=100) == 90
    assert apply_vouchers([fifteen_percent], total=100) == 85
    assert apply_vouchers([five_dollar], total=100) == 95
    assert apply_vouchers([ten_percent, fifteen_percent], total=100) == 76.5
    assert (
        apply_vouchers([ten_percent, fifteen_percent, five_dollar], total=100) == 71.5
    )


def test_e35():
    assert find_max(1) == 1
    assert find_max(-1, -10, 8, 5) == 8
    assert find_max(1, 2, 3) == 3
    assert find_max(10, 20, 30) == 30
    assert find_max(100, 200, 300) == 300


def test_e36():
    assert sum_digits("") == 0
    assert sum_digits("1") == 1
    assert sum_digits("123") == 6
    assert sum_digits("123456") == 21
    assert sum_digits("123456789") == 45


def test_e37():
    assert multiply(5, 5) == 25
    assert multiply(10, 2) == 20
    assert multiply(10, 0) == 0


def test_e38():
    assert count_vowels("hello") == 2
    assert count_vowels("world") == 1
    assert count_vowels("applepie") == 4
    assert count_vowels("racecar") == 3
    assert count_vowels("headphones") == 4


def test_e39():
    assert count_char_freq("hello", "l") == 2
    assert count_char_freq("hello", "o") == 1
    assert count_char_freq("Programming in python", "p") == 1
    assert count_char_freq("Programming in python".lower(), "p") == 2
