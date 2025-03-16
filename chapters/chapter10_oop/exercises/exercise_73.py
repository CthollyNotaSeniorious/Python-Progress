# Exercise 73 - Library Management System [Part 3/3]
# In this exercise, you will implement the `Library` class that will hold a collection of shelves.

# The `Library` class should have the following methods:
# 1. `add_shelf(shelf: BookShelf)`: Add a shelf to the library.
# 2. `remove_shelf(shelf: BookShelf)`: Remove a shelf from the library.
# 3. `get_books() -> List[Book]`: Return a list of all the books from all the shelves in the library.
# 4. `is_book_in_library(book: Book) -> bool`: Return `True` if the book is in the library, otherwise `False`.


# Note: Feel free to define any additional methods or attributes that
# you think are necessary for the `BookShelf` class.

# See `test_e73()` in `tests/test_ch10.py` for the expected behavior.

from .exercise_71 import Book, Genre  # noqa: F401
from .exercise_72 import BookShelf  # noqa: F401


class Library:
    # Add your code here.
    ...
