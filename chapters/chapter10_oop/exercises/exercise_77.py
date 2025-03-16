# Exercise 77 - Content Creators
# We have two types of Content Creators: Bloggers and Vloggers.
# Both of them should have a method called `create_content` that calls the appropriate method to create content.
# We want to define a protocol called `ContentCreator` that has the `create_content` method.
# See `test_e77()` in `tests/test_ch10.py` for the expected behavior.

from typing import Protocol


class ContentCreator(Protocol):
    def create_content(self) -> str: ...


class Blogger:
    def add_post(self, title: str):
        return f"Creating a new post: {title}"

    # TODO: Write create_content() method.


class Vlogger:
    def add_video(self, title: str) -> None:
        return f"Creating a new video: {title} with path: /videos/{title}.mp4"

    # TODO: Write create_content() method.


def create_content(creator: ContentCreator, title: str) -> str:
    # Your code here
    ...
