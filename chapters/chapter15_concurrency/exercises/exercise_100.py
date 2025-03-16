# Exercise 100 - Decorator for Async Functions
# Given the following `time_it` decorator, extend it to support async functions.
# NOTE: To run the unit tests for this exercise, you need to install the following:
# $ pip install pytest pytest-asyncio

import asyncio  # noqa: F401
from functools import wraps
import timeit
from typing import Callable, Any


def time_it(
    _func: Callable | None = None,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            start = timeit.default_timer()
            result = func(*args, **kwargs)
            end = timeit.default_timer()
            print(f"Time taken for {func.__name__}: {end - start:.4f} seconds")
            return result

        # Your code should go here.
        # Add an `async_wrapper` function to handle async functions
        ...

        # Hint: Check if the function is a coroutine function using `asyncio.iscoroutinefunction()`
        # before returning the appropriate wrapper function.
        return wrapper

    if _func is None:
        return decorator
    else:
        return decorator(_func)
