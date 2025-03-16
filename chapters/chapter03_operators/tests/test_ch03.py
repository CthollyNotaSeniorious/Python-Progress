from ..exercises.exercise_08 import compute_area_of_circle
from ..exercises.exercise_09 import compute_slope
from ..exercises.exercise_10 import bitwise_operations
from ..exercises.exercise_11 import area_of_triangle
from ..exercises.exercise_12 import calculate_hypotenuse
from ..exercises.exercise_13 import add_without_plus_operator
from ..exercises.exercise_14 import generate_stats_report


def test_e08():
    assert compute_area_of_circle(0) == 0
    assert compute_area_of_circle(1) == 3.14159
    assert compute_area_of_circle(2) == 12.56636


def test_e09():
    assert compute_slope(0, 0, 4, 2) == 0.5
    assert compute_slope(0, 0, 1, 1) == 1
    assert compute_slope(0, 0, 2, 4) == 2


def test_e10():
    assert bitwise_operations(0, 0) == "0 0 0"
    assert bitwise_operations(5, 3) == "1 7 6"
    assert bitwise_operations(10, 5) == "0 15 15"
    assert bitwise_operations(15, 10) == "10 15 5"


def test_e11():
    assert area_of_triangle(0, 0) == 0
    assert area_of_triangle(1, 1) == 0.5
    assert area_of_triangle(2, 2) == 2
    assert area_of_triangle(3, 3) == 4.5


def test_e12():
    assert calculate_hypotenuse(3, 4) == 5
    assert calculate_hypotenuse(5, 12) == 13
    assert calculate_hypotenuse(8, 15) == 17
    assert calculate_hypotenuse(7, 24) == 25


def test_e13():
    assert add_without_plus_operator(0, 0) == 0
    assert add_without_plus_operator(10, 2) == 12
    assert add_without_plus_operator(2, 10) == 12
    assert add_without_plus_operator(-20, 10) == -10
    assert add_without_plus_operator(-10, -20) == -30


def test_e14():
    assert (
        generate_stats_report(1, 0, 0)
        == r"The team played 1 games. They won 100.0% of the games, lost 0.0% of the games, and drew 0.0% of the games."
    )
    assert (
        generate_stats_report(3, 2, 1)
        == r"The team played 6 games. They won 50.0% of the games, lost 33.3% of the games, and drew 16.7% of the games."
    )
    assert (
        generate_stats_report(5, 5, 5)
        == r"The team played 15 games. They won 33.3% of the games, lost 33.3% of the games, and drew 33.3% of the games."
    )
    assert (
        generate_stats_report(21, 11, 3)
        == r"The team played 35 games. They won 60.0% of the games, lost 31.4% of the games, and drew 8.6% of the games."
    )
