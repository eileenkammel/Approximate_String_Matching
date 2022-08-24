# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770

from model.metrics.levenshtein import Levenshtein


class TestLevenshtein:

    def test_substitution(self):
        assert Levenshtein.min_edit_dist("bill", "Bill") == 1

    def test_substitution1(self):
        assert Levenshtein.min_edit_dist("bill", "will") == 1

    def test_substitution2(self):
        assert Levenshtein.min_edit_dist("lake", "lame") == 1

    def test_substitution3(self):
        assert Levenshtein.min_edit_dist("bat", "bee") == 2

    def test_substitution4(self):
        assert Levenshtein.min_edit_dist("cat", "car") == 1

    def test_deletion(self):
        assert Levenshtein.min_edit_dist("hero", "her") == 1

    def test_deletion1(self):
        assert Levenshtein.min_edit_dist("sailboat", "boat") == 4

    def test_deletion2(self):
        assert Levenshtein.min_edit_dist("theater", "tea") == 4

    def test_deletion3(self):
        assert Levenshtein.min_edit_dist("fall", "all") == 1

    def test_insertion(self):
        assert Levenshtein.min_edit_dist("met", "meet") == 1

    def test_insertion1(self):
        assert Levenshtein.min_edit_dist("bee", "bumblebee") == 6

    def test_insertion2(self):
        assert Levenshtein.min_edit_dist("sum", "scrum") == 2

    def test_insertion3(self):
        assert Levenshtein.min_edit_dist("bus", "busy") == 1

    def test_deletion_insertion(self):
        assert Levenshtein.min_edit_dist("tree", "reef") == 2

    def test_substitution_insertion(self):
        assert Levenshtein.min_edit_dist("hell", "helps") == 2
