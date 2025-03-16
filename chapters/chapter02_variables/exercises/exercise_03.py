# Exercise 03 - Add Numbers
# Write a program that adds two numbers (provided as strings) and returns the sum as a string.
# For example, given the strings "123" and "456", the function should return "579".
# Hint: Can built-in functions help for type conversion?


def add_numbers(num1, num2):
    # Your code should go here.

    return str(int(num1) + int(num2))

num1 = str(input("Masukkan angka - 1: "))
num2 = str(input("Masukkan angka - 2: "))

print(add_numbers(num1, num2))