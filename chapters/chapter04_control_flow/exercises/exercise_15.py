# Exercise 15 - FizzBuzz
# Write a program that takes an integer as input and returns either:
# 1. "Fizz" if the number is divisible by 3,
# 2. "Buzz" if the number is divisible by 5, and
# 3. "FizzBuzz" if the number is divisible by both 3 and 5.

# There is a bug in the code below. Find it and fix it.


def fizzbuzz(number: int) -> str:
    if number % 3 == 0 or number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
