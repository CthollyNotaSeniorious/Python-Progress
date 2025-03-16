# Exercise 13 - Add Without Plus Operator
# This program below adds two numbers without using the '+' operator.

# There is a bug in the code below. Find it and fix it.


def add_without_plus_operator(a, b):
    # Continue the loop until the carry (b) becomes zero.
    while b != 0:
        # Calculate the bitwise AND of 'a' and 'b'.
        data = a & b
        # XOR 'a' and 'b' to get the sum without considering carry.
        a = a ^ b
        b = data >> 1

    return a
