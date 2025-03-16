# Exercise 81 - Functools
# Write a function that uses `functools.partial` to create a function that always multiplies by 10.
from functools import partial  # noqa: F401


def multiply(x, y):
    return x * y


multiply_by_10 = ...
