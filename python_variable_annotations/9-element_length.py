#!/usr/bin/env python3
"""module element_length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples (element, length of element)
    for each element in lst.
    """
    return [(i, len(i)) for i in lst]
