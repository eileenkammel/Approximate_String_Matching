# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770

import pytest as pt
from model.bk_tree import BKTree


@pt.fixture(scope="session", autouse=True)
def test_tree():
    test_tree = BKTree()
    test_tree.set_up_from_file("model/demo_wordlist.txt")
    return test_tree


class TestBK:

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
