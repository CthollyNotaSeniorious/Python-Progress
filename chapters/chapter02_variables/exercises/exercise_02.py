# Exercise 02 - Temperature Conversion
# Write a program that converts a temperature from Celsius to Fahrenheit.
# Hint: The formula is: F = C * 9/5 + 32


def celsius_to_fahrenheit(celsius):
    # Your code should go here.
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celcius = int(input("Masukkan suhu dalam celcius: "))
print(celsius_to_fahrenheit(celcius))