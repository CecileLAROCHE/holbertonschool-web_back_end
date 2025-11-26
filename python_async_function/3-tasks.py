#!/usr/bin/env python3
"""
Measure runtime of executing task_wait_random.
"""
import asyncio

# Import correct pour un fichier commençant par un chiffre
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    This function creates and returns an asyncio.Task
    that will execute the wait_random coroutine with the given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
