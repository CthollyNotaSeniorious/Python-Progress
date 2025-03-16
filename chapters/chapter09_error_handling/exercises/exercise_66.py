# Exercise 66 - ProductSalesCalculator
# Given the following class, fix the code so that it raises a custom exception called `InvalidQuantityError`
# instead of the print message.


class InvalidQuantityError(Exception):
    pass


class ProductSalesCalculator:
    def __init__(self, price: float, quantity: int):
        if quantity <= 0:
            print("Quantity must be greater than zero")
        self.price = price
        self.quantity = quantity

    def calculate_total(self) -> float:
        return self.price * self.quantity
