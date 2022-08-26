# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
"""User Interface for the Approximate String Matching. Part of
Controller within the Model-View-Controller design pattern.
"""

import sys
from model.bk_tree import BKTree
from model.metrics.sorensen_dice import SorensenDiceCoefficient
from view.view import ApproxMatchViewer
from model.metrics.levenshtein import Levenshtein


class InteractiveMatcher:
    """Interactive Matcher for approximate string matching.

    Accepts and handles user input. Passes user input on
    to the BK-Tree Model, calls the appropriate model methods.
    Model output is passed on to ApproxMatchViewer.
    """
    def __init__(self):
        self.view = ApproxMatchViewer
        self.tree = BKTree()

    def set_up_tree(self, filepath: str, metric_name: str, save: bool = False):
        """Inititializes the BK-Tree set-up.

        The Tree is either set-up new from a textfile or loaded from
        a pkl. file depending on the filepath passed. The metric class
        is determined from the user input string. Tree is saved to a .pkl
        file if user decided to do so.

        Args:
            filepath: Path to a .txt or .pkl file
            metric: Name of one of the available metrics. If not given
            default is Levenshtein.
            save: Decide if tree gets saved once set up.
        """
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
        """Executes the interactive matching mode.

        User is asked for input of query word and edit distance
        tolerance limit. That input is passes on to the model.
        """
        while True:
            word = input("Query word: ")
            if word == "":
                break
            max_dist = float(input("Max edit distance: "))
            matches = self.tree.query(word, max_dist)
            self.view.show_matches(word, max_dist, matches)

    @staticmethod
    def determine_metric(metric_name: str):
        """Determines which metric class to load.

        Commandline argument string is translated to matching
        metreics class.

        Args:
            metric_name: Name of one of the available metrics.

        Returns:
            one of the Metric classes.
        """
        if metric_name == "Levenshtein":
            return Levenshtein
        if metric_name in ["SorensenDiceCoefficient", "SDC", "sdc"]:
            return SorensenDiceCoefficient
        print("No suitable metric name was given.")
        sys.exit()
