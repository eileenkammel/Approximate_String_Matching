# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770
"""Executable demo of the interactive approximate matching.
Uses a BK-Tree with 8 english words and the Levenshtein Distance.
"""
if __name__ == "__main__":
    from controller.controller import InteractiveMatcher

    demo = InteractiveMatcher()
    demo.set_up_tree("demo_data/demo_tree.pkl", "Levenshtein")
    demo.find_matches()
