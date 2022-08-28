# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

from controller.controller import InteractiveMatcher

demo = InteractiveMatcher()
demo.set_up_tree("demo_data/demo_tree.pkl", "Levenshtein")
demo.find_matches()


