#!/usr/bin/env python3
"""
222
"""

index_range = __import__('0-simple_helper_function').index_range


def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
    """Return a dictionary with pagination info (hypermedia)."""
    # 1. validate inputs (comme dans get_page)
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    # 2. get the page data by reusing get_page
    data = self.get_page(page, page_size)

    # 3. page_size returned is the length of data
    page_size_returned = len(data)

    # 4. total items and total pages
    total_items = len(self.dataset())
    total_pages = math.ceil(total_items / page_size)

    # 5. determine prev_page and next_page
    if page > 1:
        prev_page = page - 1
    else:
        prev_page = None

    if page < total_pages:
        next_page = page + 1
    else:
        next_page = None

    # 6. construct result dict
    return {
        'page_size': page_size_returned,
        'page': page,
        'data': data,
        'next_page': next_page,
        'prev_page': prev_page,
        'total_pages': total_pages
    }
