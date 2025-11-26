#!/usr/bin/env python3
"""
Module that contains an asynchronous function for waiting a random delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay between 0 and max_delay seconds.
    """
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return (x)
