# Exercise 84 - Log This
# Given this "RateInterestCalculator" class with two methods,
# we need to replace the print() messages with log statements instead with
# the appropriate Log Level.

# Can you fix this?

import logging  # noqa: F401


class RateInterestCalculator:
    def __init__(self) -> None:
        pass

    def foo():
        print("Info - ...")
        ...
        print("ERROR - something happened")

    def bar():
        print("Info - ...")

    def _baz():
        print("debug - ....")
