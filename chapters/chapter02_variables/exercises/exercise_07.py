# Exercise 07 - Midpoint Calculation
# Write a program that calculates the midpoint between two points.
# The program should take the x and y coordinates of two points as input
# and return the midpoint as a tuple.

# The formula for calculating the midpoint is as follows:
# midpoint_x = (x1 + x2) / 2
# midpoint_y = (y1 + y2) / 2
# The midpoint is the point that is exactly halfway between two points.
# For example, given the points (1, 2) and (3, 4), the midpoint should be (2, 3).


# Note: you can return more than one value by separating them with a comma.


def calculate_midpoint(x1, y1, x2, y2):
    # Your code should go here.
    return (x1 + x2) / 2, (y1 + y2) / 2

x1 = float(input('Masukkan koordinat x1: '))
y1 = float(input('Masukkan koordinat y1: '))
x2 = float(input('Masukkan koordinat x2: '))
y2 = float(input('Masukkan koordinat y2: '))
print(calculate_midpoint(x1, y1, x2, y2))