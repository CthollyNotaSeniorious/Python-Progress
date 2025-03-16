# Exercise 98 - Asynchronous Processing
# Write an asynchronous function `process_data()` that fetches data from multiple sources and processes it concurrently.
# The function should take a list of sources and return a list of processed data.
# NOTE: To run the unit tests for this exercise, you need to install the following:
# $ pip install pytest pytest-asyncio

import asyncio
import random


async def fetch_data(source: str) -> str:
    await asyncio.sleep(random.uniform(0.1, 1.0))  # Simulate a network delay
    return f"Data from {source}"


# Update the function signature and implementation.
def process_data(sources: list[str]) -> list[str]:
    # Your code should go here.
    ...
