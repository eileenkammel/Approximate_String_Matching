# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

import argparse
from controller.controller import InteractiveMatcher


parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", type=str, help="Path to either a .txt file containing a wordlist or a .pkl file containing a pre set-up and pickeled BK-Tree")
parser.add_argument("-s", action="store_true")
parser.add_argument("-m", type=str, const="Levenshtein", nargs="?")

args = parser.parse_args()

file = args.f
save = args.s
metric = args.m

test = InteractiveMatcher()

test.set_up_tree(file, metric, save)
#test.find_matches()
