# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770
"""Abstract Metrics Class that defines an interface for the concrete metrics
so that they are tuly interchangable.
"""
from abc import ABC, abstractmethod


class Metric(ABC):
    """Abstract class for matching metrics."""

    @staticmethod
    @abstractmethod
    def min_edit_dist(word1: str, word2: str):
        """Calculates the minimum edit distance of tow words.
        Args:
            word1: Source word.
            word2: Target word.

        Returns:
            Min edit distance of metric appropriate type.
        """
        pass
