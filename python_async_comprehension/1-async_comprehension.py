#!/usr/bin/env python3
"""
Module contenant une coroutine asynchrone permettant de récupérer
une liste de 10 nombres aléatoires générés de manière asynchrone.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
     Exécute une compréhension asynchrone pour consommer les valeurs
    produites par async_generator.

    La compréhension :
        - attend chaque valeur produite par async_generator
        - les collecte dans une liste
        - retourne cette liste complète de 10 floats

    Returns:
        List[float]: une liste contenant les 10 valeurs générées.
    """
    return [value async for value in async_generator()]
