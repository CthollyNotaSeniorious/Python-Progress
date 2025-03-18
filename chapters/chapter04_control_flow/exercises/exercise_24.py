# Exercise 24 - Calculate Total Length
# Write a program that calculates the total length of all words in a list.
# For example, given the list ['hello', 'world'], the total length is 10.


def calculate_total_length(words):
    # Your code should go here.

    return sum(len(word) for word in words)

print(calculate_total_length(['hello', 'world']))