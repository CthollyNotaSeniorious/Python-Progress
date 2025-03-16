# Exercise 05 - Average Grade
# Write a program that takes three grades (int or float) from a user and calculate the average grade (float).
# The average grade should be **rounded to two decimal places**.

def compute_average_grade(grade1, grade2, grade3):
    # Your code should go here.

    return round((grade1 + grade2 + grade3) / 3, 2)

grade1 = float(input("Masukkan nilai: "))
grade2 = float(input("Masukkan nilai: "))
grade3 = float(input("Masukkan nilai: "))
print(compute_average_grade(grade1, grade2, grade3))