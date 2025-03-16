# Exercise 95 - Testing SalaryCalculator class.

# Write a test for this class using Pytest. Make sure to test the class with the following inputs:
# 1 - hourly_rate = 10, hours_worked = 40 - Expected output: 400
# 2 - hourly_rate = 10, hours_worked = 50 - Expected output: 500
# 3 - hourly_rate = 10, hours_worked = 60 - Expected output: 600
# 4 - hourly_rate = 10, hours_worked = 0  - Expected output: ValueError
# 5 - hourly_rate = 10, hours_worked = -1 - Expected output: ValueError


# Given this working class called SalaryCalculator:
class SalaryCalculator:
    def __init__(self, hourly_rate: float):
        self.hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked: int) -> float:
        if hours_worked <= 0:
            raise ValueError("Hours worked must be greater than 0.")
        return self.hourly_rate * hours_worked
