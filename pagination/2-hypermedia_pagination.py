#!/usr/bin/env python3
"""
Hypermedia pagination helper function.

This module defines a method `get_hyper` that provides hypermedia-style
pagination for a dataset. It returns a dictionary containing the page data,
page size, current page number, previous and next page numbers, and total
number of pages.
"""

import math

# Import the helper function from task 0
index_range = __import__('0-simple_helper_function').index_range


def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
    """
    Return a dictionary containing pagination information (hypermedia style).

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        dict: Dictionary containing the following keys:
            - page_size: number of items on the current page
            - page: current page number
            - data: list of items on the current page
            - next_page: number of the next page, None if last page
            - prev_page: number of the previous page, None if first page
            - total_pages: total number of pages in the dataset
    """
    # 1. Validate inputs using assert statements
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    # 2. Get the current page data by reusing get_page
    data = self.get_page(page, page_size)

    # 3. Calculate the page size of the returned data
    page_size_returned = len(data)

    # 4. Calculate total number of items and total pages
    total_items = len(self.dataset())
    total_pages = math.ceil(total_items / page_size)

    # 5. Determine the previous page number
    if page > 1:
        prev_page = page - 1
    else:
        prev_page = None

    # 6. Determine the next page number
    if page < total_pages:
        next_page = page + 1
    else:
        next_page = None

    # 7. Construct and return the dictionary with pagination info
    return {
        'page_size': page_size_returned,
        'page': page,
        'data': data,
        'next_page': next_page,
        'prev_page': prev_page,
        'total_pages': total_pages
    }
