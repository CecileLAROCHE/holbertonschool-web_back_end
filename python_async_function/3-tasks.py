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
    Spawn task_wait_random n times and return the list of delays
    in ascending order without using sort().
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
