# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

import pickle as pkl
from model.bk_tree import BKTree
from view.view import ApproxMatchViewer
from model.levenshtein import Levenshtein


class InteractiveMatcher:

    def __init__(self):
        self.view = ApproxMatchViewer
        self.tree = BKTree()
        self.metric = None

    def get_data(self, filepath, save=False, metric=Levenshtein):
        self.tree.set_up_from_file(filepath)

    def find_matches(self):
        while True:
            word = input("Query word: ")
            if word == "":
                break
            max_dist = int(input("Max edit distance: "))
            matches = self.tree.query(word, max_dist)
            self.view.show_matches(word, max_dist, matches)
