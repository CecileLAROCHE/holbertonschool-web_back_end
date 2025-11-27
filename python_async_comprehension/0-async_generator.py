#!/usr/bin/env python3
"""
Module contenant une coroutine asynchrone permettant de générer
des nombres aléatoires de manière non bloquante.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine asynchrone qui génère un flot (generator) de 10 nombres.

    À chaque itération :
    - Attend 1 seconde de manière asynchrone (sans bloquer l'exécution)
      grâce à `await asyncio.sleep(1)`
    - Génère un nombre flottant aléatoire entre 0 et 10 utilisant le
      module `random`
    - Renvoie la valeur générée avec `yield`, ce qui en fait un
      générateur asynchrone.

    Retour :
        AsyncGenerator[float, None] :
        Un générateur asynchrone produisant dix valeurs flottantes.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random()
