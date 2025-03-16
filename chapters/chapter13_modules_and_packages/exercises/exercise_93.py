# Exercise 93 - PyTime Module

# Create a new package called "PyTime" with the following modules:
# 1 - date_conversion.py
# 2 - time_conversion.py
# Make sure to create the write structure for the package and modules so
# that the tests can be run successfully.


# 1 - date_conversion.py (Function already implemented)
def is_leap_year(year) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# 2 - time_conversion.py (Implement the following functions)
def hours_to_minutes(hours) -> int: ...
def minutes_to_seconds(minutes) -> int: ...
def seconds_to_minutes(seconds) -> int: ...
