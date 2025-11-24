#!/usr/bin/env python3
"""module make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        """Function that multiplies x by multiplier"""
        return x * multiplier
    return multiplier_function
