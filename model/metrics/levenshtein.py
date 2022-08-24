# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770

import numpy as np
from model.metrics.abstract_metric import Metric

# Implements the dynamic programming version of calculating the
# minimum Levenshtein Distance from Jurafsky & Martin (2021).


class Levenshtein(Metric):
    """Levenshtein Distance Metric."""

    @staticmethod
    def min_edit_dist(source, target):
        """Calculates minimum Levenshtein Distance of two words.

        Levenshtein Distance indicates how many operations are
        nessecary to transform a source word into a target word.
        Comparing words is case sensitve, so that e.g.
        Bill and bill differ.
        Costs:
        insertion = 1 operation
        deletion = 1 operation
        substitution = 1 operation if substrings differ, 0 operations
        if substrings are identical.

        Args:
            source: str, source word
            target: str, target word

        Returns:
            int: min Levenshtein Distance of two given words.
        """
        n = len(source)
        m = len(target)
        dm = np.full((n+1, m+1), 0)
        for row in range(1, n+1):
            dm[row, 0] = (
                dm[(row-1), 0] + 1)
        for column in range(1, m+1):
            dm[0, column] = (dm[0, (column-1)] + 1)
        for row in range(1, n+1):
            for column in range(1, m+1):
                dm[row, column] = min(dm[(row-1), column]+1,
                                      dm[row-1, column-1] +
                                      (Levenshtein.substitute(
                                          source[row-1], target[column-1])),
                                      dm[row, column-1] + 1
                                      )
        return dm[n, m]

    @staticmethod
    def substitute(source_char, target_char):
        """Determines substitution cost.

        Args:
        source_char: str, character in source string
        target_char: str, character in target string

        Retuns:
        int, cost of substitution
        """
        if source_char == target_char:
            return 0
        return 1
