# Exercise 09 - Slope of a Line
# Write a program that computes the slope of a line given two points.


def compute_slope(x1, y1, x2, y2):
    # Your code should go here.

    return (y2 - y1)/(x2 - x1)

print(compute_slope(1, 2, 3, 4))