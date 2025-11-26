#!/usr/bin/env python3
"""
Measure runtime of executing wait_n.
"""
import asyncio
import time

# Import correct pour un fichier commençant par un chiffre
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay)
    and return the average time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    total_time = end - start
    return total_time / n
