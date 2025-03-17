# Exercise 18 - Check Number
# Write a program that returns:
# - 'Positive' if the number is greater than 0
# - 'Negative' if the number is less than 0
# - 'Zero' if the number is equal to 0


def check_number(number):
    # Your code should go here.
    if number > 0:
        return f"Positive"
    if number < 0:
        return f"Negative"
    if number == 0:
        return f"Zero"

print(check_number(0))