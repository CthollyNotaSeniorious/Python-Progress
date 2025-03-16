# Exercise 04 - Difference in Length
# Write a program that returns the length difference between two words.
# For example, given the words "Python" and "Programming", the function should return 3.
# Note: The function should return the absolute value of the difference.
# Hint: Can a built-in function help us here?


def compute_length_difference(word1, word2):
    # Your code should go here.

    return abs(len(word1) - len(word2))

word1 = input("Masukkan kata pertama: ")
word2 = input("Masukkan kata kedua: ")

print(compute_length_difference(word1, word2))