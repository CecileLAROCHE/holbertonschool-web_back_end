#!/usr/bin/env python3
"""

"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Génère 10 floats entre 0 et 10, avec 1 sec entre chaque.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
