# -*- coding: utf-8 -*-
# Author: Eileen Kammel, 811770
"""Burkard-Keller-Tree for the Approximate String Matching. Part of the Model
within the Model-View-Controller design pattern.
The BK-Tree is implemented in two parts: The nodes of the tree
are their own class. A BKNode object stores information about its label/word
and about its children, also BKNodes, and their edit distasnce from the label.
The BKTree stores information about its depth, node count, its root node and
the metric used to generate the tree.
The Tree is build by linking nodes together, beginning with the rood node.
"""
import os
import pickle as pkl
from collections import deque
from model.metrics.abstract_metric import Metric


class BKNode():
    def __init__(self, word: str):
        self._contents = (word, [])

    def get_node_label(self):
        """Return the label of a node."""
        return self._contents[0]

    def set_children(self, child, distance):
        """Add a child its edit distance to a node."""
        self._contents[1].append((child, distance))

    def get_children_with_distance(self):
        """Return a children list of tuples each containing
        a child BKNode object and its edit distance.
        """
        return self._contents[1]

    def get_child_node(self):
        """Return a single child BKNode."""
        return self._contents[1][0]

    def get_all_child_nodes(self):
        """Return a list of child BKNode without edit distance."""
        return [child[0] for child in self._contents[1]]

    def get_child_distances(self):
        """Return a list of edit distances from all children."""
        return [child[1]for child in self._contents[1]]


class BKTree():
    def __init__(self):
        self.tree_root = None
        self._depth = 0
        self._words = 0
        self.metric = None

    def set_words(self):
        """Increment total word count by 1."""
        self._words += 1

    def get_words(self):
        """Return word count."""
        return self._words

    @staticmethod
    def depth(node: BKNode):
        """Recursively finds max depth of the tree.

        Args:
            node: Node to determine max depth of.

        Returns:
            int: Max Depth of a tree.
        """
        if len(node.get_all_child_nodes()) == 0:
            return 0
        max_depth = 0
        for child in node.get_all_child_nodes():
            child_depth = BKTree.depth(child)
            if child_depth > max_depth:
                max_depth = child_depth
        return (1 + max_depth)

    def set_depth(self):
        """Set depth attribute by calling the depth function."""
        self._depth = BKTree.depth(self.tree_root)

    def get_depth(self):
        """Return depth of the tree."""
        return self._depth

    def get_tree_stats(self):
        """Return depth and word count of the tree."""
        return self._depth, self._words

    def set_metric(self, metric: Metric):
        """Set metric used to build tree."""
        self.metric = metric

    def set_up_from_file(self, filepath: str, metric: Metric):
        """Set up the BK-Tree.

        Tree is set up by selecting a root and then adding new nodes to it
        while simultaneously incrementing the word count of the tree.
        Words come from a textfile as source. After set-up is completed,
        depth of the tree is set.

        Args:
            filepath: Filepath to text file for source words.
            metric: Metric class to use in tree set-up.
        """
        self.set_metric(metric)
        with open(filepath, "r", encoding="utf-8") as wordlist:
            root = wordlist.readline().strip()
            self.set_root(root)
            while True:
                word = wordlist.readline().strip()
                if not word:
                    break
                self.add(word, self.tree_root)
        self.set_depth()

    def save_to_file(self):
        """Pickle and save BKTree object."""
        filename = input(
            "Enter a filename with .pkl file extension to save the tree: ")
        if not os.path.exists(f"model/{filename}"):
            with open(filename, "wb") as outfile:
                pkl.dump(self, outfile)

    @staticmethod
    def load_from_file(filepath: str):
        """Load pre-build and pickled tree from a file.

        Args:
            filepath: Filepath to a pickled Tree.
        """
        with open(filepath, "rb") as infile:
            tree = pkl.load(infile)
        return tree

    def set_root(self, word: str):
        """Set root node of a BK-Tree.

        Args:
            word: Word to set as tree root.
        """
        root_node = BKNode(word)
        self.tree_root = root_node
        self.set_words()

    def add(self, word: str, node: BKNode):
        """Add a new word to the BK-Tree.

        A new node is instantiated with the given word and then
        added as a child to an appropriate exisiting node. After each
        addition total word count is incremented by 1.

        Args:
            word: Word to add to tree.
            node: Node to add new child to.
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

    def query(self, word: str, max_dist: float):
        """Public query function.

        Accepts the search parameters for the string matching.

        Args:
            word: Query word to find matches for.
            max_dist: Edit ditance tolerance limit.

        Returns:
            List of words which are within the edit distance
            tolerance limit for the query word.
        """
        return self._search(word, self.tree_root, max_dist)

    def _search(self, word: str, node: BKNode, max_dist: float):
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
            word: Query word to find matches for.
            node: Current node to compare query word against.
            max_dist: Edit ditance tolerance limit.

        Returns:
            matches: List of words which are within the edit distance
            tolerance limit for the query word.
        """
        nodes_to_visit = deque([node])
        matches = []
        while nodes_to_visit:
            current_node = nodes_to_visit.popleft()
            node_word = current_node.get_node_label()
            dist = self.metric.min_edit_dist(node_word, word)
            if dist <= max_dist:
                matches.append(node_word)
            next_level_nodes = current_node.get_children_with_distance()
            candidates = [child[0] for child in next_level_nodes
                          if child[1] > (dist - max_dist)
                          and child[1] <= (dist + max_dist)
                          ]
            nodes_to_visit.extend(candidates)
        return matches
