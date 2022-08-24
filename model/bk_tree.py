# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770

import os
import pickle as pkl
from collections import deque
from model.metrics.levenshtein import Levenshtein


class BKNode():
    def __init__(self, word):
        self._contents = (word, [])

    def get_node_label(self):
        return self._contents[0]

    def set_children(self, child, distance):
        self._contents[1].append((child, distance))

    def get_children_with_distance(self):
        return self._contents[1]

    def get_child_node(self):
        return self._contents[1][0]

    def get_all_child_nodes(self):
        return [child[0] for child in self._contents[1]]

    def get_child_distances(self):
        return [child[1]for child in self._contents[1]]


class BKTree():
    def __init__(self, distance_metric=Levenshtein):
        self.tree_root = None
        self._depth = 0
        self._words = 0
        self.metric = distance_metric

    def set_words(self):
        self._words += 1

    def get_words(self):
        return self._words

    @staticmethod
    def depth(node):
        """Finds max depth of the tree."""
        if len(node.get_all_child_nodes()) == 0:
            return 0
        max_depth = 0
        for child in node.get_all_child_nodes():
            child_depth = BKTree.depth(child)
            if child_depth > max_depth:
                max_depth = child_depth
        return (1 + max_depth)

    def set_depth(self):
        self._depth = BKTree.depth(self.tree_root)

    def get_depth(self):
        return self._depth

    def get_tree_stats(self):
        return self._depth, self._words

    def set_up_from_file(self, filename):
        """Sets up the BK-Tree.

        Tree is set up by selecting a root and then adding word by word new
        nodes to it. Words come from a textfile as source.

        Args:
            filename (str): filename for source words
        """
        with open(filename, "r", encoding="utf-8") as wordlist:
            root = wordlist.readline().strip()
            self.set_root(root)
            while True:
                word = wordlist.readline().strip()
                if not word:
                    break
                self.add(word, self.tree_root)
        self.set_depth()

    def save_to_file(self):
        filename = input(
            "Please enter a filename with .pkl file extension to save the tree: ")
        if not os.path.exists(f"model/{filename}"):
            with open(filename, "wb") as outfile:
                pkl.dump(self, outfile)

    @staticmethod
    def load_from_file(filename):
        with open(filename, "rb") as infile:
            tree = pkl.load(infile)
        return tree

    def __str__(self):
        pass

    def set_root(self, word):
        """Sets root node of a BK-Tree.

        Args:
            word (str): Word to set as tree root.
        """
        root_node = BKNode(word)
        self.tree_root = root_node
        self.set_words()

    def add(self, word, node):
        """Adds a new word to the Bk-Tree.

        A new node is instanciated with the given word and then
        added as a child to an appropriate exisiting node.

        Args:
            word (str): word to add to tree
            node (BKNode): node to add new child to
        """
        new_node = BKNode(word)
        dist = self.metric.min_edit_dist(node.get_node_label(), word)
        children = node.get_children_with_distance()
        if not children or dist not in node.get_child_distances():
            node.set_children(new_node, dist)
            self.set_words()
            return
        conflict_node = [child for child in children if child[1] == dist]
        return self.add(word, conflict_node[0][0])

    def query(self, word, max_dist):
        """Public query function.

        Args:
            word (str): query word to find matches for
            max_dist (int): edit ditance tolerance limit

        Returns:
            List of words which are within the edit distance
            tolerance limit for the query word.
        """
        return self._search(word, self.tree_root, max_dist)

    def _search(self, word, node, max_dist):
        """Searches BK-Tree for matches regarding a given word and
        maximum edit distance.

        Search after breadth first principle. Only subtrees whose
        root nodes edit distance regarding the query word
        is within a certain edit distance range are visited.
        The range is definded as follows:
        (d - max_dist, d + max_dist)
        d being the edit distance regarding the query word and the word
        of the current node, max_dist being an edit distance tolerance limit.

        Args:
            word (str): query word to find matches for
            node (BKNode): current node to compare query word against
            max_dist (int): edit ditance tolerance limit

        Returns:
            matches (list): list of words which are within the edit distance
            tolerance limit for the query word.
        """
        nodes_to_visit = deque([node])
        matches = []
        while nodes_to_visit:
            current_node = nodes_to_visit.popleft()
            node_word = current_node.get_node_label()
            dist = Levenshtein.min_edit_dist(node_word, word)
            if dist <= max_dist:
                matches.append(node_word)
            next_level_nodes = current_node.get_children_with_distance()
            candidates = [child[0] for child in next_level_nodes
                          if child[1] in range(dist-max_dist, dist+max_dist+1)
                          ]
            nodes_to_visit.extend(candidates)
        return matches
