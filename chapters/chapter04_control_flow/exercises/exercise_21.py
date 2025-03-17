# Exercise 21 - Sum Numbers
# Write a program that sums the numbers from start to end.
# For example, if the start is 1 and the end is 5, the sum is 15 (1 + 2 + 3 + 4 + 5).

# Can you solve this once using a for loop and once using a while loop?


def sum_numbers(start, end):
    # Your code should go here.
    result = 0
    for i in range (start, end + 1):
        result += i

    return result

print(sum_numbers(10, 15))