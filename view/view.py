# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

"""Viewer for the Approximate String Matching. Informs the User
about the matches for the query and the stats of the BK-Tree.
Part of the View within the Model-View-Controller design pattern.
"""


class ApproxMatchViewer:
    """Print output for User to see."""

    @staticmethod
    def show_tree_stats(depth: int, words: int):
        """Print message informing User about tree depth and node count.

        Args:
            depth: Depth of the tree.
            words: Word/Node coiunt of the tree.
        """
        print(
            f"""A BK-Tree with depth {depth},
             containing {words} unique words has been created.""")

    @staticmethod
    def show_matches(query_word: int, max_dist: float, matches: list):
        """Print message informing User about found matches.

        Args:
            query_word: Word the matches relate to.
            max_dist: Edit distance tolerance limit.
            matches: List of all matches for query_word.
        """
        print(f"For {query_word} and maximum edit distance {max_dist} the matches are:", ", ".join(matches))
