#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # They truncate to 1000 in instruction, but create full index
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return page info, resilient to deletion."""
        
        # 1. Validate input
        assert isinstance(index, int) and index >= 0
        indexed_data = self.indexed_dataset()
        assert index <= max(indexed_data.keys())

        data = []
        current_index = index

        # 2. Collect exactly page_size existing rows
        while len(data) < page_size and current_index <= max(indexed_data.keys()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        # 3. Next index is where we stopped scanning
        next_index = current_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
