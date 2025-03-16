# Exercise 06 - Binary to Decimal
# Write a program that takes a binary string as input and
# returns its decimal representation as an integer.
# For example, given the binary string "1010", the function should return 10.
# or given the binary string "1101", the function should return 13.


def convert_binary_to_decimal(binary):
    # Your code should go here.
    return int(binary, 2)

binary = input("Masukkan binary: ")
print(convert_binary_to_decimal(binary))