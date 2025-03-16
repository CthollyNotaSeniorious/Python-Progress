import logging
import textwrap
from pathlib import Path
import pytest
import tempfile
from datetime import date, datetime
from ..exercises.exercise_79 import days_until_next_birthday
from ..exercises.exercise_80 import Address, Person
from ..exercises.exercise_81 import multiply_by_10
from ..exercises.exercise_82 import flatten_list_of_lists
from ..exercises.exercise_83 import compute_fibonacci
from ..exercises.exercise_84 import RateInterestCalculator
from ..exercises.exercise_85 import parse_transactions, Transaction


def test_e79():
    assert days_until_next_birthday(date(2024, 1, 1), date(2024, 1, 1)) == 0
    assert days_until_next_birthday(date(2024, 1, 1), date(2024, 1, 2)) == 365
    assert days_until_next_birthday(date(2024, 1, 1), date(2024, 12, 31)) == 1


def test_e80():
    address = Address(street="123 Main St", city="Springfield", zip_code="12345")
    person = Person(name="John Doe", age=30, address=address)
    assert person.name == "John Doe"
    assert person.age == 30
    assert person.address.street == "123 Main St"
    assert person.address.city == "Springfield"
    assert person.address.zip_code == "12345"
    assert person.previous_address == []

    address_2 = Address(street="456 Elm St", city="Springfield", zip_code="12345")
    address_3 = Address(street="789 Oak St", city="Springfield", zip_code="12345")
    person_2 = Person(
        name="Jane Doe",
        age=28,
        address=address,
        previous_address=[address_2, address_3],
    )
    assert person_2.name == "Jane Doe"
    assert person_2.age == 28
    assert person_2.address.street == "123 Main St"
    assert person_2.address.city == "Springfield"
    assert person_2.address.zip_code == "12345"
    assert person_2.previous_address == [address_2, address_3]


def test_e81():
    assert multiply_by_10(5) == 50
    assert multiply_by_10(10) == 100
    assert multiply_by_10(15) == 150
    assert multiply_by_10(0) == 0


def test_e82():
    assert flatten_list_of_lists([[]]) == []
    assert flatten_list_of_lists([[1, 2], [3, 4], [5, 6]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]
    assert flatten_list_of_lists([[1, 2, 3]]) == [1, 2, 3]
    assert flatten_list_of_lists([[1], [2], [3]]) == [1, 2, 3]
    assert flatten_list_of_lists([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten_list_of_lists([[1], [2, 3], [4]]) == [1, 2, 3, 4]


def test_e83():
    assert compute_fibonacci.cache_info().hits == 0, "Cache hits should be 0 initially"
    assert compute_fibonacci(2) == 1, "First call should not be cached"
    assert compute_fibonacci(2) == 1, "Second call should use cache"
    assert (
        compute_fibonacci.cache_info().hits == 1
    ), "Cache hits should be 1 after second call"
    assert compute_fibonacci(3) == 2, "Third call should not be cached"
    assert compute_fibonacci(10) == 55


@pytest.fixture
def caplog_setup(caplog):
    # Set up the logger to capture log messages
    caplog.set_level(logging.INFO)
    return caplog


def test_e84(caplog_setup):
    calculator = RateInterestCalculator()
    calculator.calculate_rate()
    assert any(
        record.levelname == "INFO" and "Calculating rate" in record.message
        for record in caplog_setup.records
    )
    assert any(
        record.levelname == "ERROR" and "An error occurred" in record.message
        for record in caplog_setup.records
    )

    calculator.calculate_interest()
    assert any(
        record.levelname == "INFO" and "Calculating interest" in record.message
        for record in caplog_setup.records
    )


@pytest.fixture
def source(file_content):
    with tempfile.NamedTemporaryFile(suffix=".txt") as tmp_file:
        source_path = Path(tmp_file.name)
        source_path.write_text(file_content)
        yield source_path


@pytest.mark.parametrize(
    "file_content, expected",
    [
        (
            textwrap.dedent(
                """2021-01-01,Sold 100 shares of AAPL
                2021-01-02,Bought 200 shares of MSFT
                2021-01-03,Sold 50 shares of AAPL
            """
            ),
            [
                Transaction(
                    timestamp=datetime(2021, 1, 1),
                    description="Sold 100 shares of AAPL",
                ),
                Transaction(
                    timestamp=datetime(2021, 1, 2),
                    description="Bought 200 shares of MSFT",
                ),
                Transaction(
                    timestamp=datetime(2021, 1, 3), description="Sold 50 shares of AAPL"
                ),
            ],
        ),
        (
            textwrap.dedent(
                """2024-09-01,Sold 100 shares of AAPL
                2024-10-01,Bought 200 shares of MSFT
                2024-11-01,Sold 50 shares of AAPL
                2024-12-01,Bought 100 shares of TSLA
            """
            ),
            [
                Transaction(
                    timestamp=datetime(2024, 9, 1),
                    description="Sold 100 shares of AAPL",
                ),
                Transaction(
                    timestamp=datetime(2024, 10, 1),
                    description="Bought 200 shares of MSFT",
                ),
                Transaction(
                    timestamp=datetime(2024, 11, 1),
                    description="Sold 50 shares of AAPL",
                ),
                Transaction(
                    timestamp=datetime(2024, 12, 1),
                    description="Bought 100 shares of TSLA",
                ),
            ],
        ),
    ],
)
def test_e85(source, expected):
    assert parse_transactions(source) == expected
