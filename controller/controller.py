# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

import sys
from model.bk_tree import BKTree
from model.metrics.sorensen_dice import SorensenDiceCoefficient
from view.view import ApproxMatchViewer
from model.metrics.levenshtein import Levenshtein


class InteractiveMatcher:

    def __init__(self):
        self.view = ApproxMatchViewer
        self.tree = BKTree()

    def set_up_tree(self, filepath, metric_name, save=False):
        metric = InteractiveMatcher.determine_metric(metric_name)
        if filepath.endswith(".txt"):
            self.tree.set_up_from_file(filepath, metric)
            if save:
                self.tree.save_to_file()
        if filepath.endswith(".pkl"):
            self.tree = BKTree.load_from_file(filepath)
        depth, words = self.tree.get_tree_stats()
        self.view.show_tree_stats(depth, words)

    def find_matches(self):
        while True:
            word = input("Query word: ")
            if word == "":
                break
            max_dist = float(input("Max edit distance: "))
            matches = self.tree.query(word, max_dist)
            self.view.show_matches(word, max_dist, matches)

    @staticmethod
    def determine_metric(metric_name):
        if metric_name == "Levenshtein":
            return Levenshtein
        if metric_name in ["SorensenDiceCoefficient", "SDC", "sdc"]:
            return SorensenDiceCoefficient
        print("No suitable metric name was given.")
        sys.exit()