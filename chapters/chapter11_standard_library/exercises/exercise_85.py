# Exercise 85 - Parse transaction files
# Given the following class and function, implement the `parse_transactions` function that reads a file
# and returns a list of transactions. Each line in the file contains a timestamp and a description separated by a comma.
# The timestamp should be converted to a `datetime` object.
#
from dataclasses import dataclass
from datetime import datetime  # noqa: F401

# Example:
# 2024-09-01,Sold 100 shares of AAPL
# 2024-10-01,Bought 200 shares of MSFT
# should return:
# [ Transaction(datetime(2024, 9, 1), "Sold 100 shares of AAPL"),
#   Transaction(datetime(2024, 10, 1), "Bought 200 shares of MSFT") ]


@dataclass
class Transaction:
    timestamp: str  # Replace with `datetime`
    description: str


def parse_transactions(filename: str) -> list[Transaction]:
    # Your code should go here.

    ...
