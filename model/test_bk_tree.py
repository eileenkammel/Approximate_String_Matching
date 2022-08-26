# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770

import pytest as pt
from model.bk_tree import BKTree
from model.metrics.levenshtein import Levenshtein


@pt.fixture(scope="session", autouse=True)
def test_tree():
    test_tree = BKTree()
    test_tree.set_up_from_file(
        "model/test_data/demo_wordlist.txt", Levenshtein)
    return test_tree


@pt.fixture(scope="session", autouse=True)
def test_tree_from_file():
    test_tree = BKTree.load_from_file("model/test_data/test_tree.pkl")
    return test_tree


class TestBKLevenshtein:

    def test1(self, test_tree):
        assert len(test_tree.tree_root.get_children_with_distance()) == 4

    def testweight(self, test_tree):
        assert test_tree.tree_root.get_child_distances()[0] == 1

    def testweight1(self, test_tree):
        assert test_tree.tree_root.get_child_distances()[1] == 2

    def testweight2(self, test_tree):
        assert test_tree.tree_root.get_child_distances()[2] == 3

    def testweight3(self, test_tree):
        assert test_tree.tree_root.get_child_distances()[3] == 4

    def testuniqueness(self, test_tree):
        assert len(test_tree.tree_root.get_child_distances()) == len(
            set(test_tree.tree_root.get_child_distances()))

    def test_search(self, test_tree):
        assert test_tree.query("hero", 2) == ["help", "hell", "hello"]

    def test_search1(self, test_tree):
        assert test_tree.query("hero", 3) == [
            "help", "hell", "hello", "helps", "shell"]

    def test_loaded_tree(self, test_tree, test_tree_from_file):
        assert test_tree.query(
            "hero", 2) == test_tree_from_file.query("hero", 2)

    def test_loaded_tree1(self, test_tree, test_tree_from_file):
        assert test_tree.query(
            "hero", 3) == test_tree_from_file.query("hero", 3)

    def test_tree_depth(self, test_tree):
        assert test_tree.get_depth() == 2

    def test_tree_words(self, test_tree):
        assert test_tree.get_words() == 8
