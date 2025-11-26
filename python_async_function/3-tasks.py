#!/usr/bin/env python3
"""
Measure runtime of executing task_wait_random.
"""
import asyncio

# Import correct pour un fichier commençant par un chiffre
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """
    Return an asyncio.Task that executes wait_random(max_delay)
    """
    return asyncio.create_task(wait_random(max_delay))
