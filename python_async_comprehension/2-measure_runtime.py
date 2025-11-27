#!/usr/bin/env python3
"""
Module contenant une coroutine permettant de mesurer le temps
d'exécution de plusieurs compréhensions asynchrones lancées en parallèle.
"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Mesure le temps nécessaire pour exécuter quatre appels
    à async_comprehension en parallèle.

    Cette fonction :
        - démarre un chronomètre,
        - lance quatre compréhensions asynchrones simultanément à l'aide de
          asyncio.gather(), ce qui permet leur exécution parallèle,
        - attend que toutes soient terminées,
        - calcule et renvoie le temps total écoulé.

    Retour :
        float : le temps total d'exécution en secondes.
    """
    start = time.time()

    await asyncio.gather(*[async_comprehension() for n in range(4)])

    end = time.time()

    total_time = end - start
    return total_time
