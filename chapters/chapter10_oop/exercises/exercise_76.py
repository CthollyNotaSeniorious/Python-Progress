# Exercise 76 - Generic Box
# Given a class called `Box` that can store items of type `int`, modify the class so that it can store items of any type.
# In other words, the `Box` class should be generic.


class Box:
    def __init__(self):
        self.item = None

    def add(self, item: int):
        self.item = item

    def get(self) -> int:
        return self.item
