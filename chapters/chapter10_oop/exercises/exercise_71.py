# Exercise 71 - Library Management System [Part 1/3]
# In the next three exercises, you will implement a simple library management system.
# Let's start first by defining our core classes (Book and Author).

# Create two dataclasses called `Author` and `Book` and an enum called `Genre`.
# The `Author` class should have the following attributes:
# 1. first_name
# 2. last_name

# The `Book` class should have the following attributes:
# 1. title
# 2. author (an instance of the `Author` class)
# 3. publication_year
# 4. genre (an instance of the `Genre` enum)

# The `Genre` enum should have the following values:
# 1. Fiction
# 2. NonFiction
# 3. Biography
# 4. History
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Author:
    # Your code should go here.
    ...


class Genre:
    # Your code should go here.
    ...


@dataclass
class Book:
    # Your code should go here.
    ...
