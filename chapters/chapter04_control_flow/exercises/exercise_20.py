# Exercise 20 - Grade Result
# Write a program that take an integer between 0 and 100
# and returns the grade result based on the following rules:
# 1. “A” if grade is between 90 and 100
# 2. “B” if grade is between 80 and 89
# 3. “C” if grade is between 70 and 79
# 4. “Not Pass” if grade is less than 70


def grade_result(grade):
    # Your code should go here.
    if grade >= 90 and grade <= 100:
        return "A"
    if grade >= 80 and grade < 90:
        return "B"
    if grade >= 70 and grade < 80:
        return "C"
    if grade < 70:
        return "Not Pass"

print(grade_result(79))
