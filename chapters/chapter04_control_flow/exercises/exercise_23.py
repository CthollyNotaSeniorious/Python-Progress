# Exercise 23 - Largest Index
# Write a program that returns the index of the largest element in the list.
# For example, given the list [1, 2, 3, 4, 5], the function should return 4.


def largest_index(elements):
    # Your code should go here.
    if not elements:
        return None
    return elements.index(max(elements))

print(largest_index([1, 2, 3, 4]))