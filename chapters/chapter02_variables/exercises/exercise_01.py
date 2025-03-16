# Exercise 01 - Convert Hours to Seconds
# Write a program that converts hours to seconds.

# For example, given the number of hours 2, the function should return 7200.


def hours_to_seconds(hours):
    # Your code should go here.

    return hours * 3600

hours = int(input("Masukkan Jam: "))
print(hours_to_seconds(hours))