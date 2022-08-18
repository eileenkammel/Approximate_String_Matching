# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770

from levenshtein import Levenshtein

class BKNode():
    def __init__(self, word):
        self.contents = (word, [])

    def get_node_label(self):
        return self.contents[0]

    def set_children(self, child, distance):
        self.contents[1].append((child, distance))

    def get_children_with_distance(self):
        return self.contents[1]

    def get_child_node(self):
        return self.contents[1][0]

    def get_child_distances(self):
        return [child[1]for child in self.contents[1]]


class BKTree():
    def __init__(self, distance_metric=Levenshtein):
        self.tree_root = None
        self.depth = 0
        self.metric = distance_metric

    def set_up_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as wordlist:
            root = wordlist.readline()
            self.set_root(root)
            while True:
                word = wordlist.readline()
                if not word:
                    break
                self.add(word, self.tree_root)

    def save_to_file(self):
        pass

    def load_from_file(self, filename):
        pass

    def set_root(self, word):
        """Sets root node of a BK-Tree.

        Args:
            word: str
        """
        root_node = BKNode(word)
        self.tree_root = root_node

    def add(self, word, node):
        new_node = BKNode(word)
        dist = self.metric.min_edit_dist(node.get_node_label(), word)
        children = node.get_children_with_distance()
        if not children or dist not in node.get_child_distances():
            node.set_children(new_node, dist)
            self.depth += 1
            return
        conflict_node = [child for child in children if child[1] == dist]
        self.depth += 1
        return self.add(word, conflict_node[0][0])

    def search(self, word, max_dist):
        pass
