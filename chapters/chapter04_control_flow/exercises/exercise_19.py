# Exercise 19 - Even or Odd Number
# Write a program that takes an integer and returns whether its an even or odd number.
# Bonus: can you solve this in a single line of code? (Hint: Search for ternary operator)


def is_even(number):
    # Your code should go here.
    result = "Genap" if number % 2 == 0 else "Ganjil"
    return result

print(is_even(-8))