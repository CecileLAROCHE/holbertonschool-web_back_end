#!/usr/bin/env python3
"""

"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    ***
    """
    start = time.time()

    task1 = async_comprehension()
    task2 = async_comprehension()
    task3 = async_comprehension()
    task4 = async_comprehension()

    await asyncio.gather(task1, task2, task3, task4)

    end = time.time()

    total_time = end - start
    return total_time
