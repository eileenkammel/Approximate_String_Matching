# -*-coding:utf-8 -*-
# Author: Eileen Kammel, 811770

import argparse
from controller.controller import InteractiveMatcher


parser = argparse.ArgumentParser()

parser.add_argument(
    "--file", type=str, help=("Path to either a .txt file containing a wordlist or \
                a .pkl file containing a pre set-up and pickeled BK-Tree."))

parser.add_argument("--save", action="store_true", help=("Flag for saving the BK-Tree. \
                If set, the tree gets saved."))

parser.add_argument("--metric", type=str, const="Levenshtein", nargs="?", help=("Name of a distance metric. \
                If omitted, Levenshtein as default is choosen. \
                Current options: \
                Sorensen Dice Coefficient \
                (SorensenDiceCoefficient, SDC, sdc)"))

args = parser.parse_args()

file = args.file
save = args.save
metric = args.metric

matcher = InteractiveMatcher()

matcher.set_up_tree(file, metric, save)
matcher.find_matches()
