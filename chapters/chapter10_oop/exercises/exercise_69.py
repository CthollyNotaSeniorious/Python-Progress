# Exercise 69 - TaxCalculator Class
# Define a `TaxCalculator` class that calculates the tax for a given income.
# The class should have a method `calculate_tax` that takes an income as a parameter and returns the tax amount.
# The tax should be calculated based on the following rules:
# - 0% tax for income less than or equal to 10,000
# - 10% tax for income greater than 10,000 and less than or equal to 50,000
# - 20% tax for income greater than 50,000 and less than or equal to 100,000
# - 30% tax for income greater than 100,000

# See `test_e69()` in `tests/test_ch10.py` for the expected behavior.


class TaxCalculator:
    def __init__(self):
        self.income = 0

    def calculate_tax(self, income: int) -> float:
        # Your code should go here.

        ...
