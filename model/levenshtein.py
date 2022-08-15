# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770

from abstract_metric import Metric


class Levenshtein(Metric):
    """Levenshtein Distance Metric."""

    @staticmethod
    def min_edit_dist(word1, word2):
        """Calculates Levenshtein Distance of two words.

        Comparing to words is case sensitve, so that e.g.
        Bill and bill differ.

        Args:
            word1: str
            word2: str

        Returns:
            int: Levenshtein Distance of two given words.
        """
        pass
