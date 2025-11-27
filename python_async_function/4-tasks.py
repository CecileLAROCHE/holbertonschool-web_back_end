#!/usr/bin/env python3
"""
Execute multiple task_wait_random tasks concurrently.
"""

import asyncio
from typing import List

# Import task_wait_random depuis le module précédent
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute task_wait_random n times concurrently and return
    a list of delay values in the order they are completed.

    :param n: Number of times to call task_wait_random
    :type n: int
    :param max_delay: Maximum value of asyncio.sleep
    :type max_delay: int
    :return: List of delays
    :rtype: List[float]
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)

    return delays
