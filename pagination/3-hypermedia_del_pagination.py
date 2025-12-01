#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            # Skip header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by position starting from 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # Create index -> row mapping
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient paginated page.
        """
        assert isinstance(index, int) and index >= 0

        indexed_data = self.indexed_dataset()
        max_key = max(indexed_data.keys())
        assert index <= max_key

        data = []
        current = index

        # Collect page_size valid rows (skip deleted indices)
        while len(data) < page_size and current <= max_key:
            if current in indexed_data:
                data.append(indexed_data[current])
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data
        }
