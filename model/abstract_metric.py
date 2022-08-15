# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770

from abc import ABC, abstractmethod


class Metric(ABC):
    """Abstract class for matching metrics."""

    @staticmethod
    @abstractmethod
    def min_edit_dist(word1, word2):
        """Calculates the similarity of two words.
        Args:
            word1: str
            word2: str

        Returns:
            similarity value of metric appropriate type
        """
        pass
