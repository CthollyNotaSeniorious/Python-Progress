# Exercise 96 - Testing ProductSalesCalculator class.

# Write a test for this class using Pytest.
# Can we test with Discount(percentage=50) as a pytest fixture?
# Make sure to test the class with the following inputs:
# 1 - price = 10, quantity = 10, discount = Discount(percentage=50) - Expected output: 50
# 1 - price = 15, quantity = 45, discount = Discount(percentage=50) - Expected output: 337.5
# 1 - price = 20, quantity = 100, discount = Discount(percentage=50) - Expected output: 1000
# 1 - price = 25, quantity = 5, discount = Discount(percentage=50) - Expected output: 62.5


from dataclasses import dataclass


@dataclass
class Discount:
    percentage: float


class ProductSalesCalculator:
    def __init__(self, price: float, quantity: int, discount: Discount):
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def calculate_total(self) -> float:
        total = self.price * self.quantity
        discount_amount = total * (self.discount.percentage / 100)
        return total - discount_amount
