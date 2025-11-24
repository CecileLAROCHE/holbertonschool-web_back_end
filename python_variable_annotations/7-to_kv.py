#!/usr/bin/env python3
"""module to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """this fonction will return Complex types - string and int/float to tuple """
    return (k, float(v ** 2))
