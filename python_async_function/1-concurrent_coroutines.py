#!/usr/bin/env python3
"""
Execute multiple coroutines concurrently.
"""
import asyncio
from typing import List

# Import correct pour un fichier commençant par un chiffre
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times and return the delays
    in ascending order WITHOUT using sort().
    """

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays: List[float] = []

    # Récupère les tâches dans l'ordre où elles se finissent
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
