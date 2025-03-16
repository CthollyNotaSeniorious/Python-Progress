import textwrap

import pytest

from ..exercises.exercise_58 import count_errors_from_file
from ..exercises.exercise_59 import count_word_frequency
from ..exercises.exercise_60 import course_grades_summary
from ..exercises.exercise_61 import inventory_management
from ..exercises.exercise_62 import is_file_sorted
from ..exercises.exercise_63 import count_emails


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """
            INFO: System started
            ERROR: System crashed
            """
            ),
            1,
        ),
        (
            textwrap.dedent(
                """
                INFO: System started
                INFO: User logged in
                ERROR: System crashed
                INFO: System restarted
                ERROR: System crashed again
            """
            ),
            2,
        ),
    ],
)
def test_e58(source, expected):
    assert count_errors_from_file(source) == expected


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """
            """
            ),
            {},
        ),
        (
            textwrap.dedent(
                """
                python is a popular programming language
            """
            ),
            {
                "python": 1,
                "is": 1,
                "a": 1,
                "popular": 1,
                "programming": 1,
                "language": 1,
            },
        ),
        (
            textwrap.dedent(
                """
                python is a popular programming language
                python is a popular programming language
            """
            ),
            {
                "python": 2,
                "is": 2,
                "a": 2,
                "popular": 2,
                "programming": 2,
                "language": 2,
            },
        ),
    ],
)
def test_e59(source, expected):
    assert count_word_frequency(source) == expected


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """Math: 90, 85, 88, 92, 95
                Science: 78, 85, 88, 92, 95
                History: 88, 85, 88, 92, 95
                English: 98, 85, 88, 92, 95"""
            ),
            [
                ("Math", 90.0),
                ("Science", 87.6),
                ("History", 89.6),
                ("English", 91.6),
            ],
        ),
        (
            textwrap.dedent(
                """Math: 90, 85, 88, 92, 95
                Science: 78, 85, 88, 92, 95
                Physics: 61, 75, 70, 92, 93, 98, 81, 59, 88, 92
            """
            ),
            [("Math", 90.0), ("Science", 87.6), ("Physics", 80.9)],
        ),
    ],
)
def test_e60(source, expected):
    assert course_grades_summary(source) == expected


@pytest.mark.parametrize(
    "file_content, restock_threshold, expected",
    [
        (
            """item_name,quantity,price
Apple,100,0.5
Banana,200,0.3
Orange,150,0.4""",
            200,
            {
                "total_inventory_value": 170.0,
                "restock_alerts": ["Apple", "Orange"],
            },
        ),
        (
            """item_name,quantity,price
Apple,100,0.5
Banana,200,0.3
Orange,150,0.4""",
            100,
            {
                "total_inventory_value": 170.0,
                "restock_alerts": [],
            },
        ),
        (
            """item_name,quantity,price
Apple,100,0.5
Banana,200,0.3
Orange,150,0.4""",
            300,
            {
                "total_inventory_value": 170.0,
                "restock_alerts": ["Apple", "Banana", "Orange"],
            },
        ),
        (
            """item_name,quantity,price
Apple,100,0.5
Banana,200,0.3
Orange,150,0.4
Pear,300,0.6
Kiwi,400,0.7""",
            250,
            {
                "total_inventory_value": 630.0,
                "restock_alerts": ["Apple", "Banana", "Orange"],
            },
        ),
    ],
)
def test_e61(source, restock_threshold, expected):
    assert inventory_management(source, restock_threshold) == expected


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """1
                2
                3
            """
            ),
            True,
        ),
        (
            textwrap.dedent(
                """1
                3
                2
            """
            ),
            False,
        ),
        (
            textwrap.dedent(
                """1
                2
                3
                4
                5
            """
            ),
            True,
        ),
        (
            textwrap.dedent(
                """1
                2
                3
                5
                4
            """
            ),
            False,
        ),
    ],
)
def test_e62(source, expected):
    assert is_file_sorted(source) is expected


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """
                username1
                username2
            """
            ),
            0,
        ),
        (
            textwrap.dedent(
                """
                username1
                test1@abc.com
                username2
            """
            ),
            1,
        ),
        (
            textwrap.dedent(
                """
                username1
                username2
                user1@abc.com
                user2@abc.com
                username3
                user3@abc.com
                """
            ),
            3,
        ),
    ],
)
def test_e63(source, expected):
    assert count_emails(source) == expected
