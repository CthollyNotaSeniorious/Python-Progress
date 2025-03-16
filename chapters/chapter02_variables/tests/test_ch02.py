from ..exercises.exercise_01 import hours_to_seconds
from ..exercises.exercise_02 import celsius_to_fahrenheit
from ..exercises.exercise_03 import add_numbers
from ..exercises.exercise_04 import compute_length_difference
from ..exercises.exercise_05 import compute_average_grade
from ..exercises.exercise_06 import convert_binary_to_decimal
from ..exercises.exercise_07 import calculate_midpoint


def test_e01():
    assert hours_to_seconds(0) == 0
    assert hours_to_seconds(1) == 3600
    assert hours_to_seconds(2) == 7200
    assert hours_to_seconds(3) == 10800


def test_e02():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(37) == 98.6


def test_e03():
    assert add_numbers("0", "0") == "0"
    assert add_numbers("1", "2") == "3"
    assert add_numbers("100", "100") == "200"
    assert add_numbers("-1000", "500") == "-500"


def test_e04():
    assert compute_length_difference("", "") == 0
    assert compute_length_difference("Hello", "World") == 0
    assert compute_length_difference("Python", "Java") == 2
    assert compute_length_difference("Python", "Programming") == 5


def test_e05():
    assert compute_average_grade(100, 100, 100) == 100
    assert compute_average_grade(94, 94, 95) == 94.33
    assert compute_average_grade(88, 77, 66) == 77
    assert compute_average_grade(72.5, 66.8, 50.5) == 63.27


def test_e06():
    assert convert_binary_to_decimal("0") == 0
    assert convert_binary_to_decimal("10") == 2
    assert convert_binary_to_decimal("11") == 3
    assert convert_binary_to_decimal("100") == 4


def test_e07():
    assert calculate_midpoint(0, 0, 0, 0) == (0.0, 0.0)
    assert calculate_midpoint(1, 2, 3, 4) == (2.0, 3.0)
    assert calculate_midpoint(5, 10, 15, 20) == (10.0, 15.0)
    assert calculate_midpoint(-5, -10, -15, -20) == (-10.0, -15.0)
