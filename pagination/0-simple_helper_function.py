#!/usr/bin/env python3
"""
This module contains a helper function used for pagination.
It computes the start and end indexes for a given page and page size.
"""


def index_range(page, page_size):
    """
    Calculate the start and end indices for a page of data.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items displayed per page.

    Returns:
        tuple: A tuple (start, end) where
            - start is the index where the page begins,
            - end is the index where the page ends (non-inclusive).
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
