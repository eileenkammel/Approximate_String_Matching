# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770


class ApproxMatchViewer:

    @staticmethod
    def show_tree_stats(depth, words):
        print(
            f"A BK-Tree with depth {depth}, containing {words} unique words has been created.")

    @staticmethod
    def show_matches(query_word, max_dist, matches):
        print(f"For {query_word} and maximum edit distance {max_dist} the matches are:", ", ".join(
            matches))
