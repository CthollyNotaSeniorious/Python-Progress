import pytest

from ..exercises.exercise_86 import EvenNumberIterator
from ..exercises.exercise_87 import FibonacciIterator
from ..exercises.exercise_88 import even_numbers_generator
from ..exercises.exercise_89 import fibonacci_generator
from ..exercises.exercise_90 import counter
from ..exercises.exercise_91 import time_this
from ..exercises.exercise_92 import repeat_it


def test_e86():
    assert list(EvenNumberIterator(5)) == [0, 2, 4, 6, 8]
    iterator = EvenNumberIterator(5)
    assert next(iterator) == 0
    assert next(iterator) == 2
    assert next(iterator) == 4
    assert next(iterator) == 6
    assert next(iterator) == 8
    with pytest.raises(StopIteration):
        next(iterator)


def test_e87():
    assert list(FibonacciIterator(5)) == [0, 1, 1, 2, 3]
    iterator = FibonacciIterator(5)
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    with pytest.raises(StopIteration):
        next(iterator)


def test_e88():
    assert list(even_numbers_generator(5)) == [0, 2, 4, 6, 8]
    iterator = even_numbers_generator(5)
    assert next(iterator) == 0
    assert next(iterator) == 2
    assert next(iterator) == 4
    assert next(iterator) == 6
    assert next(iterator) == 8
    with pytest.raises(StopIteration):
        next(iterator)


def test_e89():
    assert list(fibonacci_generator(5)) == [0, 1, 1, 2, 3]
    iterator = fibonacci_generator(5)
    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    with pytest.raises(StopIteration):
        next(iterator)


def test_e90():
    c = counter()
    assert c() == 1
    assert c() == 2
    assert c() == 3


def test_e91():
    @time_this
    def my_function():
        pass

    my_function()


def test_e92():
    @repeat_it(3)
    def my_function():
        pass

    my_function()
    my_function()
