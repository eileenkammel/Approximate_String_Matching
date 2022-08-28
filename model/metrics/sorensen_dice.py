# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

from model.metrics.abstract_metric import Metric

"""Implements the Sorensen Dice Coefficient based on the wikipedia article:
https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient
Part of the Model within the Model-View-Controller design pattern.
"""


class SorensenDiceCoefficient(Metric):
    """Sorensen Dice Coefficient."""

    @staticmethod
    def min_edit_dist(source: str, target: str):
        """Calculates the Sorensen Dice Coefficient of two words.

        The SDC is based on the count of intersections of bigrams in
        the two words.
        x = Count of bigrams in source
        y = Count of bigrams in target
        z = Count of intersections/ bigrams in source AND target.
        SDC = (2*z)/(x+y)

        Args:
            source: Source word
            target: Target word

        Returns:
            float: Sorensen Dice Coefficient, between 0 and 1.

        """
        bigrams_s, len_bs = SorensenDiceCoefficient.bigrams(source)
        bigrams_t, len_bt = SorensenDiceCoefficient.bigrams(target)
        intersection_count = SorensenDiceCoefficient.count_intersections(
            bigrams_s, bigrams_t)
        return (2*intersection_count)/(len_bs+len_bt)

    @staticmethod
    def bigrams(word: str):
        """Constructs character bigrams on a word.

        Args:
            word : Word to construct bigrams for.

        Returns:
            List of bigrams (str) and int lenght of that list.
        """
        bigrams = []
        if len(word) == 2:
            return [word], 1
        for idx, _ in enumerate(word):
            if idx <= (len(word)-2):
                bigram = word[idx] + word[idx+1]
                bigrams.append(bigram)
        return bigrams, len(bigrams)

    def count_intersections(bigrams_source: list, bigrams_target: list):
        """Counts intersections of to bigram lists.

        Args:
            bigrams_source: List of bigrams in source word.
            bigrams_target: List of bigrams in target word.

        Returns:
            Count of intersections.
        """
        intersections = [
            bigram for bigram in bigrams_source if bigram in bigrams_target]
        return len(intersections)


