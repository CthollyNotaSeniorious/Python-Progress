# Exercise 94 - Simple Unit Testing

# We have a function called clean_text() that takes a string and returns the string with all the special characters removed.
# Write a test for this function using Pytest. Make sure to test the function with the following inputs:
# 1 - "Hello, World!"                - Expected output: "HelloWorld"
# 2 - "Hello, World! 123"            - Expected output: "HelloWorld123"
# 3 - "Hello, World! 123 @#"         - Expected output: "HelloWorld123"
# 4 - "Hello, World! 123 @# $%^"     - Expected output: "HelloWorld123"
# 5 - "Hello, World! 123 @# $%^ &*(" - Expected output: "HelloWorld123"


def clean_text(text: str) -> str:
    return "".join([char for char in text if char.isalnum()])
