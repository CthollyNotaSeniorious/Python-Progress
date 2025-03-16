from ..exercises.exercise_15 import fizzbuzz
from ..exercises.exercise_16 import is_prime
from ..exercises.exercise_17 import is_alice_happy
from ..exercises.exercise_18 import check_number
from ..exercises.exercise_19 import is_even
from ..exercises.exercise_20 import grade_result
from ..exercises.exercise_21 import sum_numbers
from ..exercises.exercise_22 import sum_even_numbers
from ..exercises.exercise_23 import largest_index
from ..exercises.exercise_24 import calculate_total_length
from ..exercises.exercise_25 import double_elements
from ..exercises.exercise_26 import find_first_divisible_by_5
from ..exercises.exercise_27 import sum_positive_numbers
from ..exercises.exercise_28 import reverse_digits
from ..exercises.exercise_29 import gpa_calculator


def test_e15():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(7) == "7"


def test_e16():
    assert is_prime(2) is True
    assert is_prime(5) is True
    assert is_prime(6) is False
    assert is_prime(21) is False
    assert is_prime(23) is True


def test_e17():
    assert is_alice_happy(10, 5) is True
    assert is_alice_happy(5, 10) is False
    assert is_alice_happy(10, 10) is False
    assert is_alice_happy(20, 10) is True
    assert is_alice_happy(10, 20) is False


def test_e18():
    assert check_number(0) == "Zero"
    assert check_number(5) == "Positive"
    assert check_number(-5) == "Negative"


def test_e19():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(4) is True
    assert is_even(5) is False


def test_e20():
    assert grade_result(90) == "A"
    assert grade_result(80) == "B"
    assert grade_result(70) == "C"
    assert grade_result(60) == "Not Pass"
    assert grade_result(50) == "Not Pass"


def test_e21():
    assert sum_numbers(0, 0) == 0
    assert sum_numbers(0, 1) == 1
    assert sum_numbers(0, 2) == 3
    assert sum_numbers(10, 15) == 75
    assert sum_numbers(1, 10) == 55
    assert sum_numbers(1, 100) == 5050


def test_e22():
    assert sum_even_numbers(1, 5) == 6
    assert sum_even_numbers(1, 10) == 30
    assert sum_even_numbers(1, 20) == 110
    assert sum_even_numbers(1, 30) == 240
    assert sum_even_numbers(1, 40) == 420


def test_e23():
    assert largest_index([1, 2, 3, 4, 5]) == 4
    assert largest_index([5, 4, 3, 2, 1]) == 0
    assert largest_index([1, 2, 5, 4, 3]) == 2
    assert largest_index([1, 2, 3, 5, 4]) == 3


def test_e24():
    assert calculate_total_length(["Hello", "World"]) == 10
    assert calculate_total_length(["Python", "Programming"]) == 17
    assert calculate_total_length(["Python", "Programming", "Language"]) == 25


def test_e25():
    assert double_elements([1, 2, 3]) == [2, 4, 6]
    assert double_elements([4, 5, 6]) == [8, 10, 12]
    assert double_elements([7, 8, 9]) == [14, 16, 18]


def test_e26():
    assert find_first_divisible_by_5([]) is None
    assert find_first_divisible_by_5([1, 2, 3, 4, 5]) == 5
    assert find_first_divisible_by_5([5, 10, 15, 20, 25]) == 5
    assert find_first_divisible_by_5([6, 7, 8, 9, 10]) == 10
    assert find_first_divisible_by_5([11, 13, 16]) is None


def test_e27():
    assert sum_positive_numbers([]) == 0
    assert sum_positive_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_positive_numbers([1, -2, 3, -4, 5]) == 9


def test_e28():
    assert reverse_digits(123) == 321
    assert reverse_digits(456) == 654
    assert reverse_digits(789) == 987
    assert reverse_digits(101) == 101


def test_e29():
    assert gpa_calculator([1]) == 1.0
    assert gpa_calculator([4, 3, 2]) == 3.0
    assert gpa_calculator([4, 3, 2, 1]) == 2.5
    assert gpa_calculator([4, 4, 4, 4]) == 4.0
    assert gpa_calculator([3, 3, 3, 3]) == 3.0
    assert gpa_calculator([3.2, 3.5, 3.8, 4]) == 3.625
