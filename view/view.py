# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

"""Viewer for the Approximate String Matching. Informs the User
about the matches for the query and the stats of the BK-Tree.
Part of the View within the Model-View-Controller design pattern.
"""


class ApproxMatchViewer:
    """Print output for user to see."""

    @staticmethod
    def show_tree_stats(depth: int, words: int):
        """Print message informing user about tree depth and node count.

        Args:
            depth: Depth of the tree.
            words: Word/Node count of the tree.
        """
        print((
            f"A BK-Tree with depth {depth} "
            f"containing {words} unique words has been created."))

    @staticmethod
    def show_matches(query_word: int, max_dist: float, matches: list):
        """Print message informing User about found matches.

        Args:
            query_word: Word the matches relate to.
            max_dist: Edit distance tolerance limit.
            matches: List of all matches for query_word.
        """
        print((
            f"For {query_word} and maximum edit distance {max_dist} "
            "the matches are: " + ", ".join(matches)))

    @staticmethod
    def inform_of_termination(reason: str):
        """Informs the user of program termination.

        Args:
            reason: Used for f-string, informs if program is
            terminated due to invalid metric name or file input.
        """
        return print(f"Program will be terminated due to invalid {reason}.")
