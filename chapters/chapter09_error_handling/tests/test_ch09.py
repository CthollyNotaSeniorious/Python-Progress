import pytest
from ..exercises.exercise_64 import divide
from ..exercises.exercise_65 import check_positive, NegativeValueError
from ..exercises.exercise_66 import ProductSalesCalculator, InvalidQuantityError
from ..exercises.exercise_67 import process_strings


def test_e64():
    assert divide(1, 1) == 1
    assert divide(1, 2) == 0.5
    assert divide(10, 0) is None
    assert divide(10, 2) == 5
    assert divide(10, 5) == 2


def test_e65():
    assert check_positive(0) == 0
    assert check_positive(10) == 10
    with pytest.raises(NegativeValueError):
        check_positive(-1)
    with pytest.raises(NegativeValueError):
        check_positive(-10)


def test_e66():
    with pytest.raises(InvalidQuantityError):
        ProductSalesCalculator(10, 0)
    with pytest.raises(InvalidQuantityError):
        ProductSalesCalculator(10, -1)

    psc = ProductSalesCalculator(10, 1)
    assert psc.calculate_total() == 10
    psc = ProductSalesCalculator(10, 2)
    assert psc.calculate_total() == 20


def test_e67():
    test_strings = ["123", "1", "abc", "456", "789", "0"]

    with pytest.raises(ExceptionGroup) as exc_info:
        process_strings(test_strings)

    exceptions = exc_info.value.exceptions
    assert len(exceptions) == 3
    print(exceptions)
    value_error_raised = any(isinstance(e, ValueError) for e in exceptions)
    assert value_error_raised, "ValueError was not raised as expected"

    index_error_count = sum(isinstance(e, IndexError) for e in exceptions)
    assert (
        index_error_count == 2
    ), "IndexError was not raised the correct number of times"
