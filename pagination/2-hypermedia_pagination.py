#!/usr/bin/env python3
"""
Hypermedia pagination helper function.

This module defines a Server class with methods to paginate a dataset
of popular baby names and provide hypermedia-style pagination info.
"""

import math
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server with a private dataset attribute."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset or load it from CSV if not already
        loaded."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset using index_range."""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)  # Appel direct à la fonction
        if start >= len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Return a dictionary containing hypermedia pagination info.

        Keys:
            - page_size: number of items on the current page
            - page: current page number
            - data: list of items on the current page
            - next_page: number of the next page, None if last page
            - prev_page: number of the previous page, None if first page
            - total_pages: total number of pages in the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.get_page(page, page_size)
        page_size_returned = len(data)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            'page_size': page_size_returned,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
