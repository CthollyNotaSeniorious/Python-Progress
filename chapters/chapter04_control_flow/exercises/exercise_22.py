# Exercise 22 - Sum Even Numbers
# Write a program that sums the even numbers from start to end.
# For example, if the start is 1 and the end is 5, the sum is 6 (2 + 4).

# Can you solve this once using a for loop and once using a while loop?


def sum_even_numbers(start, end):
    # Your code should go here.
    value = 0
    for i in range(start, end):
        if i % 2 == 0:
            value += i
        elif i % 2 == 1:
            value += 0
    return value

print(sum_even_numbers(1, 7))